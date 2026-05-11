# Operation Dispatch Contract v1

## Purpose

This contract freezes how client-runtime transport entrypoints hand API
operations to the runtime boundary without making any transport implementation
canonical in the wrong place.

API owns the operation-to-transport contract.
Runtime will implement listeners later.
SDKs will consume the contract later.

## Dispatch Flow

```text
client
  -> SDK transport
  -> transport entrypoint
  -> normalized request envelope
  -> runtime/boundary/api
  -> guards / handler binding
  -> runtime module handler
  -> normalized response envelope or stream frame handoff
  -> SDK
  -> client
```

## Normalization Rule

- Transport entrypoints normalize physical transport frames into API request
  envelopes before runtime dispatch.
- Runtime-side transport listeners do not define a second operation grammar.
- The same canonical `operation_id` must survive normalization, dispatch,
  response handling, and stream frame handoff.

## Ownership

- `api/mappings/operation-transport-map.v1.json` owns which transport classes
  are allowed for each operation id.
- `api/transports/local-ipc-rpc/` owns the API.04 Local IPC RPC discovery,
  handshake, and frame contract for native-local transport entrypoints.
- `api/transports/local-http-loopback/` owns the API.05 Local HTTP Loopback
  discovery, route, header, origin, token, and request-response contract for
  browser-facing local transport entrypoints.
- `yai/runtime/boundary/api` receives normalized request envelopes.
- `yai/runtime/boundary/api` owns dispatch, guard chain, handler binding, and
  response normalization.
- Physical listeners live under `yai/runtime/boundary/transport` and
  `yai/runtime/boundary/service`.
- SDK clients never call runtime internals directly.
- CLI, Loom, web, and editor clients consume SDK transports rather than
  defining their own transport grammar.
- Provider/model transport starts after runtime dispatch, not before it.
- Stream event framing is separate from response-envelope framing.

## Dispatch Targets

- `runtime_boundary_api`: local runtime operation dispatch after transport
  normalization.
- `platform_remote_api`: remote platform/account boundary operations such as
  `auth.*` and `identity.*`.
- `sdk_local_only`: high-level composition surfaces that remain SDK-facing
  projections rather than direct transport entrypoints in API.02.
- `compat_only`: migration-era compatibility surfaces that remain local and do
  not recover canonical ownership.

## Test and Compat Rule

- test or compatibility entrypoints still normalize into API request envelopes
- test or compatibility entrypoints do not bypass guards or operation mapping
- subprocess compatibility remains outside canonical product transport
  selection

## Non-Goals

- no IPC/RPC codec definition
- no HTTP route implementation
- no SSE/WebSocket implementation
- no LAN listener implementation
- no remote platform client implementation
