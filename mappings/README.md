# Mappings

`api/mappings/` is the canonical API-owned mapping surface between operation
grammar and transport classes.

This root answers three questions:

- which API operations may travel over which transport classes
- how SDKs should select a transport from the allowed set
- how runtime transport entrypoints normalize requests before dispatch into
  `yai/runtime/boundary/api`

Primary files:

- `operation-transport-map.v1.schema.json`
- `operation-transport-map.v1.json`
- `operation-dispatch-contract.v1.md`
- `transport-selection-policy.v1.md`
- `streamable-operation-policy.v1.md`
- `lan-exposure-policy.v1.md`
- `provider-transport-exclusion-policy.v1.md`

Boundary:

- `api/mappings/` owns operation-to-transport contracts only.
- `../transports/` owns the transport class vocabulary.
- `../registry/` owns operation ids and API exposure grammar.
- `../schemas/` owns API envelope/schema shape.
- `../yai/runtime/boundary/transport` and `../yai/runtime/boundary/service`
  will implement listeners later.
- `../sdk` consumes this mapping; it does not invent a separate transport
  grammar.
