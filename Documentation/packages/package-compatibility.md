# Package Compatibility

Package compatibility is evaluated across separate layers:

- protocol version;
- SDK package version;
- generated surface version;
- conformance profile version;
- repository release version.

A package is compatible when it declares the protocol and conformance profile it
supports and passes the checks required for that profile.

## INTF.6 Package Status

| Package | Path | Validation status | Residual labels |
| --- | --- | --- | --- |
| Rust `yai-sdk-rust` | `packages/rust` | INTF.4 `fmt`, `check`, and `test` passed | `passed`, `pending-provenance`, `pending-protocol-drift-check` |
| Python `yailabs-yai-sdk` / `yai_sdk` | `packages/python` | compile passed; no tests discovered | `no-tests-discovered`, `pending-provenance`, `pending-protocol-drift-check` |
| TypeScript `@yailabs/sdk` | `packages/typescript` | dependency install required for `tsc` checks | `dependency-install-required`, `pending-provenance`, `pending-protocol-drift-check` |
| C `<yai_sdk/...>` | `packages/c` | law compatibility export required for strict checks | `law-compatibility-export-required`, `pending-provenance`, `pending-protocol-drift-check`, `manual-review` |

## Release Readiness Rule

Package release readiness requires:

- conformance profile `interface-package-alignment.v1` applicability;
- generated output exclusion guard passing;
- protocol/package drift guard reviewed;
- provenance recorded for generated/package-facing surfaces;
- language validation residuals resolved or explicitly accepted by release
  policy;
- package docs preserving the protocol truth boundary.

INTF.6 owns guardrails, provenance, and package validation hardening. INTF.7
owns SDK tombstone and absence guard.
