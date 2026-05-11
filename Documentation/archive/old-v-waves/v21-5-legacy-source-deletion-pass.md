# V21.5 - Legacy Source Deletion Pass

## Status

* Delivery: V21.5
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: legacy source deletion + build-reference cleanup + documentation/report
* Previous delivery: V21.4 - API/SDK Surface Extraction
* Next delivery: V21.6 - CLI Source Absence Guardrail

## Purpose

V21.5 deletes deletion-ready legacy C `cli/source/` material after extraction.

## Scope

* deletion-ready areas confirmed;
* selected legacy files/subtrees deleted;
* build references updated;
* Rust CLI remains canonical;
* blocked residuals recorded;
* no behavior change intended.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `Documentation/cli/legacy-source-deletion-pass.md` | create | deletion pass record |
| api | `Documentation/waves/v21-5-legacy-source-deletion-pass.md` | create | delivery report |
| cli | `source/out` | delete | deletion-ready legacy rendering stubs |
| cli | `source/shared` | delete | deletion-ready legacy helper subtree |
| cli | `MIGRATION_MAP.md` | update | reflect deleted shared-helper migration source |
| yai | `Makefile` | update | remove unused legacy source inventory that referenced deleted paths |

## Deletion Decision

| Legacy area | V21.3 readiness | V21.4 readiness | Delete in V21.5? | Reason |
| ----------- | --------------- | --------------- | ---------------- | ------ |
| `source/out` | partial | partial | yes | semantics already extracted; no Rust CLI dependency; only broader references were in an unused Makefile inventory list removed here |
| `source/shared` | partial | partial | yes | semantics already extracted; no Rust CLI dependency; only broader references were in an unused Makefile inventory list removed here |
| `source/cmd/session` | n/a | partial | no | explicitly non-canonical, but still retained as residual command family until a later focused deletion pass |
| `source/cmd/logs` | partial | partial | no | records/evidence surface preserved, but residual command tree still retained |
| `source/cmd/runtime` | partial | partial | no | runtime wrappers remain partially blocked and `source/main.c` still anchors residual legacy tree presence |
| `source/cmd/provider` | partial | partial | no | provider family preserved but residual command tree remains |
| `source/cmd/agent` | partial | partial | no | agent grammar preserved but residual command tree remains |
| `source/cmd/flow` | blocked | partial | no | heavy blocked semantic area from V21.3 |
| `source/cmd/govern` | partial | partial | no | partial only; residual governance wrappers remain |
| `source/cmd/knowledge` | blocked | partial | no | heavy blocked semantic area from V21.3 |
| `source/cmd/analytics` | partial | partial | no | thin wrapper, but not required for this first deletion pass |
| `source/cmd/case` | n/a | partial | no | large partial case surface remains retained |
| `source/main.c` | blocked | n/a | no | still used as residual external-source sentinel in `yai/Makefile` and still mixes blocked domains |

## Deleted Paths

| Deleted path | Reason | Validation |
| ------------ | ------ | ---------- |
| `cli/source/out` | disposable output stubs with no remaining preserved semantics and no active build dependency | subtree absent from filesystem after deletion; no remaining `Makefile` references to deleted paths |
| `cli/source/shared` | disposable helper subtree with Rust parity already present in canonical CLI/config surfaces | subtree absent from filesystem after deletion; no remaining `Makefile` references to deleted paths |

## Remaining Residuals

| Remaining path | Reason retained | Future wave |
| -------------- | --------------- | ----------- |
| `cli/source/main.c` | residual sentinel plus blocked mixed-domain entrypoint | V21.6/follow-up |
| `cli/source/cmd/runtime` | partial residual runtime family | V21.6/follow-up |
| `cli/source/cmd/provider` | partial residual provider family | V21.6/follow-up |
| `cli/source/cmd/agent` | partial residual agent family | V21.6/follow-up |
| `cli/source/cmd/flow` | blocked semantic mass | V21.6/follow-up |
| `cli/source/cmd/govern` | partial residual governance family | V21.6/follow-up |
| `cli/source/cmd/knowledge` | blocked semantic mass | V21.6/follow-up |
| `cli/source/cmd/analytics` | partial residual analytics family | V21.6/follow-up |
| `cli/source/cmd/logs` | partial residual logs/records family | V21.6/follow-up |
| `cli/source/cmd/case` | partial residual case family | V21.6/follow-up |
| `cli/source/cmd/session` | non-canonical residual compatibility family | V21.6/follow-up |
| `cli/source/assets/shell` | residual legacy shell asset family | V21.6/follow-up |
| `cli/source/README.md` and `cli/source/MIGRATION_MAP.md` | quarantine and local residual context | V21.6/follow-up |

## Build Reference Cleanup

| Reference | Before | After | Result |
| --------- | ------ | ----- | ------ |
| Cargo -> source | none | none | pass |
| Rust src -> source | none | none | pass |
| Rust tests -> source | none | none | pass |
| yai Makefile -> deleted paths | yes | no | pass |
| docs -> deleted paths | historical/current | historical/current | pass |

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f Documentation/cli/legacy-source-deletion-pass.md` | pass | new doc |
| api | `test -f Documentation/waves/v21-5-legacy-source-deletion-pass.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | contract check |
| api | `git diff --check` | pass | required |
| cli | `cargo fmt --check` | pass | required |
| cli | `cargo test` | pass | required |
| cli | `cargo build` | pass | required |
| cli | `git diff --check` | pass | required |
| cli | post-deletion source inspection | pass | remaining legacy source recorded |
| cli | dependency regression scan | pass | no Rust/Cargo dependency on `source/` |
| yai | `make info` | pass | Makefile still valid |
| yai | `make yai` | pass | broader build still passes |
| yai | `git diff --check` | pass | required after Makefile edit |
| sdk | `git diff --check` | not run | not touched |
| loom | `git diff --check` | not run | not touched |

## Findings

### Finding A - Deletion Began

Deletion-ready legacy `source/` material was removed.

### Finding B - Rust CLI Remains Canonical

Rust `src/` remains the canonical CLI and tests/build still pass.

### Finding C - Residuals Are Explicit

Any remaining legacy C areas are retained only because blockers remain.

### Finding D - V21.6 Can Add Guardrails

After deletion pass, V21.6 can prevent source dependency or recreation.

## V21.5 Completion Checklist

* [x] `Documentation/cli/legacy-source-deletion-pass.md` exists
* [x] `Documentation/waves/v21-5-legacy-source-deletion-pass.md` exists
* [x] deletion decision table completed
* [x] deletion-ready areas deleted or explicitly deferred
* [x] build references to deleted paths removed
* [x] Rust CLI cargo validation passes
* [x] yai make validation passes if relevant
* [x] no source files moved
* [x] no runtime behavior added
* [x] no API/SDK implementation added
* [x] no session canonicalization added
* [x] remaining residuals recorded
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
