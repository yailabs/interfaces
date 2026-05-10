# Request Response Model

The request/response model is the transport-neutral envelope contract for API operations.

## Request Envelope Fields

- `operation_id`
- `request_id`
- `client`
- `session` when explicitly supported by a compatibility boundary
- `case_ref`
- `principal_ref`
- `input`
- `metadata`
- `idempotency_key`

## Response Envelope Fields

- `operation_id`
- `request_id`
- `status`
- `result`
- `error`
- `records`
- `evidence`
- `warnings`
- `metadata`

## Artifact References

- `schemas/request-envelope.v1.schema.json`
- `schemas/response-envelope.v1.schema.json`
- `envelopes/request-envelope.v1.md`
- `envelopes/response-envelope.v1.md`
