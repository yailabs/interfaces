# YAI Rust SDK

Transport-bound Rust SDK surface for native clients.

This package lives in `interfaces/packages/rust` and preserves the package name
`yai-sdk-rust`. It is an official SDK package projection over YAI Interfaces
protocol truth; it does not define protocol truth.

INTF.4 validation: `cargo fmt --check`, `cargo check`, and `cargo test` passed.

## Current Scope
- transport trait (`YaiTransport`)
- typed envelope/status/error model
- operation registry constants
- canonical `system` surface via `client.system().status()`
- canonical `providers` surface via `client.providers().list()`
- canonical `conversation` and `prompting` seeds for `conversation.current` and `prompting.context.assemble`
- current HTTP transport foundation (`HttpTransport`) configured with `YAI_API_ENDPOINT`

Compatibility aliases:
- `client.runtime().status_inspect()` -> canonical `system.status`
- `client.provider().list_inspect()` -> canonical `providers.list`

## Transport Model
- `NotConfiguredTransport`: explicit `TransportNotConfigured`
- `HttpTransport`: current HTTP client transport implementation
- no endpoint configured => `TransportNotConfigured`
- endpoint unreachable => `TransportUnavailable`
- non-success API status => `ApiError` or `OperationUnavailable`
- invalid response envelope => `DecodeError`

API.01 freeze:
- SDK owns client-side transports only
- `local_ipc_rpc` is the primary native local transport class for Rust
  Console-compatible native clients, legacy CLI/Loom compatibility surfaces,
  and other native local clients
- `HttpTransport` remains a current implementation path, not the only canonical
  transport vocabulary
- provider/model transport is outside Rust SDK client transport ownership

API.02 mapping rule:
- Rust SDK consumes interfaces operation-to-transport mapping from
  `../../mappings`
- Rust SDK does not invent transport grammar or runtime dispatch targets
- migration-era compatibility helpers remain compatibility-only and do not
  extend the canonical API operation map

API.03 envelope rule:
- Rust SDK will encode and decode API request envelopes, response envelopes,
  and stream event frames from the interfaces package source tree
- current simplified Rust envelope types remain migration-era implementation
  until later SDK alignment waves
- Rust SDK does not define envelope grammar independently

A5 call-context rule:
- SDK propagates call context.
- SDK does not materialize system call records.
- SDK does not perform control-plane admission.
- `system_call_ref` is optional and normally runtime-created later.
- `work_case_ref` is optional and separate from client attachment.
- Rust `YaiCallContext` carries request/correlation ids, client refs,
  system/root context, optional work-case binding, optional system call ref, and
  transport.
- Local IPC RPC and HTTP request construction include call context where
  available without changing explicit transport selection.

API.04 Local IPC RPC rule:
- `local_ipc_rpc` is the target default native-local transport for Console,
  legacy CLI/Loom compatibility surfaces, and other Rust-native local clients
  in a later implementation wave
- current `HttpTransport` remains migration-era implementation
- Rust SDK must consume API discovery, handshake, frame, stream, and security
  contracts from `../../transports/local-ipc-rpc` later

SDK.01 implementation note:
- `LocalIpcRpcTransport` is now available as an explicit Rust SDK transport
- it is not selected automatically and does not switch Console consumers or
  legacy CLI/Loom compatibility surfaces
- runtime listener availability remains partial after RT.02, so safe
  `not_configured`, `endpoint_missing`, `permission_denied`,
  `version_mismatch`, and `runtime_unavailable` posture remains expected
- `HttpTransport` remains available as migration-era or development override

API.05 Local HTTP Loopback note:
- Rust may retain HTTP as explicit override or development transport
- native-local target default remains `local_ipc_rpc`
- Rust HTTP override behavior must consume API route, header, and error
  contracts rather than inventing its own grammar

API.06 Local Event Stream note:
- RPC streaming over `local_ipc_rpc` is the target native-local stream binding
- Console behavior remains unchanged until later implementation waves; legacy
  CLI/Loom compatibility surfaces remain unchanged

API.07 LAN and Remote note:
- `lan_secure` and `remote_https` are not default Console transports
- native-local target default remains `local_ipc_rpc`
- `remote_https` is platform or capability boundary only, not default local
  runtime execution

API.08 Test and Compat note:
- `in_process_test` may be used for Rust SDK or conformance harnesses later
- `subprocess_stdio_compat` is compatibility or debug only
- Rust SDK must not prefer subprocess compatibility for new canonical
  transports

API.09 implementation readiness:
- `local_ipc_rpc` is frozen and ready for Rust client implementation in
  `SDK.01`
- `local_http_loopback` remains explicit override or development transport and
  aligns to `SDK.02` rather than replacing native-local default
- `local_event_stream` aligns to `SDK.03` for canonical stream client work
- readiness and handoff are centralized in
  interfaces transport implementation readiness and handoff artifacts

## Posture
- no runtime/core direct imports
- no fake success/ready claims
- system/runtime status is real only when transport returns a valid envelope
- Local IPC RPC client construction is explicit; there is no automatic default
  switch in SDK.01
- Rust SDK client transport does not make the client a case owner, active case
  owner, or system/root case surface

## V20 runtime alignment

- canonical runtime/system status accepts lifecycle, health, readiness, transport,
  `operationalReadiness`, `sealReason`, `authPosture`, `casePosture`,
  `operatorContextPosture`, `clientPosture`, `sessionPosture`, and optional
  `controlPlan`
- compatibility runtime control planning is plan-only
- no Rust SDK surface claims runtime start/stop/restart executed unless a real
  transport result proves it
