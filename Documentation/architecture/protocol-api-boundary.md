# Protocol API Boundary

The API protocol boundary separates public contract truth from runtime and client implementations.

## API Owns

- Operation names, families, verbs, and projection records.
- Request, response, readiness, error, and stream frame shape.
- Transport contracts and operation-to-transport mapping.
- Contract indexes for registries, schemas, fixtures, OpenAPI, and transport artifacts.

## API Does Not Own

- Runtime system behavior beyond the API projection.
- SDK package APIs beyond the protocol contract they consume.
- Console terminal UX and interaction flow.
- Historical product surfaces preserved in `archive/`.

## Contract Taxonomy

Canonical contract material is stored in `registry/`, `schemas/`, `envelopes/`, `errors/`, `mappings/`, `transports/`, `openapi/`, and `conformance/`. Documentation explains those contracts; it does not replace the artifacts.
