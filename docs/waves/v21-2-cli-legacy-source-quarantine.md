# V21.2 - CLI Legacy Source Quarantine

## Status

* Delivery: V21.2
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: legacy source quarantine documentation + guardrail preparation
* Previous delivery: V21.1 - CLI Legacy Source Extraction Map
* Next delivery: V21.3 - Runtime/Core Logic Extraction

## Purpose

V21.2 quarantines the legacy C `cli/source/` tree.

## Scope

Record:

* `source/` marked non-canonical;
* `source/` marked extraction-only;
* stale `source/README.md` path wording corrected if touched;
* new dependency rule documented;
* broader `yai/Makefile` references recorded, not removed;
* no C files deleted;
* no C files moved;
* no behavior changed.

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `docs/cli/legacy-source-quarantine.md` | create | quarantine policy |
| api | `docs/waves/v21-2-cli-legacy-source-quarantine.md` | create | delivery report |
| cli | `source/README.md` | update | quarantine banner / stale path fix |
| cli | `README.md` | update | quarantine boundary |
| cli | `MIGRATION_MAP.md` | update | staged source deletion |

## Quarantine Result

| Check | Result | Notes |
| ----- | ------ | ----- |
| `source/` still exists | yes | no deletion in V21.2 |
| `source/` canonical CLI | no | Rust `src/` remains canonical |
| `source/` extraction-only | yes | documented in API and CLI docs |
| `source/README.md` stale path fixed | yes | `../cli/src` -> `../src` |
| new Rust dependency on `source/` added | no | required |
| behavior changed | no | required |

## Dependency Guard Result

| Check | Result | Notes |
| ----- | ------ | ----- |
| Cargo depends on `source/` | no | no `build.rs`; `Cargo.toml` still points at `src/main.rs` |
| Rust `src/` depends on `source/` | no | dependency regression scan stayed clean |
| Rust tests depend on `source/` | no | dependency regression scan stayed clean |
| broader `yai/Makefile` references `source/` | yes | expected from V21.1; recorded, not removed |
| guardrail script added | no | deferred; policy documented first |

## Residuals Carried Forward

| Residual | Future wave | Notes |
| -------- | ----------- | ----- |
| extract runtime/core candidates | V21.3 | runtime/provider/agent/flow/etc. |
| extract API/SDK candidates | V21.4 | typed surfaces/contracts |
| delete migrated source subtrees | V21.5 | staged deletion |
| prevent source recreation | V21.6 | absence guardrail |

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f docs/cli/legacy-source-quarantine.md` | pass | new doc |
| api | `test -f docs/waves/v21-2-cli-legacy-source-quarantine.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | available |
| cli | `cargo fmt --check` | pass | required because CLI docs/source docs touched |
| cli | `cargo test` | pass | required because CLI docs/source docs touched |
| cli | `cargo build` | pass | required because CLI docs/source docs touched |
| cli | quarantine inspection commands | pass | `source/` present; quarantine wording verified |
| yai | `make info` | not run | broader references recorded from inspection; `yai` not edited |
| yai | `make yai` | not run | `yai` not edited |
| sdk | validation | not run | untouched |
| loom | validation | not run | untouched |

## Findings

### Finding A - source/ Is Quarantined

Record:
`cli/source/` is now explicitly legacy, non-canonical, and extraction-only.

### Finding B - New Dependencies Are Forbidden

Record:
Rust `src/`, tests, and Cargo build metadata must not gain new dependencies on
`source/`.

### Finding C - Broader Build References Remain

Record:
Any existing `yai/Makefile` reference remains recorded and must be handled in
V21.3/V21.5.

### Finding D - Deletion Is Still Staged

Record:
No files are deleted in V21.2; deletion begins only after extraction.

## V21.2 Completion Checklist

* [x] `docs/cli/legacy-source-quarantine.md` exists
* [x] `docs/waves/v21-2-cli-legacy-source-quarantine.md` exists
* [x] `source/` marked non-canonical
* [x] `source/` marked extraction-only
* [x] new dependency rule documented
* [x] stale `source/README.md` path fixed or residual recorded
* [x] broader `yai/Makefile` references recorded
* [x] no `source/` files deleted
* [x] no `source/` files moved
* [x] no behavior changed
* [x] no new Rust dependency on `source/`
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched

## Pass Criteria

* V21.2 report exists
* quarantine policy exists
* `source/` is explicitly non-canonical and extraction-only
* no files are deleted or moved
* no new dependencies are added
* validation results are recorded truthfully

## Fail Criteria

* V21.2 deletes C source
* V21.2 moves C source
* V21.2 changes CLI/runtime behavior
* V21.2 treats legacy C as canonical CLI
* V21.2 adds Rust dependency on `source/`
* V21.2 hides broader build references
* V21.2 edits unrelated files
