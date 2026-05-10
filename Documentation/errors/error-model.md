# Error Model

API errors use a structured protocol shape shared across transports.

## Error Semantics

An error identifies code, message, classification, retryability, safe metadata, and any domain references needed by clients. Transport-specific status or exit behavior maps to the canonical error, not the other way around.

## Artifact References

- `schemas/error.v1.schema.json`
- `errors/api-error-model.v1.md`
- `errors/error-code-registry.v1.json`
