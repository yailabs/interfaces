# Runtime Control Plan

## Status

* Delivery: V19
* Status: active model
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Purpose

Define `controlPlan` as a plan/projection, not execution.

## Definition

`controlPlan` is a declarative projection of possible runtime control actions
and their requirements/status.

It is not proof that any control action was executed.

## Conceptual Shape

```json
{
  "controlPlan": {
    "serviceManager": "unavailable | launchd | systemd | manual | unknown",
    "start": {
      "available": false,
      "reason": "service_manager_unavailable",
      "executionClaim": false
    },
    "stop": {
      "available": false,
      "reason": "service_manager_unavailable",
      "executionClaim": false
    },
    "restart": {
      "available": false,
      "reason": "service_manager_unavailable",
      "executionClaim": false
    }
  }
}
```

Allowed values:

```text
serviceManager:
  unavailable
  launchd
  systemd
  manual
  unknown

control action availability:
  available
  unavailable
  planned
  unsupported

control reasons:
  service_manager_unavailable
  dev_wrapper_only
  not_implemented
  unsupported_platform
  insufficient_permission
  unknown
```

## Boundary Rules

```text
controlPlan != control execution
controlPlan != service lifecycle
controlPlan != operationalReadiness
controlPlan != dev-wrapper
controlPlan != service manager
controlPlan != auth
controlPlan != case
controlPlan != operator context
controlPlan != session
controlPlan must not claim start/stop/restart occurred unless executed and validated
dev-wrapper commands may inform controlPlan but do not execute canonical control
```

## No Fake Execution Claims

```text
No status/help/report output may claim runtime start/stop/restart executed unless
the control path actually executed and validation recorded the result.
```

## Relationship To Dev Wrapper

```text
Makefile and service bootstrap commands are dev-wrapper/ops surfaces. They may
inform local setup but they are not canonical runtime control execution.
```

## Local CLI Note

V19 does not require the local CLI to project `controlPlan` immediately.

If `yai runtime status` does not yet expose `controlPlan`, that absence must be
recorded truthfully rather than replaced with fake start/stop/restart claims.

If a future CLI status surface exposes `controlPlan`, it must keep these facts
separate:

* service-manager detection is not control execution;
* lifecycle inspection is not operational authorization;
* a control plan may describe `start`, `stop`, or `restart` availability
  without claiming the action happened.

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| SDK runtime surface alignment | V20 |
| CLI SDK-first wiring | V21 |
| service lifecycle operations | later service manager wave |
| detach semantics | V26 |
| logout policy | V27 |
