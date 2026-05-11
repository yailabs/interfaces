# V21.7 - Residual Domain Source Deletion Pass

## Status

* Delivery: V21.7
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: residual legacy command-family deletion + build-reference cleanup + documentation/report
* Previous delivery: V21.6 - CLI Source Dependency / Recreation Guardrail
* Next delivery: V21.8 - Legacy Entrypoint / Makefile Source Removal

## Purpose

V21.7 deletes deletion-ready residual domain command families under
`cli/source/cmd`.

## Scope

* residual command-family readiness confirmed;
* deletion-ready command-family subtrees deleted;
* build references updated;
* guardrail expanded;
* remaining residuals recorded;
* no behavior change intended.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `Documentation/cli/residual-domain-source-deletion-pass.md` | create | residual deletion record |
| api | `Documentation/waves/v21-7-residual-domain-source-deletion-pass.md` | create | delivery report |
| cli | `source/cmd/runtime` | delete | deletion-ready residual command family |
| cli | `source/cmd/provider` | delete | deletion-ready residual command family |
| cli | `source/cmd/agent` | delete | deletion-ready residual command family |
| cli | `source/cmd/govern` | delete | deletion-ready residual command family |
| cli | `source/cmd/analytics` | delete | deletion-ready residual command family |
| cli | `source/cmd/logs` | delete | deletion-ready residual command family |
| cli | `source/cmd/session` | delete | deletion-ready residual command family |
| cli | `scripts/check-no-source-dependency.sh` | update | block recreation of newly deleted paths |
| cli | `MIGRATION_MAP.md` | update | reflect deleted/residual family status |

## Deletion Decision

| Legacy area | V21.3/V21.4 readiness | Active build reference? | Delete in V21.7? | Reason |
| ----------- | --------------------- | ----------------------- | ---------------- | ------ |
| `source/cmd/runtime` | partial | no | yes | semantics extracted; no active Rust/Cargo or `yai/Makefile` file-level dependency remained |
| `source/cmd/provider` | partial | no | yes | semantics extracted; no active Rust/Cargo or `yai/Makefile` file-level dependency remained |
| `source/cmd/agent` | partial | no | yes | semantics extracted; no active Rust/Cargo or `yai/Makefile` file-level dependency remained |
| `source/cmd/flow` | blocked/partial | no | no | still explicitly heavy/blocked from V21.3/V21.4 |
| `source/cmd/govern` | partial | no | yes | semantics extracted; no active Rust/Cargo or `yai/Makefile` file-level dependency remained |
| `source/cmd/knowledge` | blocked/partial | no | no | still explicitly heavy/blocked from V21.3/V21.4 |
| `source/cmd/analytics` | partial | no | yes | thin derived wrapper, semantics extracted, no active file-level dependency remained |
| `source/cmd/logs` | partial | no | yes | receipt-tail wrapper, semantics extracted, no active file-level dependency remained |
| `source/cmd/case` | partial | no | no | heavy partial case/query surface retained for later focused deletion |
| `source/cmd/session` | partial | no | yes | non-canonical compatibility family; no active file-level dependency remained |
| `source/assets/shell` | not deletion-ready | yes | no | still referenced by `yai/Makefile` asset copy and test harness |
| `source/main.c` | blocked | yes | no | retained as Makefile sentinel/entrypoint residual; V21.8 owns removal decision |

## Deleted Paths

| Deleted path | Reason | Validation |
| ------------ | ------ | ---------- |
| `cli/source/cmd/runtime` | extraction-covered partial residual with no active build dependency | subtree absent after deletion; guardrail blocks recreation |
| `cli/source/cmd/provider` | extraction-covered partial residual with no active build dependency | subtree absent after deletion; guardrail blocks recreation |
| `cli/source/cmd/agent` | extraction-covered partial residual with no active build dependency | subtree absent after deletion; guardrail blocks recreation |
| `cli/source/cmd/govern` | extraction-covered partial residual with no active build dependency | subtree absent after deletion; guardrail blocks recreation |
| `cli/source/cmd/analytics` | extraction-covered thin residual with no active build dependency | subtree absent after deletion; guardrail blocks recreation |
| `cli/source/cmd/logs` | extraction-covered residual with no active build dependency | subtree absent after deletion; guardrail blocks recreation |
| `cli/source/cmd/session` | non-canonical compatibility residual with no active build dependency | subtree absent after deletion; guardrail blocks recreation |

## Remaining Residuals

| Remaining path | Reason retained | Future wave |
| -------------- | --------------- | ----------- |
| `cli/source/main.c` | residual sentinel and blocked mixed-domain entrypoint | V21.8/follow-up |
| `cli/source/cmd/flow` | blocked semantic mass | V21.8/follow-up |
| `cli/source/cmd/knowledge` | blocked semantic mass | V21.8/follow-up |
| `cli/source/cmd/case` | heavy partial case/query surface | V21.8/follow-up |
| `cli/source/assets/shell` | retained shell assets still referenced by Makefile/tests | V21.8/follow-up |
| `cli/source/cmd/ai` | non-target residual family | later follow-up |
| `cli/source/cmd/inspect` | non-target residual family | later follow-up |
| `cli/source/cmd/models` | non-target residual family | later follow-up |
| `cli/source/cmd/query` | non-target residual family | later follow-up |
| `cli/source/cmd/skills` | non-target residual family | later follow-up |
| `cli/source/cmd/dispatch.c` and `cli/source/cmd/root.h` | residual glue | later follow-up |

## Build Reference Cleanup

| Reference | Before | After | Result |
| --------- | ------ | ----- | ------ |
| Rust Cargo/src/tests -> source | none | none | pass |
| yai Makefile -> deleted paths | no | no | pass |
| docs -> deleted paths | historical/current | historical/current | pass |
| guardrail -> deleted paths | partial | updated | pass |

## Full Absence Status

```text
source/ fully removed: no
full absence guardrail active: no
partial guardrail active: yes
```

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f Documentation/cli/residual-domain-source-deletion-pass.md` | pass | new doc |
| api | `test -f Documentation/waves/v21-7-residual-domain-source-deletion-pass.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | if available |
| api | `git diff --check` | pass | required |
| cli | `scripts/check-no-source-dependency.sh` | pass | required |
| cli | `cargo fmt --check` | pass | required |
| cli | `cargo test` | pass | required |
| cli | `cargo build` | pass | required |
| cli | `git diff --check` | pass | required |
| cli | post-deletion source inspection | pass | deleted family subtrees absent; remaining source recorded |
| cli | dependency regression scan | pass | no Rust/Cargo dependency on source |
| yai | `make info` | pass | relevant verification |
| yai | `make yai` | pass | relevant verification |
| yai | `git diff --check` | not run | not touched in V21.7 |
| sdk | `git diff --check` | not run | not touched |
| loom | `git diff --check` | not run | not touched |

## Findings

### Finding A - Residual Command Deletion Began

Additional deletion-ready command-family subtrees were removed.

### Finding B - Guardrail Expanded

The guardrail now blocks recreation of V21.5 and V21.7 deleted subtrees.

### Finding C - Remaining Residuals Are Narrower

Any remaining `source/` areas are explicitly retained for V21.8 or follow-up.

### Finding D - Full Absence Still Must Be Truthful

If `source/` remains, full absence is not claimed.

## V21.7 Completion Checklist

* [x] `Documentation/cli/residual-domain-source-deletion-pass.md` exists
* [x] `Documentation/waves/v21-7-residual-domain-source-deletion-pass.md` exists
* [x] deletion decision table completed
* [x] deletion-ready residual command-family areas deleted or explicitly deferred
* [x] build references to deleted paths removed
* [x] guardrail expanded to block newly deleted paths
* [x] Rust CLI cargo validation passes
* [x] yai make validation passes if relevant
* [x] no source files moved
* [x] no runtime behavior added
* [x] no API/SDK implementation added
* [x] no session canonicalization added
* [x] remaining residuals recorded
* [x] full absence not falsely claimed
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
