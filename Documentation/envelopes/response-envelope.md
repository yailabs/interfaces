# Response Envelope

A response envelope carries completion status, result payloads, errors, warnings, records, evidence, and metadata for an API operation.

## Status Semantics

Responses must distinguish successful results, structured errors, warnings, and metadata. Error responses use the canonical error model rather than transport-specific ad hoc payloads.

## Artifact References

- `schemas/response-envelope.v1.schema.json`
- `envelopes/response-envelope.v1.md`
