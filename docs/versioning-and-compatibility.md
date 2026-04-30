# API Versioning and Compatibility

- Contracts evolve with explicit versioned schema/envelope identifiers.
- Envelope and error model changes must preserve backward compatibility unless explicitly version-bumped.
- Family contracts may be `stable`, `transitional`, or `deferred`, and must be declared honestly.

Canonical statuses:
- `ok`
- `partial`
- `pending`
- `ready`
- `unavailable`
- `blocked`
- `denied`
- `error`
