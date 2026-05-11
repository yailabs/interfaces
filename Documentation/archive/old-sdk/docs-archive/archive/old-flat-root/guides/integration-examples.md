# Integration Examples

The SDK ships with self-contained examples under `examples/`:

- `01_basic_connection.c`: open client, configure logging, execute ping
- `02_workspace_context.c`: set/switch/unset/get/resolve current workspace binding
- `03_custom_control_call.c`: send typed control call model and parse typed runtime/governance state
- `04_workspace_verticalized.c`: use canonical typed workspace families (`graph`, `db`, `data`, `knowledge`, `policy`, `debug`)
- `05_source_plane_typed.c`: use typed source-plane APIs (`enroll`, `attach`, `emit`, `status`, `summary`)

## Operational semantics used by examples

- examples target the unified runtime (`core`, `exec`, `data`, `graph`,
  `knowledge`) through runtime control calls
- workspace context is binding context, not just a label
- replies must be interpreted with readiness semantics:
  - runtime liveness
  - workspace selected
  - workspace-bound capabilities ready/degraded/unbound

## Suggested manual flow

1. Run `01_basic_connection` to validate ingress/liveness.
2. Run `02_workspace_context` to bind active workspace.
3. Run `03_custom_control_call` for low-level typed control-call fallback.
4. Run `04_workspace_verticalized` for first-class `yai ws ...` family helpers.
5. Run `05_source_plane_typed` for first-class source-plane wrappers.
6. Verify response includes decision/evidence/execution and binding metadata.

Build all examples:

```bash
make examples
```

Binaries are generated under `dist/bin/`.

## SDK-2 model-contract usage

For typed request/response handling:

- build requests with `yai_sdk_control_call_t` + `yai_sdk_client_call`
- extract runtime/binding state with `yai_sdk_reply_runtime_state`
- extract governance/attachability state with `yai_sdk_reply_governance_state`
- prefer first-class workspace helpers for canonical families:
  - `yai_sdk_ws_graph_*`
  - `yai_sdk_ws_db_*`
  - `yai_sdk_ws_data_*`
  - `yai_sdk_ws_knowledge_*`
  - `yai_sdk_ws_policy_*`
  - `yai_sdk_ws_recovery_*`
  - `yai_sdk_ws_debug_resolution`
  - `yai_sdk_source_*`

Raw JSON call path (`yai_sdk_client_call_json`) remains available as compatibility path.
It is not the primary consumer path when typed workspace-family helpers exist.

Runtime locator/transport configuration model: `Documentation/SDK_RUNTIME_LOCATOR_AND_TRANSPORT_MODEL.md`.


Canonical onboarding flow: `Documentation/SDK_QUICKSTART.md`.
