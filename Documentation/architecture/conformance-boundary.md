# Conformance Boundary

Conformance proves that interface artifacts, generated surfaces, and SDK
packages align with the claimed protocol and compatibility profiles.

## Conformance Owns

- Protocol integrity checks.
- Schema, registry, envelope, error, mapping, and transport checks.
- Generated surface provenance checks.
- SDK package alignment checks after SDK drain.
- Compatibility profile evidence.

## Conformance Does Not Own

- Runtime feature completeness.
- Console UX correctness.
- Web/account/product behavior.
- Package release decisions without validation evidence.

## Rule

Conformance must distinguish protocol existence from implementation readiness.
An operation can be valid protocol truth while runtime support is unavailable,
blocked, deferred, or not implemented.
