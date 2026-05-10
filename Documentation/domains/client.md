# Client Domain

The client domain documents API-facing client references, connection references, attachment references, call context, and client-safe projection rules.

## API Owns

- Client reference and attachment schemas.
- Client connection projection boundaries.
- Call context fields carried in envelopes.
- Protocol metadata used by clients.

## API Delegates

- Terminal client UX truth to `../console/Documentation`.
- Typed client and package truth to `../sdk/Documentation`.
- Runtime implementation truth to `../yai/Documentation`.

## Artifact References

- `schemas/client-ref.v1.schema.json`
- `schemas/client-connection-ref.v1.schema.json`
- `schemas/client-attachment-ref.v1.schema.json`
- `schemas/client-surface-status.v1.schema.json`
- `conformance/check_client_call_context_projection.py`
