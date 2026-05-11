# Envelope Error Stream Model

The API uses a shared wire model across request/response operations, readiness projection payloads, errors, and event frames.

## Envelope Layer

- Request envelopes carry operation identity, request identity, client context, case or principal references, input, metadata, and idempotency data.
- Response envelopes carry operation identity, request identity, status, result or error, records, evidence, warnings, and metadata.
- Readiness envelopes expose safe service posture without leaking runtime internals.

## Error Layer

Errors use a canonical structured error shape, registered error codes, HTTP status mapping, and transport-specific mapping rules.

## Stream Layer

Stream frames carry event identity, type, sequencing, payload, error or terminal status, and resume semantics. Event stream transport docs define the concrete binding.
