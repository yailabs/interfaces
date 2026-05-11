# SDK Conformance

SDK conformance verifies that packages align to YAI Interfaces protocol truth.

SDK packages must:

- consume operation registry, schema, mapping, envelope, error, and transport
  artifacts;
- preserve package identities;
- expose typed consumption surfaces;
- identify generated or projected material as projection;
- record validation residuals when package checks are blocked.

SDK packages must not define protocol truth. They must not create protocol
operations, redefine transport grammar, redefine envelope grammar, or treat
generated/build output as source.

Current package identities:

- Rust: `packages/rust`, `yai-sdk-rust`
- Python: `packages/python`, `yailabs-yai-sdk`, import `yai_sdk`
- TypeScript: `packages/typescript`, `@yailabs/sdk`
- C: `packages/c`, include prefix `<yai_sdk/...>`
