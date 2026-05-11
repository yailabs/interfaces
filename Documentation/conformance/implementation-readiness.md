# Implementation Readiness

Implementation readiness records whether protocol artifacts, generated
surfaces, and SDK packages are ready for downstream runtime or client work.

Current package readiness after INTF.4:

| Package | Readiness | Notes |
| --- | --- | --- |
| Rust | Ready for current package checks | `cargo fmt`, `cargo check`, and `cargo test` passed |
| Python | Compile-ready | Python compile passed; no tests were discovered |
| TypeScript | Blocked on dependency install | `tsc` unavailable because `node_modules` was not moved |
| C | Blocked on law compatibility export | strict `make check-config` cannot pass without export |

INTF.6 owns guardrails, provenance, and package validation hardening. Until
then, residuals are explicit readiness constraints, not hidden failures.
