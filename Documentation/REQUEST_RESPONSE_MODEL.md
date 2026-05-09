# Request/Response Model

Canonical request envelope fields:
- operation_id, request_id, client, session, case_ref, principal_ref, input, metadata, idempotency_key

Canonical response envelope fields:
- operation_id, request_id, status, result, error, records, evidence, warnings, metadata

Schemas:
- `schemas/request-envelope.v1.schema.json`
- `schemas/response-envelope.v1.schema.json`
- `schemas/error.v1.schema.json`
- `schemas/operation-result.v1.schema.json`
