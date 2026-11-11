#!/usr/bin/env bash
# Frontmatter readers shared by check-pack.sh and build-readme-skills.sh.

# Prints the frontmatter description text, plain or as a folded or literal block.
frontmatter_description() {
  awk '
    NR > 1 && $0 == "---" { exit }
    in_block && /^[ \t]+[^ \t]/ { print; next }
    { in_block = 0 }
    /^description:[ \t]*[>|][-+]?[ \t]*$/ { in_block = 1; next }
    /^description:/ { sub(/^description:[ \t]*/, ""); print }
  ' "$1"
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

# Prints the frontmatter category value.
frontmatter_category() {
  awk '
    NR > 1 && $0 == "---" { exit }
    /^category:/ { sub(/^category:[ \t]*/, ""); print }
  ' "$1"
}
