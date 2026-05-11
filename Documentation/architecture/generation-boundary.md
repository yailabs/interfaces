# Generation Boundary

Generated outputs are not source of truth.

Generated surfaces require provenance that identifies:

- registry input;
- schema input;
- mapping input;
- generator identity and version;
- source commit or release;
- conformance profile.

OpenAPI is projection. SDK generated constants, generated clients, generated
schemas, and generated registries must trace back to canonical protocol
artifacts.

TypeScript `dist/`, C `dist/` and `build/`, and Rust `target/` are build
outputs. They were intentionally excluded from INTF.4 and must not be treated
as source.
