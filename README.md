# YAI Interfaces

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

## Repository Status

This repository was canonicalized from the former API source base in INTF.2.
After INTF.4, official SDK packages now live under:

- `packages/rust`
- `packages/python`
- `packages/typescript`
- `packages/c`

The previous SDK repository has been tombstoned and is historical only. It is
not the active developer-interface authority.

## Source Of Truth

Canonical developer-interface truth lives in this repository:

- `registry/`
- `schemas/`
- `mappings/`
- `transports/`
- `envelopes/`
- `errors/`
- `contracts/`
- `lifecycle/`
- `fixtures/`
- `conformance/`
- `openapi/`
- `projections/`
- `packages/`
- `Documentation/`

Protocol, operation registry, schema, and mapping artifacts are source of
truth. OpenAPI is a projection. SDK packages are typed consumption surfaces and
must not define protocol truth.

## Boundaries

YAI runtime and system behavior belong to the YAI runtime repository.

Console terminal UX belongs to the Console repository.

Web, account, download, dashboard, and commercial product surfaces belong to
their product repositories.

Developer and client flow:

```text
external client or Console or future Studio
  -> interfaces SDK/API
  -> yai runtime/system effect
```

## Build And Validation

Documentation validation for this repository starts with:

```sh
python3 -m json.tool interface-manifest.json >/dev/null
git diff --check
```

Protocol and package conformance checks are indexed under `conformance/` and
`Documentation/conformance/`.

## Licensing

YAI is the YAI Community Source Tree. Development and non-production use are
permitted under the applicable license terms. Commercial licensing is required
for production, organizational, persistent, collaborative, customer-affecting,
or business-critical use.
