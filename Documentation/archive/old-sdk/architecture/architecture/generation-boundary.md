# Generation Boundary

Generated SDK surfaces are projections over API artifacts and package templates.

## Generated Surface Inputs

- API registry and schema artifacts.
- API envelope, error, mapping, and transport artifacts.
- SDK package templates and language-specific generation rules.

## Boundary Rules

- Generated code must not invent protocol grammar.
- Generated clients must preserve API status, error, and envelope semantics.
- Generated outputs must be indexed and validated before release claims.
- Hand-written package code remains valid when generation is not yet available.

## Artifact References

- `generated/`
- `extraction/`
- `tools/`
