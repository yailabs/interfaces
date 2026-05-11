# Generated Surface Index

Generated surface docs:

- `Documentation/generation/generated-surface.md`
- `Documentation/generation/sdk-generation.md`
- `Documentation/generation/schema-generation.md`
- `Documentation/generation/openapi-generation.md`
- `Documentation/generation/registry-generation.md`
- `Documentation/generation/provenance-requirements.md`
- `generators/provenance-policy.md`
- `projections/generated/README.md`

Generated/build outputs are not protocol source of truth. OpenAPI is
projection. SDK operation constants and SDK envelope/status/error types are
package projections.

Excluded generated/build output paths:

- `packages/rust/target`
- `packages/typescript/node_modules`
- `packages/typescript/dist`
- `packages/c/build`
- `packages/c/dist`

Guard script:

- `tools/checks/check-generated-output-exclusion.sh`
