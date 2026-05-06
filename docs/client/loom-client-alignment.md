# Loom Client Alignment

## Status

* Delivery: V22
* Status: active client alignment
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Align Loom as a governed long-lived client.

## Client Role

```text
Loom is a long-lived client/TUI surface.
It observes and presents runtime/auth/case/operator/readiness posture.
It does not own domain truth.
```

## Ownership Table

| Concern | Owner |
| ------- | ----- |
| auth truth | auth/E/V auth context |
| account_ref | E platform |
| root case | case plane |
| active_case_ref | operator context |
| runtime lifecycle | runtime/service plane |
| readiness projection | runtime/readiness plane |
| entitlement/license/machine refs | E contracts consumed by V |
| Loom connection state | Loom client state |
| session | legacy compatibility only |

## Loom Must Consume

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

## Loom Must Not Consume

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
| `session attached` | `client connected` / `runtime posture observed` |
| `session selected case` | `operator_context.active_case_ref` |
| `client logged in` | `auth posture: authenticated/local-dev/unauthenticated` |
| `runtime ready because UI connected` | `readiness projection` |
| `Loom owns case` | `Loom observes case posture` |

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| VS Code client alignment | V23 |
| desktop/long-lived client model | V24 |
| machine authorization consumption | V39 |
| license lease consumption | V40 |
| SDK auth/case clients | V48/V49 |
| entitlement/license clients | V50 |
