# Operation To Transport Mapping

Operation-to-transport mapping controls which transports may carry each operation.

## Artifact Authority

- `mappings/operation-transport-map.v1.json`
- `mappings/operation-transport-map.v1.schema.json`
- `mappings/operation-dispatch-contract.v1.md`
- `mappings/transport-selection-policy.v1.md`
- `mappings/streamable-operation-policy.v1.md`
- `mappings/lan-exposure-policy.v1.md`

## Mapping Semantics

Each mapping record determines whether an operation can use local IPC, loopback HTTP, event stream, secure remote exposure, subprocess compatibility, or in-process test dispatch.

## Policy

- Local transports are preferred for local runtime integration.
- Event stream is reserved for streamable or watch-style operations.
- Remote exposure requires explicit policy and security posture.
- Compatibility transports must not redefine operation semantics.
- In-process test transport is for conformance and harness use.
