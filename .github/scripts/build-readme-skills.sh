#!/usr/bin/env bash
# Writes the skills catalog between the skills markers in README.md.
# --check exits non-zero when the block is stale instead of writing it.
set -euo pipefail

export LC_ALL=C.UTF-8
source "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
cd "$(git rev-parse --show-toplevel)"

START='<!-- skills:start -->'
END='<!-- skills:end -->'

# Prints the marker-to-marker block, markers included.
catalog() {
  local file name category description
  echo "$START"
  echo '| Skill | Category | Description |'
  echo '| --- | --- | --- |'
  for file in skills/*/SKILL.md; do
    name=$(basename "$(dirname "$file")")
    [[ "$name" == rules ]] && continue
    category=$(frontmatter_category "$file")
    description=$(frontmatter_description "$file" | tr '\n' ' ' | sed -E 's/^ +| +$//g; s/\|/\\|/g')
    printf '%s\t%s\t%s\n' "$category" "$name" "$description"
  done | sort -t$'\t' -k1,1 -k2,2 | while IFS=$'\t' read -r category name description; do
    printf '| [`/%s`](./skills/%s/SKILL.md) | %s | %s |\n' "$name" "$name" "$category" "$description"
  done
  echo "$END"
}

# Prints README.md with the block between the markers replaced by $1's contents.
render() {
  awk -v block_file="$1" -v start="$START" -v end="$END" '
    $0 == start { while ((getline line < block_file) > 0) print line; skipping = 1; next }
    $0 == end { skipping = 0; next }
    !skipping { print }
  ' README.md
}

main() {
  tmp=$(mktemp -d)
  trap 'rm -rf "$tmp"' EXIT
  grep -qxF "$START" README.md && grep -qxF "$END" README.md ||
    { echo "README.md is missing the skills:start or skills:end marker"; exit 1; }
  catalog >"$tmp/block"
  render "$tmp/block" >"$tmp/rendered"
  if [[ "${1:-}" == --check ]]; then
    cmp -s README.md "$tmp/rendered" ||
      { echo "README.md skills catalog is stale: run bash .github/scripts/build-readme-skills.sh"; exit 1; }
    return 0
  fi
  cat "$tmp/rendered" >README.md
}

main "$@"
