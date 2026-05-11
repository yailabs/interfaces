# Package Boundary

Official SDK packages live under `packages/`:

- Rust: `packages/rust`, package name `yai-sdk-rust`;
- Python: `packages/python`, distribution `yailabs-yai-sdk`, import
  `yai_sdk`;
- TypeScript: `packages/typescript`, package name `@yailabs/sdk`;
- C: `packages/c`, include prefix `<yai_sdk/...>`.

Package versions are separate from protocol version. A package version records
language package release state. It must declare the protocol version,
generated-surface version, and conformance profile it supports.

Package manifests and README files may describe package usage. They do not
replace protocol registry, schema, mapping, or conformance authority.
