# Protocol/API Boundary

The protocol/API boundary separates public developer-interface contract truth
from runtime, SDK package, Console, and Web implementations.

## Interfaces Owns

- Operation names, families, verbs, and projection records.
- Request, response, readiness, error, and stream frame shape.
- Transport contracts and operation-to-transport mapping.
- Contract indexes for registries, schemas, fixtures, OpenAPI, and transport artifacts.

## Interfaces Does Not Own

- Runtime system behavior beyond the protocol/API projection.
- SDK package behavior beyond the protocol contract they consume.
- Console terminal UX and interaction flow.
- Web/account/product surfaces.
- Historical product surfaces preserved in `archive/`.

## Contract Taxonomy

Canonical contract material is stored in `registry/`, `schemas/`,
`envelopes/`, `errors/`, `mappings/`, `transports/`, `openapi/`,
`contracts/`, `lifecycle/`, and `conformance/`. Documentation explains those
contracts; it does not replace the artifacts.
