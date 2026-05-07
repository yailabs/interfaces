# API.06 — Local Event Stream Contract Verticalization

## Status

* Delivery: API.06
* Status: done
* Track: API / Transport / SDK / Runtime alignment
* Repo branch: `refoundation/phase-01`
* Repo change type: Local Event Stream contract verticalization
* Previous delivery: API.05 — Local HTTP Loopback Contract Verticalization
* Next delivery: API.07 — LAN Secure Contract Verticalization

## Purpose

API.06 defines Local Event Stream as the primary realtime projection transport
contract before implementation.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| `api` | `transports/local-event-stream.v1.md` | modified | expand the root Local Event Stream contract and link the verticalized subtree |
| `api` | `transports/local-event-stream/README.md` | added | create the Local Event Stream contract root |
| `api` | `transports/local-event-stream/sse-binding.v1.md` | added | define SSE as the primary web binding |
| `api` | `transports/local-event-stream/rpc-stream-binding.v1.md` | added | define RPC-over-IPC as the primary native-local stream binding |
| `api` | `transports/local-event-stream/websocket-reservation.v1.md` | added | reserve WebSocket for future bidirectional use only |
| `api` | `transports/local-event-stream/event-frame.v1.schema.json` | added | freeze the Local Event Stream event-frame schema |
| `api` | `transports/local-event-stream/event-types.v1.json` | added | register canonical event types |
| `api` | `transports/local-event-stream/subscription-model.v1.md` | added | define stream open and subscribe posture |
| `api` | `transports/local-event-stream/heartbeat-reconnect.v1.md` | added | define heartbeat, reconnect, and resume posture |
| `api` | `transports/local-event-stream/backpressure-resume.v1.md` | added | define slow-consumer and resume posture |
| `api` | `transports/local-event-stream/security-redaction.v1.md` | added | define projection-safe and redacted stream payload posture |
| `api` | `transports/local-event-stream/errors-terminal-events.v1.md` | added | preserve transport vs operation stream errors and terminal-event semantics |
| `api` | `transports/local-event-stream/conformance-profile.v1.md` | added | define minimum contract claims for future implementations |
| `api` | `docs/local-event-stream-contract.md` | added | summarize the API.06 contract |
| `api` | `docs/waves/api-06-local-event-stream-contract-verticalization.md` | added | record scope and validation |
| `api` | `conformance/check_local_event_stream_contract.py` | added | validate Local Event Stream contract structure and wording |
| `api` | `conformance/README.md` | modified | register the new API.06 conformance checker |
| `api` | `mappings/streamable-operation-policy.v1.md` | modified | cross-link streamable policy to the Local Event Stream contract subtree |
| `api` | `mappings/transport-selection-policy.v1.md` | modified | cross-link selection policy to the Local Event Stream contract |
| `api` | `transports/README.md` | modified | cross-link the verticalized Local Event Stream subtree |
| `yai` | `runtime/connections/README.md` | modified | document future stream observation scope |
| `yai` | `runtime/boundary/transport/README.md` | modified | align future SSE/RPC stream carrier ownership |
| `yai` | `runtime/boundary/service/README.md` | modified | place SSE under future service exposure and reserve WebSocket |
| `yai` | `runtime/boundary/api/README.md` | modified | clarify streamable dispatch handoff without physical serving |
| `sdk` | `generated/README.md` | modified | keep generated realtime artifacts as API contract projections only |
| `sdk` | `packages/typescript/README.md` | modified | align TypeScript realtime ownership to Local Event Stream and SSE |
| `sdk` | `packages/rust/README.md` | modified | align Rust native-local realtime ownership to RPC streaming over IPC later |

## Existing Surface Audit

| Surface | Result | Notes |
| ------- | ------ | ----- |
| `api/transports/local-event-stream.v1.md` | updated | pre-existing root contract now points to a verticalized subtree |
| `api` streamable operations | audited | current watchable operations remain `case.records.tail`, `state.records.tail`, `workflow.runs.watch` |
| `yai/runtime/connections` | documented | remains future observation surface, not stream grammar owner |
| `yai/runtime/boundary/transport` | documented | remains future SSE/RPC stream carrier boundary |
| `sdk/packages/typescript` | documented | current docs already separate `local_event_stream` from loopback request-response |
| `sdk/packages/rust` | documented | current docs already keep native-local target on IPC and HTTP as migration-era override |
| `cli` | untouched | no stream client behavior added |
| `loom` | untouched | no realtime transport behavior added |

## Contract Result

Record:
- primary web binding: SSE
- primary native-local binding: RPC streaming over `local_ipc_rpc`
- WebSocket reservation: future bidirectional only, not primary in v1
- event frame fields: `schema`, `stream_id`, `event_id`, `operation_id`, `request_id`, optional `correlation_id`, optional `client`, `sequence`, `event_type`, `created_at`, optional `data`, optional `error`, `terminal`, `heartbeat`, optional `retry_after_ms`, optional `resume_token`, optional `redaction`
- event types: `stream.open`, `stream.heartbeat`, `stream.data`, `stream.warning`, `stream.error`, `stream.cancelled`, `stream.closed`
- subscription posture: `operation_id`, `request_id`, optional `stream_id`, optional `filters`, optional `resume_token`, optional `last_event_id`, `client_ref`, optional `case_ref`
- current streamable operations remain `case.records.tail`, `state.records.tail`, `workflow.runs.watch`
- heartbeat, reconnect, resume, backpressure, and terminal-event posture are explicit
- stream frames remain distinct from response envelopes

## Security Result

Record:
- stream payloads must be projection-safe
- sensitive provider or model raw payloads must not be streamed directly
- provider credentials must never appear in stream payloads
- LAN remains blocked by default unless `lan_secure` is separately enabled
- browser streams must obey the same local origin and token posture as Local HTTP Loopback where applicable

## Runtime/SDK Ownership Result

Record:
- API owns contract
- runtime will implement event publication and stream serving later
- SDK will implement stream clients later
- stream frames are not response envelopes
- CLI/Loom behavior unchanged

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| `api` | `find transports/local-event-stream* transports mappings schemas conformance docs -maxdepth 4 -type f | sort` | pass | confirmed Local Event Stream subtree, checker, and wave report exist |
| `api` | `python3 - <<'PY' ... watchable ops ... PY` | pass | confirmed current watchable operations are `case.records.tail`, `state.records.tail`, and `workflow.runs.watch` |
| `api` | `rg -n "local_event_stream\|stream.open\|stream.heartbeat\|stream.data\|stream.warning\|stream.error\|stream.cancelled\|stream.closed\|SSE\|WebSocket\|heartbeat\|resume_token\|last_event_id\|backpressure\|redaction\|streamable" README.md transports mappings schemas conformance docs 2>/dev/null \|\| true` | pass | audit confirmed current stream/watch contract vocabulary |
| `yai` | `find runtime/connections runtime/boundary/transport runtime/boundary/service runtime/boundary/api -maxdepth 3 -type f | sort` | pass | confirmed relevant runtime surfaces exist |
| `yai` | `rg -n "stream_id\|event_id\|request_id\|client_ref\|heartbeat\|reconnect\|SSE\|WebSocket\|local_event_stream\|stream frame\|streamable\|implementation" runtime/connections runtime/boundary/transport runtime/boundary/service runtime/boundary/api README.md 2>/dev/null \|\| true` | pass | audit confirmed documentation alignment points |
| `sdk` | `rg -n "local_event_stream\|SSE\|WebSocket\|stream.open\|stream.frame\|stream.closed\|heartbeat\|resume_token\|YaiTransport\|HttpTransport\|watch\|tail\|stream" README.md generated packages/typescript packages/rust 2>/dev/null \|\| true` | pass | audit confirmed current TypeScript/Rust stream references and compat surfaces |
| `cli` | `test ! -e source` | pass | required source-absence guard |
| `cli` | `scripts/check-no-source-dependency.sh` | pass | required |
| `cli` | `rg -n "local_event_stream\|SSE\|WebSocket\|watch\|tail\|stream\|runtime" README.md src tests 2>/dev/null \|\| true` | pass | current CLI remains behavior-unchanged |
| `loom` | `rg -n "local_event_stream\|SSE\|WebSocket\|watch\|tail\|stream\|runtime\|backend" README.md src tests 2>/dev/null \|\| true` | pass | current Loom remains behavior-unchanged |
| `api` | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| `api` | `python3 conformance/check_operation_registry.py` | pass | `conformance: ok` |
| `api` | `python3 conformance/check_operation_transport_mapping.py` | pass | `operation-transport-map: ok` |
| `api` | `python3 conformance/check_api_envelope_error_stream.py` | pass | `api-envelope-error-stream: ok` |
| `api` | `python3 conformance/check_local_event_stream_contract.py` | pass | `local-event-stream-contract: ok` |
| `api` | `python3 -m json.tool transports/local-event-stream/event-frame.v1.schema.json >/dev/null` | pass | event-frame schema parses |
| `api` | `python3 -m json.tool transports/local-event-stream/event-types.v1.json >/dev/null` | pass | event-types registry parses |
| `api` | `git diff --check` | pass | required |
| `yai` | `git diff --check` | pass | required |
| `sdk` | `git diff --check` | pass | docs-only touches |
| `cli` | `git diff --check` | pass | untouched |
| `loom` | `git diff --check` | pass | untouched |
| `all` | `rg -n "SSE server implemented\|WebSocket server implemented\|RPC streaming implemented\|SDK stream client implemented\|provider transport is local_event_stream\|LAN enabled by default\|API implements stream server\|API owns event bus" ../api ../yai ../sdk ../cli ../loom 2>/dev/null \|\| true` | pass/classified | any matches are expected only in checker forbidden-phrase lists or wave-report command text; no positive implementation claims found |

## Non-Implementation Confirmation

Record:
- no SSE server implementation
- no WebSocket server implementation
- no RPC streaming implementation
- no runtime event bus implementation
- no SDK stream client implementation
- no dashboard, CLI, or Loom behavior change
