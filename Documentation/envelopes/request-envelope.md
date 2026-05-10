# Request Envelope

A request envelope carries the operation identity, caller context, domain references, operation input, and metadata required to dispatch an API operation.

## Required Semantics

- `operation_id` identifies the registered operation.
- `request_id` allows correlation and idempotent retry behavior.
- Client and principal references identify the caller boundary without transferring client ownership to API.
- Domain references such as case or operator context are explicit inputs, not hidden runtime state.
- `metadata` carries protocol metadata, not arbitrary runtime internals.

## Artifact References

- `schemas/request-envelope.v1.schema.json`
- `envelopes/request-envelope.v1.md`
