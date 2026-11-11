#!/usr/bin/env bash
# Checks the pack's own rules. Run from anywhere inside the repo.
# Uses only bash, git, grep, awk, sed, tr, wc, cmp, and jq (all on ubuntu-latest).
set -euo pipefail

export LC_ALL=C.UTF-8
source "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
cd "$(git rev-parse --show-toplevel)"

failures=0

fail() {
  echo "FAIL: $*"
  failures=$((failures + 1))
}

# Tracked files plus new untracked ones, so a local run sees work in progress.
repo_files() {
  git ls-files --cached --others --exclude-standard | while IFS= read -r f; do
    [[ -f "$f" ]] && printf '%s\n' "$f"
  done
}

check_agents_size() {
  local size
  size=$(wc -c <AGENTS.md)
  ((size < 8192)) || fail "AGENTS.md is $size bytes (limit: under 8192)"
}

check_agents_marker() {
  local first plugin_version pattern='^<!-- gabriel-skills-agents v([0-9]+\.[0-9]+\.[0-9]+) -->$'
  first=$(head -n 1 AGENTS.md)
  [[ "$first" =~ $pattern ]] ||
    { fail "AGENTS.md first line '$first' is not <!-- gabriel-skills-agents vX.Y.Z -->"; return 0; }
  plugin_version=$(jq -r '.version' .cursor-plugin/plugin.json)
  [[ "${BASH_REMATCH[1]}" == "$plugin_version" ]] ||
    fail "AGENTS.md marker version ${BASH_REMATCH[1]} is not plugin.json version $plugin_version"
}

# Prints each backticked .md path in the File column of the AGENTS.md Read when table.
read_when_paths() {
  awk '
    /^## Read when[ \t]*$/ { inside = 1; next }
    inside && /^## / { exit }
    inside && /^\|/ {
      n = split($0, cells, "|")
      file = cells[n - 1]
      while (match(file, /`[^`]+`/)) {
        print substr(file, RSTART + 1, RLENGTH - 2)
        file = substr(file, RSTART + RLENGTH)
      }
    }
  ' AGENTS.md | grep '\.md$' | grep -vxF 'docs/design.md' || true
}

check_read_when_files() {
  local path
  while IFS= read -r path; do
    [[ -f "skills/$path" ]] || fail "AGENTS.md Read when table names skills/$path, which does not exist"
  done < <(read_when_paths)
}

# Prints each backticked folder/file.md path in one AGENTS.md section. $1 is the heading text.
section_paths() {
  awk -v heading="## $1" '
    $0 == heading { inside = 1; next }
    inside && /^## / { exit }
    inside {
      line = $0
      while (match(line, /`[^` ]+\/[^` ]+\.md`/)) {
        print substr(line, RSTART + 1, RLENGTH - 2)
        line = substr(line, RSTART + RLENGTH)
      }
    }
  ' AGENTS.md
}

check_section_files() {
  local section path
  for section in Skills Rules; do
    while IFS= read -r path; do
      [[ -f "skills/$path" ]] || fail "AGENTS.md $section section names skills/$path, which does not exist"
    done < <(section_paths "$section")
  done
}

check_description_length() {
  local file words
  for file in skills/*/SKILL.md; do
    words=$(frontmatter_description "$file" | wc -w)
    ((words <= 60)) || fail "$file: description is $words words (limit: 60)"
  done
}

check_no_dashes() {
  local hits
  # Byte patterns for U+2013, U+2014, U+2015, so BSD grep (no -P) finds them too.
  hits=$(repo_files | tr '\n' '\0' |
    LC_ALL=C xargs -0 grep -nI -e $'\xe2\x80\x93' -e $'\xe2\x80\x94' -e $'\xe2\x80\x95' -- 2>/dev/null || true)
  [[ -z "$hits" ]] && return 0
  while IFS= read -r hit; do
    fail "dash character at ${hit%%:*}:$(cut -d: -f2 <<<"$hit")"
  done <<<"$hits"
}

check_skill_frontmatter() {
  local file folder name desc
  for file in skills/*/SKILL.md; do
    folder=$(basename "$(dirname "$file")")
    name='' desc=''
    { IFS= read -r name || true; IFS= read -r desc || true; } < <(frontmatter_fields "$file")
    [[ "$name" == "$folder" ]] || fail "$file: frontmatter name '$name' is not '$folder'"
    [[ "$desc" == 1 ]] || fail "$file: frontmatter description is missing or empty"
  done
}

# Prints "line<TAB>target" for each markdown link outside fences and inline code.
extract_links() {
  awk '
    /^[ \t]*(```|~~~)/ { fenced = !fenced; next }
    fenced { next }
    {
      text = $0
      gsub(/`[^`]*`/, "", text)
      while (match(text, /\]\([^)]+\)/)) {
        target = substr(text, RSTART + 2, RLENGTH - 3)
        sub(/[ \t].*/, "", target)
        gsub(/^<|>$/, "", target)
        printf "%d\t%s\n", NR, target
        text = substr(text, RSTART + RLENGTH)
      }
    }
  ' "$1"
}

# Prints GitHub heading slugs for a markdown file, with -1, -2 for duplicates.
heading_slugs() {
  awk '
    /^[ \t]*(```|~~~)/ { fenced = !fenced; next }
    fenced { next }
    /^#{1,6}[ \t]/ { sub(/^#+[ \t]+/, ""); sub(/[ \t]+#*[ \t]*$/, ""); print }
  ' "$1" |
    sed -E 's/\[([^]]*)\]\([^)]*\)/\1/g' |
    tr 'A-Z' 'a-z' |
    tr -d '!"#$%&'\''()*+,./:;<=>?@[\\]^`{|}~' |
    tr ' ' '-' |
    awk '{ n = seen[$0]++; print (n ? $0 "-" n : $0) }'
}

is_external() {
  [[ "$1" =~ ^(https?:|mailto:) ]]
}

# Prints the file a link points to; a pure #anchor points to the linking file.
link_destination() {
  local file=$1 path=${2%%#*}
  [[ -z "$path" ]] && { printf '%s\n' "$file"; return 0; }
  printf '%s\n' "$(dirname "$file")/$path"
}

has_anchor() {
  local dest=$1 target=$2
  [[ "$target" != *"#"* || "$dest" != *.md ]] && return 0
  heading_slugs "$dest" | grep -qxF -- "${target#*#}"
}

check_one_link() {
  local file=$1 line=$2 target=$3 dest
  is_external "$target" && return 0
  dest=$(link_destination "$file" "$target")
  [[ -e "$dest" ]] || { fail "$file:$line: broken link $target"; return 0; }
  has_anchor "$dest" "$target" || fail "$file:$line: missing anchor $target"
}

check_links() {
  local file line target
  while IFS= read -r file; do
    while IFS=$'\t' read -r line target; do
      check_one_link "$file" "$line" "$target"
    done < <(extract_links "$file")
  done < <(repo_files | grep '\.md$')
}

# Every backticked path.md#anchor in AGENTS.md must name a file under skills/ with that heading.
check_agents_anchors() {
  local ref
  while IFS= read -r ref; do
    [[ -f "skills/${ref%%#*}" ]] || { fail "AGENTS.md names skills/$ref, but the file does not exist"; continue; }
    heading_slugs "skills/${ref%%#*}" | grep -qxF -- "${ref#*#}" ||
      fail "AGENTS.md names skills/$ref, but that file has no such heading"
  done < <(grep -o '`[^` ]*\.md#[^` ]*`' AGENTS.md | tr -d '`')
}

# Word budgets for what an agent reads on one journey. Words, not lines, so rewrapping cannot move
# the number. Raise a cap only with a stated reason (how-to.md).
RULES=skills/rules
BUDGETS=(
  "build-start|7519|AGENTS.md skills/task/SKILL.md skills/task/reference.md $RULES/execution.md $RULES/code-quality.md $RULES/code-structure.md"
  "build-full|25931|AGENTS.md skills/task/SKILL.md skills/task/reference.md $RULES/execution.md $RULES/code-quality.md $RULES/code-structure.md $RULES/strong-foundation.md $RULES/planning.md $RULES/user-experience.md $RULES/main-context.md $RULES/writing-style.md $RULES/keep-it-simple.md $RULES/testing.md $RULES/no-unrequested-tests.md skills/task/doctrine.md skills/verification/SKILL.md skills/verification/doctrine.md skills/verification/reference.md skills/review/SKILL.md skills/review/contract.md"
  "review-start|9353|AGENTS.md skills/review/SKILL.md skills/review/contract.md $RULES/code-quality.md $RULES/code-structure.md"
  "pack-total|54852|@pack"
)

# Prints the files of one journey; @pack means AGENTS.md plus every skills markdown file.
budget_files() {
  if [[ "$1" == @pack ]]; then
    echo AGENTS.md
    repo_files | grep '^skills/.*\.md$'
  else
    tr ' ' '\n' <<<"$1"
  fi
}

check_read_budgets() {
  local entry name cap files file total
  for entry in "${BUDGETS[@]}"; do
    IFS='|' read -r name cap files <<<"$entry"
    total=0
    while IFS= read -r file; do
      [[ -f "$file" ]] || { fail "read budget $name lists $file, which does not exist"; continue; }
      total=$((total + $(wc -w <"$file")))
    done < <(budget_files "$files")
    echo "$name: $total words (cap $cap)"
    ((total <= cap)) || fail "read budget $name is $total words (cap: $cap)"
  done
}

check_plugin_versions() {
  local plugin=.cursor-plugin/plugin.json want file mismatched
  want=$(jq -er '.version' "$plugin") || { fail "$plugin does not parse or has no version"; return 0; }
  for file in .cursor-plugin/marketplace.json .claude-plugin/plugin.json \
    .claude-plugin/marketplace.json .agents/plugins/marketplace.json; do
    mismatched=$(jq -r --arg want "$want" '
      [.version, .metadata.version, .plugins[]?.version] | map(select(. != null)) |
      if length == 0 then "none" else map(select(. != $want)) | join(" ") end' "$file") ||
      { fail "$file does not parse"; continue; }
    [[ -z "$mismatched" ]] || fail "$file has version(s) $mismatched but $plugin has $want"
  done
}

# Each skill must be routable: in the AGENTS.md Skills table, and in the generated README catalog.
# rules/ is not a workflow; setup is user-started only.
check_skill_registries() {
  local file name skills_table
  skills_table=$(awk '/^## Skills[ \t]*$/ { inside = 1; next } inside && /^## / { exit } inside && /^\|/' AGENTS.md)
  for file in skills/*/SKILL.md; do
    name=$(basename "$(dirname "$file")")
    [[ "$name" == rules || "$name" == setup-gabriel-skills ]] && continue
    grep -qF "\`$name/SKILL.md\`" <<<"$skills_table" ||
      fail "AGENTS.md Skills table does not list $name/SKILL.md"
  done
  bash "$(dirname "${BASH_SOURCE[0]}")/build-readme-skills.sh" --check || fail "README.md skills catalog is stale"
}

main() {
  local check
  for check in check_agents_size check_agents_marker check_read_when_files check_section_files check_agents_anchors \
    check_no_dashes check_skill_frontmatter check_description_length check_links \
    check_plugin_versions check_skill_registries check_read_budgets; do
    echo "== $check"
    "$check"
  done
  if ((failures > 0)); then
    echo "$failures check failure(s)"
    exit 1
  fi
  echo "All checks passed"
}

main "$@"
