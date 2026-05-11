# Enterprise SDK Standard

The SDK is the official typed client consumption layer for YAI packages and product integrations.

## Standard

- SDK packages consume API contracts from `../api`.
- SDK packages do not own runtime implementation.
- SDK packages must preserve unavailable, blocked, denied, and error status honestly.
- Direct runtime adapter usage is exception-only for debug, conformance, or bootstrap contexts.
- Compatibility aliases must be explicit and must not displace canonical API-aligned names.

## Package Scope

The standard applies to Rust, TypeScript, Python, C, generated surfaces, examples, and developer-facing docs.
