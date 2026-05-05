# Legacy Entrypoint / Makefile Source Removal

## Status

* Delivery: V21.8
* Status: active deletion pass
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Purpose

Remove the legacy C entrypoint/sentinel and remaining Makefile source references.

## Deleted Areas

| Deleted path | Reason | Prior extraction artifact |
| ------------ | ------ | ------------------------- |
| `source/main.c` | residual Makefile sentinel/entrypoint anchor was removable after V21.3 runtime/core extraction and V21.4 API/SDK extraction preserved its useful semantics outside `cli/source/` | `docs/cli/legacy-runtime-core-extraction.md`, `Documentation/legacy-cli-runtime-core-extraction.md` |
| `source/cmd/ai` | obsolete compatibility-only family that only emitted removed-command guidance and had no active Rust/Cargo/Makefile dependency | not applicable; obsolete compatibility shim |
| `source/cmd/query` | obsolete compatibility shim routing legacy `query` into newer family owners; no active Rust/Cargo/Makefile dependency remained | not applicable; obsolete compatibility shim |
| `source/cmd/dispatch.c` | legacy central dispatcher became orphaned once the monolithic `source/main.c` entrypoint was removed | not applicable; orphaned residual glue |

## Remaining Areas

| Remaining path | Reason retained | Future action |
| -------------- | --------------- | ------------- |
| `source/assets/shell` | retained because `yai/tests/harness/yai/test_cli_surface_contract.sh` still points to `../cli/source/assets/shell/yai-top-render.py` | V21.9 or follow-up after harness/path cleanup is explicitly in scope |
| `source/cmd/flow` | heavy blocked semantic area from V21.3/V21.4 | V21.9/follow-up after explicit blocker resolution |
| `source/cmd/knowledge` | heavy blocked semantic area from V21.3/V21.4 | V21.9/follow-up after explicit blocker resolution |
| `source/cmd/case` | heavy partial case/query surface; also still contains direct shell-asset path assumptions | V21.9/follow-up after focused deletion planning |
| `source/cmd/inspect` | contains real runtime inspection wrapper logic not explicitly drained in V21.8 | later focused cleanup |
| `source/cmd/models` | contains non-trivial model surface wrapper logic not explicitly drained in V21.8 | later focused cleanup |
| `source/cmd/skills` | thin residual family, but not explicitly drained or validated for deletion in V21.8 | later focused cleanup |
| `source/cmd/root.h` | still included by retained residual command families | remove only when those residual families are removed |
| `source/README.md` | quarantine banner is still useful while residual source remains | remove when `source/` is gone |
| `source/MIGRATION_MAP.md` | local historical residue retained while `source/` still exists | remove when `source/` is gone |

## Makefile Reference Cleanup

| Reference | Before | After | Result |
| --------- | ------ | ----- | ------ |
| `CLI_SOURCE` | present | absent | removed |
| `source/main.c` sentinel | present | absent | removed |
| `source/assets/shell` | present | absent | removed from `Makefile`; residual test-harness blocker remains outside `Makefile` |
| command-family refs | absent | absent | no active `Makefile` command-family path refs remained |

## Full Absence Readiness

```text
source/ fully removed: no
ready for full absence guardrail: no
```
