# API.09 — Transport Contract Index / Implementation Readiness Matrix

## Status

* Delivery: API.09
* Status: done
* Track: API / Transport / SDK / Runtime alignment
* Repo branch: `refoundation/phase-01`
* Repo change type: transport contract index + implementation readiness matrix
* Previous delivery: API.08 — In-process Test / Subprocess Stdio Compatibility Boundary
* Next delivery: RT.01 — Runtime Transport Boundary Skeleton

## Purpose

State that API.09 closes the API transport contract freeze phase and hands off to
runtime/SDK implementation waves.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| `api` | `transports/README.md` | modified | add API.09 close-out links for index, readiness, and handoff |
| `api` | `transports/transport-contract-index.v1.md` | added | create one canonical index for the frozen transport contract set |
| `api` | `transports/implementation-readiness-matrix.v1.json` | added | create machine-readable readiness classification for all transport contracts |
| `api` | `transports/implementation-readiness-matrix.v1.md` | added | provide human-readable readiness table for runtime and SDK handoff |
| `api` | `transports/implementation-handoff.v1.md` | added | define the next runtime, SDK, CLI, Loom, and Web implementation sequence |
| `api` | `Documentation/transport-contract-index-implementation-readiness.md` | added | summarize API.09 freeze closure and product vs future vs non-product posture |
| `api` | `Documentation/waves/api-09-transport-contract-index-implementation-readiness-matrix.md` | added | record API.09 scope and validation |
| `api` | `conformance/check_transport_contract_index.py` | added | validate index presence, readiness values, and handoff classification |
| `api` | `conformance/README.md` | modified | register the API.09 conformance checker |
| `api` | `mappings/transport-selection-policy.v1.md` | modified | cross-link transport selection to the API.09 readiness and handoff surfaces |
| `yai` | `runtime/boundary/transport/README.md` | modified | point runtime transport ownership to the API.09 index and handoff |
| `yai` | `runtime/boundary/service/README.md` | modified | point service exposure sequencing to the API.09 readiness matrix |
| `yai` | `runtime/boundary/api/README.md` | modified | point normalized dispatch to the API.09 handoff without changing behavior |
| `sdk` | `README.md` | modified | point SDK package ownership to the API.09 readiness and handoff surfaces |
| `sdk` | `generated/README.md` | modified | align generated outputs with API.09 sequencing |
| `sdk` | `packages/rust/README.md` | modified | clarify Rust implementation ordering against API.09 |
| `sdk` | `packages/typescript/README.md` | modified | clarify TypeScript implementation ordering against API.09 |

## Transport Contract Index

| Transport | Contract status | Role | Product status |
| --------- | --------------- | ---- | -------------- |
| `local_ipc_rpc` | frozen | native-local | primary product |
| `local_http_loopback` | frozen | browser/dashboard | primary product |
| `local_event_stream` | frozen | realtime | primary product |
| `lan_secure` | frozen | paired LAN | controlled future |
| `remote_https` | frozen | platform/account/future | controlled future |
| `provider_transport_boundary` | frozen | runtime-provider split | separate boundary |
| `in_process_test` | frozen | test/conformance | non-product |
| `subprocess_stdio_compat` | frozen | compat/debug/migration | compat only |

## Implementation Readiness Matrix

| Transport | Contract status | Implementation priority | Runtime readiness | SDK readiness | Client default | Next runtime wave | Next SDK wave | Next client wave |
| --------- | --------------- | ----------------------- | ----------------- | ------------- | -------------- | ----------------- | ------------- | ---------------- |
| `local_ipc_rpc` | frozen | primary_now | ready_for_implementation | ready_for_client_implementation | cli_loom_native | `RT.01 / RT.02` | `SDK.01` | `CLI.01 / LOOM.01` |
| `local_http_loopback` | frozen | primary_now | ready_for_implementation | ready_for_client_implementation | dashboard_web | `RT.03` | `SDK.02` | `WEB.01` |
| `local_event_stream` | frozen | primary_now | ready_for_implementation | ready_for_client_implementation | realtime | `RT.04` | `SDK.03` | `WEB.01 / CLI.01 / LOOM.01` |
| `lan_secure` | frozen | controlled_future | future_only | future_only | none | none | none | none |
| `remote_https` | frozen | controlled_future | future_only | future_only | none | none | none | none |
| `provider_transport_boundary` | frozen | separate_boundary | separate_provider_boundary | separate_provider_boundary | none | none | none | none |
| `in_process_test` | frozen | test_only | not_product | test_only | none | none | none | none |
| `subprocess_stdio_compat` | frozen | compat_only | not_product | compat_only | none | none | none | none |

## Handoff Sequence

Record:
- `RT.01 — Runtime Transport Boundary Skeleton`
- `RT.02 — Local IPC RPC Runtime Listener`
- `SDK.01 — Rust Local IPC RPC Client Transport`
- `CLI.01 — CLI Local IPC RPC Default`
- `LOOM.01 — Loom Local IPC RPC Default`
- `RT.03 — Local HTTP Loopback Runtime Server`
- `SDK.02 — TypeScript Local HTTP Loopback Client`
- `WEB.01 — Dashboard Local Runtime Binding`
- `RT.04 — Local Event Stream Runtime Serving`
- `SDK.03 — Stream Clients TS/Rust`

## Non-Implementation Confirmation

Record:
- no runtime implementation
- no SDK implementation
- no CLI/Loom/Web behavior change
- no OpenAPI expansion
- no package changes

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| `api` | `find transports -maxdepth 3 -type f | sort` | pass | confirmed all eight transport roots plus API.09 index, matrix, and handoff files exist |
| `api` | `find Documentation/waves conformance mappings projections -maxdepth 2 -type f | sort` | pass | confirmed API.09 wave report and checker exist in canonical surfaces |
| `api` | `rg -n "local_ipc_rpc\|local_http_loopback\|local_event_stream\|lan_secure\|remote_https\|provider_transport_boundary\|in_process_test\|subprocess_stdio_compat\|implementation readiness\|handoff\|RT\.\|SDK\.\|CLI\.\|LOOM\.\|WEB\." README.md transports docs conformance mappings projections 2>/dev/null \|\| true` | pass | audit confirmed index, readiness, and handoff vocabulary landed across API docs |
| `yai` | `rg -n "implementation readiness\|transport contract index\|local_ipc_rpc\|local_http_loopback\|local_event_stream\|RT\.01\|RT\.02\|RT\.03\|RT\.04" runtime/boundary runtime/connections providers/transport include/ipc README.md 2>/dev/null \|\| true` | pass | audit confirmed runtime boundary docs now point to API.09 readiness and handoff |
| `sdk` | `rg -n "implementation readiness\|transport contract index\|local_ipc_rpc\|local_http_loopback\|local_event_stream\|SDK\.01\|SDK\.02\|SDK\.03" README.md generated packages/rust packages/typescript packages/python packages/c 2>/dev/null \|\| true` | pass | audit confirmed SDK docs now point to API.09 readiness and named handoff waves |
| `api` | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| `api` | `python3 conformance/check_operation_registry.py` | pass | `conformance: ok` |
| `api` | `python3 conformance/check_operation_transport_mapping.py` | pass | `operation-transport-map: ok` |
| `api` | `python3 conformance/check_api_envelope_error_stream.py` | pass | `api-envelope-error-stream: ok` |
| `api` | `python3 conformance/check_local_ipc_rpc_contract.py` | pass | `local-ipc-rpc-contract: ok` |
| `api` | `python3 conformance/check_local_http_loopback_contract.py` | pass | `local-http-loopback-contract: ok` |
| `api` | `python3 conformance/check_local_event_stream_contract.py` | pass | `local-event-stream-contract: ok` |
| `api` | `python3 conformance/check_lan_remote_boundary.py` | pass | `lan-remote-boundary: ok` |
| `api` | `python3 conformance/check_test_compat_transport_boundary.py` | pass | `test-compat-transport-boundary: ok` |
| `api` | `python3 conformance/check_transport_contract_index.py` | pass | `transport-contract-index: ok` |
| `api` | `python3 -m json.tool transports/implementation-readiness-matrix.v1.json >/dev/null` | pass | readiness matrix JSON parsed cleanly |
| `api` | `git diff --check` | pass | required |
| `yai` | `git diff --check` | pass | required |
| `yai` | `make -j4` | pass | `make: '/home/mothx/.cache/yai/build/yai/bin/yai' is up to date.` |
| `yai` | `make -j4 yai` | pass | `make: Nothing to be done for 'yai'.` |
| `cli` | `test ! -e source` | pass | required source absence guard |
| `cli` | `scripts/check-no-source-dependency.sh` | pass | required source guard |
| `cli` | `git diff --check` | pass | required |
| `sdk` | `git diff --check` | pass | required |
| `loom` | `git diff --check` | pass | required |
| `all` | `rg -n "transport implementation complete\|runtime listener implemented\|SDK transport implemented\|CLI already uses local_ipc_rpc\|Loom already uses local_ipc_rpc\|dashboard already uses local_http_loopback\|LAN ready for default\|Remote HTTPS is default runtime\|subprocess is canonical product transport\|in_process_test is product transport" ../api ../yai ../sdk ../cli ../loom 2>/dev/null \|\| true` | pass/classified | matches appeared only in checker forbidden-phrase lists, prior wave non-implementation wording, or this report command text; no positive implementation claims found |
