#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

required_roots=(
  "registry/api-operations.v1.json"
  "schemas"
  "mappings/operation-transport-map.v1.json"
  "envelopes"
  "errors"
  "packages/rust/README.md"
  "packages/python/README.md"
  "packages/typescript/README.md"
  "packages/c/README.md"
)

failed=0
for rel in "${required_roots[@]}"; do
  if [[ ! -e "$rel" ]]; then
    printf 'package-protocol-drift: missing required root artifact: %s\n' "$rel" >&2
    failed=1
  fi
done

blocked_generated=(
  "packages/rust/target"
  "packages/typescript/node_modules"
  "packages/typescript/dist"
  "packages/c/build"
  "packages/c/dist"
)

for rel in "${blocked_generated[@]}"; do
  if [[ -d "$rel" ]]; then
    printf 'package-protocol-drift: forbidden generated output present: %s\n' "$rel" >&2
    failed=1
  fi
done

if [[ "$failed" -ne 0 ]]; then
  exit 1
fi

scan() {
  local pattern="$1"
  local label="$2"
  shift 2
  if command -v rg >/dev/null 2>&1; then
    if rg -n "$pattern" "$@" >/tmp/yai-intf6-drift-scan.out 2>/dev/null; then
      printf 'package-protocol-drift: warning: %s\n' "$label" >&2
      cat /tmp/yai-intf6-drift-scan.out >&2
    fi
  else
    if grep -R -n -E "$pattern" "$@" >/tmp/yai-intf6-drift-scan.out 2>/dev/null; then
      printf 'package-protocol-drift: warning: %s\n' "$label" >&2
      cat /tmp/yai-intf6-drift-scan.out >&2
    fi
  fi
}

scan 'YAI_SDK_CMD_WORKSPACE_' 'C compatibility command-id vocabulary requires manual review' packages/c
scan 'const[[:space:]]+[A-Za-z0-9_]*OPERATION|static[[:space:]]+const[[:space:]].*operation|operationId|operation_id' 'hardcoded operation constants or operation ids may require protocol alignment review' packages/rust packages/python packages/typescript packages/c
scan 'struct[[:space:]].*(Envelope|Status|Error)|class[[:space:]].*(Envelope|Status|Error)|interface[[:space:]].*(Envelope|Status|Error)|type[[:space:]].*(Envelope|Status|Error)' 'duplicated envelope/status/error package types may require projection provenance review' packages/rust packages/python packages/typescript packages/c

printf 'package-protocol-drift: ok with manual-review warnings if printed\n'
