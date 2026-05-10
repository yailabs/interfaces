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


Consumption rule:
- SDK is the official client consumption layer.
- Direct API repo consumption is limited to debug/conformance/bootstrap integrations.
- Legacy session contracts remain compatibility surfaces and do not redefine identity/operator-context ownership.
