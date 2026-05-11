# Package Taxonomy

YAI Interfaces has four official SDK package families:

| Language | Path | Identity | Role |
| --- | --- | --- | --- |
| Rust | `packages/rust` | `yai-sdk-rust` | Native typed client and transport package |
| Python | `packages/python` | `yailabs-yai-sdk` / `yai_sdk` | Python typed client package |
| TypeScript | `packages/typescript` | `@yailabs/sdk` | Browser, Node, and web-client typed package |
| C | `packages/c` | `<yai_sdk/...>` | Native C package and compatibility-heavy bindings |

All package families are projections over the canonical interface artifacts.
They may carry language-specific ergonomics, but protocol truth remains in the
registry, schema, mapping, transport, envelope, error, and contract roots.
