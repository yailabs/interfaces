# API.10 — Operation Transport Mapping Drift Reconciliation

## Status

* Delivery: API.10
* Status: done
* Track: API / Transport mapping conformance
* Repo branch: `refoundation/phase-01`
* Repo change type: operation-to-transport mapping alignment with current runtime reality
* Previous delivery: RT.04 — Local IPC RPC Operation Coverage Expansion
* Next delivery: CLI.03 — Broader CLI IPC Runtime Surface or RT.HTTP.01 — Local HTTP Loopback Runtime Server Skeleton

## Purpose

Reconcile `operation-transport-map.v1.json` with the current registry and with
the RT.04 Local IPC RPC runtime reality.

This wave is mapping and conformance only.
It does not add runtime, SDK, CLI, or Loom behavior.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| `api` | `mappings/operation-transport-map.v1.json` | update | reconcile mapping entry count, registry parity, and RT.04 IPC coverage notes |
| `api` | `conformance/check_operation_transport_mapping.py` | update | enforce RT.04 mapping truth for supported/deferred IPC read surfaces |
| `api` | `Documentation/operation-to-transport-mapping.md` | update | document mapping as contract + readiness projection rather than runtime implementation claim |
| `api` | `transports/implementation-readiness-matrix.v1.json` | update | sync Local IPC RPC readiness with RT.04 reality |
| `api` | `transports/implementation-readiness-matrix.v1.md` | update | sync Local IPC RPC readiness wording with RT.04 reality |
| `api` | `Documentation/waves/api-10-operation-transport-mapping-drift-reconciliation.md` | add | record API.10 outcomes |

## Reconciliation Result

RT.04-supported IPC operations are now represented explicitly in mapping notes:
- `system.status`
- `system.check`
- `system.runtime.inspect`

RT.04-deferred IPC operations are now represented explicitly in mapping notes:
- `case.current`
- `case.list`
- `case.show`
- `providers.list`
- `models.list`

Provider/model execution remains excluded from client-runtime transport
selection and mutating/provider/model execution notes now state that current
RT.04 Local IPC RPC probe coverage is blocked or unsupported until separately
justified.

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| `api` | `python3 conformance/check_operation_transport_mapping.py` | pass | mapping count, registry parity, and RT.04 IPC notes aligned |
| `api` | `python3 conformance/check_transport_contract_index.py` | pass | transport index still valid |
| `api` | `python3 conformance/check_api_envelope_error_stream.py` | pass | envelope/error stream unchanged and valid |
| `api` | `python3 -m json.tool mappings/operation-transport-map.v1.json >/dev/null` | pass | mapping JSON well-formed |
| `api` | `git diff --check` | pass | no patch-format drift |
| `yai` | `python3 tools/build/check_local_ipc_rpc_operation_coverage.py` | pass | RT.04 runtime truth still valid |
| `yai` | `git diff --check` | pass | no formatting drift in `yai` |
| `sdk` | `cargo test --manifest-path packages/rust/Cargo.toml` | pass | SDK unchanged and compatible |
| `sdk` | `git diff --check` | pass | no SDK formatting drift |
| `cli` | `test ! -e source && scripts/check-no-source-dependency.sh && cargo test` | pass | CLI unchanged |
| `cli` | `git diff --check` | pass | no CLI formatting drift |
| `loom` | `cargo test` | pass | Loom unchanged |
| `loom` | `git diff --check` | pass | no Loom formatting drift |

## Non-Implementation Confirmation

- no runtime behavior added
- no SDK behavior added
- no CLI behavior changed
- no Loom behavior changed
- no Local HTTP implementation added
- no Local Event Stream implementation added
- no LAN or Remote HTTPS behavior changed
