# SDK Generation Gate (Wave 14 Input)

Wave 14 SDK generation is allowed only when the following gate is satisfied.

## Mandatory source

- SDK input repository: `../api`.
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


Wave 13D prerequisite: root `yai/api/` removed. SDK generation input remains `../api` only.

## Wave 14 Handoff

- SDK workspace path: `../sdk`.
- SDK source mode: contract-bound from `api`.
- Initial SDK languages: TypeScript, Python.
- Initial SDK transport: abstract placeholder.
- `sdkGeneratedFromOpenApi`: false.
- `sdkGeneratedFromCli`: false.
- `sdkGeneratedFromCoreStructs`: false.
