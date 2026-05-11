# YAI Interfaces

YAI Interfaces is the canonical developer-interface repository for YAI.

It owns:

- protocol contracts;
- operation semantics;
- transports;
- envelopes;
- errors;
- schemas;
- registries;
- fixtures;
- OpenAPI projections;
- conformance;
- mappings;
- contracts;
- lifecycle models;
- generated surfaces;
- official SDK packages after SDK drain;
- developer examples and integration contracts.

It does not own:

- YAI runtime implementation;
- YAI service lifecycle implementation;
- Console terminal UX;
- Web/account/product surfaces.

## Repository Status

This repository was locally canonicalized from the former `api` source base in
INTF.2. It is currently `pre-sdk-drain`: API/protocol artifacts are present,
while official SDK packages remain in the separate `sdk` repository until later
INTF waves classify and drain them.

The remote may still point to the historical API repository until a separate
remote rename is performed.

## Source Of Truth

Canonical developer-interface truth lives in the artifact and documentation
roots in this repository:

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
- `Documentation/`

OpenAPI is a projection over interface contracts. SDK packages consume these
contracts after drain; they do not define protocol truth.

## Boundaries

YAI runtime and system behavior belong to `../yai`.

Console terminal UX belongs to `../console`.

Web, account, download, dashboard, and commercial product surfaces belong to
`../web`.

SDK package source remains in `../sdk` until the SDK drain waves move package
material into `interfaces/packages/`.

## Build And Validation

Typical validation during the pre-sdk-drain phase:

```sh
python3 -m json.tool interface-manifest.json >/dev/null
python3 -m json.tool registry/api-operations.v1.json >/dev/null
```

Conformance checks remain under `conformance/`.

## Licensing

YAI is the YAI Community Source Tree. Development and non-production use are
permitted under the applicable license terms. Commercial licensing is required
for production, organizational, persistent, collaborative, customer-affecting,
or business-critical use.
