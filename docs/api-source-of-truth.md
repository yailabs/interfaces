# API Source of Truth

`../api` is the canonical owner of YAI operation grammar.

Canonical grammar sources:
- `registry/api-families.v1.json`
- `registry/api-verbs.v1.json`
- `registry/api-operations.v1.json`
- `registry/api-operation-projections.v1.json`
- `schemas/operation-*.v1.schema.json`

Rules:
- runtime does not own command grammar.
- CLI/Loom/SDK are projections/consumers, not grammar owners.
- C under `contracts/` is reference/helper implementation, not primary grammar truth.
