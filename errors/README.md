# Error Model

`api/errors/` defines the canonical transport-facing API error grammar.

Primary files:

- `api-error-model.v1.md`
- `error-code-registry.v1.json`
- `error-http-status-map.v1.json`
- `error-transport-map.v1.md`

Canonical API error fields:

- `code`
- `message`
- `category`
- `retryable`
- `transport_error`
- `operation_error`
- `guard_error`
- `details` (optional)
- `cause` (optional)
- `refs` (optional)

Error codes are API-owned and versioned here. Transport failure, guard failure,
and operation failure must remain distinguishable.
