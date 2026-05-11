# SDK Quickstart (Canonical SDK-3 Path)

This quickstart demonstrates the canonical SDK consumer path after SDK-1/SDK-2/WSV-5:

- include `yai_sdk/public.h`
- use workspace-first context
- call typed workspace family helpers for the canonical `ws` surface
- parse typed runtime/governance state from replies

## 1) Open client

```c
#include <yai_sdk/public.h>

yai_sdk_client_t *client = NULL;
yai_sdk_client_opts_t opts = {
  .ws_id = "demo",
  .role = "operator",
  .arming = 1,
  .auto_handshake = 1,
  .correlation_id = "quickstart",
};

int rc = yai_sdk_client_open(&client, &opts);
```

## 2) Bind workspace context

```c
yai_sdk_workspace_bind("demo");
```

## 3) Call canonical typed workspace helpers

```c
yai_sdk_reply_t reply = {0};
rc = yai_sdk_ws_status(client, &reply);           /* workspace lifecycle/binding */
yai_sdk_reply_free(&reply);
rc = yai_sdk_ws_graph_summary(client, &reply);    /* graph family */
yai_sdk_reply_free(&reply);
rc = yai_sdk_ws_db_status(client, &reply);        /* db family (direct/composed) */
yai_sdk_reply_free(&reply);
rc = yai_sdk_ws_data_evidence(client, &reply);    /* data family */
yai_sdk_reply_free(&reply);
rc = yai_sdk_ws_knowledge_status(client, &reply); /* knowledge family */
yai_sdk_reply_free(&reply);
rc = yai_sdk_ws_policy_effective(client, &reply); /* policy family */
```

## 4) Parse canonical models from reply payloads

```c
yai_sdk_runtime_state_t runtime_state;
yai_sdk_governance_state_t governance_state;

if (rc == YAI_SDK_OK) {
  yai_sdk_reply_runtime_state(&reply, &runtime_state);
  yai_sdk_reply_governance_state(&reply, &governance_state);
}
```

## 5) Interpret readiness and binding

Use model fields, not string heuristics:

- runtime liveness: `runtime_state.liveness`
- workspace binding: `runtime_state.workspace_binding`
- family readiness:
  - `runtime_state.exec`
  - `runtime_state.data`
  - `runtime_state.graph`
  - `runtime_state.knowledge`
- governance effect/review/blocked:
  - `governance_state.effect`
  - `governance_state.review_state`
  - `governance_state.blocked`

## 6) Cleanup

```c
yai_sdk_reply_free(&reply);
yai_sdk_client_close(client);
```

## Sample output shape (human)

```text
command=yai.workspace.query code=OK summary=workspace_query_result
workspace=demo binding=3 data_ready=1
governance effect= review= blocked=0
```

Numeric binding values map to `yai_sdk_binding_state_t` in `yai_sdk/models.h`.

Low-level fallback remains available via `yai_sdk_client_call` + `yai_sdk_control_call_t`,
but it is secondary to canonical typed families.
For composition/direct-backing status by family, see `Documentation/WSV84_COMPOSITION_DEBT_DISPOSITION.md`.
