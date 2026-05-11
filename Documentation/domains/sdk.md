# SDK Projection Domain

The SDK projection domain documents the protocol contracts consumed by official
SDK packages. SDK packages are typed consumption surfaces and must not define
protocol truth.

## Interfaces Scope

- Operation grammar and registry records consumed by typed clients.
- Request and response envelope contracts.
- Error codes and transport mapping.
- Schema and OpenAPI projections.
- Package compatibility and conformance status.

## Package Truth

Official SDK packages live under:

- `packages/rust`
- `packages/python`
- `packages/typescript`
- `packages/c`

Package docs live under `Documentation/packages/` and package indexes live
under `Documentation/reference/`.
