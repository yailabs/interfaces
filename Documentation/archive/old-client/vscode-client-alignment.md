# VS Code Client Alignment

## Status

* Delivery: V23
* Status: active client alignment
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Align VS Code as a governed editor client.

## Client Role

```text
VS Code is a long-lived editor client.
It observes and presents runtime/auth/case/operator/readiness/license/gate
posture in editor context.
It does not own domain truth.
```

## Editor Boundary

```text
Editor workspace/folder/window context is not case ownership.
VS Code may bind an editor context to a case, but the case remains owned by the
case plane and current selection remains operator_context.active_case_ref.
```

## Ownership Table

| Concern | Owner |
| ------- | ----- |
| auth truth | auth/E/V auth context |
| account_ref | E platform |
| root case | case plane |
| active_case_ref | operator context |
| workspace/editor context | VS Code client state |
| runtime lifecycle | runtime/service plane |
| readiness projection | runtime/readiness plane |
| entitlement_ref | E contract consumed by V |
| machine_authorization_ref | E contract consumed by V |
| license_lease | E contract consumed by V |
| runtime_gate_decision | E/V gate contract |
| session | legacy compatibility only |

## VS Code May Consume

```text
account_ref
principal_ref
auth_context
entitlement_ref
machine_authorization_ref
license_lease
runtime_gate_decision
```

when available through safe contracts.

## VS Code Must Not Consume

```text
pricing
billing provider object
Supabase user object
account profile
raw provider identity
full commercial plan objects
```

## Wording Rules

| Avoid | Use |
| ----- | --- |
| `VS Code session` as domain | `VS Code client connection` |
| `workspace owns case` | `workspace bound to case_ref` |
| `editor selected case` | `operator_context.active_case_ref` |
| `extension logged in` | `auth posture observed` |
| `runtime ready because extension connected` | `readiness projection` |
| `VS Code owns entitlement/license` | `VS Code observes gate/license posture` |

## Workspace Refs

VS Code may later carry:

```text
workspace_ref
editor_window_ref
project_folder_ref
operator_context_ref
```

These refs are editor/client posture only. They must not replace:

```text
case_ref
root_case_ref
operator_context.active_case_ref
auth_context
```

## E Gate Boundary

VS Code may display entitlement/license/machine authorization posture once E
contracts provide refs, leases and gate decisions.

VS Code must consume refs and runtime_gate_decision only.

VS Code must not consume:

```text
pricing
billing provider objects
Supabase user objects
account profiles
raw provider identities
commercial plan objects
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| desktop/long-lived client model | V24 |
| case-bound jobs | V25 |
| machine authorization consumption | V42 |
| license lease consumption | V43 |
| local lease cache/reboot continuity | V44 |
| runtime license check request/response | V46/V47 |
| sealed-by-license behavior | V48 |
| SDK auth/case clients | V58/V59 |
| entitlement/license clients | V60 |
