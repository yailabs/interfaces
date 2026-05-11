#!/usr/bin/env bash
set -euo pipefail

# Compatibility helper: resolve a LAW repository root for build-time headers.
# No structural dependency pin is implied by this lookup.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"

if [[ -n "${YAI_SDK_COMPAT_LAW_DIR:-}" && -f "${YAI_SDK_COMPAT_LAW_DIR}/contracts/protocol/include/protocol.h" ]]; then
  echo "${YAI_SDK_COMPAT_LAW_DIR}"
  exit 0
fi

CANDIDATES=(
  "${REPO_ROOT}/compat/law-export"
  "${REPO_ROOT}/deps/law"
  "${REPO_ROOT}/../law"
)

for p in "${CANDIDATES[@]}"; do
  if [[ -f "${p}/contracts/protocol/include/protocol.h" ]]; then
    echo "${p}"
    exit 0
  fi
done

echo "WARN: compatibility law export not found." >&2
echo "Set YAI_SDK_COMPAT_LAW_DIR or provide ../law for local builds." >&2
exit 2
