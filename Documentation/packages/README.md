# SDK Packages

Official SDK packages live inside YAI Interfaces:

- Rust: `packages/rust`
- Python: `packages/python`
- TypeScript: `packages/typescript`
- C: `packages/c`

The old standalone SDK repository has been tombstoned. Active package work must
use `interfaces/packages`.

SDK packages are typed consumption surfaces. They consume protocol contracts,
operation registries, schemas, mappings, envelopes, errors, and transport
contracts from this repository. They must not define protocol truth.

Package versions are language package versions and remain separate from
protocol version, generated surface version, conformance profile version, and
repository release version.
