# V20 - SDK Runtime Surface Alignment

## Status

* Delivery: V20
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: SDK runtime surface alignment + documentation/report
* Previous delivery: V19 - Runtime Control Plan
* Next delivery: V21 - CLI SDK-first Wiring

## Purpose

V20 aligns SDK runtime surfaces with lifecycle/health/readiness/controlPlan
semantics.

## Scope

Record:

* TypeScript runtime surface inspected/aligned;
* Rust runtime/system surface inspected/aligned;
* controlPlan semantics verified;
* unavailable transport behavior verified or documented;
* no fake start/stop/restart claims introduced;
* no runtime control execution implemented;
* no CLI SDK-first refactor done.

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `Documentation/sdk/sdk-runtime-surface-alignment.md` | create | SDK runtime alignment model |
| api | `Documentation/waves/v20-sdk-runtime-surface-alignment.md` | create | delivery report |
| sdk | `README.md` | update | runtime/controlPlan boundary clarification |
| sdk | `packages/typescript/README.md` | update | TypeScript runtime/controlPlan guidance |
| sdk | `packages/typescript/src/surfaces/system.ts` | update | canonical runtime field coverage |
| sdk | `packages/typescript/src/surfaces/runtime.ts` | update | typed controlPlan projection |
| sdk | `packages/typescript/src/index.ts` | update | export runtime control plan types |
| sdk | `packages/rust/README.md` | update | Rust runtime/controlPlan guidance |
| sdk | `packages/rust/src/operations.rs` | update | compat control-plan operation constant |
| sdk | `packages/rust/src/surfaces/system.rs` | update | canonical runtime field coverage |
| sdk | `packages/rust/src/surfaces/runtime.rs` | update | compat control-plan inspect surface |

## TypeScript SDK Alignment

| Surface | Status | Notes |
| ------- | ------ | ----- |
| runtime status | aligned | canonical runtime posture fields are now typed on `RuntimeServiceStatus` |
| controlPlan | aligned | `runtime.controlPlan()` remains plan/projection only |
| unavailable transport | aligned | unconfigured transport stays `unavailable` with `execution_claim: false` |
| start/stop/restart execution claims | none | no execution path added |

## Rust SDK Alignment

| Surface | Status | Notes |
| ------- | ------ | ----- |
| runtime/system status | aligned | canonical posture fields and optional `control_plan` are typed on `RuntimeServiceStatus` |
| controlPlan | aligned | compatibility runtime alias now exposes `control_plan_inspect()` |
| unavailable transport | aligned | not-configured transport stays `TransportNotConfigured`; no fake ready path |
| start/stop/restart execution claims | none | no execution path added |

## Runtime Field Coverage

| Field | TypeScript SDK | Rust SDK | Notes |
| ----- | -------------- | -------- | ----- |
| `lifecycle` | yes | yes | TS keeps `lifecycleState` plus canonical `lifecycle`; Rust accepts both |
| `health` | yes | yes | typed in both SDKs |
| `readiness` | yes | yes | typed in both SDKs |
| `operationalReadiness` | yes | yes | typed in both SDKs |
| `sealReason` | yes | yes | typed in both SDKs |
| `authPosture` | yes | yes | TS canonical field added; Rust optional field added |
| `casePosture` | yes | yes | TS canonical field added; Rust optional field added |
| `operatorContextPosture` | yes | yes | typed in both SDKs |
| `clientPosture` | yes | yes | TS canonical field added; Rust optional field added |
| `sessionPosture` | yes | yes | TS canonical field added; Rust optional field added |
| `controlPlan` | yes | yes | TS typed surface present; Rust typed field plus compat inspect method |

## controlPlan Rules

```text
controlPlan is plan/projection, not execution.
SDK controlPlan must not claim start/stop/restart succeeded unless actual
transport execution and validation prove it.
```

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f Documentation/sdk/sdk-runtime-surface-alignment.md` | pass | new SDK doc |
| api | `test -f Documentation/waves/v20-sdk-runtime-surface-alignment.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | available and clean |
| sdk/typescript | `npm run typecheck` | pass | run in `packages/typescript` |
| sdk/typescript | `npm run build` | pass | run in `packages/typescript` |
| sdk/typescript | existing tests | not run | no obvious automated TS test command beyond typecheck/build |
| sdk/rust | `cargo check` | pass | run in `packages/rust` |
| sdk/rust | `cargo test` | pass | run in `packages/rust` |
| sdk/c | validation | not run | untouched |
| cli | validation | not run | untouched |
| loom | validation | not run | untouched |
| yai | validation | not run | untouched |

## Findings

### Finding A - TypeScript Runtime Surface Aligned

Record:
TypeScript runtime status/controlPlan surfaces are aligned and typed with
canonical posture fields.

### Finding B - Rust Runtime Surface Aligned

Record:
Rust runtime/system surfaces are aligned with canonical posture fields, and the
runtime compatibility alias now exposes plan-only control inspection.

### Finding C - controlPlan Remains Plan

Record:
SDK `controlPlan` does not claim execution.

### Finding D - Unavailable Transport Remains Truthful

Record:
SDK unavailable transport behavior does not fake ready/healthy/running.

### Finding E - V21 Can Wire CLI SDK-First

Record:
With SDK runtime semantics aligned, V21 can move CLI toward SDK-first wiring
without inheriting fake runtime claims.
