# C Package

- Include prefix: `<yai_sdk/...>`
- Source path: `packages/c`
- Role: native C SDK package and compatibility-heavy bindings

## Protocol Truth Boundary

The C package consumes YAI Interfaces protocol artifacts. It may expose C
headers, native helpers, and compatibility surfaces, but it must not define
protocol truth.

## Validation Status

- INTF.4 `make check-config`: blocked because no law compatibility export was
  available.
- INTF.4 `make check`: blocked at `check-config` for the same reason.
- Status: `law-compatibility-export-required`

C `build/` and `dist/` are build/release outputs, not source, and were
intentionally excluded from INTF.4.

## Residual Validation Issues

- `law-compatibility-export-required`
- `pending-provenance`
- `pending-protocol-drift-check`
- `manual-review`

The old command-id vocabulary remains compatibility-only pending explicit
mapping to current interfaces operation ids.

Next validation owner/wave: INTF.6 guardrails and INTF.7 SDK tombstone /
absence guard.
