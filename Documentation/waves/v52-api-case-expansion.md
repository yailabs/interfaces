# V52 — API Case Expansion

## Status

* Delivery: V52
* Status: done
* Track: V — API Canon
* Branch: `refoundation/phase-01`
* Previous delivery: V51 — API Registry Refactor
* Next delivery: V53 — API Auth Surfaces

## Scope

Recorded and delivered:

* canonical `case` API operation expansion
* case response schema and fixtures
* operator-context boundary alignment
* legacy/deprecated case naming mappings
* case-specific conformance checks

Not delivered:

* CLI behavior changes
* SDK generation
* TUI behavior
* runtime implementation
* endpoint/server implementation

## Files Changed

| File | Change |
| ---- | ------ |
| `registry/api-operations.v1.json` | added canonical `case.root/open/enter/leave/status/close`; deprecated `case.create` and `case.use`; normalized case response schemas |
| `registry/api-operation-projections.v1.json` | added case projection rule and deprecated alias mappings |
| `registry/api-surfaces.v1.json` | expanded canonical public case surface |
| `registry/api-families.v1.json` | clarified case family description and resources |
| `registry/yai-actions.v1.json` | corrected stale `case.*` API candidates and `case.close` implementation metadata |
| `schemas/case-operation.v1.schema.json` | added V52 case response envelope |
| `fixtures/case-operation/*.json` | added canonical case-operation fixtures |
| `conformance/check_case_operations.py` | added V52 case conformance checks |
| `conformance/check_operation_registry.py` | extended registry conformance for canonical case operations |
| `Documentation/api-case-expansion.md` | documented V52 API case decisions |
| `Documentation/waves/v52-api-case-expansion.md` | recorded delivery report |

## Registry Decisions

| Decision | Result |
| -------- | ------ |
| `case` canonical over `session` | enforced |
| active case owned by operator context | enforced |
| `case.open` distinct from `case.enter` | enforced |
| `case.leave` clears operator context only | enforced |
| `case.close` non-destructive by default | enforced in schema, fixtures, and docs |
| `case.create` -> `case.open` | deprecated compatibility alias |
| `case.use` -> `case.enter` | deprecated compatibility alias |

## Action Registry Alignment

* `yai-actions` consumed: yes
* remaining drift: `context.*` remains unresolved and intentionally deferred
* tiny V52 corrections applied: yes, only for stale `case.*` API candidate and
  implementation metadata

## Validation

| Repo | Command | Result |
| ---- | ------- | ------ |
| `api` | `python3 -m json.tool registry/yai-actions.v1.json >/dev/null` | pass |
| `api` | `python3 -m json.tool registry/api-families.v1.json >/dev/null` | pass |
| `api` | `python3 -m json.tool registry/api-operations.v1.json >/dev/null` | pass |
| `api` | `python3 -m json.tool registry/api-operation-projections.v1.json >/dev/null` | pass |
| `api` | `python3 -m json.tool registry/api-surfaces.v1.json >/dev/null` | pass |
| `api` | `python3 conformance/check_case_operations.py` | pass |
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

* full canonical API case operation set added or normalized: yes
* request/response envelope shape defined: yes
* case tree vs operator context split documented: yes
* `case.close` non-destructive by default: yes
* `case` kept distinct from session: yes
* `case.create` legacy/deprecated path recorded: yes
* `case.use` legacy/deprecated path recorded: yes
* V52 case conformance check added: yes
* no CLI/SDK/TUI/runtime implementation changes: yes

## Drift Note

The delivery box referenced lowercase `api/docs/...` paths, but the current
repo truth uses `api/Documentation/...` as the live canonical documentation
surface. V52 aligned to the repository rather than inventing a new doc root.
