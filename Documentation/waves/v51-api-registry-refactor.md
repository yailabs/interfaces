# V51 — API Registry Refactor

## Status

* Delivery: V51
* Status: done
* Track: V — API Canon
* Branch: `refoundation/phase-01`
* Previous delivery: V50.10 — Command System Refactor Readiness
* Next delivery: V52 — API Case Expansion

## Scope

* families changed: yes
* operations changed: yes
* projections changed: yes
* legacy/deprecated entries marked: yes
* forbidden entries locked: yes
* conformance added/updated: yes
* no CLI/SDK/TUI/runtime implementation: yes

## Files Changed

| File | Change |
| ---- | ------ |
| `registry/api-families.v1.json` | Added V51 families and marked session legacy. |
| `registry/api-verbs.v1.json` | Added core lifecycle verbs needed by the refactored registry. |
| `registry/api-operations.v1.json` | Added action-aligned operations, marked legacy compatibility operations, and deepened capability families. |
| `registry/api-operation-projections.v1.json` | Added family projection rules, legacy alias mappings, and forbidden action locks. |
| `registry/api-surfaces.v1.json` | Added/updated canonical surfaces and marked session surface legacy. |
| `registry/README.md` | Rewrote registry principles for V51. |
| `Documentation/api-registry-refactor.md` | Added the V51 registry decision document. |
| `Documentation/waves/v51-api-registry-refactor.md` | Added this delivery report. |
| `conformance/check_yai_actions_registry.py` | Added action registry seed validation. |
| `conformance/check_operation_registry.py` | Reworked registry conformance around V51 rules. |
| `conformance/check_api_contracts.py` | Updated surface/family validation for V51 registry shape. |

## Registry Decisions

| Topic | Decision |
| ----- | -------- |
| session | kept only as legacy/deprecated compatibility family |
| flow/workflow | `workflow` canonical, `flow` legacy alias only |
| records/state.records | `state.records.*` canonical, root `records.*` non-canonical |
| providers/models/agents | API plural retained, CLI/TUI singular projection preserved |
| policy_pack | added as canonical API family |
| materialization | added as canonical API family; CLI/TUI may project `materialize` |
| intake | added as canonical API family |
| lineage | promoted to first-class API family |
| evidence | promoted to first-class API family |
| license/machine/limits | added as explicit posture/projection families |
| logs | added as scoped-only family; no generic root logs owner |
| runtime/query/inspect/policy roots | locked as forbidden where applicable |

## Action Registry Alignment

* yai-actions consumed: yes
* drift remaining: yes
* intentionally deferred actions: yes

Remaining drift is intentional:

* `yai-actions.v1.json` still contains many `api_operation_candidate: none verified` seed rows.
* V51 does not rewrite the full action seed; it refactors the canonical API registry and adds conformance around the boundary.
* Direct action-seed metadata sync can now proceed safely in later waves because canonical family and operation names are fixed.

## Validation

Executed:

* `python3 -m json.tool registry/yai-actions.v1.json >/dev/null`
* `python3 -m json.tool registry/api-families.v1.json >/dev/null`
* `python3 -m json.tool registry/api-operations.v1.json >/dev/null`
* `python3 -m json.tool registry/api-operation-projections.v1.json >/dev/null`
* `python3 -m json.tool registry/api-surfaces.v1.json >/dev/null`
* `python3 conformance/check_yai_actions_registry.py`
* `python3 conformance/check_operation_registry.py`
* `python3 conformance/check_api_contracts.py`
* `git diff --check`
* `test ! -e source`
* `scripts/check-no-source-dependency.sh`
* `cargo fmt --check`
* `cargo test`
* `cargo build`
* `make info`
* `make yai`
* `git diff --check` in `cli`, `yai`, `sdk`, and `loom`

Results:

* `check_yai_actions_registry.py` -> `yai-actions: ok`
* `check_operation_registry.py` -> `conformance: ok`
* `check_api_contracts.py` -> `api-contracts: ok`
* `cli` source absence guard -> pass
* `cli` test/build -> pass
* `yai` make/info -> pass
* `sdk` / `loom` `git diff --check` -> pass

## Completion Checklist

* session legacy/deprecated: yes
* workflow canonical: yes
* state.records canonical: yes
* provider/model/agent API plural retained: yes
* CLI singular projection preserved: yes
* materialization/intake/policy_pack added or documented: yes
* lineage/evidence addressed: yes
* forbidden root query/inspect/policy/runtime lifecycle locked: yes
* check_operation_registry passes: yes
* check_api_contracts passes: yes
* no implementation changes: yes
