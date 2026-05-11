# SDK Package Taxonomy

- `packages/c`: targets Console compatibility/native clients; `yai-cli` remains a legacy command name.
- `packages/typescript`: targets `yai-design`, `yai-console`, `yai-desktop`, `yai-vscode`.
- `packages/python`: targets integrations and automation.
- `packages/rust`: targets native Rust clients (Console native).
- direct runtime adapter imports are forbidden for normal product paths; exception-only usage is `debug/conformance/bootstrap`.

Future language packages may be added without changing API contract ownership.


Design consumer repository path: `../design` (product identity: YAI Design).
