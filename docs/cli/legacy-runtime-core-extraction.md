# Legacy Runtime/Core Extraction

## Status

* Delivery: V21.3
* Status: active extraction artifact
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Purpose

Extract useful runtime/core/domain semantics from quarantined `cli/source/`
before deletion.

## Extraction Principle

```text
Do not preserve the legacy C CLI.
Preserve only useful semantics in the correct architectural layer.
```

## Source Areas Reviewed

| Legacy area | What was reviewed | Current reading |
| ----------- | ----------------- | --------------- |
| `source/main.c` | monolithic root dispatch, legacy start/stop/status, case/knowledge/explain/console shims, work/policy/evidence/provider route fields | mixed runtime/core semantics plus large compatibility shell |
| `source/shared` | argv/path/help/passthrough helpers | CLI plumbing, not domain ownership |
| `source/out` | text/json/table/tsv/shell emitters | rendering stubs, not runtime/core semantics |
| `source/cmd/runtime` | runtime status/root adapters and `runtime/auth.c` helper | runtime boundary vocabulary plus legacy auth/session contamination |
| `source/cmd/provider` | provider list/status/connect/probe/models/doctor wrappers | mostly thin boundary/API wrappers |
| `source/cmd/agent` | env seeding, agent subcommand grammar, orchestration dispatch delegation | agent/workflow entry vocabulary with runtime env coupling |
| `source/cmd/flow` | flow root/dispatch plus large `surface.c` orchestration and cognition delta logic | major runtime/core semantic hub |
| `source/cmd/govern` | intake/legal/authority/review/publication wrappers | governance/control vocabulary plus legacy session guard |
| `source/cmd/knowledge` | knowledge root plus very large `records.c` read-model hub | major state/records/lineage/analytics semantic hub |
| `source/cmd/analytics` | analytics query wrapper | thin derived-surface wrapper |
| `source/cmd/logs` | logs latest over `operational_receipt` tails | direct canonical-record read semantic |

## Extracted Concepts

| Concept | Legacy source | Classification | Target owner | Notes |
| ------- | ------------- | -------------- | ------------ | ----- |
| runtime status is a boundary/API concern, not CLI-owned lifecycle control | `source/cmd/runtime/status.c`, `source/cmd/runtime/root.c`, `source/main.c` | `runtime_lifecycle_semantic` | `yai/core` + `api` | Legacy `runtime` family mixes status with banned `start`/`stop` compatibility; preserve only the status/lifecycle distinction |
| runtime layout/env seeding from installed entrypoint path | `source/cmd/agent/root.c`, `source/cmd/flow/root.c`, `source/cmd/flow/flow_dispatch.c` | `runtime_lifecycle_semantic` | `yai/core` | `YAI_ROOTFS`, `YAI_RUN_ROOT`, and `YAI_RUNTIME_ROOT` resolution belongs to runtime layout/runtime activation, not CLI ownership |
| provider posture includes route, lifecycle, probe, and model-selection vocabulary | `source/cmd/provider/*.c`, `source/main.c` | `provider_authority_semantic` | `api` + `sdk` + `yai/core` | Thin CLI wrappers are disposable, but provider status/probe/connect/models vocabulary and provider route fields are canonical candidates |
| agent invocation vocabulary is case/scope/input/provider aware and should remain governed | `source/cmd/agent/root.c`, `source/cmd/flow/flow_dispatch.c`, `source/cmd/flow/surface.c` | `agent_authority_semantic` | `yai/core` + `api` + `sdk` | `--scope`, `--actor`, `--agent`, `--provider`, `--input`, and review-sensitive/flow-sensitive posture are domain semantics, not CLI semantics |
| flow execution is tied to pending items, gates, blockers, review, authority, and operational effects | `source/cmd/flow/root.c`, `source/cmd/flow/flow_dispatch.c`, `source/cmd/flow/surface.c` | `flow_execution_semantic` | `yai/core` + `api` | Legacy flow surface still carries execution, gating, pending, reconciliation, hierarchy, and module semantics that must survive outside CLI |
| governance qualifies and routes; it must not stay as session-gated CLI behavior | `source/cmd/govern/intake_main.c`, `source/cmd/govern/*.c`, `source/main.c` | `governance_control_semantic` | `yai/core` + `api` | Authority/review/legal/publication/intake belong to governance/control planes; the legacy session guard is a contamination signal, not a pattern to preserve |
| knowledge is a state/records/lineage/read-model plane, not a CLI command family owner | `source/cmd/knowledge/root.c`, `source/cmd/knowledge/records.c`, `source/main.c` | `knowledge_memory_semantic` | `yai/core` + `api` | `records`, `lineage`, `topology`, `context`, `memory`, `retrieval`, `inference`, `query`, and `summarize` imply canonical data-plane responsibilities |
| analytics is derived understanding, not primary truth | `source/cmd/analytics/query.c`, `source/cmd/knowledge/records.c` | `analytics_semantic` | `yai/core` + `api` + `sdk` | The wrapper is thin, but the derived analytics families in `records.c` show useful read-model boundaries |
| logs latest should tail canonical `operational_receipt` records, not invent a separate log truth | `source/cmd/logs/root.c`, `source/cmd/knowledge/records.c` | `logs_records_evidence_semantic` | `yai/core` + `api` + `sdk` | Useful preserved semantic: receipts live in canonical records and are readable through tail/query surfaces |
| current-work, evidence, authority, review, flow, and provider route refs are linked state/lineage vocabulary | `source/main.c`, `source/cmd/flow/surface.c`, `source/cmd/knowledge/records.c` | `state_lineage_recall_semantic` | `yai/core` | `current_work_id`, `case_current_work_id`, `linked_evidence_ref`, `active_authority_ref`, `active_flow_id`, `provider_lifecycle_state`, and lineage/promotion fields are runtime/state semantics |
| legacy session guards and session-rooted admission are contamination to remove, not domain truth to keep | `source/main.c`, `source/cmd/govern/intake_main.c`, `source/cmd/runtime/auth.c` | `session_legacy_semantic` | `cli` | Preserve only the negative doctrine: session must not remain the admission authority for runtime/core behavior |
| hard-cutover aliases reveal non-canonical families that should not be revived | `source/main.c`, `source/cmd/flow/root.c`, `source/cmd/agent/root.c` | `case_boundary_semantic` | `cli` + `api` | `providers`, `execution`, `orchestration`, `state`, `graph`, `cognition`, and plural `agents` are compatibility residue, not canonical ownership roots |

## Extraction Table

| Legacy area | Extracted semantics | Target owner | Extraction artifact | Deletion readiness |
| ----------- | ------------------- | ------------ | ------------------- | ------------------ |
| `source/main.c` | legacy lifecycle control grammar, current-work/evidence/authority/provider-route state, cognition aliases, case/knowledge/govern routing | `yai/core` + `api` | this doc + `Documentation/legacy-cli-runtime-core-extraction.md` | blocked |
| `source/shared` | argv/path/passthrough helper patterns only; no runtime/core ownership | `cli` | this doc records `remove_without_extraction` posture | partial |
| `source/out` | output/rendering stubs only; no runtime/core ownership | `cli` | this doc records `remove_without_extraction` posture | partial |
| `source/cmd/runtime` | runtime status boundary vocabulary; lifecycle/control separation; legacy auth/session contamination | `yai/core` + `api` | this doc | partial |
| `source/cmd/provider` | provider status/probe/connect/models vocabulary and provider posture hooks | `api` + `sdk` + `yai/core` | this doc, with V21.4 follow-up for typed surfaces | partial |
| `source/cmd/agent` | scope/actor/agent/provider/input vocabulary, agent run/context entry grammar, runtime env seeding | `yai/core` + `api` + `sdk` | this doc | partial |
| `source/cmd/flow` | orchestration/flow/pending/gate/review/authority/graph semantics, cognition delta vocabulary | `yai/core` + `api` | this doc + `Documentation/legacy-cli-runtime-core-extraction.md` | blocked |
| `source/cmd/govern` | intake/legal/authority/review/publication semantics and legacy session-guard contamination | `yai/core` + `api` | this doc | partial |
| `source/cmd/knowledge` | records/query/lineage/topology/context/memory/retrieval/inference plus DuckDB/read-model families | `yai/core` + `api` | this doc + `Documentation/legacy-cli-runtime-core-extraction.md` | blocked |
| `source/cmd/analytics` | derived analytics query/status vocabulary | `api` + `sdk` + `yai/core` | this doc | partial |
| `source/cmd/logs` | `operational_receipt` tail/query semantics over canonical records | `yai/core` + `api` + `sdk` | this doc | partial |

## Deletion Readiness

| Legacy area | Deletion readiness | Blocking reason |
| ----------- | ------------------ | --------------- |
| `source/main.c` | blocked | monolithic mix of lifecycle, session gating, case/knowledge/govern/flow/agent routing, and work/evidence/provider state still needs split preservation |
| `source/shared` | partial | mostly disposable CLI plumbing, but broader build references still exist in `yai/Makefile` |
| `source/out` | partial | no runtime/core semantic value, but broader build references still exist in `yai/Makefile` |
| `source/cmd/runtime` | partial | status/lifecycle doctrine is now preserved, but API/SDK surface cleanup and legacy auth helper removal remain |
| `source/cmd/provider` | partial | thin wrappers are disposable, but typed provider surfaces and posture contracts still need V21.4 extraction |
| `source/cmd/agent` | partial | important agent/scope/provider grammar preserved, but typed surfaces and substrate boundaries still need V21.4 |
| `source/cmd/flow` | blocked | large surface still carries core orchestration, pending/gate/posture, cognition delta, and review/authority semantics |
| `source/cmd/govern` | partial | governance semantics are identified, but session-guard contamination and API/SDK surface cleanup remain |
| `source/cmd/knowledge` | blocked | major read-model/catalog/state/lineage/analytics semantics still live in `records.c` and need staged preservation |
| `source/cmd/analytics` | partial | wrapper is thin, but derived analytics families still depend on knowledge/state extraction context |
| `source/cmd/logs` | partial | receipt-tail semantic preserved, but API/SDK query surface extraction and build cleanup remain |

## Follow-up Waves

| Wave | Purpose |
| ---- | ------- |
| V21.4 | Extract API/SDK surface candidates |
| V21.5 | Delete migrated/obsolete source subtrees |
| V21.6 | Add absence guardrail |
