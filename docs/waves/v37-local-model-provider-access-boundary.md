# V37 — Local Model / Provider Access Boundary

## Status

* Delivery: V37
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: local model/provider access boundary docs + contract schema/fixtures + validation/conformance report
* Previous delivery: V36 — Case / Job / Flow Limit Boundary
* Next delivery: V38 — Cloud Compute Boundary

## Purpose

V37 defines governed access boundaries for local models, external providers,
hosted models and custom/fine-tuned models.

## Scope

* access target vocabulary documented;
* access mode vocabulary documented;
* decision statuses documented;
* blocked reasons documented;
* credential boundary documented;
* local/offline boundary documented;
* E/V boundary documented;
* billing/metering/provider budget boundary documented;
* JSON schema created;
* fixtures created;
* conformance script created or deviation recorded;
* no model/provider execution implemented;
* no credentials/secrets implemented;
* no provider budget evaluator implemented;
* CLI source absence verified.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `docs/execution/local-model-provider-access-boundary.md` | create | model/provider access boundary |
| api | `docs/waves/v37-local-model-provider-access-boundary.md` | create | delivery report |
| api | `schemas/local-model-provider-access-boundary.v1.schema.json` | create | access boundary schema |
| api | `fixtures/local-model-provider-access-boundary/*.json` | create | representative access fixtures |
| api | `conformance/check_local_model_provider_access_boundary.py` | create | dependency-free fixture/schema check |
| yai | `Documentation/execution/local-model-provider-access-boundary.md` | create | runtime/core access boundary record |

## Contract Artifacts

| Artifact | Status | Notes |
| -------- | ------ | ----- |
| model/provider access doc | created | API execution doctrine added. |
| JSON schema | created | Dependency-free contract artifact. |
| fixtures | created | Representative local, provider, hosted, custom, and credential-boundary examples. |
| conformance script | created | Dependency-free fixture/schema validation. |
| yai runtime/core doc | created | Runtime/core boundary recorded. |

## Model / Provider Access Model

| Concern | V37 policy |
| ------- | ---------- |
| `access_target` | required |
| `access_mode` | required |
| `case_ref` | required for case-scoped model/provider work |
| `runtime_gate_decision_ref` | optional gate posture |
| `entitlement_ref` | optional authorization posture |
| `machine_authorization_ref` | optional authorization posture |
| `license_lease_ref` | optional authorization posture |
| `limit_projection_ref` | optional safe limit posture |
| `provider_budget_ref` | optional safe future posture |
| credentials/secrets | not exposed to V/core |
| billing/metering | not implemented / not owned |
| local model | not automatically free/unlimited |
| hosted/custom model | future optional capability |

## Fixture Summary

| Fixture | Scenario | Expected invariant |
| ------- | -------- | ------------------ |
| `local-model-allowed.json` | local model allowed | access target/mode present |
| `provider-blocked-missing-entitlement.json` | provider lacks entitlement | blocked reason present |
| `provider-blocked-budget.json` | provider budget exceeded | blocked reason present, no billing implementation |
| `hosted-model-requires-cloud-gate.json` | hosted model requires cloud gate | hosted access not implied live |
| `custom-model-not-implemented.json` | custom model future capability | not implemented decision |
| `user-owned-provider-credentials-boundary.json` | user-owned credentials required | no secret material |

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
| api | `test -f docs/execution/local-model-provider-access-boundary.md` | pass | new policy doc |
| api | `test -f docs/waves/v37-local-model-provider-access-boundary.md` | pass | new report |
| api | `test -f schemas/local-model-provider-access-boundary.v1.schema.json` | pass | schema |
| api | `test -f conformance/check_local_model_provider_access_boundary.py` | pass | conformance |
| api | `python3 conformance/check_local_model_provider_access_boundary.py` | pass | V37 conformance |
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
| api | `find fixtures/local-model-provider-access-boundary -name '*.json' -print0 \| xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | fixtures JSON |
| api | `git diff --check` | pass | required |
| yai | `test -f Documentation/execution/local-model-provider-access-boundary.md` | pass | new runtime/core doc |
| yai | `make info` | pass | yai touched |
| yai | `make yai` | pass | yai touched |
| yai | `git diff --check` | pass | yai touched |
| cli | `test ! -e source` | pass | source absence confidence |
| cli | `scripts/check-no-source-dependency.sh` | pass | source absence guard |
| sdk | validation | not run | docs-only unless touched |
| loom | validation | not run | docs-only unless touched |

## Findings

### Finding A — Model/Provider Access Is Governed

Record:
Local model and provider access are governed runtime actions, not free-floating
or automatically unlimited.

### Finding B — Credentials Stay Out Of V/Core Contracts

Record:
Provider credentials and secrets must not enter V/core contracts.

### Finding C — Hosted/Custom Models Are Future Optional Capabilities

Record:
Hosted and custom/fine-tuned model access are not implied live by local runtime
presence.

### Finding D — Provider Budget / Limits Are Safe Posture Only

Record:
V37 may reference provider_budget_ref and limit_projection_ref but implements no
billing, metering or budget evaluator.

### Finding E — V38 Can Define Cloud Compute Boundary

Record:
Cloud compute can now be separated from provider/model access.

## V37 Completion Checklist

* [x] `docs/execution/local-model-provider-access-boundary.md` exists
* [x] `docs/waves/v37-local-model-provider-access-boundary.md` exists
* [x] `schemas/local-model-provider-access-boundary.v1.schema.json` exists
* [x] fixtures exist
* [x] conformance script exists or deviation recorded
* [x] `yai/Documentation/execution/local-model-provider-access-boundary.md` exists
* [x] access target vocabulary documented
* [x] access mode vocabulary documented
* [x] decision statuses documented
* [x] blocked reasons documented
* [x] credential boundary documented
* [x] local/offline boundary documented
* [x] E/V boundary documented
* [x] billing/metering/provider budget boundary documented
* [x] no local model implementation added
* [x] no provider execution implemented
* [x] no hosted/custom model implementation added
* [x] no credential/secrets implementation added
* [x] no provider budget evaluator implemented
* [x] no API endpoint added
* [x] no SDK provider/model client added
* [x] no CLI behavior added
* [x] no session mutation added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
