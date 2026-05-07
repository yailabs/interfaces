# Operation-to-Transport Mapping

## Purpose

API.02 freezes the first canonical mapping between API operation ids and
allowed transport classes.

Transport vocabulary was frozen in API.01.
This document answers which operations may travel over which transport classes
and where transport entrypoints must dispatch normalized envelopes.

## Source Files

- `mappings/operation-transport-map.v1.schema.json`
- `mappings/operation-transport-map.v1.json`
- `mappings/operation-dispatch-contract.v1.md`
- `mappings/transport-selection-policy.v1.md`
- `mappings/streamable-operation-policy.v1.md`
- `mappings/lan-exposure-policy.v1.md`
- `mappings/provider-transport-exclusion-policy.v1.md`

## Mapping Summary

The initial map covers all 112 operations currently present in
`registry/api-operations.v1.json`.

- 92 operations dispatch to `runtime_boundary_api`
- 8 operations dispatch to `platform_remote_api`
- 8 operations are deferred as `sdk_local_only` high-level compositions
- 4 operations remain `compat_only`

Transport default distribution:

- `local_ipc_rpc`: 93
- `local_event_stream`: 3
- `remote_https`: 8
- `none`: 8

## Canonical Interpretation

- Local runtime operations default to `local_ipc_rpc`.
- Browser/dashboard-safe local operations may additionally use
  `local_http_loopback`.
- Streamable watch/tail operations use `local_event_stream`.
- `lan_secure` remains controlled and opt-in.
- `remote_https` is reserved for platform/account boundary operations.
- High-level composition projections remain outside direct transport dispatch in
  API.02.

## Dispatch Boundary

Transport entrypoints normalize incoming requests into canonical API operation
envelopes and dispatch them into `yai/runtime/boundary/api`.

`yai/runtime/boundary/api` owns:

- dispatch
- guard chain
- handler binding
- response normalization

`yai/runtime/boundary/transport` and `yai/runtime/boundary/service` will own
physical listeners later.

## Provider Separation

Some operations may eventually trigger provider/model work after runtime
dispatch. That does not make provider/model transport a client-runtime
transport.

`provider_transport_boundary` is excluded from client-runtime mapping and exists
only as a boundary classification to prevent ownership confusion.

## Non-Goals

- no listener implementation
- no transport codec implementation
- no SDK transport implementation
- no OpenAPI route expansion
- no provider invocation behavior change
