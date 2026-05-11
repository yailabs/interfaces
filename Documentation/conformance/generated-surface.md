# Generated Surface

Generated SDK surfaces must remain projections over API artifacts and package rules.

## Validation

- Generated files must declare or imply their API artifact source.
- Generated package code must preserve API envelope, error, and status semantics.
- Generated output must be indexed before release claims.
- Generated code must not create runtime, protocol, or terminal UX authority.

## Artifact References

- `generated/`
- `extraction/sdk-source-manifest.json`
- `reference/generated-surface-index.md`
