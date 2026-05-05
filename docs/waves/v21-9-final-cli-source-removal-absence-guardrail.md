# V21.9 - Final CLI Source Removal / Absence Guardrail

## Status

* Delivery: V21.9
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: final source removal + absence guardrail + documentation/report
* Previous delivery: V21.8 - Legacy Entrypoint / Makefile Source Removal
* Next delivery: V22 - Loom Client Alignment

## Purpose

V21.9 removes final `cli/source/` residuals if safe and activates full absence
guardrail if `source/` is gone.

## Scope

* final residuals inspected;
* harness blocker closed or retained explicitly;
* remaining source files deleted or blocker recorded;
* guardrail updated;
* full absence status recorded truthfully;
* no behavior change intended.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `docs/cli/final-cli-source-removal-absence-guardrail.md` | create | final source removal record |
| api | `docs/waves/v21-9-final-cli-source-removal-absence-guardrail.md` | create | delivery report |
| cli | `source/...` | delete | final residual source deletion |
| cli | `scripts/check-no-source-dependency.sh` | update | full absence guardrail |
| cli | `README.md` | update | reflect final absence |
| cli | `MIGRATION_MAP.md` | update | reflect final absence |
| cli | `docs/migration-from-c-cli.md` | update | reflect final absence |
| yai | `tests/harness/yai/test_cli_surface_contract.sh` | update | remove `source/assets/shell` dependency |

## Deletion Decision

| Legacy area | Active reference? | Delete in V21.9? | Reason |
| ----------- | ----------------- | ---------------- | ------ |
| `source/assets/shell` | yes -> no | yes | harness blocker was safely removed; no active build/test dependency remained |
| `source/cmd/flow` | no | yes | semantics preserved in V21.3/V21.4; no active dependency remained |
| `source/cmd/knowledge` | no | yes | semantics preserved in V21.3/V21.4; no active dependency remained |
| `source/cmd/case` | no | yes | no active dependency remained after harness cleanup |
| `source/cmd/inspect` | no | yes | no active dependency remained |
| `source/cmd/models` | no | yes | no active dependency remained |
| `source/cmd/skills` | no | yes | no active dependency remained |
| `source/cmd/root.h` | no | yes | orphaned after final command-family deletion |
| `source/README.md` | no | yes | quarantine banner no longer needed once `source/` was removed |
| `source/MIGRATION_MAP.md` | no | yes | local historical residue no longer needed once `source/` was removed |

## Deleted Paths

| Deleted path | Reason | Validation |
| ------------ | ------ | ---------- |
| `cli/source/assets/shell` | legacy shell assets no longer had an active harness/build consumer | directory absent after deletion |
| `cli/source/cmd/flow` | extracted semantics preserved; no active dependency remained | directory absent after deletion |
| `cli/source/cmd/knowledge` | extracted semantics preserved; no active dependency remained | directory absent after deletion |
| `cli/source/cmd/case` | no active dependency remained | directory absent after deletion |
| `cli/source/cmd/inspect` | no active dependency remained | directory absent after deletion |
| `cli/source/cmd/models` | no active dependency remained | directory absent after deletion |
| `cli/source/cmd/skills` | no active dependency remained | directory absent after deletion |
| `cli/source/cmd/root.h` | orphaned residual header | file absent after deletion |
| `cli/source/README.md` | no longer needed after full removal | file absent after deletion |
| `cli/source/MIGRATION_MAP.md` | no longer needed after full removal | file absent after deletion |
| `cli/source/` | final residual directory removed | `test ! -e source` passes |

## Remaining Residuals

No remaining `cli/source/` paths.

## Full Absence Status

```text
source/ fully removed: yes
full absence guardrail active: yes
partial guardrail active: no
ready for V22: yes
```

## Guardrail Status

| Guard | Status | Notes |
| ----- | ------ | ----- |
| block `source/` existence | active | fails if `cli/source/` exists |
| block Cargo/src/tests dependencies | active | required |
| block deleted subtree recreation | superseded | covered by full source absence guard |
| docs historical references allowed | yes | if clearly historical |

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f docs/cli/final-cli-source-removal-absence-guardrail.md` | pass | new doc |
| api | `test -f docs/waves/v21-9-final-cli-source-removal-absence-guardrail.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| api | `git diff --check` | pass | required |
| cli | `test ! -e source` | pass | full source removal confirmed |
| cli | `scripts/check-no-source-dependency.sh` | pass | full absence guardrail active |
| cli | `cargo fmt --check` | pass | required |
| cli | `cargo test` | pass | warnings only; tests passed |
| cli | `cargo build` | pass | warnings only |
| cli | `git diff --check` | pass | required |
| cli | dependency regression scan | pass | no `Cargo.toml`/`src`/`tests` dependency on `source/` |
| yai | harness script validation | pass | `bash tests/harness/yai/test_cli_surface_contract.sh` |
| yai | `make info` | pass | required |
| yai | `make yai` | pass | validated with `make -B yai` rebuild |
| yai | `git diff --check` | pass | required |
| sdk | `git diff --check` | not run | not touched |
| loom | `git diff --check` | not run | not touched |

## Findings

### Finding A - Final Source Status Is Known

`cli/source/` is either fully removed or exact blockers remain.

### Finding B - Absence Guardrail Is Active If Possible

If source is gone, guardrail blocks source recreation.

### Finding C - Rust CLI Remains Canonical

Rust `src/` remains the only CLI implementation.

### Finding D - V22 Can Proceed Only With Truthful Source Status

Loom alignment proceeds after source absence or after final blocker is explicit.

## V21.9 Completion Checklist

* [x] `docs/cli/final-cli-source-removal-absence-guardrail.md` exists
* [x] `docs/waves/v21-9-final-cli-source-removal-absence-guardrail.md` exists
* [x] final residuals inspected
* [x] harness blocker closed or retained explicitly
* [x] remaining source deleted or exact blocker recorded
* [x] full absence status recorded truthfully
* [x] guardrail updated
* [x] Rust CLI cargo validation passes
* [x] yai make validation passes
* [x] no source files moved
* [x] no runtime behavior added
* [x] no API/SDK implementation added
* [x] no session canonicalization added
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
