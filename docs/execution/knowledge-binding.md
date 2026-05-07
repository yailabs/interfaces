# Knowledge Binding

## Status

* Delivery: V30
* Status: active execution/knowledge contract
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`

## Purpose

Define knowledge and materialized memory as case-bound governed state.

## Canonical Invariant

```text
knowledge.case_ref is required.
```

Knowledge is case-native governed state. It may be written manually, derived
from evidence or records, materialized from job/provider outputs, or preserved
as working memory for a governed case, but the ownership boundary remains the
case.

## Knowledge Is Not Owned By

Knowledge must not be treated as owned by:

```text
session
client
shell
terminal
Loom
VS Code
Desktop window
workspace
runtime process
provider response alone
model response alone
job alone
evidence alone
license_lease
auth_context
```

## Shape

The canonical knowledge shape may include:

```text
knowledge_ref
case_ref
knowledge_kind
title
summary optional
body_ref optional
created_at
updated_at optional
created_by_principal_ref optional
created_from_client_ref optional
source_evidence_refs optional
source_record_refs optional
source_job_refs optional
source_provider_call_refs optional
source_artifact_refs optional
lineage_refs optional
content_digest optional
retention_policy_ref optional
visibility
recall_policy
write_policy
derivation_status
```

Field role notes:

```text
source_evidence_refs are optional derivation inputs only.
source_record_refs are optional durable record inputs only.
source_job_refs are optional execution provenance only.
source_provider_call_refs are optional source provenance only.
source_artifact_refs and lineage_refs provide traceability, not ownership replacement.
recall_policy and write_policy constrain governed access posture without implementing retrieval or storage.
```

## Knowledge Kinds

| Kind | Meaning |
| ---- | ------- |
| `manual_note` | operator-authored knowledge note |
| `summary` | case summary or synthesized overview |
| `decision_note` | knowledge note about a decision or conclusion |
| `case_memory` | durable case memory item |
| `derived_fact` | derived but governed fact |
| `working_state` | active governed working state for a case |
| `research_note` | research or investigation note |
| `code_context` | implementation or code-context knowledge bound to the case |
| `runbook` | case-bound operational or remediation runbook |
| `artifact_index` | index or catalog of case artifacts |
| `evidence_summary` | knowledge distilled from evidence sets |
| `system_observation` | system-produced observation materialized as knowledge |

## Visibility

| Visibility | Meaning |
| ---------- | ------- |
| `private` | visible only to the local or narrow owning posture |
| `case_visible` | visible to the governed case surface |
| `team_visible` | visible to the authorized team surface |
| `admin_visible` | visible to administrative or governance operators |
| `system_internal` | system-internal knowledge surface only |

## Recall Policy

| Recall policy | Meaning |
| ------------- | ------- |
| `not_recallable` | never eligible for governed recall surfaces |
| `case_recallable` | recallable within the case boundary |
| `active_case_recallable` | recallable only when the case is actively selected |
| `authorized_context_recallable` | recallable only through authorized context posture |
| `admin_only` | recallable only for administrative or governance posture |
| `unknown` | recall posture is not yet resolved |

## Write Policy

| Write policy | Meaning |
| ------------ | ------- |
| `append_only` | new material may append without rewriting history |
| `mutable_with_lineage` | mutation is allowed only with lineage preserved |
| `sealed_writes` | existing knowledge remains while writes are sealed |
| `system_only` | write surface is reserved to system/governed automation |
| `explicit_approval_required` | writes require explicit approval posture |
| `unknown` | write posture is not yet resolved |

## Derivation Status

| Derivation status | Meaning |
| ----------------- | ------- |
| `manual` | authored directly by a person or explicit operator action |
| `derived` | derived from source evidence, records, jobs, or outputs |
| `materialized` | materialized into a governed knowledge form |
| `stale` | knowledge exists but freshness is degraded |
| `superseded` | knowledge has been replaced by a later governed item |
| `retracted` | knowledge remains recorded but is no longer valid |
| `unknown` | derivation state is not yet known |

## Ownership And Lineage

```text
Knowledge belongs to case_ref.
Knowledge may reference evidence, records, jobs, provider calls, artifacts, and lineage.
Those refs provide derivation and provenance, not ownership replacement.
```

This means a provider output, model response, job result, or evidence set may
contribute knowledge, but none of those surfaces own the knowledge by
themselves.

## Detach / Logout / Seal Rules

```text
detach does not delete knowledge
logout does not delete knowledge by default
runtime seal does not delete knowledge by default
license lease expiry does not delete knowledge by default
knowledge writes may be sealed while knowledge reads remain governed by policy
recall must not bypass auth/case/gate policy
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| provider authority binding | V31 |
| agent authority binding | V32 |
| flow binding | V33 |
| analytics binding | V34 |
| runtime gate registry | V35 |
| SDK case clients | V59 |
| entitlement/license clients | V60 |
