# A1 — Operation Transport Mapping Drift Reconciliation

## Status
Delivery: A1
Status: done
Track: A-series / API transport mapping
Repo branch: refoundation/phase-01
Previous delivery: A0 — Unified Spine Reality Audit
Next delivery: A2 — Case Topology Vocabulary / System Case vs Work Case Boundary

## Purpose
Reconcile the API operation-to-transport mapping with the verified RT.04 Local
IPC RPC runtime reality.

A1 is mapping, conformance, and documentation only. It does not add runtime,
SDK, CLI, Loom, transport, or system-call-lineage behavior.

The current `api` checkout uses `Documentation/` as the verified documentation
root. The delivery box still names `docs/`; A1 updates the canonical surface
that exists in the tree instead of recreating a parallel `docs/` directory.

## Files Changed
| File | Change type | Reason |
| ---- | ----------- | ------ |
| `mappings/operation-transport-map.v1.json` | update | add explicit RT.04 Local IPC RPC coverage markers for supported, deferred, and blocked audited operations |
| `mappings/operation-transport-map.v1.schema.json` | update | allow narrow A1 fields for IPC coverage, readiness, and notes |
| `mappings/transport-selection-policy.v1.md` | update | state that contract-allowed transport is not the same as audited runtime support |
| `mappings/streamable-operation-policy.v1.md` | update | preserve stream boundary and prevent RT.04 IPC audit from widening stream claims |
| `mappings/provider-transport-exclusion-policy.v1.md` | update | preserve provider/model exclusion for `providers.list` and `models.list` |
| `Documentation/operation-to-transport-mapping.md` | update | document the explicit A1 IPC coverage fields and the `Documentation/` topology reality |
| `Documentation/waves/a1-operation-transport-mapping-drift-reconciliation.md` | add | record the A1 delivery outcome |
| `conformance/check_operation_transport_mapping.py` | update | validate explicit RT.04 IPC coverage truth and keep provider/model, LAN, Remote, and stream guardrails |
| `conformance/README.md` | update | note the A1 RT.04 Local IPC RPC coverage enforcement |

## Runtime Reality Consumed
`local_ipc_rpc` runtime readiness: `read_projection_probe_ready`

Supported over Local IPC RPC:
- `system.status`
- `system.check`
- `system.runtime.inspect`

Deferred over Local IPC RPC:
- `case.current`
- `case.list`
- `case.show`
- `providers.list`
- `models.list`

Blocked or unsupported in the RT.04 audited probe surface:
- `conversation.messages.send`
- provider/model invocation surfaces such as `providers.calls.run` and `models.runs.run`
- unknown operations

## Mapping Result
| Operation | `local_ipc_rpc` status | Reason |
| --------- | ---------------------- | ------ |
| `system.status` | supported | preserved RT.03 status/read surface and supported by RT.04 safe read/projection dispatch |
| `system.check` | supported | supported by RT.04 safe read/projection dispatch |
| `system.runtime.inspect` | supported | supported by RT.04 safe read/projection dispatch |
| `case.current` | deferred | audited in RT.04; existing case projection path is wider than the controlled probe surface |
| `case.list` | deferred | audited in RT.04; existing case registry/list projection path is wider than the controlled probe surface |
| `case.show` | deferred | audited in RT.04; existing case lookup projection path is wider than the controlled probe surface |
| `providers.list` | deferred | audited in RT.04; no safe static provider registry projection is wired into the IPC probe path |
| `models.list` | deferred | audited in RT.04; no safe static model registry projection is wired into the IPC probe path |

Blocked examples were recorded explicitly in mapping data as `runtime_ipc_coverage=blocked` for `conversation.messages.send`, `providers.calls.run`, and `models.runs.run`.

## Provider/Model Boundary
Provider/model transport remains excluded from client-runtime transport
selection.

- `providers.list` stays a client-runtime read surface in contract terms, but
  its A1 IPC reality is `deferred`.
- `models.list` stays a client-runtime read surface in contract terms, but its
  A1 IPC reality is `deferred`.
- `providers.list` must not imply provider transport calls, credential reads,
  or provider availability.
- `models.list` must not imply model load, model invocation, or model
  availability.
- `providers.calls.run` and `models.runs.run` remain blocked over the audited
  RT.04 Local IPC RPC surface.

## A0 Boundary Preservation
A1 does not implement `client_subject_ref`, `system_call_ref`,
control-plane admission, or system call record materialization.

Those remain future A-series work for A2/A3/A4/A5/A6.

## Validation Commands
| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| `api` | `python3 conformance/check_operation_transport_mapping.py` | pass | explicit RT.04 IPC coverage markers validated |
| `api` | `python3 conformance/check_transport_contract_index.py` | pass | transport contract index still aligned |
| `api` | `python3 conformance/check_api_envelope_error_stream.py` | pass | envelope/error/stream contract unchanged |
| `api` | `python3 -m json.tool mappings/operation-transport-map.v1.json >/dev/null` | pass | mapping JSON parses |
| `api` | `git diff --check` | pass | no patch-format drift |
| `yai` | `python3 tools/build/check_local_ipc_rpc_operation_coverage.py` | pass | RT.04 coverage truth still validated |
| `yai` | `~/.cache/yai/build/yai/bin/local-ipc-rpc-probe` | pass | manual probe showed `read_projection_probe_ready` plus supported/deferred/blocked/unsupported behavior |
| `yai` | `git diff --check` | pass | no formatting drift introduced in `yai` |
| `sdk` | `cargo test --manifest-path packages/rust/Cargo.toml` | pass | SDK transport/tests unchanged and compatible |
| `sdk` | `git diff --check` | pass | no SDK patch-format drift |
| `cli` | `test ! -e source` | pass | source tree drain guard still holds |
| `cli` | `scripts/check-no-source-dependency.sh` | pass | no CLI source dependency regression |
| `cli` | `cargo test` | pass | CLI unchanged; tests passed with pre-existing warnings only |
| `cli` | `git diff --check` | pass | no CLI patch-format drift |
| `loom` | `cargo test` | pass | Loom unchanged |
| `loom` | `git diff --check` | pass | no Loom patch-format drift |
| `all` | `rg -n "full IPC operation coverage\|IPC production ready\|all operations supported over IPC\|provider transport called by IPC\|model invoked by IPC\|state mutation over IPC\|LAN listener implemented\|HTTP server implemented\|Remote HTTPS client implemented\|client_subject_ref implemented\|system_call_ref implemented\|control plane admission implemented" ../api ../yai ../sdk ../cli ../loom 2>/dev/null \|\| true` | pass/classified | matches appeared only in negative policy text, checker forbidden-phrase lists, or historical wave-report command text; no positive forbidden implementation claims found |

## Non-Implementation Confirmation
- No runtime behavior changed.
- No SDK behavior changed.
- No CLI behavior changed.
- No Loom behavior changed.
- No OpenAPI surface changed.
- No registry operation IDs were added.
- No transport behavior changed.
- No LAN, HTTP, or Remote behavior changed.
- No provider/model invocation behavior changed.
- No SCL behavior changed.
