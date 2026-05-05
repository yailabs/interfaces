# V21.4 — API/SDK Surface Extraction

## Status

* Delivery: V21.4
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: API/SDK semantic surface extraction documentation + migration planning
* Previous delivery: V21.3 — Runtime/Core Logic Extraction
* Next delivery: V21.5 — Legacy Source Deletion Pass

## Purpose

V21.4 extracts API/SDK surface candidates from quarantined `cli/source/`
without implementing those surfaces.

## Scope

Record:

* legacy API/SDK candidate areas inspected;
* candidate API operations/read models/schemas recorded;
* candidate SDK clients/types recorded;
* session-like candidates classified as legacy/non-canonical;
* deletion readiness updated;
* no source deleted;
* no source moved;
* no API/SDK implementation added;
* no behavior changed.

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `docs/cli/legacy-api-sdk-surface-extraction.md` | create | API/SDK extraction artifact |
| api | `docs/waves/v21-4-api-sdk-surface-extraction.md` | create | delivery report |
| sdk | `docs/legacy-cli-surface-candidates.md` | create | SDK candidate surface record |

## API Candidate Summary

| Domain | Candidate API surfaces | Source | Future wave |
| ------ | ---------------------- | ------ | ----------- |
| runtime | `system.status`, `system.runtime.inspect`, future case-bound runtime inspect/readiness summaries | `source/cmd/runtime/status.c`, `source/cmd/case/surface.c` | V41, V47 or later |
| case | `case.current`, `case.list`, `case.show`, `case.records.tail`, future `case.facts.show`, `case.watch.show`, gui summaries | `source/cmd/case/surface.c` | V42 |
| auth/session legacy | `session.status`, `session.summary`, substrate entry classified as compatibility/removal only | `source/cmd/session/*.c` | V43, V51-V55 |
| provider | `providers.list`, `providers.probe`, future `providers.status/current/select/connect/models/doctor`, `models.list`, `models.capabilities.show` | `source/cmd/provider/*.c`, `source/cmd/models/surface.c` | V31, V37, V47 |
| agent | `agents.list`, `agents.trace`, future typed run/invoke surface with `scope/actor/agent/provider/input` | `source/cmd/agent/root.c`, `source/cmd/flow/surface.c` | V32, V47 |
| flow | `workflow.list`, `workflow.show`, `workflow.steps.pending`, `workflow.runs.watch`, future snapshot/blocker/gate/reconcile surfaces | `source/cmd/flow/*.c` | V33, V47 |
| knowledge | `knowledge.query`, `knowledge.lineage.trace`, future context/memory/topology/query families and record-backed read models | `source/cmd/knowledge/*.c` | V30, V49 or later |
| records/evidence/logs | `state.records.query`, `state.records.tail`, future `records.operational_receipts.tail`, evidence summaries | `source/cmd/logs/root.c`, `source/cmd/knowledge/records.c`, `source/cmd/case/surface.c` | V29, V47 |
| analytics | `analytics.query`, future `analytics.show` and summary projections | `source/cmd/analytics/query.c`, `source/cmd/knowledge/records.c` | V34 |

## SDK Candidate Summary

| Domain | Candidate SDK surfaces | Source | Future wave |
| ------ | ---------------------- | ------ | ----------- |
| runtime | `client.system().status()`, `client.runtime().status_inspect()`, future `client.case().runtimeInspect()` | `source/cmd/runtime/status.c`, `source/cmd/case/surface.c` | V20, V58 |
| case | `client.case().current/list/show/recordsTail()`, future watch/facts/runtime typed helpers | `source/cmd/case/surface.c` | V49 |
| auth | no new auth canon extracted; legacy session/status stays compatibility-only | `source/cmd/session/*.c` | V48 |
| entitlement/license | no entitlement/license client candidate extracted from legacy C | none | V50 |
| provider/model access | `client.providers()` family plus `client.models()` capability/model-selection helpers | `source/cmd/provider/*.c`, `source/cmd/models/surface.c` | V37, V50 |
| agent | future `client.agent()` / `client.agents()` run/trace helpers | `source/cmd/agent/root.c`, `source/cmd/flow/surface.c` | V32, Vlater |
| flow | `client.workflow()` richer snapshot/explain/reconcile/blocker helpers | `source/cmd/flow/*.c` | V33, Vlater |
| knowledge/records | `client.knowledge()`, `client.records()`, `client.state()` richer read-model/tail/query helpers | `source/cmd/knowledge/*.c`, `source/cmd/logs/root.c` | V29, V30, Vlater |

## Deletion Readiness Update

| Legacy area | Deletion readiness after V21.4 | Blocking reason |
| ----------- | ------------------------------ | --------------- |
| `source/cmd/runtime` | partial | status/readiness surface shapes are preserved, but subtree still exists and broader legacy build references remain |
| `source/cmd/provider` | partial | provider/model operation shapes are preserved, but wrappers remain in the quarantined tree |
| `source/cmd/agent` | partial | agent request grammar is preserved, but deletion still depends on broader build cleanup |
| `source/cmd/flow` | partial | API/SDK candidate read models are documented, but subtree is still large and referenced in legacy build wiring |
| `source/cmd/govern` | partial | governance surface shapes are preserved, but compatibility/session contamination and build cleanup remain |
| `source/cmd/knowledge` | partial | knowledge/read-model families are preserved, but `records.c` remains in legacy C until deletion pass |
| `source/cmd/analytics` | partial | analytics query/show family is documented, but subtree still exists in broader legacy references |
| `source/cmd/logs` | partial | receipts-tail semantics are preserved, but transport-visible implementation is not moved in this wave |
| `source/cmd/case` | partial | case facts/runtime/watch candidates are documented, but the large legacy case surface still exists |
| `source/cmd/session` | partial | session is now explicitly legacy/non-canonical, but deletion waits on compatibility/deprecation waves |
| `source/out` | partial | no preserved API/SDK semantics remain, but subtree is still present until V21.5 |
| `source/shared` | partial | no preserved API/SDK semantics remain, but subtree is still present until V21.5 |

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f docs/cli/legacy-api-sdk-surface-extraction.md` | pass | new extraction doc |
| api | `test -f docs/waves/v21-4-api-sdk-surface-extraction.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| sdk | `test -f docs/legacy-cli-surface-candidates.md` | pass | new SDK candidate doc |
| sdk | `git diff --check` | pass | docs validation |
| cli | `find source/cmd -maxdepth 4 -type f | sort`; `find source/shared -maxdepth 5 -type f | sort`; `find source/out -maxdepth 5 -type f | sort`; semantic `rg` scan over `source` | pass | candidate inspection completed over runtime/provider/agent/flow/govern/knowledge/analytics/logs/case/session/shared/out |
| cli | `cargo fmt --check` | pass | CLI untouched for behavior; validation still run |
| cli | `cargo test` | pass | warnings only; tests passed |
| cli | `cargo build` | pass | warnings only; build passed |
| yai | `make info`; `make yai`; `git diff --check` | pass | validation run even though no yai files changed in V21.4 |
| loom | validation | not run | no loom files touched |

## Findings

### Finding A — API/SDK Surface Candidates Extracted

Record:
Useful API/SDK surface shapes have been preserved outside `cli/source/`.

### Finding B — Session Remains Non-Canonical

Record:
Session-like surfaces are legacy compatibility/removal candidates, not API/SDK canon.

### Finding C — SDK Owns Typed Clients, Not Execution

Record:
SDK candidates are typed clients/request-response surfaces, not runtime execution.

### Finding D — V21.5 Can Begin Deletion

Record:
With runtime/core and API/SDK semantics extracted, V21.5 can start deleting
migrated/obsolete legacy source subtrees.

## V21.4 Completion Checklist

* [x] `docs/cli/legacy-api-sdk-surface-extraction.md` exists
* [x] `docs/waves/v21-4-api-sdk-surface-extraction.md` exists
* [x] `sdk/docs/legacy-cli-surface-candidates.md` exists
* [x] API candidate surfaces extracted
* [x] SDK candidate surfaces extracted
* [x] session-like surfaces classified legacy/non-canonical
* [x] deletion readiness updated
* [x] no source files deleted
* [x] no source files moved
* [x] no API implementation added
* [x] no SDK implementation added
* [x] no behavior changed
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched

## Pass Criteria

* V21.4 report exists
* API/SDK extraction docs exist
* reviewed legacy areas have API/SDK candidate classifications
* future API/SDK waves are identified
* no files are deleted or moved
* no implementation is added
* validation results are recorded truthfully

## Fail Criteria

* V21.4 deletes legacy source
* V21.4 moves legacy source
* V21.4 implements API/SDK code prematurely
* V21.4 treats session as canonical API/SDK surface
* V21.4 treats SDK as execution owner
* V21.4 hides unknowns
* V21.4 edits unrelated files
