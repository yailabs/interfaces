# Python Package

- Distribution: `yailabs-yai-sdk`
- Import: `yai_sdk`
- Source path: `packages/python`
- Role: Python typed SDK package

## Protocol Truth Boundary

The Python package consumes YAI Interfaces protocol artifacts. It may expose
typed clients, Python helpers, and package examples, but it must not define
protocol truth.

## Validation Status

- INTF.4 compile validation: passed.
- INTF.4 `pytest`: found 0 tests and exited 5.
- Status: `no-tests-discovered`

The pytest result is classified as `no-tests-discovered`, not a package
failure.

## Residual Validation Issues

- `pending-provenance`
- `pending-protocol-drift-check`

Next validation owner/wave: INTF.6 guardrails and INTF.7 SDK tombstone /
absence guard.
