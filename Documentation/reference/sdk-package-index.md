# SDK Package Index

Canonical replacement for the old standalone SDK repository:

- `interfaces/packages`

| Language | Path | Package identity | INTF.4 validation |
| --- | --- | --- | --- |
| Rust | `packages/rust` | `yai-sdk-rust` | `cargo fmt`, `cargo check`, and `cargo test` passed |
| Python | `packages/python` | `yailabs-yai-sdk`, import `yai_sdk` | compile passed; no tests discovered |
| TypeScript | `packages/typescript` | `@yailabs/sdk` | `tsc` unavailable because dependencies were not moved |
| C | `packages/c` | `<yai_sdk/...>` | law compatibility export required |

SDK packages are typed consumption/projection surfaces. They must not define
protocol truth.

The old standalone SDK repository is tombstone/historical only and is not an
active source for package code, generated surfaces, conformance, or developer
documentation.
