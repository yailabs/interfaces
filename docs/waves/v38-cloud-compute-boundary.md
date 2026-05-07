# V38 — Cloud Compute Boundary

## Status

* Delivery: V38
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: cloud compute boundary docs + contract schema/fixtures + validation/conformance report
* Previous delivery: V37 — Local Model / Provider Access Boundary
* Next delivery: V39 — Local Machine Identity Store

## Purpose

V38 defines cloud compute as optional governed capacity, distinct from local
runtime execution.

## Scope

* compute target vocabulary documented;
* compute mode vocabulary documented;
* decision statuses documented;
* blocked reasons documented;
* infrastructure boundary documented;
* local/cloud boundary documented;
* E/V boundary documented;
* billing/metering/capacity boundary documented;
* JSON schema created;
* fixtures created;
* conformance script created or deviation recorded;
* no cloud compute implementation;
* no remote job handoff implementation;
* no queue/scheduler implementation;
* no cloud provider integration;
* no credentials/secrets implementation;
* CLI source absence verified.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `docs/execution/cloud-compute-boundary.md` | create | cloud compute boundary |
| api | `docs/waves/v38-cloud-compute-boundary.md` | create | delivery report |
| api | `schemas/cloud-compute-boundary.v1.schema.json` | create | cloud compute boundary schema |
| api | `fixtures/cloud-compute-boundary/*.json` | create | representative cloud compute fixtures |
| api | `conformance/check_cloud_compute_boundary.py` | create | dependency-free fixture/schema check |
| yai | `Documentation/execution/cloud-compute-boundary.md` | create | runtime/core cloud compute boundary record |

## Contract Artifacts

| Artifact | Status | Notes |
| -------- | ------ | ----- |
| cloud compute boundary doc | created | API execution doctrine added. |
| JSON schema | created | Dependency-free contract artifact. |
| fixtures | created | Representative local, blocked, queue, dedicated, and deferred examples. |
| conformance script | created | Dependency-free fixture/schema validation. |
| yai runtime/core doc | created | Runtime/core boundary recorded. |

## Cloud Compute Boundary Model

| Concern | V38 policy |
| ------- | ---------- |
| `compute_target` | required |
| `compute_mode` | required |
| `case_ref` | required for case-scoped cloud work |
| local runtime | not cloud compute |
| hosted model | not full cloud compute by itself |
| cloud compute | optional governed capacity |
| priority queue | safe posture ref only |
| dedicated capacity | safe posture ref only |
| billing/metering | not implemented / not owned |
| cloud provider secrets | forbidden from V/core |
| infrastructure provider account | forbidden from V/core |

## Fixture Summary

| Fixture | Scenario | Expected invariant |
| ------- | -------- | ------------------ |
| `local-runtime-not-cloud.json` | local runtime work | cloud compute not implied |
| `cloud-compute-blocked-missing-entitlement.json` | missing entitlement | blocked reason present |
| `cloud-compute-blocked-capacity.json` | no cloud capacity | blocked reason present |
| `priority-queue-required.json` | priority queue posture | queue ref only, no implementation |
| `dedicated-capacity-not-implemented.json` | dedicated capacity future | not implemented decision |
| `managed-remote-job-deferred.json` | remote job handoff future | deferred/no implementation |

## CLI Source Absence Check

Record:

```text
cli/source/ exists: no
full absence guardrail active: yes
Rust src/ is the only CLI implementation: yes
```

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f docs/execution/cloud-compute-boundary.md` | pass | new policy doc |
| api | `test -f docs/waves/v38-cloud-compute-boundary.md` | pass | new report |
| api | `test -f schemas/cloud-compute-boundary.v1.schema.json` | pass | schema |
| api | `test -f conformance/check_cloud_compute_boundary.py` | pass | conformance |
| api | `python3 conformance/check_cloud_compute_boundary.py` | pass | V38 conformance |
| api | `python3 conformance/check_local_model_provider_access_boundary.py` | pass | V37 regression |
| api | `python3 conformance/check_case_job_flow_limit_boundary.py` | pass | V36 regression |
| api | `python3 conformance/check_runtime_gate_registry.py` | pass | V35 regression |
| api | `python3 conformance/check_analytics_binding.py` | pass | V34 regression |
| api | `python3 conformance/check_flow_binding.py` | pass | V33 regression |
| api | `python3 conformance/check_agent_authority_binding.py` | pass | V32 regression |
| api | `python3 conformance/check_provider_authority_binding.py` | pass | V31 regression |
| api | `python3 conformance/check_knowledge_binding.py` | pass | V30 regression |
| api | `python3 conformance/check_case_evidence_binding.py` | pass | V29 regression |
| api | `python3 conformance/check_logout_seal_policy.py` | pass | V28 regression |
| api | `python3 conformance/check_api_contracts.py` | pass | existing conformance |
| api | `find schemas -name '*.json' -print0 \| xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | schema JSON |
| api | `find fixtures/cloud-compute-boundary -name '*.json' -print0 \| xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | fixtures JSON |
| api | `git diff --check` | pass | required |
| yai | `test -f Documentation/execution/cloud-compute-boundary.md` | pass | new runtime/core doc |
| yai | `make info` | pass | yai touched |
| yai | `make yai` | pass | yai touched |
| yai | `git diff --check` | pass | yai touched |
| cli | `test ! -e source` | pass | source absence confidence |
| cli | `scripts/check-no-source-dependency.sh` | pass | source absence guard |
| sdk | validation | not run | docs-only unless touched |
| loom | validation | not run | docs-only unless touched |

## Findings

### Finding A — Cloud Compute Is Optional Capacity

Record:
Cloud compute is optional governed capacity, not the default runtime truth.

### Finding B — Local Runtime Is Not Cloud Compute

Record:
Local runtime execution remains distinct from cloud execution.

### Finding C — Online Authorization Is Not Cloud Execution

Record:
Online authorization may authorize local work without moving execution to cloud.

### Finding D — Cloud Secrets Stay Out Of V/Core

Record:
Cloud provider secrets and infrastructure provider account objects must not enter
V/core contracts.

### Finding E — V39 Can Start Local Machine Identity

Record:
With cloud separated from local runtime, V39 can define local machine identity.

## V38 Completion Checklist

* [x] `docs/execution/cloud-compute-boundary.md` exists
* [x] `docs/waves/v38-cloud-compute-boundary.md` exists
* [x] `schemas/cloud-compute-boundary.v1.schema.json` exists
* [x] fixtures exist
* [x] conformance script exists or deviation recorded
* [x] `yai/Documentation/execution/cloud-compute-boundary.md` exists
* [x] compute target vocabulary documented
* [x] compute mode vocabulary documented
* [x] decision statuses documented
* [x] blocked reasons documented
* [x] infrastructure boundary documented
* [x] local/cloud boundary documented
* [x] E/V boundary documented
* [x] billing/metering/capacity boundary documented
* [x] no cloud compute implementation added
* [x] no remote job handoff implemented
* [x] no queue/scheduler implemented
* [x] no cloud provider integration added
* [x] no credentials/secrets implementation added
* [x] no API endpoint added
* [x] no SDK cloud client added
* [x] no CLI behavior added
* [x] no session mutation added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
