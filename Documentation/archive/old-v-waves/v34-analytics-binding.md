# V34 — Analytics Binding

## Status

* Delivery: V34
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: analytics binding docs + contract schema/fixtures + validation/conformance report
* Previous delivery: V33 — Flow Binding
* Next delivery: V35 — Runtime Gate Registry

## Purpose

V34 defines analytics as derived from governed case-bound activity and creates a
verifiable contract artifact.

## Scope

Record:

* analytics_event.case_ref invariant documented;
* analytics_projection.case_ref rule documented for case-scoped projections;
* analytics kinds documented;
* analytics scopes documented;
* decision statuses documented;
* safe blocked/redaction reasons documented;
* billing/metering boundary documented;
* E/V boundary documented;
* JSON schema created;
* fixtures created;
* conformance script created;
* no analytics storage implemented;
* no telemetry/dashboard/optimization implementation;
* no billing/metering/limit evaluator implemented;
* CLI source absence verified.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `Documentation/execution/analytics-binding.md` | create | analytics binding |
| api | `Documentation/waves/v34-analytics-binding.md` | create | delivery report |
| api | `schemas/analytics-binding.v1.schema.json` | create | analytics binding contract schema |
| api | `fixtures/analytics-binding/*.json` | create | representative analytics binding fixtures |
| api | `conformance/check_analytics_binding.py` | create | dependency-free fixture/schema check |
| yai | `Documentation/execution/analytics-binding.md` | create | runtime/core analytics binding record |

## Contract Artifacts

| Artifact | Status | Notes |
| -------- | ------ | ----- |
| analytics binding doc | created | API-side canonical analytics binding contract |
| JSON schema | created | dependency-free JSON contract for derived analytics |
| fixtures | created | five representative analytics binding scenarios |
| conformance script | created | validates JSON parsing, required keys, enum values, case-scope rules, and array posture |
| yai runtime/core doc | created | runtime/core companion analytics binding record |

## Analytics Binding Model

| Concern | V34 policy |
| ------- | ---------- |
| `case_ref` | required for case/case_tree analytics |
| `analytics_ref` | analytics identity |
| `analytics_kind` | derived metric/event category |
| `analytics_scope` | case/account/machine/runtime/system scope |
| source records/evidence/knowledge | source material only |
| source jobs/flows/agents/providers | source material only |
| runtime_gate_decision refs | source/decision material only |
| license/machine refs | posture refs only |
| billing/metering | not implemented / not owned |
| session | no ownership |

## Fixture Summary

| Fixture | Scenario | Expected invariant |
| ------- | -------- | ------------------ |
| `case-activity-analytics.json` | case activity summary | `case_ref` present |
| `job-completion-analytics.json` | job completion metric | job ref optional, case remains scope |
| `flow-progress-analytics.json` | flow progress metric | flow ref optional, case remains scope |
| `provider-blocked-analytics.json` | blocked provider activity | blocked reason recorded |
| `evidence-growth-analytics.json` | evidence growth summary | evidence refs source material only |

## V23 Residual

```text
V23 VS Code docs present: yes
If no, residual remains from V24-V33 baseline and is not fixed in V34.
```

## CLI Source Absence Check

```text
cli/source/ exists: no
full absence guardrail active: yes
Rust src/ is the only CLI implementation: yes
```

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f Documentation/execution/analytics-binding.md` | pass | new policy doc |
| api | `test -f Documentation/waves/v34-analytics-binding.md` | pass | new report |
| api | `test -f schemas/analytics-binding.v1.schema.json` | pass | schema |
| api | `test -f conformance/check_analytics_binding.py` | pass | conformance |
| api | `python3 conformance/check_analytics_binding.py` | pass | `analytics-binding: ok` |
| api | `python3 conformance/check_flow_binding.py` | pass | V33 regression |
| api | `python3 conformance/check_agent_authority_binding.py` | pass | V32 regression |
| api | `python3 conformance/check_provider_authority_binding.py` | pass | V31 regression |
| api | `python3 conformance/check_knowledge_binding.py` | pass | V30 regression |
| api | `python3 conformance/check_case_evidence_binding.py` | pass | V29 regression |
| api | `python3 conformance/check_logout_seal_policy.py` | pass | V28 regression |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| api | `find schemas -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | schema JSON |
| api | `find fixtures/analytics-binding -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | fixtures JSON |
| api | `git diff --check` | pass | required |
| yai | `test -f Documentation/execution/analytics-binding.md` | pass | new runtime/core doc |
| yai | `make info` | pass | yai touched |
| yai | `make yai` | pass | `Nothing to be done for 'yai'` |
| yai | `git diff --check` | pass | yai touched |
| cli | `test ! -e source` | pass | source absence confidence |
| cli | `scripts/check-no-source-dependency.sh` | pass | source absence guard |
| cli | `cargo fmt --check` | not run | cli not touched |
| cli | `cargo test` | not run | cli not touched |
| sdk | validation | not run | docs-only unless touched |
| loom | validation | not run | docs-only unless touched |

## Findings

### Finding A — Analytics Is Derived

Record:
Analytics derives from governed case-bound activity and is not primary truth.

### Finding B — Analytics Does Not Own Source Material

Record:
Analytics may summarize records, evidence, knowledge, jobs, flows, agents and
provider calls, but does not own or replace them.

### Finding C — Analytics Is Not Billing / Metering

Record:
V34 distinguishes analytics from billing meters, quota counters and usage
ledgers.

### Finding D — Analytics Must Respect E/V Boundary

Record:
Analytics may reference safe refs/projections but must not consume forbidden E
objects.

### Finding E — Runtime Gate Registry Can Build On Analytics Boundary

Record:
V35 can define runtime action gates without treating analytics as authority.

## V34 Completion Checklist

* [x] `Documentation/execution/analytics-binding.md` exists
* [x] `Documentation/waves/v34-analytics-binding.md` exists
* [x] `schemas/analytics-binding.v1.schema.json` exists
* [x] fixtures exist
* [x] conformance script exists
* [x] `Documentation/execution/analytics-binding.md` exists
* [x] analytics_event.case_ref invariant documented
* [x] analytics_projection.case_ref case-scoped rule documented
* [x] analytics kinds documented
* [x] analytics scopes documented
* [x] decision statuses documented
* [x] safe blocked/redaction reasons documented
* [x] visibility documented
* [x] retention posture documented
* [x] billing/metering boundary documented
* [x] E/V boundary documented
* [x] no analytics storage implemented
* [x] no telemetry/dashboard/optimization implementation added
* [x] no billing/metering/limit evaluator added
* [x] no API endpoint added
* [x] no SDK analytics client added
* [x] no CLI behavior added
* [x] no session mutation added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
