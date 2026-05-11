# V53 — API Auth Surfaces

## Status

* Delivery: V53
* Status: done
* Track: V — API Canon
* Branch: `refoundation/phase-01`
* Previous delivery: V52 — API Case Expansion
* Next delivery: V54 — API Operator Context Surfaces

## Scope

Recorded and delivered:

* auth operations added and normalized
* auth response schema and fixtures
* no-session auth boundary recorded
* auth versus entitlement, machine, license, and runtime boundary recorded
* logout boundary recorded
* auth-specific conformance checks

Not delivered:

* CLI behavior changes
* SDK generation
* TUI behavior
* runtime implementation
* provider auth implementation
* browser or device login implementation
* endpoint/server implementation

## Files Changed

| File | Change |
| ---- | ------ |
| `registry/api-families.v1.json` | clarified canonical auth family meaning and no-session notes |
| `registry/api-surfaces.v1.json` | expanded canonical public auth surface |
| `registry/api-operations.v1.json` | added and normalized V53 auth operation set |
| `registry/api-operation-projections.v1.json` | added auth projection rule and deprecated `auth.whoami` alias mapping |
| `registry/yai-actions.v1.json` | corrected stale `auth.login.local_dev` mapping and added future auth action rows |
| `schemas/auth-operation.v1.schema.json` | added V53 auth operation response envelope |
| `fixtures/auth-operation/*.json` | added canonical auth-operation fixtures |
| `conformance/check_auth_operations.py` | added V53 auth conformance checks |
| `conformance/check_operation_registry.py` | extended registry conformance for canonical auth operations |
| `Documentation/api-auth-surfaces.md` | documented V53 auth API decisions |
| `Documentation/waves/v53-api-auth-surfaces.md` | recorded delivery report |

## Operation Summary

| Operation | Status | Meaning |
| --------- | ------ | ------- |
| `auth.login` | canonical | request canonical login posture |
| `auth.login.local_dev` | compatibility canonicalized | local-dev login bootstrap with explicit non-production meaning |
| `auth.status` | canonical | inspect auth posture |
| `auth.logout` | canonical | clear auth posture only |
| `auth.context.inspect` | future API contract | inspect safe auth-context projection |
| `auth.provider.status` | future API contract | inspect provider-auth adapter posture safely |
| `auth.device_login.start` | future API contract | start device-login contract only |
| `auth.device_login.status` | future API contract | inspect device-login attempt contract |
| `auth.device_login.cancel` | future API contract | cancel device-login attempt contract |
| `auth.whoami` | deprecated compatibility | older wording mapped to `auth.context.inspect` |

## Fixture Summary

| Fixture | Coverage |
| ------- | -------- |
| `auth-login-unavailable.json` | production login unavailable posture |
| `auth-login-local-dev.json` | local-dev login posture |
| `auth-status-unauthenticated.json` | unauthenticated auth status |
| `auth-status-local-dev.json` | local-dev auth status |
| `auth-logout-clears-auth-only.json` | logout clears auth only |
| `auth-context-inspect-safe.json` | safe auth-context inspection |
| `auth-provider-status-not-configured.json` | provider-auth not configured posture |
| `auth-device-login-start-contract.json` | contract-only future device login start |

## Validation

| Repo | Command | Result |
| ---- | ------- | ------ |
| `api` | `test -f Documentation/api-auth-surfaces.md` | pass |
| `api` | `test -f Documentation/waves/v53-api-auth-surfaces.md` | pass |
| `api` | `test -f schemas/auth-operation.v1.schema.json` | pass |
| `api` | `test -f conformance/check_auth_operations.py` | pass |
| `api` | `python3 -m json.tool schemas/auth-operation.v1.schema.json >/dev/null` | pass |
| `api` | `find fixtures/auth-operation -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass |
| `api` | `python3 conformance/check_auth_operations.py` | pass |
| `api` | `python3 conformance/check_case_operations.py` | pass |
| `api` | `python3 conformance/check_yai_actions_registry.py` | pass |
| `api` | `python3 conformance/check_operation_registry.py` | pass |
| `api` | `python3 conformance/check_api_contracts.py` | pass |
| `api` | `git diff --check` | pass |
| `cli` | `test ! -e source` | pass |
| `cli` | `scripts/check-no-source-dependency.sh` | pass |
| `cli` | `cargo fmt --check` | pass |
| `cli` | `cargo test` | pass |
| `cli` | `cargo build` | pass |
| `cli` | `git diff --check` | pass |
| `yai` | `make info` | pass |
| `yai` | `make yai` | pass |
| `yai` | `git diff --check` | pass |
| `sdk` | `git diff --check` | pass |
| `loom` | `git diff --check` | pass |

## Completion Checklist

* full auth operation set exists: yes
* auth does not own session: yes
* auth does not imply entitlement, machine authorization, license lease, or runtime allowed: yes
* logout boundary recorded: yes
* schema created: yes
* fixtures created: yes
* auth conformance passes: yes
* operation registry conformance passes: yes
* no CLI, SDK, TUI, or runtime behavior added: yes
