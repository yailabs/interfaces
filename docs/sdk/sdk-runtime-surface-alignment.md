# SDK Runtime Surface Alignment

## Status

* Delivery: V20
* Status: active alignment model
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Purpose

Align SDK runtime surfaces with canonical runtime readiness and `controlPlan`
semantics.

## Required Runtime Fields

| Field | Meaning |
| ----- | ------- |
| `lifecycle` | runtime service lifecycle posture |
| `health` | runtime health posture |
| `readiness` | runtime readiness posture |
| `operationalReadiness` | governed operation posture |
| `sealReason` | reason operational readiness is sealed/blocked |
| `authPosture` | auth posture |
| `casePosture` | case/root/tree posture |
| `operatorContextPosture` | operator/active case posture |
| `clientPosture` | client invocation posture |
| `sessionPosture` | legacy ignored/compat posture |
| `controlPlan` | possible control actions; not execution |

## SDK Rules

```text
SDK runtime status must not fake ready.
SDK controlPlan must not fake start/stop/restart execution.
SDK transport unavailable must remain unavailable/error.
SDK clients are transport/library clients, not domain owners.
Session is not readiness or authorization source.
```

## Surface Alignment

| SDK | Runtime status | controlPlan | Notes |
| --- | -------------- | ----------- | ----- |
| TypeScript | aligned | aligned | canonical fields and plan-only control surface are typed |
| Rust | aligned | partial | canonical fields are typed; compat control-plan method is present on runtime alias |
| C | not checked | not checked | V20 scope stayed on TypeScript and Rust |
| Python | not present | not present | no V20 runtime/controlPlan surface work |

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| CLI SDK-first wiring | V21 |
| Loom alignment | V22 |
| VS Code alignment | V23 |
| API operator context surfaces | V37 |
| SDK auth clients | V38 |
| SDK case clients | V39 |
