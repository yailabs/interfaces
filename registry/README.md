# API Registry

Registry files are the canonical API operation and projection grammar source.

They are not runtime truth.
They do not own CLI command strings, TUI menu labels, or transport endpoint
behavior.

V51 alignment rules:

- API registry is operation/projection canon.
- API registry is not runtime truth.
- API registry must not preserve session as canonical domain truth.
- API registry must distinguish API family names from CLI/TUI projection names.
- API registry must expose legacy, deprecated, and forbidden status explicitly.
- API identity/auth/account contracts project to `../yai/src/runtime/access`; `identity` is not a native YAI runtime plane.
- Action alignment is seeded from `yai-actions.v1.json`.

Primary files:
- `api-families.v1.json`
- `api-verbs.v1.json`
- `api-operations.v1.json`
- `api-operation-projections.v1.json`
- `api-surfaces.v1.json`
- `api-clients.v1.json`
- `api-errors.v1.json`
- `api-envelopes.v1.json`
- `yai-actions.v1.json`

Non-goals:
- runtime command tree ownership
- CLI command catalog ownership
- protocol cutover ownership
