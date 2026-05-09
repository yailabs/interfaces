# A2 — Operation Transport Mapping Drift Reconciliation

## Status
Delivery: A2
Status: done
Track: A-series / API transport mapping
Repo branch: refoundation/phase-01
Previous delivery: A1 — Console Canonicalization / Legacy CLI-Loom Drain
Next delivery: A3 — Case Topology Vocabulary / System Case vs Work Case Boundary

## Purpose
Explain that A2 reconciles the API mapping with RT.04 runtime reality and A1
Console naming without widening runtime, SDK, Console, CLI-compat, or
Loom-compat behavior.

The canonical mapping JSON and schema already reflected the audited RT.04 Local
IPC RPC truth in this checkout, so A2 leaves those data surfaces unchanged and
reconciles the surrounding documentation, conformance wording, and A-series
delivery markers.

The current `api` checkout uses `Documentation/` as the canonical
documentation root. Older delivery boxes may still say `docs/`; A2 updates the
verified canonical surface instead of recreating a parallel `docs/` tree.

Console is the canonical terminal client. CLI and Loom remain compatibility or
historical names only where they are referenced.

## Files Changed
| File | Change type | Reason |
| ---- | ----------- | ------ |
| `Documentation/operation-to-transport-mapping.md` | update | move active transport-mapping narrative from A1 to A2 and preserve Console canonical naming |
| `Documentation/waves/a-series-map.md` | update | mark A1 done, A2 done, and A3 next in the accepted A-series sequence |
| `Documentation/waves/a2-operation-transport-mapping-drift-reconciliation.md` | add | record the A2 reconciliation outcome on the canonical `Documentation/` surface |
| `mappings/transport-selection-policy.v1.md` | update | keep RT.04 IPC truth scoped to A2 and preserve Console-first client naming |
| `mappings/streamable-operation-policy.v1.md` | update | keep request/response IPC audit separate from stream support while preserving Console naming |
| `mappings/provider-transport-exclusion-policy.v1.md` | update | keep provider/model transport excluded and preserve compatibility naming boundaries |
| `conformance/check_operation_transport_mapping.py` | update | validate A2 documentation surfaces and preserve Console naming guardrails where this delivery touches active docs |
| `conformance/README.md` | update | describe the A2 RT.04 IPC coverage enforcement accurately |

## Runtime Reality Consumed
`local_ipc_rpc = read_projection_probe_ready`

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

Blocked or unsupported over Local IPC RPC:
- `conversation.messages.send`
- mutating case operations
- provider invocation
- model invocation
- unknown operations

## Mapping Result
| Operation | `local_ipc_rpc` status | Reason |
| --------- | ---------------------- | ------ |
| `system.status` | supported | preserved RT.03 safe status surface and supported by RT.04 safe read/projection dispatch |
| `system.check` | supported | supported by RT.04 safe read/projection dispatch |
| `system.runtime.inspect` | supported | supported by RT.04 safe read/projection dispatch |
| `case.current` | deferred | audited in RT.04; existing case projection path remains wider than the current safe IPC probe surface |
| `case.list` | deferred | audited in RT.04; existing case registry/list projection path remains wider than the current safe IPC probe surface |
| `case.show` | deferred | audited in RT.04; existing case lookup projection path remains wider than the current safe IPC probe surface |
| `providers.list` | deferred | audited in RT.04; must not imply provider transport calls, credential reads, or provider availability |
| `models.list` | deferred | audited in RT.04; must not imply model load, model invocation, or model availability |

## Provider/Model Boundary
Provider/model transport remains excluded from client-runtime transport
selection.

- `providers.list` remains a client-runtime read surface in contract terms, but
  its IPC runtime coverage remains deferred.
- `models.list` remains a client-runtime read surface in contract terms, but
  its IPC runtime coverage remains deferred.
- `providers.list` must not imply provider transport calls, provider credential
  reads, or provider availability.
- `models.list` must not imply model load, model invocation, or model
  availability.
- Provider transport and model execution remain outside client-runtime
  transport selection.

## A0/A1 Boundary Preservation
A2 does not implement `client_subject_ref`, `system_call_ref`,
control-plane admission, system call record materialization, or case topology
rename.

A2 preserves Console as the canonical terminal client wording where active
client naming is touched.

## Validation Commands
| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| `api` | `git status --short` | pass | only the scoped A2 doc/policy/checker files are modified in the worktree |
| `api` | `git branch --show-current` | pass | `refoundation/phase-01` |
| `api` | `python3 conformance/check_operation_transport_mapping.py` | pass | `operation-transport-map: ok` |
| `api` | `python3 conformance/check_transport_contract_index.py` | pass | `transport-contract-index: ok` |
| `api` | `python3 conformance/check_api_envelope_error_stream.py` | pass | `api-envelope-error-stream: ok` |
| `api` | `python3 -m json.tool mappings/operation-transport-map.v1.json >/dev/null` | pass | mapping JSON parses |
| `api` | `git diff --check` | pass | no patch formatting drift |
| `yai` | `python3 tools/build/check_local_ipc_rpc_operation_coverage.py` | fail | pre-existing reference drift: probe output no longer contains the `e2e.*payload=` markers expected by the checker |
| `yai` | `~/.cache/yai/build/yai/bin/local-ipc-rpc-probe` | pass with drift noted | command exits and reports `read_projection_probe_ready`, but the output shape is narrower than the checker expects |
| `yai` | `git diff --check` | pass | no formatting drift in `yai` worktree |
| `sdk` | `cargo test --manifest-path packages/rust/Cargo.toml` | pass | 11 unit tests, 8 Local IPC RPC transport tests, and doc tests passed |
| `sdk` | `git diff --check` | pass | no SDK patch formatting drift |
| `console` | `cargo fmt --check` | pass | formatting clean |
| `console` | `cargo test` | pass | 25 tests passed across unit, contract, snapshot, and smoke suites |
| `console` | `cargo build` | pass | build succeeded |
| `console` | `git diff --check` | pass | no Console patch formatting drift |
| `cli` | `test ! -e source` | pass | `source/` remains absent |
| `cli` | `scripts/check-no-source-dependency.sh` | fail | script is absent in the current `cli` checkout |
| `cli` | `cargo test` | fail | current `cli` checkout has no `Cargo.toml`; repo appears reduced to a minimal README surface |
| `cli` | `git diff --check` | pass | no CLI patch formatting drift |
| `loom` | `cargo fmt --check` | not run | `/home/mothx/COMPUTER_SCIENCE/DEV_CODE/YAI/loom` is not present in the current workspace |
| `loom` | `cargo test` | not run | `/home/mothx/COMPUTER_SCIENCE/DEV_CODE/YAI/loom` is not present in the current workspace |
| `loom` | `cargo build` | not run | `/home/mothx/COMPUTER_SCIENCE/DEV_CODE/YAI/loom` is not present in the current workspace |
| `loom` | `git diff --check` | not run | `/home/mothx/COMPUTER_SCIENCE/DEV_CODE/YAI/loom` is not present in the current workspace |
| `all` | `rg -n "full IPC operation coverage\|IPC production ready\|all operations supported over IPC\|provider transport called by IPC\|model invoked by IPC\|state mutation over IPC\|LAN listener implemented\|HTTP server implemented\|Remote HTTPS client implemented\|client_subject_ref implemented\|system_call_ref implemented\|control plane admission implemented\|Loom as canonical terminal client\|CLI as canonical terminal client" ../api ../yai ../sdk ../console ../cli ../loom 2>/dev/null \|\| true` | pass/classified | matches appear in negative policy text, checker forbidden-phrase lists, or historical wave-report command text; no positive forbidden implementation claim was introduced by A2 |

## Non-Implementation Confirmation
No runtime, SDK, Console, CLI-compat, Loom-compat, OpenAPI, registry
expansion, transport behavior, or SCL behavior changed.
