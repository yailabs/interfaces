# V21.6 - CLI Source Dependency / Recreation Guardrail

## Status

* Delivery: V21.6
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: guardrail script/check + documentation/report
* Previous delivery: V21.5 - Legacy Source Deletion Pass
* Next delivery: V21.7 - Residual Domain Source Deletion Pass

## Purpose

V21.6 adds a partial guardrail after the first deletion pass.

## Scope

* deleted subtrees guarded against recreation;
* new Rust/Cargo/test dependencies on `source/` blocked;
* remaining source residuals recorded;
* full source absence not claimed yet;
* no behavior changed.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `docs/cli/legacy-source-guardrail.md` | create | partial guardrail model |
| api | `docs/waves/v21-6-cli-source-dependency-recreation-guardrail.md` | create | delivery report |
| cli | `scripts/check-no-source-dependency.sh` | create | source dependency/recreation guard |
| cli | `MIGRATION_MAP.md` | update | document guardrail path |

## Guardrail Coverage

| Guard | Status | Notes |
| ----- | ------ | ----- |
| block `source/out` recreation | implemented | shell check fails if directory exists |
| block `source/shared` recreation | implemented | shell check fails if directory exists |
| block Cargo dependency on `source/` | implemented | `rg` scan over `Cargo.toml` |
| block Rust `src/` dependency on `source/` | implemented | `rg` scan over `src` |
| block Rust tests dependency on `source/` | implemented | `rg` scan over `tests` |
| block docs historical references | no | docs may reference quarantine |
| block all `source/` existence | no | residual source still exists |

## Remaining Residuals

| Remaining path | Reason retained | Future wave |
| -------------- | --------------- | ----------- |
| `source/main.c` | residual entrypoint and Makefile sentinel | V21.7/V21.8 |
| `source/cmd/runtime` | partial residual runtime family | V21.7 |
| `source/cmd/provider` | partial residual provider family | V21.7 |
| `source/cmd/agent` | partial residual agent family | V21.7 |
| `source/cmd/flow` | heavy semantic area | V21.7 |
| `source/cmd/govern` | partial residual governance family | V21.7 |
| `source/cmd/knowledge` | heavy semantic area | V21.7 |
| `source/cmd/analytics` | partial residual analytics family | V21.7 |
| `source/cmd/logs` | partial residual logs family | V21.7 |
| `source/cmd/case` | heavy semantic area | V21.7 |
| `source/cmd/session` | non-canonical compatibility residue | V21.7/V21.8 |
| `source/assets/shell` | residual shell UX assets | V21.7/V21.8 |

## Full Absence Status

```text
source/ fully removed: no
full absence guardrail active: no
partial dependency/recreation guardrail active: yes
```

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f docs/cli/legacy-source-guardrail.md` | pass | new doc |
| api | `test -f docs/waves/v21-6-cli-source-dependency-recreation-guardrail.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | if available |
| api | `git diff --check` | pass | required |
| cli | `scripts/check-no-source-dependency.sh` | pass | required |
| cli | `cargo fmt --check` | pass | required |
| cli | `cargo test` | pass | required |
| cli | `cargo build` | pass | required |
| cli | `git diff --check` | pass | required |
| cli | post-guard source inspection | pass | remaining source recorded; `source/out` and `source/shared` still absent |
| yai | `make info` | pass | relevant verification |
| yai | `make yai` | pass | relevant verification |
| yai | `git diff --check` | not run | not touched in V21.6 |
| sdk | `git diff --check` | not run | not touched |
| loom | `git diff --check` | not run | not touched |

## Findings

### Finding A - Partial Guardrail Exists

V21.6 prevents recreation of deleted subtrees and new Rust/Cargo/test
dependencies on `source/`.

### Finding B - Full Absence Is Not Yet True

Because residual `source/` remains, V21.6 is not the final source absence
guardrail.

### Finding C - Residual Deletion Must Continue

Remaining command families need another deletion pass.

### Finding D - V21.7 Can Delete Residual Domains

V21.7 should focus on deleting or shrinking residual command families now that
extraction artifacts exist.

## V21.6 Completion Checklist

* [x] `docs/cli/legacy-source-guardrail.md` exists
* [x] `docs/waves/v21-6-cli-source-dependency-recreation-guardrail.md` exists
* [x] guardrail check exists
* [x] guardrail blocks `source/out` recreation
* [x] guardrail blocks `source/shared` recreation
* [x] guardrail blocks Cargo dependency on `source/`
* [x] guardrail blocks Rust `src/` dependency on `source/`
* [x] guardrail blocks Rust tests dependency on `source/`
* [x] full source absence not falsely claimed
* [x] remaining residuals recorded
* [x] no behavior changed
* [x] no source files moved
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
