# Rust Package

- Package name: `yai-sdk-rust`
- Source path: `packages/rust`
- Role: native typed SDK package

## Protocol Truth Boundary

The Rust package consumes YAI Interfaces protocol artifacts. It may expose typed
clients, transport bindings, operation constants, status types, and envelope
helpers, but it must not define protocol truth.

## Validation Status

- INTF.4 `cargo fmt --check`: passed after formatting during INTF.4.
- INTF.4 `cargo check`: passed.
- INTF.4 `cargo test`: passed.
- Status: `passed`

## Residual Validation Issues

- `pending-provenance`
- `pending-protocol-drift-check`

Generated or build output such as Rust `target/` is not source and was
intentionally excluded from INTF.4.

Next validation owner/wave: INTF.6 guardrails and INTF.7 SDK tombstone /
absence guard.
