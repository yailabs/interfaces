# Residual Domain Source Deletion Pass

## Status

* Delivery: V21.7
* Status: active deletion pass
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Purpose

Delete deletion-ready residual `source/cmd` domain families after extraction.

## Deleted Areas

| Deleted path | Reason | Prior extraction artifact |
| ------------ | ------ | ------------------------- |
| `source/cmd/runtime` | runtime status/control wrapper family was extraction-covered, had no active Rust/Cargo dependency, and had no active `yai/Makefile` file-level dependency | `docs/cli/legacy-runtime-core-extraction.md`, `docs/cli/legacy-api-sdk-surface-extraction.md` |
| `source/cmd/provider` | provider wrapper family was extraction-covered and not needed by active build/test paths | `docs/cli/legacy-runtime-core-extraction.md`, `docs/cli/legacy-api-sdk-surface-extraction.md` |
| `source/cmd/agent` | agent wrapper family was extraction-covered and not needed by active build/test paths | `docs/cli/legacy-runtime-core-extraction.md`, `docs/cli/legacy-api-sdk-surface-extraction.md` |
| `source/cmd/govern` | governance wrapper family was extraction-covered and not needed by active build/test paths | `docs/cli/legacy-runtime-core-extraction.md`, `docs/cli/legacy-api-sdk-surface-extraction.md` |
| `source/cmd/analytics` | thin derived wrapper family was extraction-covered and not needed by active build/test paths | `docs/cli/legacy-runtime-core-extraction.md`, `docs/cli/legacy-api-sdk-surface-extraction.md` |
| `source/cmd/logs` | receipt-tail wrapper family was extraction-covered and not needed by active build/test paths | `docs/cli/legacy-runtime-core-extraction.md`, `docs/cli/legacy-api-sdk-surface-extraction.md` |
| `source/cmd/session` | legacy non-canonical compatibility family was no longer needed by active build/test paths | `docs/cli/legacy-api-sdk-surface-extraction.md` |

## Remaining Areas

| Remaining path | Reason retained | Future action |
| -------------- | --------------- | ------------- |
| `source/main.c` | residual entrypoint and `yai/Makefile` sentinel still present | V21.8 entrypoint/sentinel removal decision |
| `source/cmd/flow` | blocked heavy semantic area from V21.3/V21.4 | V21.8 or follow-up after explicit blocker resolution |
| `source/cmd/knowledge` | blocked heavy semantic area from V21.3/V21.4 | V21.8 or follow-up after explicit blocker resolution |
| `source/cmd/case` | heavy partial case/query surface retained for later focused deletion | V21.8 or follow-up |
| `source/assets/shell` | legacy shell assets not yet proven deletion-ready | V21.8 or follow-up |
| `source/cmd/ai` | non-target residual compatibility family not evaluated for deletion in V21.7 | later focused cleanup |
| `source/cmd/inspect` | non-target residual compatibility family not evaluated for deletion in V21.7 | later focused cleanup |
| `source/cmd/models` | non-target residual compatibility family not evaluated for deletion in V21.7 | later focused cleanup |
| `source/cmd/query` | non-target residual compatibility family not evaluated for deletion in V21.7 | later focused cleanup |
| `source/cmd/skills` | non-target residual compatibility family not evaluated for deletion in V21.7 | later focused cleanup |
| `source/cmd/dispatch.c` and `source/cmd/root.h` | residual command glue not evaluated for deletion in V21.7 | later focused cleanup |
| `source/README.md` and `source/MIGRATION_MAP.md` | local quarantine/historical residue while `source/` still exists | remove when full source tree is removed |

## Guardrail Expansion

| Deleted path | Guarded against recreation |
| ------------ | -------------------------- |
| `source/out` | yes |
| `source/shared` | yes |
| `source/cmd/runtime` | yes |
| `source/cmd/provider` | yes |
| `source/cmd/agent` | yes |
| `source/cmd/govern` | yes |
| `source/cmd/analytics` | yes |
| `source/cmd/logs` | yes |
| `source/cmd/session` | yes |

## Full Absence Status

```text
source/ fully removed: no
full absence guardrail active: no
```
