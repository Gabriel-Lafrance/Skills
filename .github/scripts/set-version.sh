#!/usr/bin/env bash
# Usage: set-version.sh X.Y.Z. Writes one version into the five plugin manifests and the AGENTS.md marker.
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

version=${1:-}
[[ "$version" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || { echo "usage: set-version.sh X.Y.Z (got '$version')"; exit 1; }

# Same paths check_plugin_versions in check-pack.sh reads.
set_manifest() {
  local file=$1 tmp
  tmp=$(mktemp)
  jq --arg v "$version" '
    (if has("version") then .version = $v else . end)
    | (if .metadata.version? != null then .metadata.version = $v else . end)
    | (if .plugins then .plugins |= map(if has("version") then .version = $v else . end) else . end)
  ' "$file" >"$tmp" || { rm -f "$tmp"; echo "set-version.sh: could not rewrite $file"; exit 1; }
  cat "$tmp" >"$file"
  rm -f "$tmp"
}

for file in .cursor-plugin/plugin.json .cursor-plugin/marketplace.json .claude-plugin/plugin.json \
  .claude-plugin/marketplace.json .agents/plugins/marketplace.json; do
  set_manifest "$file"
done

tmp=$(mktemp)
sed "1s/.*/<!-- gabriel-skills-agents v$version -->/" AGENTS.md >"$tmp" || { rm -f "$tmp"; echo "set-version.sh: could not rewrite AGENTS.md"; exit 1; }
cat "$tmp" >AGENTS.md
rm -f "$tmp"
