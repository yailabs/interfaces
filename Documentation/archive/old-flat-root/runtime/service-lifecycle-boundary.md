# Service Lifecycle Boundary

## Status

* Delivery: V17
* Status: active local boundary model
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Purpose

Separate runtime service lifecycle from readiness and operational authorization.

## Lifecycle States

| State | Meaning |
| ----- | ------- |
| `running` | runtime service process is alive |
| `stopped` | runtime service process is not running |
| `degraded` | runtime service is alive but impaired |
| `unavailable` | lifecycle cannot be inspected or transport unavailable |
| `unknown` | lifecycle source not available |

## Separate Readiness States

| Field | Meaning |
| ----- | ------- |
| `operationalReadiness` | whether governed operational mutation is allowed |
| `sealReason` | why operation is sealed or blocked |
| `authPosture` | auth posture |
| `casePosture` | case/root/tree posture |
| `operatorContextPosture` | operator/active case posture |
| `clientPosture` | client invocation posture |
| `sessionPosture` | legacy ignored/compat posture |

## Boundary Rules

```text
service lifecycle != operational readiness
service lifecycle != auth posture
service lifecycle != case posture
service lifecycle != operator context
service lifecycle != session status
running runtime may still be sealed
healthy runtime may still block operational mutation
stopped runtime does not mean logged out
logout does not stop runtime
shell detach does not stop runtime
client detach does not stop runtime
runtime_transport_unavailable is transport/lifecycle posture, not auth failure
```

## Examples

| Scenario | Lifecycle | Operational readiness |
| -------- | --------- | --------------------- |
| runtime running but missing auth | running | sealed |
| runtime healthy but no active case | running or degraded | blocked |
| runtime transport unavailable but local auth/case ready | unavailable | ready locally |
| runtime stopped after logout | stopped | independent; logout does not stop runtime |
| shell detach | unchanged | unchanged |

## Local CLI Note

V17 keeps runtime lifecycle, health, and readiness as transport-facing
inspection values. The local CLI may still project `operationalReadiness`,
`sealReason`, `authPosture`, `casePosture`, `operatorContextPosture`,
`clientPosture`, and `sessionPosture` even when lifecycle is `unavailable`.

This means:

* a runtime can be uninspectable over transport while local operational posture
  is ready;
* a runtime can be running or healthy while governed mutation remains sealed or
  blocked;
* shell/client/session posture must not be treated as lifecycle control.

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| dev wrapper boundary | V18 |
| runtime control plan | V19 |
| SDK runtime surface alignment | V20 |
| CLI SDK-first wiring | V21 |
| detach semantics | V26 |
| logout policy | V27 |
