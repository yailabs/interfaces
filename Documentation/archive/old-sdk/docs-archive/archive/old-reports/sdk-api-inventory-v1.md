# SDK API Inventory v1

Generated for API Discipline v1.

## Canonical Public Headers (`public_stable`)

- `include/yai_sdk/public.h`
- `include/yai_sdk/transport.h`
- `include/yai_sdk/source.h`
- `include/yai_sdk/errors.h`
- `include/yai_sdk/paths.h`
- `include/yai_sdk/context.h`
- `include/yai_sdk/client.h`
- `include/yai_sdk/catalog.h`
- `include/yai_sdk/protocol.h`
- `include/yai_sdk/rpc.h`
- `include/yai_sdk/log.h`
- `include/yai_sdk/reply/reply.h`
- `include/yai_sdk/reply/reply_builder.h`
- `include/yai_sdk/reply/reply_json.h`

## Internal Headers (`internal`)

- `include/yai_sdk/registry/registry.h`
- `include/yai_sdk/registry/registry_help.h`
- `include/yai_sdk/registry/registry_paths.h`
- `include/yai_sdk/registry/registry_cache.h`
- `include/yai_sdk/registry/registry_registry.h`
- `include/yai_sdk/registry/registry_types.h`
- `include/yai_sdk/registry/registry_validate.h`

## Module Classification

- `client` -> `public_stable`
- `catalog/help_index` -> `public_stable`
- `context/workspace` -> `public_stable`
- `reply` -> `public_stable`
- `protocol/rpc` -> `public_stable`
- `logging` -> `public_stable`
- `registry raw loaders/validators` -> `internal`

## Examples and Wrappers

- Examples: `examples/01_basic_connection.c`, `examples/02_workspace_context.c`, `examples/03_custom_control_call.c`, `examples/04_workspace_verticalized.c`
- Source example: `examples/05_source_plane_typed.c`
- Wrapper skeleton: `wrappers/python/yai_sdk.py`

## CLI Coupling Status

`cli` should consume only `public_stable` headers (prefer `yai_sdk/public.h`).
No `yai_sdk/registry/*` include is allowed in CLI production code.

## Wave CLI-2A Inventory Delta

Added Rust SDK operations/surfaces:

- `session.status.inspect`
- `case.current.inspect`
- `provider.list.inspect`
- `models.list.inspect`

All four are surfaced via `YaiClient` family accessors and `surfaces/*` modules.
