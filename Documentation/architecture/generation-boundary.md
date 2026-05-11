# Generation Boundary

Generated surfaces are projections over YAI Interfaces artifacts and generator
templates.

## Generated Surface Inputs

- Interface operation and registry artifacts.
- Interface schemas, envelopes, errors, mappings, lifecycle, and transport
  contracts.
- SDK package templates after SDK drain.
- OpenAPI generation templates.
- Registry and schema generation rules.

## Boundary Rules

- Generated code must not invent protocol grammar.
- Generated clients must preserve operation ids, status, error, envelope, and
  transport semantics from interface artifacts.
- Generated outputs must record provenance before release claims.
- Handwritten package code remains valid when generation is not yet available,
  but it must not drift from interface contracts.

## Artifact References

- `projections/`
- `generators/`
- `openapi/`
- `schemas/`
- `interface-manifest.json`
