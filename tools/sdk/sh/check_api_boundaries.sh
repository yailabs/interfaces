#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

fail() {
  echo "api-boundary-check: $1" >&2
  exit 1
}

PUBLIC_HEADER="$ROOT/packages/c/include/yai_sdk/public.h"
if rg -n "yai_sdk/registry/" "$PUBLIC_HEADER" >/dev/null 2>&1; then
  fail "public.h must not include registry internal headers"
fi

# Legacy wrappers are removed; block reintroduction.
if [[ -e "$ROOT/include/yai_sdk/yai_sdk.h" || -e "$ROOT/include/yai_sdk/yai.h" ]]; then
  fail "legacy wrapper headers must not exist"
fi
if [[ -e "$ROOT/include/yai_sdk/registry/command_catalog.h" ]]; then
  fail "legacy command_catalog compat header must not exist"
fi

# If sibling CLI repo exists, ensure it does not include SDK registry internals
# and does not regress to legacy workspace command ids.
CLI_ROOT="$(cd "$ROOT/.." && pwd)/cli"
if [[ -d "$CLI_ROOT" ]]; then
  if rg -n "#include\s+[<\"]yai_sdk/registry/" "$CLI_ROOT/include" "$CLI_ROOT/src" "$CLI_ROOT/tests" -S >/dev/null 2>&1; then
    rg -n "#include\s+[<\"]yai_sdk/registry/" "$CLI_ROOT/include" "$CLI_ROOT/src" "$CLI_ROOT/tests" -S >&2 || true
    fail "cli includes SDK internal registry headers"
  fi
  if rg -n "yai\.workspace\.(activate|deactivate)" "$CLI_ROOT/src" "$CLI_ROOT/tests" -S >/dev/null 2>&1; then
    rg -n "yai\.workspace\.(activate|deactivate)" "$CLI_ROOT/src" "$CLI_ROOT/tests" -S >&2 || true
    fail "cli uses legacy workspace command ids; use set/switch/unset/clear"
  fi
fi

echo "api-boundary-check: ok"
