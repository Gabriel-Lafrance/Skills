#!/usr/bin/env bash
# Quick check that every skill is discoverable and has required frontmatter.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail=0
for skill in skills/*/SKILL.md; do
  dir="$(dirname "$skill")"
  name="$(basename "$dir")"
  if ! grep -q '^name:' "$skill"; then
    echo "FAIL $name: missing name frontmatter"
    fail=1
  fi
  if ! grep -q '^description:' "$skill"; then
    echo "FAIL $name: missing description frontmatter"
    fail=1
  fi
done

echo "Listing via npx skills…"
npx skills@latest add "$ROOT" --list >/tmp/gabriel-skills-list.txt
count="$(grep -c '^│    [a-z]' /tmp/gabriel-skills-list.txt || true)"
echo "Discovered skill lines: $count"
if [[ "$fail" -ne 0 ]]; then
  exit 1
fi
echo "OK"
