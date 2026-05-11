# TypeScript Package

- Package name: `@yailabs/sdk`
- Source path: `packages/typescript`
- Role: TypeScript SDK package for browser, Node, and web-client consumers

## Protocol Truth Boundary

The TypeScript package consumes YAI Interfaces protocol artifacts. It may expose
typed clients, package transports, generated constants, and examples, but it
must not define protocol truth.

## Validation Status

- INTF.4 `npm test`: blocked because `tsc` was not found.
- INTF.4 `npm run typecheck`: blocked because `tsc` was not found.
- `node_modules` was intentionally not moved.
- Status: `dependency-install-required`

TypeScript `dist/` is generated output, not source, and was intentionally
excluded from INTF.4.

## Residual Validation Issues

- `dependency-install-required`
- `pending-provenance`
- `pending-protocol-drift-check`

Next validation owner/wave: INTF.6 guardrails and INTF.7 SDK tombstone /
absence guard.
