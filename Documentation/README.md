# API Documentation

`api/Documentation` is the canonical documentation surface for the YAI API protocol. It owns the public API contract language: protocol shape, operation grammar, operation registry, operation-to-transport mapping, transports, envelopes, errors, API-facing domain projections, conformance, and indexes for API artifact roots.

## Ownership

API owns:

- protocol and operation grammar
- operation registry and operation-to-transport mapping
- API transports, envelopes, errors, and stream frame semantics
- registries and domain projections exposed through the API
- API conformance policy and OpenAPI projection documentation
- the API/client boundary

API delegates:

- YAI owns runtime and system truth in `../yai/Documentation`
- SDK owns typed client and package truth in `../sdk/Documentation`
- Console owns terminal client UX truth in `../console/Documentation`

## Official Reading Path

1. `Documentation/README.md`
2. `Documentation/INDEX.md`
3. `Documentation/architecture/overview.md`
4. `Documentation/architecture/api-source-of-truth.md`
5. `Documentation/architecture/protocol-api-boundary.md`
6. `Documentation/architecture/operation-model.md`
7. `Documentation/operations/operation-grammar.md`
8. `Documentation/operations/operation-to-transport-mapping.md`
9. `Documentation/architecture/transport-model.md`
10. `Documentation/transports/local-ipc-rpc.md`
11. `Documentation/envelopes/request-response-model.md`
12. `Documentation/errors/error-model.md`
13. `Documentation/conformance/conformance-policy.md`
14. `Documentation/reference/registry-index.md`

## Sections

- `architecture/` defines ownership and protocol boundaries.
- `operations/` defines operation grammar, registry semantics, and projections.
- `transports/` defines transport contracts and compatibility boundaries.
- `envelopes/` defines request, response, readiness, and stream frames.
- `errors/` defines error shape, codes, status mapping, and transport mapping.
- `domains/` defines API-facing domain projections.
- `conformance/` defines release, compatibility, readiness, and checks.
- `reference/` indexes artifact roots without moving them.
- `decisions/` records active API decisions.
- `internal/` and `archive/` are not the public reading path.

Do not use `internal/` or `archive/` as current API authority unless a canonical document explicitly points there for history.
