#!/usr/bin/env bash
# Checks the pack's own rules. Run from anywhere inside the repo.
# Uses only bash, git, grep, awk, tr, cmp, and jq (all on ubuntu-latest).
set -euo pipefail

export LC_ALL=C.UTF-8
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

check_agents_copy() {
  local copy=skills/setup-toolkit/templates/AGENTS.md
  cmp -s AGENTS.md "$copy" || fail "AGENTS.md and $copy differ"
}

check_agents_size() {
  local size
  size=$(wc -c <AGENTS.md)
  ((size < 8192)) || fail "AGENTS.md is $size bytes (limit: under 8192)"
}

check_agents_marker() {
  local first
  first=$(head -n 1 AGENTS.md)
  [[ "$first" == "<!-- gabriel-skills-agents -->" ]] ||
    fail "AGENTS.md first line is not <!-- gabriel-skills-agents -->"
}

check_no_dashes() {
  local hits
  hits=$(repo_files | tr '\n' '\0' |
    xargs -0 grep -nIP '[\x{2013}\x{2014}\x{2015}]' -- 2>/dev/null || true)
  [[ -z "$hits" ]] && return 0
  while IFS= read -r hit; do
    fail "dash character at ${hit%%:*}:$(cut -d: -f2 <<<"$hit")"
  done <<<"$hits"
}

# Prints two lines from the YAML frontmatter: the name, then 1 if a description
# has text. Prints nothing when the frontmatter is missing or unclosed.
frontmatter_fields() {
  awk '
    NR == 1 && $0 != "---" { exit }
    NR > 1 && $0 == "---" { done = 1; exit }
    want_block && /^[ \t]+[^ \t]/ { desc = 1 }
    { want_block = 0 }
    /^name:/ { name = $0; sub(/^name:[ \t]*/, "", name); gsub(/["\047]/, "", name) }
    /^description:[ \t]*[>|][-+]?[ \t]*$/ { want_block = 1; next }
    /^description:[ \t]*[^ \t]/ { desc = 1 }
    END { if (done) printf "%s\n%d\n", name, desc }
  ' "$1"
}

check_skill_frontmatter() {
  local file folder fields
  for file in skills/*/SKILL.md; do
    folder=$(basename "$(dirname "$file")")
    mapfile -t fields < <(frontmatter_fields "$file")
    [[ "${fields[0]:-}" == "$folder" ]] || fail "$file: frontmatter name '${fields[0]:-}' is not '$folder'"
    [[ "${fields[1]:-0}" == 1 ]] || fail "$file: frontmatter description is missing or empty"
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

check_plugin_versions() {
  local plugin=.cursor-plugin/plugin.json market=.cursor-plugin/marketplace.json want mismatched
  want=$(jq -er '.version' "$plugin") || { fail "$plugin does not parse or has no version"; return 0; }
  jq -er '.metadata.version // .plugins[0].version' "$market" >/dev/null ||
    { fail "$market does not parse or has no version"; return 0; }
  mismatched=$(jq -r --arg want "$want" \
    '.metadata.version, .plugins[]?.version | select(. != null and . != $want)' "$market")
  [[ -z "$mismatched" ]] || fail "$market has version(s) $(echo $mismatched) but $plugin has $want"
}

main() {
  local check
  for check in check_agents_copy check_agents_size check_agents_marker check_no_dashes \
    check_skill_frontmatter check_links check_plugin_versions; do
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
