# API Projection Source of Truth

`../api` is the canonical owner of YAI API exposure grammar.

Canonical API projection sources:
- `registry/api-families.v1.json`
- `registry/api-verbs.v1.json`
- `registry/api-operations.v1.json`
- `registry/api-operation-projections.v1.json`
- `schemas/operation-*.v1.schema.json`

Rules:
- `yai/protocols` defines transport-neutral protocol meaning.
- `api` projects that meaning into API operation grammar and API-facing schemas.
- runtime does not own API grammar.
- Console/SDK are projections or consumers, not API grammar owners.
- Legacy CLI/Loom names remain compatibility/history only and do not define
  separate canonical clients.
- C under `contracts/` is reference/helper implementation, not primary protocol truth.
