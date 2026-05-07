# API.04 — Local IPC RPC Contract Verticalization

## Status

* Delivery: API.04
* Status: done
* Track: API / Transport / SDK / Runtime alignment
* Repo branch: `refoundation/phase-01`
* Repo change type: Local IPC RPC contract verticalization
* Previous delivery: API.03 — API Envelope / Error / Stream Frame Alignment
* Next delivery: API.05 — Local HTTP Loopback Contract Verticalization

## Purpose

API.04 defines Local IPC RPC as the primary native-local transport contract
before implementation. The wave freezes discovery, handshake, frame, stream,
security, and error posture so runtime and SDK can implement later without
inventing separate grammars.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| `api` | `transports/local-ipc-rpc.v1.md` | modified | expand the root Local IPC RPC contract and link the verticalized subtree |
| `api` | `transports/local-ipc-rpc/README.md` | added | create the Local IPC RPC contract root |
| `api` | `transports/local-ipc-rpc/discovery.v1.md` | added | define discovery order and error classes |
| `api` | `transports/local-ipc-rpc/handshake.v1.md` | added | define handshake fields and negotiation results |
| `api` | `transports/local-ipc-rpc/frame.v1.schema.json` | added | freeze the v1 frame wrapper schema |
| `api` | `transports/local-ipc-rpc/frame-model.v1.md` | added | explain frame fields and payload carriage |
| `api` | `transports/local-ipc-rpc/message-types.v1.json` | added | register required frame types |
| `api` | `transports/local-ipc-rpc/security.v1.md` | added | define same-machine/no-LAN security posture |
| `api` | `transports/local-ipc-rpc/streaming.v1.md` | added | define stream handling for streamable operations |
| `api` | `transports/local-ipc-rpc/cancellation-timeout.v1.md` | added | define cancel and timeout semantics |
| `api` | `transports/local-ipc-rpc/errors.v1.md` | added | preserve transport vs operation error distinction |
| `api` | `transports/local-ipc-rpc/platform-bindings.v1.md` | added | freeze Unix socket and named-pipe posture |
| `api` | `transports/local-ipc-rpc/conformance-profile.v1.md` | added | define required contract claims for future implementations |
| `api` | `docs/local-ipc-rpc-contract.md` | added | summarize the API.04 contract |
| `api` | `docs/waves/api-04-local-ipc-rpc-contract-verticalization.md` | added | record scope and validation |
| `api` | `conformance/check_local_ipc_rpc_contract.py` | added | validate Local IPC RPC contract structure and wording |
| `api` | `conformance/README.md` | modified | register the new API.04 conformance checker |
| `api` | `mappings/operation-dispatch-contract.v1.md` | modified | cross-link dispatch ownership to the API.04 Local IPC RPC contract |
| `api` | `mappings/transport-selection-policy.v1.md` | modified | cross-link selection policy to Local IPC RPC contract docs |
| `yai` | `include/ipc/README.md` | modified | keep IPC headers as C/ABI surface, not API transport owner |
| `yai` | `runtime/boundary/transport/README.md` | modified | align runtime transport boundary to future Local IPC RPC implementation ownership |
| `yai` | `runtime/boundary/api/README.md` | modified | clarify normalized entry from Unix socket or named pipe callers |
| `yai` | `runtime/connections/README.md` | modified | document Local IPC RPC connection observation scope |
| `sdk` | `generated/README.md` | modified | keep generated IPC artifacts as projections only |
| `sdk` | `packages/rust/README.md` | modified | state Local IPC RPC is the future Rust-native default |
| `sdk` | `packages/typescript/README.md` | modified | keep browser TS on loopback/SSE and prevent TS IPC grammar ownership |

## Existing Surface Audit

| Surface | Result | Notes |
| ------- | ------ | ----- |
| `api/transports/local-ipc-rpc.v1.md` | updated | pre-existing root contract now points to the verticalized subtree |
| `yai/include/ipc` | documented | existing C/ABI header area already exists and remains non-owner of API transport contracts |
| `yai/runtime/boundary/transport` | documented | existing runtime transport boundary remains implementation-side only |
| `yai/runtime/connections` | documented | existing connection observation surface now records IPC-specific observation scope |
| `sdk/packages/rust` | documented | current HTTP migration-era transport remains in place; no Rust IPC transport added |
| `cli` | untouched | current HTTP-based migration behavior remains unchanged |
| `loom` | untouched | current endpoint-based migration behavior remains unchanged |

## Contract Result

Record:
- platform bindings: Unix domain socket on macOS/Linux; Windows named pipe
- discovery order: explicit config, `YAI_LOCAL_IPC_ENDPOINT`, runtime discovery file, platform default path, then `not_configured`
- handshake fields: transport name/version, API envelope version, client ref, frame versions, stream modes, requested capabilities, plus runtime negotiation result
- frame model: `frame_schema`, `frame_id`, `frame_type`, `frame_version`, optional `request_id`, optional `correlation_id`, optional `stream_id`, optional `sequence`, `payload_encoding`, `payload`, `payload_size`, optional `flags`, optional `created_at`
- message types: `handshake.request`, `handshake.response`, `operation.request`, `operation.response`, `stream.open`, `stream.frame`, `stream.close`, `cancel.request`, `heartbeat`, `error`
- security posture: same-machine, no LAN, same-user default, runtime-owned endpoint lifecycle, no world-writable endpoint, no provider credential leakage
- stream behavior: allowed only for API.02 streamable operations and carries API.03 watch-event frames
- cancellation/timeout semantics: request-scoped timeout, advisory `cancel.request`, and distinct transport timeout vs operation timeout
- error distinction: transport error remains separate from operation and guard error

## Security Result

Record:
- same-machine only
- Unix socket and named-pipe posture only
- same-user default permissions
- no LAN
- no provider credential leakage
- no world-writable endpoint

## Runtime/SDK Ownership Result

Record:
- API owns contract
- runtime will implement listener later
- SDK will implement client later
- CLI/Loom behavior unchanged

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| `api` | `find transports/local-ipc-rpc* transports mappings schemas errors envelopes conformance docs -maxdepth 4 -type f | sort` | pass | confirmed Local IPC RPC subtree, checker, and wave report exist |
| `api` | `rg -n "local_ipc_rpc\|IPC\|RPC\|Unix domain socket\|named pipe\|handshake\|frame\|stream\|heartbeat\|cancel\|timeout\|transport error\|operation error\|same-machine\|LAN\|provider transport\|implementation" README.md transports mappings schemas errors envelopes conformance docs 2>/dev/null \|\| true` | pass | audit confirmed contract vocabulary and pre-existing transport docs |
| `yai` | `find include/ipc runtime/boundary runtime/connections providers/transport -maxdepth 3 -type f | sort` | pass | confirmed pre-existing IPC headers and runtime boundary surfaces |
| `yai` | `rg -n "IPC\|RPC\|Unix domain socket\|named pipe\|local_ipc_rpc\|handshake\|frame\|connection\|stream_id\|request_id\|client_ref\|transport error\|operation error\|provider transport" include/ipc runtime/boundary runtime/connections providers/transport README.md 2>/dev/null \|\| true` | pass | audit confirmed documentation alignment points and existing IPC header presence |
| `sdk` | `rg -n "local_ipc_rpc\|IPC\|RPC\|YaiTransport\|HttpTransport\|transport\|frame\|handshake\|envelope\|stream\|YAI_API_ENDPOINT" README.md generated packages/rust packages/typescript packages/python packages/c 2>/dev/null \|\| true` | pass | audit confirmed HTTP migration-era Rust transport and existing out-of-scope C IPC/RPC implementation surfaces |
| `cli` | `test ! -e source` | pass | required source-absence guard |
| `cli` | `scripts/check-no-source-dependency.sh` | pass | required |
| `cli` | `rg -n "HttpTransport\|YAI_API_ENDPOINT\|local_ipc_rpc\|IPC\|RPC\|transport\|runtime" README.md src tests 2>/dev/null \|\| true` | pass | current CLI still reflects migration-era HTTP transport usage |
| `loom` | `rg -n "HttpTransport\|YAI_API_ENDPOINT\|local_ipc_rpc\|IPC\|RPC\|transport\|runtime\|backend" README.md src tests 2>/dev/null \|\| true` | pass | current Loom still reflects migration-era endpoint/backend wording |
| `api` | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| `api` | `python3 conformance/check_operation_registry.py` | pass | `conformance: ok` |
| `api` | `python3 conformance/check_operation_transport_mapping.py` | pass | `operation-transport-map: ok` |
| `api` | `python3 conformance/check_api_envelope_error_stream.py` | pass | `api-envelope-error-stream: ok` |
| `api` | `python3 conformance/check_local_ipc_rpc_contract.py` | pass | `local-ipc-rpc-contract: ok` |
| `api` | `python3 -m json.tool transports/local-ipc-rpc/frame.v1.schema.json >/dev/null` | pass | frame schema parses |
| `api` | `python3 -m json.tool transports/local-ipc-rpc/message-types.v1.json >/dev/null` | pass | message-type registry parses |
| `api` | `git diff --check` | pass | required |
| `yai` | `git diff --check` | pass | required |
| `cli` | `git diff --check` | pass | untouched |
| `sdk` | `git diff --check` | pass | docs-only touches |
| `loom` | `git diff --check` | pass | untouched |
| `all` | `rg -n "IPC listener implemented\|Unix socket server implemented\|named pipe server implemented\|SDK implements local_ipc_rpc\|CLI defaults to IPC\|Loom defaults to IPC\|LAN enabled by default\|provider transport is local_ipc_rpc\|API implements IPC server\|API owns socket lifecycle" ../api ../yai ../sdk ../cli ../loom 2>/dev/null \|\| true` | pass/classified | matches appeared only inside the API.04 checker forbidden-phrase list and wave-report command text; no positive implementation claims found |

## Non-Implementation Confirmation

Record:
- no IPC listener
- no socket or named-pipe server
- no SDK `LocalIpcRpcTransport`
- no CLI/Loom default switch
- no provider/model behavior change
