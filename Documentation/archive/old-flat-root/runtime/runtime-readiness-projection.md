# Runtime Readiness Projection

## Status

* Delivery: V15
* Status: active local projection model
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Purpose

Define canonical runtime readiness projection fields.

## Projection Fields

| Field | Meaning |
| ----- | ------- |
| `lifecycle` | runtime service lifecycle posture |
| `health` | runtime health posture |
| `readiness` | runtime readiness posture |
| `operationalReadiness` | whether governed operational actions are allowed |
| `sealReason` | reason operational readiness is sealed or blocked |
| `authPosture` | auth state |
| `casePosture` | root/tree/case boundary state |
| `operatorContextPosture` | active-case/operator context state |
| `clientPosture` | client invocation posture |
| `sessionPosture` | legacy ignored/compat state |

## Core Distinctions

```text
runtime running != runtime authorized
runtime healthy != operational actions allowed
client attached != login
auth login != shell
case selected != session
```

## Local Projection Rules

| State | operationalReadiness | sealReason |
| ----- | -------------------- | ---------- |
| no auth | sealed | `missing_auth_context` |
| auth but no root | sealed | `missing_root_case` |
| auth/root but no tree | sealed | `missing_case_tree` |
| auth/root/tree but no active case | blocked | `missing_operator_context` |
| auth/root/tree/active case | ready | `none` |
| runtime transport unavailable | separate lifecycle/transport issue | `runtime_transport_unavailable` only for transport visibility |

## Boundary Rules

```text
readiness projection != service lifecycle control
readiness projection != production entitlement
readiness projection != session status
runtime transport unavailable != auth failure
local operational readiness can be projected from local auth/case/operator state
```

## Local CLI Note

V15 keeps lifecycle, health, and readiness as runtime transport projections when
reachable. `operationalReadiness`, `sealReason`, `authPosture`,
`casePosture`, `operatorContextPosture`, `clientPosture`, and
`sessionPosture` are projected locally from:

* local auth marker
* local root case marker
* local case tree manifest
* local operator context marker
* current CLI client posture

This means `runtime_transport_unavailable` does not erase local auth/case
posture. It is reported separately from operational authorization.

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| allowed/blocked surface matrix | V16 |
| service lifecycle boundary | V17 |
| dev wrapper boundary | V18 |
| runtime control plan | V19 |
| SDK runtime surface alignment | V20 |
| CLI SDK-first wiring | V21 |
