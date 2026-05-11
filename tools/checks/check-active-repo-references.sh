#!/usr/bin/env sh
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
interfaces_root=$(CDPATH= cd -- "$script_dir/../.." && pwd)
workspace_root=$(CDPATH= cd -- "$interfaces_root/.." && pwd)

cd "$workspace_root"

paths="
yai/Documentation
yai/README.md
interfaces/Documentation
interfaces/README.md
interfaces/VERSIONING.md
console/Documentation
console/README.md
console/PRODUCT.md
sdk/README.md
sdk/TOMBSTONE.md
sdk/MIGRATION.md
"

api_pattern='github.com/yailabs/api|yailabs/api|\.\./api|api repo|api repository|API repo|API repository|standalone API|standalone api'
sdk_pattern='github.com/yailabs/sdk|yailabs/sdk|\.\./sdk|sdk repo|sdk repository|SDK repo|SDK repository|standalone SDK|standalone sdk'

status=0

scan() {
  label=$1
  pattern=$2

  if ! command -v rg >/dev/null 2>&1; then
    echo "active-repo-reference: warning: rg unavailable; skipping $label scan"
    return 0
  fi

  hits=$(rg -n "$pattern" $paths \
    --glob '!**/archive/**' \
    --glob '!**/internal/**' || true)

  if [ -z "$hits" ]; then
    echo "active-repo-reference: $label: no hits"
    return 0
  fi

  tmp_file=$(mktemp "${TMPDIR:-/tmp}/yai-active-repo-reference.XXXXXX")
  printf '%s\n' "$hits" > "$tmp_file"

  while IFS= read -r line; do
    case "$line" in
      *'@yailabs/sdk'*|*'yailabs-yai-sdk'*|*'yai_sdk'*|*'<yai_sdk/'*|*'include/yai_sdk'*)
        echo "active-repo-reference: allowed-package-or-import: $line"
        ;;
      *'tombstone'*|*'Tombstone'*|*'historical'*|*'Historical'*|*'old standalone SDK repository'*|*'Old standalone SDK repository'*|*'Old API repository name'*)
        echo "active-repo-reference: allowed-tombstone-or-history: $line"
        ;;
      *'api-envelope'*|*'api-error'*|*'api-families'*|*'api-operations'*|*'api-verbs'*|*'API surface'*|*'SDK/API surface'*)
        echo "active-repo-reference: allowed-concept-term: $line"
        ;;
      *)
        echo "active-repo-reference: forbidden: $line"
        status=1
        ;;
    esac
  done < "$tmp_file"

  rm -f "$tmp_file"
}

scan "api" "$api_pattern"
scan "sdk" "$sdk_pattern"

exit "$status"
