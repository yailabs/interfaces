# YAI Interfaces Documentation

`interfaces/Documentation` is the canonical documentation surface for the YAI
developer interface. It covers protocol truth, operation semantics, transports,
envelopes, errors, schemas, registries, fixtures, conformance, OpenAPI
projections, mappings, contracts, lifecycle models, generated surfaces,
official SDK packages, developer examples, and integration contracts.

## Ownership

YAI Interfaces is the canonical developer-interface repository.

It owns:

- protocol contracts;
- operation semantics;
- transports;
- envelopes;
- errors;
- schemas;
- registries;
- fixtures;
- conformance;
- OpenAPI projections;
- mappings;
- contracts;
- lifecycle models;
- generated surfaces;
- official SDK packages;
- developer examples and integration contracts.

It does not own:

- YAI runtime implementation;
- YAI service lifecycle implementation;
- Console terminal UX;
- Web/account/product surfaces.

After INTF.4, SDK packages now live under:

- `packages/rust`
- `packages/python`
- `packages/typescript`
- `packages/c`

The previous SDK repository has been tombstoned and is historical only.
Historical material is kept under `archive/` and `internal/`; active
documentation uses this repository as the developer-interface authority.

## Official Reading Path

1. `Documentation/README.md`
2. `Documentation/INDEX.md`
3. `Documentation/architecture/overview.md`
4. `Documentation/architecture/interface-source-of-truth.md`
5. `Documentation/architecture/protocol-api-boundary.md`
6. `Documentation/architecture/sdk-consumption-boundary.md`
7. `Documentation/architecture/generation-boundary.md`
8. `Documentation/operations/operation-grammar.md`
9. `Documentation/operations/operation-to-transport-mapping.md`
10. `Documentation/transports/local-ipc-rpc.md`
11. `Documentation/envelopes/request-response-model.md`
12. `Documentation/errors/error-model.md`
13. `Documentation/conformance/conformance-policy.md`
14. `Documentation/packages/README.md`
15. `Documentation/generation/README.md`
16. `Documentation/examples/README.md`
17. `Documentation/reference/registry-index.md`

## Sections

- `architecture/` defines ownership, protocol/API boundaries, SDK consumption,
  generation, package, conformance, and external developer boundaries.
- `operations/` defines operation grammar, registry semantics, and projections.
- `transports/` defines transport contracts and compatibility boundaries.
- `envelopes/` defines request, response, readiness, and stream frames.
- `errors/` defines error shape, codes, status mapping, and transport mapping.
- `domains/` defines protocol/API-facing domain projections.
- `conformance/` defines release, compatibility, readiness, and checks.
- `packages/` defines official SDK package boundaries.
- `generation/` defines generated surface and generator boundaries.
- `examples/` defines protocol and SDK example boundaries.
- `reference/` indexes artifact roots without moving them.
- `decisions/` records active interface decisions.
- `internal/` and `archive/` are not the public reading path.

Do not use `internal/` or `archive/` as current interface authority unless a
canonical document explicitly points there for history.
