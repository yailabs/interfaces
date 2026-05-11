# Legacy CLI Surface Candidates

## Status

* Delivery: V21.4
* Source: quarantined `cli/source/`
* Target: SDK surface candidate preservation

## Purpose

Record SDK-worthy surface candidates extracted from legacy CLI C source.

## SDK Ownership Rule

```text
SDK owns typed clients and request/response surfaces.
SDK does not own runtime/domain execution.
```

## Candidate Surfaces

| Candidate | Legacy source | Proposed SDK family | Notes |
| --------- | ------------- | ------------------- | ----- |
| runtime posture status | `source/cmd/runtime/status.c` | `client.system().status()` and compatibility `client.runtime().status_inspect()` | Preserve status/readiness/control-plan typing; do not preserve legacy runtime-control wrappers |
| case runtime/watch/facts summaries | `source/cmd/case/surface.c` | future typed `client.case().runtimeInspect()`, `watchSnapshot()`, `facts()` | Legacy case surface suggests case-bound read models and summary envelopes |
| provider family | `source/cmd/provider/*.c` | `client.providers()` plus future `status/current/select/connect/disconnect/probe/models/doctor` typed methods | Keep operation grouping and request naming, not CLI implementation |
| model capability selection | `source/cmd/models/surface.c`, `source/cmd/provider/models.c` | `client.models()` plus provider-scoped model selection types | Useful for typed request/response models around provider/model posture |
| agent invocation | `source/cmd/agent/root.c` | future `client.agent()` / `client.agents()` run and trace surfaces | Preserve request fields such as `scope`, `actor`, `agent`, `provider`, `input` |
| workflow snapshot and pending | `source/cmd/flow/surface.c`, `source/cmd/flow/flow_dispatch.c` | `client.workflow()` with future snapshot/explain/reconcile/blocker methods | Existing workflow list/show/watch methods likely grow here rather than through CLI-owned logic |
| governance posture and gate explain | `source/cmd/govern/*.c`, `source/cmd/flow/surface.c` | `client.governance()` and `client.control()` | Read models for review, authority, allowed/blocked reasons, and gate posture belong in typed SDK envelopes |
| knowledge/query/lineage/topology | `source/cmd/knowledge/*.c` | `client.knowledge()` and future typed state/read-model helpers | Preserve query family naming and result-shape hints from legacy records/read models |
| records/evidence/log tail | `source/cmd/logs/root.c`, `source/cmd/knowledge/records.c` | `client.records()` / `client.state()` future tail/query helpers | `logs latest` is really a typed canonical-record tail surface |
| analytics summary/query/show | `source/cmd/analytics/query.c` | `client.analytics()` future summary/show helpers | Derived surface only; SDK must not let analytics become primary truth |
| session summary/welcome | `source/cmd/session/status.c`, `source/cmd/session/session_shell_surface.c` | compatibility/deprecation only, not a growth family | Session remains legacy compatibility, not a canonical SDK destination |
| substrate entry bootstrap | `source/cmd/session/substrate_entry_cli.c` | remove without SDK canon | This is a legacy entry parser, not a typed SDK client family |
| shared passthrough/path helpers | `source/shared/core.c` | remove without SDK canon | CLI glue does not define transport contracts for SDK ownership |
| output stubs | `source/out/*.c` | remove without SDK canon | Stub emitters do not provide meaningful typed SDK surface value |

## Non-Implementation Note

```text
This document does not implement SDK clients.
It preserves extracted surface candidates before legacy source deletion.
```
