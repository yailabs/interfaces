# Extraction Notes

- extracted from: `yai/api`
- extraction wave: 13
- source branch: `feature/topology-refactor-7`
- source root: `api/`
- runtime source of truth: `yai`

This is an initial contract-first extraction and remains intentionally partial.
Known couplings are tracked under `extraction/` docs.


## Wave 13B Mirror Clarification

- `yai/api` remains temporary compatibility mirror while runtime/build consumers are drained.
- `core/api` is not a canonical target.
- SDK generation remains deferred to Wave 14 and must target `api`.


## Contract Source Rule (Wave 13C)

- Canonical contract source: `../api`
- `yai/api`: temporary runtime-adapter/compatibility mirror
- Wave 14 SDK input: this repository/workspace


Wave 13D status: root `yai/api/` removed. Contracts remain canonical in `api`; runtime adapters remain in `yai/core/runtime/boundary/api`.

## Wave 14 Start

- SDK handoff workspace: `../sdk`
- SDK source mode: contract-bound from `api`
- SDK languages: TypeScript, Python
- SDK generated from OpenAPI: no (OpenAPI scaffold only)

## Client Consumption Boundary (Wave 14B)

- `api` is the canonical contract source, not the normal application dependency.
- Clients should normally consume SDK packages built from/bound to this contract surface.
- Direct API consumption is limited to low-level conformance, debug integrations, and temporary bootstrap.


## Wave 14C3

API enterprise hardening is active on `feature/topology-refactor-7`. OpenAPI and conformance remain scaffolded; SDK generation remains contract-bound.


## Wave 14D Alignment

- API remains canonical contract source and client-neutral.
- SDK is the official client consumption layer.
- Clients should not use this repo as an application dependency except debug/conformance/bootstrap cases.
- API does not own client UI behavior or SDK convenience semantics.
