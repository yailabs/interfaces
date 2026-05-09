# Console Client Alignment

## Status

* Delivery: A1
* Status: active client alignment
* Track: A - Console canonicalization / legacy CLI-Loom drain
* Repo branch: `refoundation/phase-01`

## Purpose

Align Console as the canonical terminal client.

## Client Role

```text
YAI Console is the canonical terminal client.
Legacy CLI/Loom surfaces are compatibility names or historical references.
Console observes and presents runtime/auth/case/operator/readiness/license/gate
posture.
Console does not own domain truth.
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
| Console connection/UI state | Console client state |
| session | legacy compatibility only |

## Wording Rules

| Avoid | Use |
| ----- | --- |
| `CLI and Loom clients` | `Console` or `terminal client` |
| `CLI/Loom` | `Console` or `legacy CLI/Loom surfaces` |
| `Loom terminal client` | `YAI Console` |
| `CLI runtime client` | `Console-compatible command surface` |
| `session attached` | `client connected` / `runtime posture observed` |
| `client logged in` | `auth posture: authenticated/local-dev/unauthenticated` |

## Runtime And Readiness Boundary

Console may render runtime transport and readiness posture from SDK/API status
projections. It must not fabricate `operationalReadiness`, `sealReason`, runtime
lifecycle state, or runtime gate outcomes from local UI connection state.

Legacy CLI/Loom names remain acceptable only for compatibility shims,
historical wave reports, tombstones, and code symbols intentionally deferred by
A1.
