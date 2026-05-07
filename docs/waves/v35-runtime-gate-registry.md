# V35 — Runtime Gate Registry

## Status

* Delivery: V35
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: runtime gate registry docs + contract schema/fixtures + validation/conformance report
* Previous delivery: V34 — Analytics Binding
* Next delivery: V36 — Case / Job / Flow Limit Boundary

## Purpose

V35 defines runtime action gate classification and creates a verifiable contract
artifact.

## Scope

Record:

* runtime_action_key invariant documented;
* action families documented;
* action categories documented;
* gate classifications documented;
* decision statuses documented;
* safe blocked reasons documented;
* sealed runtime rules documented;
* billing/metering boundary documented;
* E/V boundary documented;
* JSON schema created;
* fixtures created;
* conformance script created;
* no runtime gate evaluator implemented;
* no entitlement/machine/license implementation;
* CLI source absence verified.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `docs/execution/runtime-gate-registry.md` | create | runtime gate registry |
| api | `docs/waves/v35-runtime-gate-registry.md` | create | delivery report |
| api | `schemas/runtime-gate-registry.v1.schema.json` | create | runtime gate registry schema |
| api | `fixtures/runtime-gate-registry/*.json` | create | representative gate registry fixtures |
| api | `conformance/check_runtime_gate_registry.py` | create | dependency-free fixture/schema check |
| yai | `Documentation/execution/runtime-gate-registry.md` | create | runtime/core gate registry record |

## Contract Artifacts

| Artifact | Status | Notes |
| -------- | ------ | ----- |
| runtime gate registry doc | created | API-side canonical action and gate classification contract |
| JSON schema | created | dependency-free JSON contract for runtime action registry entries |
| fixtures | created | six representative runtime action gate scenarios |
| conformance script | created | validates JSON parsing, required fields, enum values, and sealed/diagnostic posture rules |
| yai runtime/core doc | created | runtime/core companion gate registry record |

## Runtime Gate Model

| Concern | V35 policy |
| ------- | ---------- |
| `runtime_action_key` | required action identity |
| `gate_classification` | required gate class |
| diagnostic actions | may be allowed while sealed |
| operational/write actions | must be gated |
| entitlement_ref | safe required ref when configured |
| machine_authorization_ref | safe required ref when configured |
| license_lease_ref | safe required ref when configured |
| limit_projection_ref | safe future limit posture |
| billing/metering | not implemented / not owned |
| session | no ownership |

## Fixture Summary

| Fixture | Scenario | Expected invariant |
| ------- | -------- | ------------------ |
| `diagnostic-runtime-status.json` | runtime status diagnostic | allowed while sealed |
| `case-open-requires-auth.json` | case open action | auth/case requirements |
| `job-start-requires-case-and-gate.json` | job start | case + runtime gate |
| `provider-call-requires-entitlement.json` | provider call | entitlement/license/gate posture |
| `agent-spawn-requires-limit.json` | agent spawn | limit-sensitive action |
| `knowledge-write-requires-case.json` | knowledge write | case/write gate |

## V23 Residual

```text
V23 VS Code docs present: yes
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
| api | `test -f docs/execution/runtime-gate-registry.md` | pass | new policy doc |
| api | `test -f docs/waves/v35-runtime-gate-registry.md` | pass | new report |
| api | `test -f schemas/runtime-gate-registry.v1.schema.json` | pass | schema |
| api | `test -f conformance/check_runtime_gate_registry.py` | pass | conformance |
| api | `python3 conformance/check_runtime_gate_registry.py` | pass | `runtime-gate-registry: ok` |
| api | `python3 conformance/check_analytics_binding.py` | pass | V34 regression |
| api | `python3 conformance/check_flow_binding.py` | pass | V33 regression |
| api | `python3 conformance/check_agent_authority_binding.py` | pass | V32 regression |
| api | `python3 conformance/check_provider_authority_binding.py` | pass | V31 regression |
| api | `python3 conformance/check_knowledge_binding.py` | pass | V30 regression |
| api | `python3 conformance/check_case_evidence_binding.py` | pass | V29 regression |
| api | `python3 conformance/check_logout_seal_policy.py` | pass | V28 regression |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| api | `find schemas -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | schema JSON |
| api | `find fixtures/runtime-gate-registry -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | fixtures JSON |
| api | `git diff --check` | pass | required |
| yai | `test -f Documentation/execution/runtime-gate-registry.md` | pass | new runtime/core doc |
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

### Finding A — Runtime Actions Are Classified

Record:
Runtime actions now have a registry model with action keys and gate classes.

### Finding B — Registry Does Not Grant Authority

Record:
The registry defines requirements; it does not evaluate or grant access.

### Finding C — Diagnostics Remain Separate

Record:
Diagnostic/read-only actions may remain available while operational/write actions
are sealed.

### Finding D — Billing/Metering Is Deferred

Record:
V35 may mark actions as limit/metering sensitive but implements no billing,
quota or meter behavior.

### Finding E — V36 Can Define Limit Boundary

Record:
V36 can define case/job/flow limits using the gate registry action classes.

## V35 Completion Checklist

* [x] `docs/execution/runtime-gate-registry.md` exists
* [x] `docs/waves/v35-runtime-gate-registry.md` exists
* [x] `schemas/runtime-gate-registry.v1.schema.json` exists
* [x] fixtures exist
* [x] conformance script exists
* [x] `Documentation/execution/runtime-gate-registry.md` exists
* [x] runtime_action_key invariant documented
* [x] gate_classification invariant documented
* [x] action families documented
* [x] action categories documented
* [x] decision statuses documented
* [x] safe blocked reasons documented
* [x] sealed runtime rules documented
* [x] billing/metering boundary documented
* [x] E/V boundary documented
* [x] no runtime gate evaluator implemented
* [x] no entitlement/machine/license implementation added
* [x] no billing/metering/limit evaluator added
* [x] no API endpoint added
* [x] no SDK gate client added
* [x] no CLI behavior added
* [x] no session mutation added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
