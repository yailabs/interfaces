# Package Validation Residuals

INTF.4 package validation produced the following results. INTF.6 preserves
these residuals as explicit guardrail inputs.

## Labels

Allowed residual labels:

- `passed`
- `no-tests-discovered`
- `dependency-install-required`
- `law-compatibility-export-required`
- `pending-provenance`
- `pending-protocol-drift-check`
- `manual-review`

## Rust

- Package: `yai-sdk-rust`
- Source path: `packages/rust`
- Validation: `cargo fmt --check`, `cargo check`, and `cargo test` passed.
- Status: `passed`
- Residual validation issues: `pending-provenance`,
  `pending-protocol-drift-check`

## Python

- Distribution/import: `yailabs-yai-sdk` / `yai_sdk`
- Source path: `packages/python`
- Validation: compile passed; `pytest` found 0 tests and exited 5.
- Status: `no-tests-discovered`
- Residual validation issues: `pending-provenance`,
  `pending-protocol-drift-check`

## TypeScript

- Package: `@yailabs/sdk`
- Source path: `packages/typescript`
- Validation: `npm test` and `npm run typecheck` were blocked because
  `node_modules` and `tsc` were unavailable.
- Status: `dependency-install-required`
- Residual validation issues: `pending-provenance`,
  `pending-protocol-drift-check`

## C

- Include prefix: `<yai_sdk/...>`
- Source path: `packages/c`
- Validation: `make check-config` and `make check` were blocked because no law
  compatibility export was available.
- Status: `law-compatibility-export-required`
- Residual validation issues: `pending-provenance`,
  `pending-protocol-drift-check`, `manual-review`

## Next Owner

INTF.6 owns guardrails, provenance policy, package alignment profile, and
lightweight drift checks. INTF.7 owns SDK tombstone and absence guard.
