# SDK Drain Package Notes

Status: INTF.4 active package drain complete.

Active SDK package source now lives under `packages/`:

- Rust: `packages/rust`, crate `yai-sdk-rust`
- Python: `packages/python`, distribution `yailabs-yai-sdk`, import `yai_sdk`
- TypeScript: `packages/typescript`, package `@yailabs/sdk`
- C: `packages/c`, include prefix `<yai_sdk/...>`

The package source moved without renaming public package identities. SDK
operation constants, envelope types, and C command-id vocabulary remain package
projections or compatibility vocabulary; they do not define protocol truth.

Generated and build outputs were not moved as active source:

- `sdk/packages/rust/target/`
- `sdk/packages/typescript/node_modules/`
- `sdk/packages/typescript/dist/`
- `sdk/packages/c/build/`
- `sdk/packages/c/dist/`

Historical standalone SDK documentation and root metadata are archived under
`Documentation/archive/old-sdk/`.
