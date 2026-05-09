# Desktop / Long-Lived Client Alignment

## Status

* Delivery: V24
* Status: active client contract
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define Desktop and similar persistent clients as governed long-lived clients.

## Client Role

```text
Desktop is a long-lived app client.
It observes and presents runtime/auth/case/operator/readiness/license/gate
posture in a persistent application context.
It does not own domain truth.
```

## Local UI State Boundary

```text
Window state, view state, local UI cache and workspace affordances are client
state only.
They are not case ownership, auth truth, runtime readiness or memory truth.
```

## Reconnect / Resume Boundary

```text
Reconnect/resume reloads posture.
It does not automatically refresh auth, license lease, runtime gate decisions or
job execution authority.
```

## Ownership Table

| Concern | Owner |
| ------- | ----- |
| auth truth | auth/E/V auth context |
| account_ref | E platform |
| root case | case plane |
| active_case_ref | operator context |
| local UI/window state | Desktop client state only |
| runtime lifecycle | runtime/service plane |
| readiness projection | runtime/readiness plane |
| records/evidence/knowledge | case/runtime planes |
| entitlement_ref | E contract consumed by V |
| machine_authorization_ref | E contract consumed by V |
| license_lease | E contract consumed by V |
| runtime_gate_decision | E/V gate contract |
| session | legacy compatibility only |

## Desktop May Consume

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

## Desktop Must Not Consume

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
| `Desktop session` as domain | `Desktop client connection` |
| `window owns case` | `window displays case_ref` |
| `workspace owns case` | `workspace bound to case_ref` |
| `Desktop logged in` | `auth posture observed` |
| `runtime ready because app opened` | `readiness projection` |
| `Desktop owns memory` | `Desktop displays case-bound knowledge/records` |
| `Desktop owns license` | `Desktop observes license posture` |

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| case-bound jobs | V25 |
| execution lease model | V26 |
| detach/continuation semantics | V27 |
| logout/seal policy | V28 |
| case evidence binding | V29 |
| knowledge binding | V30 |
| machine authorization consumption | V42 |
| license lease consumption | V43 |
| local lease cache/reboot continuity | V44 |
| runtime license check request/response | V46/V47 |
| sealed-by-license behavior | V48 |
