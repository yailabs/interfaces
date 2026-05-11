# SDK API Discipline

## Canonical entry

- `#include <yai_sdk/public.h>`

## API classes

### public_stable (canonical)

- `yai_sdk/public.h`
- `yai_sdk/core.h`
- `yai_sdk/runtime.h`
- `yai_sdk/models.h`
- `yai_sdk/transport.h`
- `yai_sdk/workspace.h`
- `yai_sdk/exec.h`
- `yai_sdk/data.h`
- `yai_sdk/graph.h`
- `yai_sdk/knowledge.h`
- `yai_sdk/source.h`
- `yai_sdk/governance.h`

### public_stable (compatibility retained)

- `yai_sdk/errors.h`
- `yai_sdk/paths.h`
- `yai_sdk/context.h`
- `yai_sdk/client.h`
- `yai_sdk/catalog.h`
- `yai_sdk/protocol.h`
- `yai_sdk/rpc.h`
- `yai_sdk/log.h`
- `yai_sdk/reply/*`

### internal (or advanced internal)

- `yai_sdk/registry/*`

## Rules

1. Do not make registry internals the public identity of SDK.
2. Canonical new integrations should use typed request/model APIs:
   - `yai_sdk_client_call`
   - `yai_sdk_reply_runtime_state`
   - `yai_sdk_reply_governance_state`
3. Compatibility JSON path (`yai_sdk_client_call_json`) is transitional and non-canonical for new usage.
4. Public API evolution is semver-governed.
5. Internal headers may evolve without public-stable guarantees.
6. Compatibility with law surfaces is declared, not structurally pinned.
