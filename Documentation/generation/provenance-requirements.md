# Provenance Requirements

Generated outputs are not protocol source of truth.

OpenAPI is projection. SDK operation constants are package projections. SDK
envelope/status/error types are package projections.

TypeScript `dist/` is generated output. Rust `target/` is generated/build
output. C `build/` and `dist/` are generated/build/release outputs. These paths
were intentionally excluded from INTF.4 and must not be moved into source
control as package source.

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

Current policy reference:

- `generators/provenance-policy.md`
- `conformance/profiles/interface-package-alignment.v1.md`
