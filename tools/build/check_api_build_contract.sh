#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "${script_dir}/../.." && pwd)"

if [[ ! -f "${repo_root}/conformance/check_api_contracts.py" ]]; then
  echo "missing conformance/check_api_contracts.py" >&2
  exit 1
fi

if [[ ! -f "${repo_root}/Documentation/build/api-build-contract.md" ]]; then
  echo "missing Documentation/build/api-build-contract.md" >&2
  exit 1
fi

cd "${repo_root}"
python3 conformance/check_api_contracts.py

echo "api build contract check: ok"
