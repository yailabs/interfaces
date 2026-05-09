# Operation-to-Transport Mapping

## Purpose

API.02 freezes the first canonical mapping between API operation ids and
allowed transport classes.
A2 reconciles that mapping with the current runtime reality after RT.04 and A1
Console canonicalization.

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

The current map covers all operations present in
`registry/api-operations.v1.json`.

The mapping is a contract surface plus readiness projection.
It is not a claim that every allowed transport already has identical runtime
implementation coverage.

For A2, `operation-transport-map.v1.json` may additionally carry:
- `runtime_ipc_coverage`
- `runtime_ipc_readiness`
- `operation_coverage_notes`

These fields are narrow Local IPC RPC reality markers for audited RT.04
coverage only. They do not widen transport behavior, add new runtime support,
or replace the broader contract mapping.

## Canonical Interpretation

- Local runtime operations default to `local_ipc_rpc`.
- Browser/dashboard-safe local operations may additionally use
  `local_http_loopback`.
- Streamable watch/tail operations use `local_event_stream`.
- `lan_secure` remains controlled and opt-in.
- `remote_https` is reserved for platform/account boundary operations.
- High-level composition projections remain outside direct transport dispatch in
  API.02.
- `runtime_ipc_coverage` is only populated where RT.04 reality was explicitly
  audited; absence means the contract map remains broader than the verified IPC
  runtime subset.
- Console is the canonical terminal client. CLI and Loom remain compatibility
  or historical names only and do not change transport truth.
- RT.04 updates runtime truth for Local IPC RPC only on a narrow audited set of
  operations:
  - supported at `read_projection_probe_ready`:
    - `system.status`
    - `system.check`
    - `system.runtime.inspect`
  - deferred at `read_projection_probe_ready`:
    - `case.current`
    - `case.list`
    - `case.show`
    - `providers.list`
    - `models.list`
- Mutating operations, provider/model execution, and unknown operations must
  not be read from the map as current RT.04 IPC support. They remain blocked,
  unsupported, or implementation-pending unless separately justified.

## Topology Note

The current `api` checkout uses `Documentation/` as the canonical
documentation root. Earlier delivery boxes and older references may still say
`docs/`; A2 updates the verified canonical surface rather than recreating a
parallel `docs/` tree.

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

For RT.04 specifically:
- `providers.list` remains a client-runtime read surface in contract terms, but
  its current IPC runtime coverage is deferred.
- `models.list` remains a client-runtime read surface in contract terms, but
  its current IPC runtime coverage is deferred.
- Provider transport and model execution remain separate from client-runtime
  transport selection.

## Non-Goals

- no listener implementation
- no transport codec implementation
- no SDK transport implementation
- no OpenAPI route expansion
- no provider invocation behavior change
