# SDK Package Conformance

Status: INTF.4 package drain baseline.

SDK packages must validate against interfaces protocol artifacts and declared
conformance profiles. Package tests may exercise package projections, but those
projections must not redefine protocol truth.

Package validation commands for INTF.4:

- Rust: `cargo fmt --check`, `cargo check`, `cargo test`
- Python: `python3 -m compileall src`, `python3 -m pytest tests`
- TypeScript: `npm test`, `npm run typecheck`
- C: `make check-config`, `make check`

C ABI compatibility remains package ABI compatibility. The old
`YAI_SDK_CMD_WORKSPACE_*` vocabulary is compatibility vocabulary pending later
isolation.
