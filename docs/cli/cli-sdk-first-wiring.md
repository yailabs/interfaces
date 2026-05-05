# CLI SDK-first Wiring

## Status

* Delivery: V21
* Status: active local alignment model
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Purpose

Make CLI a pure client of SDK/API/runtime surfaces.

## Rule

```text
CLI is a client.
CLI must not own runtime lifecycle, readiness, controlPlan execution, auth,
case tree, active case, or session.
```

## Runtime Status

After V21, `yai runtime status` consumes the Rust SDK canonical `system.status`
surface directly for runtime lifecycle, health, readiness, and transport truth.

The CLI command name remains `runtime status`, but the runtime-facing truth comes
from SDK/API transport semantics rather than a CLI-owned runtime assumption.

## Local Projection

```text
Local auth/case/operator readiness projection may be composed by the CLI from
local state, but runtime lifecycle/health/readiness must remain SDK/API/transport
truth.
```

## controlPlan

```text
controlPlan is plan/projection only.
CLI must not claim runtime control execution unless SDK/API transport proves it.
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| Loom alignment | V22 |
| VS Code alignment | V23 |
| case-bound jobs | V24 |
| API operator context surfaces | V37 |
| SDK auth clients | V38 |
| SDK case clients | V39 |
