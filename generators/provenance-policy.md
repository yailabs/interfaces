# Generator Provenance Policy

Generated outputs are not protocol source of truth.

OpenAPI is projection. SDK operation constants are package projections. SDK
envelope/status/error types are package projections.

Generated/build output classes:

- TypeScript `dist/` is generated output.
- Rust `target/` is generated/build output.
- C `build/` and `dist/` are generated/build/release outputs.

Generated outputs retained in interfaces must record:

- source registry version or digest;
- source schema version or digest;
- source mapping version or digest;
- generator name;
- generator version;
- generation command;
- generated surface version/stamp;
- source commit or release tag where available;
- conformance profile used for validation.

The active INTF.6 conformance profile is
`conformance/profiles/interface-package-alignment.v1.md`.
