# Lifecycle Vocabulary

`api/lifecycle/` defines API-facing operation result and lifecycle-adjacent
status vocabulary, not runtime service-manager implementation.

Primary files:

- `operation-result-model.v1.md`

Canonical API response status vocabulary:

- `ok`
- `accepted`
- `partial`
- `unavailable`
- `blocked`
- `invalid`
- `failed`

Family compatibility and readiness claims must be explicit and version-aware.
Transport failure must stay distinct from operation result status.
