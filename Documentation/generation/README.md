# Generation

Generation docs define generated-surface boundaries and provenance
requirements.

Generated outputs are not source of truth. OpenAPI is projection. SDK operation
constants and envelope types are package projections pending validation.

Generated outputs require registry, schema, mapping, and generator provenance.
TypeScript `dist/`, Rust `target/`, and C `build/` and `dist/` were
intentionally excluded from INTF.4.
