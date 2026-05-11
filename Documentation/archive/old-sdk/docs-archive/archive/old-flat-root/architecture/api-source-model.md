# API Source Readiness Notes

Source registry: `../api/registry/api-operations.v1.json`.

Wave 16B posture:
- TypeScript SDK exposes typed plane clients and operation IDs.
- SDK transport remains abstract until a real transport is provided.
- Client methods do not claim runtime execution when transport is unavailable.
- OpenAPI and conformance remain scaffolded in API.

Wave 22D8: API-sourced identity/account fields are reference/posture-only contracts and are not account-backend capabilities.
