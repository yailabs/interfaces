# SDK Public Runtime Surface

This document defines the canonical SDK-1 public surface for unified runtime
consumers.

## Canonical include entry

```c
#include <yai_sdk/public.h>
```

## Canonical public taxonomy headers

- `yai_sdk/core.h`
- `yai_sdk/runtime.h`
- `yai_sdk/models.h`
- `yai_sdk/transport.h`
- `yai_sdk/workspace.h`
- `yai_sdk/exec.h`
- `yai_sdk/db.h`
- `yai_sdk/data.h`
- `yai_sdk/graph.h`
- `yai_sdk/knowledge.h`
- `yai_sdk/source.h`
- `yai_sdk/policy.h`
- `yai_sdk/recovery.h`
- `yai_sdk/debug.h`
- `yai_sdk/governance.h`

## Compatibility headers retained

The following remain available for compatibility, but are no longer the primary
public taxonomy axis:

- `yai_sdk/client.h`
- `yai_sdk/context.h`
- `yai_sdk/paths.h`
- `yai_sdk/catalog.h`
- `yai_sdk/protocol.h`
- `yai_sdk/rpc.h`
- `yai_sdk/reply/*`

## Public model decisions (SDK-1)

- Unified runtime is the only public runtime model.
- Workspace is a first-class binding context.
- Execution-facing surface aligns with `exec`.
- Data-plane surface aligns with `data`.
- Graph surface aligns with `graph`.
- Knowledge-support surface aligns with `knowledge`.
- Governance-facing commands are exposed as workspace-bound runtime commands.

## Transitional compatibility policy

Compatibility modules stay thin and non-canonical. New public surface design and
consumer documentation must target canonical taxonomy headers above.

## SDK-2 client contract layer

Canonical model contract is exposed through `yai_sdk/models.h` and client APIs:

- `yai_sdk_client_call` for request-model based control calls
- `yai_sdk_reply_runtime_state` for unified runtime/workspace/binding extraction
- `yai_sdk_reply_governance_state` for governance/attachability state extraction

This model layer is canonical for runtime status, workspace binding, capability-family readiness, and governance-facing consumer interpretation.

## Canonical consumer truth path

1. `README.md`
2. `Documentation/SDK_QUICKSTART.md`
3. `Documentation/INTEGRATION_EXAMPLES.md`
4. `examples/01_basic_connection.c`
5. `examples/02_workspace_context.c`
6. `examples/03_custom_control_call.c`
7. `examples/04_workspace_verticalized.c`
8. `examples/05_source_plane_typed.c`
9. `tests/public_surface_smoke.c` + `tests/models_contract_smoke.c` + `tests/workspace_typed_surface_smoke.c` + `tests/source_typed_surface_smoke.c`
10. `tests/runtime_locator_smoke.c`

## DX-1 extension

Public surface includes `yai_sdk/targets.h` for explicit owner/edge/mesh/overlay
runtime target taxonomy and remote association descriptors.
