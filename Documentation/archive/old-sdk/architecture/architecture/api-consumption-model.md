# API Consumption Model

SDK packages consume API contracts from the API repository. They do not redefine protocol identity.

API identity/auth/account contracts are upstream access projection contracts. SDKs may expose typed clients for those contracts, but they do not make `identity` a native YAI runtime plane. Runtime-facing access posture is consumed by `../yai/src/runtime/access`.

## Source Inputs

- `../api/registry/`
- `../api/schemas/`
- `../api/envelopes/`
- `../api/errors/`
- `../api/mappings/`
- `../api/transports/`
- `../api/openapi/`

## SDK Responsibilities

- Generate or hand-write typed client surfaces from API contract input.
- Preserve operation ids and status/error semantics from API artifacts.
- Report unavailable or deferred operations honestly.
- Keep compatibility aliases separate from canonical operation names.

## Non-Responsibilities

SDK does not own API protocol, operation grammar, transport grammar, envelope shape, or error registry truth. Those remain in `../api/Documentation` and API artifacts.
