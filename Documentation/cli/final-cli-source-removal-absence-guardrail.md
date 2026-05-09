# Final CLI Source Removal / Absence Guardrail

## Status

* Delivery: V21.9
* Status: final removal attempt / absence guardrail
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Purpose

Remove the final `cli/source/` residuals and enforce absence if possible.

## Deleted Areas

| Deleted path | Reason |
| ------------ | ------ |
| `source/assets/shell` | harness dependency was removed from `yai/tests/harness/yai/test_cli_surface_contract.sh`, so legacy shell assets no longer had an active runtime/build/test consumer |
| `source/cmd/flow` | runtime/core and API/SDK semantics were already extracted in V21.3/V21.4, and no active Cargo/Rust/Makefile/harness dependency remained |
| `source/cmd/knowledge` | heavy semantic area had already been preserved in extraction artifacts; no active build/test dependency remained |
| `source/cmd/case` | no active build/harness dependency remained after shell-asset blocker closure |
| `source/cmd/inspect` | legacy inspect wrapper family had no active build/test dependency |
| `source/cmd/models` | legacy models wrapper family had no active build/test dependency |
| `source/cmd/skills` | thin residual family had no active build/test dependency |
| `source/cmd/root.h` | shared residual header became orphaned after final command-family deletion |
| `source/README.md` | quarantine banner no longer needed after full source removal |
| `source/MIGRATION_MAP.md` | local historical residue no longer needed after full source removal |
| `source/` | directory removed after final residual deletion |

## Remaining Areas

No `cli/source/` residuals remain.

## Active Reference Cleanup

| Reference | Before | After | Result |
| --------- | ------ | ----- | ------ |
| yai harness `source/assets/shell` reference | present | absent | pass |
| yai Makefile source refs | absent | absent | pass |
| Rust Cargo/src/tests source refs | absent | absent | pass |
| docs source refs | historical/current | historical/current | historical |

## Guardrail

```text
full absence guardrail active: yes
cli/source/ must not exist.
```
