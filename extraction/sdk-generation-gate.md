# SDK Generation Gate

Current status: superseded by the unified `interfaces` repository.

SDK generation inputs now come from the protocol registry, schemas, mappings,
and provenance policy in this repository. The old standalone `api` repository
name and the old standalone `sdk` workspace are historical only.

## Mandatory source

- SDK input repository: `interfaces` (this repository).
- SDK package roots: `packages/rust`, `packages/python`,
  `packages/typescript`, and `packages/c`.
- `yai/api` is not a canonical SDK input source.

## Prohibited SDK sources

- CLI output text
- raw core structs
- ad-hoc runtime internals

## Contract maturity checks

- family-by-family eligibility declared explicitly
- deferred/unavailable families declared honestly
- envelope/lifecycle vocabulary aligned
- OpenAPI may be scaffolded; SDK can start contract-bound if explicitly scoped
- conformance remains scaffolded and must be reported as such


Wave 13D removed root `yai/api/`. SDK generation input is now the
`interfaces` registry/schema/mapping surface.

## Current Package Handoff

- SDK workspace path: `packages/`.
- SDK source mode: package projection from `interfaces`.
- SDK languages: Rust, Python, TypeScript, and C.
- SDK transport: package projection over interface transport contracts.
- `sdkGeneratedFromOpenApi`: false.
- `sdkGeneratedFromCli`: false.
- `sdkGeneratedFromCoreStructs`: false.
