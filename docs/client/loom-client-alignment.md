# Loom Client Alignment

## Status

* Delivery: V22
* Status: active client alignment
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Align Loom as a governed long-lived client.

## Client Role

```text
Loom is a long-lived client/TUI surface.
It observes and presents runtime/auth/case/operator/readiness/license/gate
posture.
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
| entitlement_ref | E contract consumed by V |
| machine_authorization_ref | E contract consumed by V |
| license_lease | E contract consumed by V |
| runtime_gate_decision | E/V gate contract |
| Loom connection state | Loom client state |
| session | legacy compatibility only |

## Loom May Consume

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
| `Loom owns license` | `Loom observes license posture` |
| `Loom owns entitlement` | `Loom observes entitlement/gate posture` |

## Runtime And Readiness Boundary

Loom may render runtime transport and readiness posture from SDK/API status
projections. It must not fabricate `operationalReadiness`, `sealReason`, runtime
lifecycle state, or runtime gate outcomes from local UI connection state.

## E Gate Boundary

Loom may display entitlement/license/machine authorization posture once E
contracts provide refs, leases and gate decisions.

Loom must consume refs and runtime_gate_decision only.

Loom must not consume:

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
| VS Code client alignment | V23 |
| desktop/long-lived client model | V24 |
| machine authorization consumption | V42 |
| license lease consumption | V43 |
| local lease cache/reboot continuity | V44 |
| runtime license check request/response | V46/V47 |
| sealed-by-license behavior | V48 |
| SDK auth/case clients | V58/V59 |
| entitlement/license clients | V60 |
