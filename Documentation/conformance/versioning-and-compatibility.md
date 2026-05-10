# Versioning And Compatibility

API versioning applies to protocol artifacts, schemas, operation records, transports, envelopes, errors, and projections.

## Compatibility Rules

- Additive operation and schema changes are preferred.
- Breaking changes require explicit versioning and migration notes.
- Transport compatibility must not change operation semantics.
- Deprecated operations remain explicit in registry artifacts until removed by policy.
- Client and SDK behavior derives from protocol version contracts.
