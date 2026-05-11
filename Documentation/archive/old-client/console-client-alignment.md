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
Console is a client subject that may produce client connections and client
attachments over time.
Console is not a case.
```

## A4 Protocol Projection

A4 defines the protocol meaning of:

- `client_subject_ref`
- `client_connection_ref`
- `client_attachment_ref`
- `system_call_ref`
- `system_root_context_ref`
- optional `work_case_ref`

For API projection, Console remains `client-subject://console` when the protocol
is later propagated into envelopes. A Console call may have a concrete
`client_connection_ref` and `client_attachment_ref`, but those refs do not make
Console a work case and do not make a session canonical.

A4 is protocol meaning only. API/SDK propagation starts later in A5.

## A5 Call Context Projection

A5 adds call-context projection fields to API envelopes.
A5 does not implement runtime admission/materialization.

The API envelope projection may carry Console as `client-subject://console`,
plus optional `client_connection_ref`, `client_attachment_ref`,
`system_root_context_ref`, `work_case_ref`, and `system_call_ref`.
`system_call_ref` remains optional because runtime-created refs start later.
`work_case_ref` remains optional and separate from client attachment.

Console remains canonical terminal client.
CLI/Loom remain compatibility names.

## Ownership Table

| Concern | Owner |
| ------- | ----- |
| auth truth | auth/E/V auth context |
| account_ref | E platform |
| root case | case plane |
| active_case_ref | operator context |
| client subject identity | future control subject taxonomy |
| client connection posture | runtime connection observation |
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
