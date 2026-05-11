#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

blocked=(
  "packages/rust/target"
  "packages/typescript/node_modules"
  "packages/typescript/dist"
  "packages/c/build"
  "packages/c/dist"
)

failed=0
for rel in "${blocked[@]}"; do
  if [[ -d "$ROOT/$rel" ]]; then
    printf 'generated-output-exclusion: forbidden directory exists: %s\n' "$rel" >&2
    failed=1
  fi
done

if [[ "$failed" -ne 0 ]]; then
  exit 1
fi

printf 'generated-output-exclusion: ok\n'
