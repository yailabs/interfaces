# Quickstart

This quickstart is the canonical starting point for SDK consumers.

## Choose A Package

- Rust native client: start with `packages/rust/README.md` and `packages/rust.md`.
- TypeScript client: start with `packages/typescript/README.md` and `packages/typescript.md`.
- Python integration: start with `packages/python/README.md` and `packages/python.md`.
- C native compatibility: start with `packages/c/README.md` and `packages/c.md`.

## Connect Explicitly

SDK clients should use explicit transport configuration. Absence of a configured transport must surface as unavailable or not configured, not as fake readiness.

## Read Next

- `guides/client-adoption.md`
- `guides/local-runtime-connection.md`
- `guides/error-handling.md`
