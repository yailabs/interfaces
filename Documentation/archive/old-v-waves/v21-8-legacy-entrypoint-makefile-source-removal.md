# V21.8 - Legacy Entrypoint / Makefile Source Removal

## Status

* Delivery: V21.8
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: legacy entrypoint/source-sentinel deletion + Makefile reference cleanup + documentation/report
* Previous delivery: V21.7 - Residual Domain Source Deletion Pass
* Next delivery: V21.9 - Final CLI Source Absence Guardrail

## Purpose

V21.8 removes the legacy entrypoint/sentinel and remaining Makefile source
anchors where safe.

## Scope

* entrypoint/sentinel readiness confirmed;
* Makefile references inspected;
* deletion-ready residual files/subtrees deleted;
* build references updated;
* guardrail expanded;
* full absence status recorded;
* no behavior change intended.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `Documentation/cli/legacy-entrypoint-makefile-source-removal.md` | create | entrypoint/source removal record |
| api | `Documentation/waves/v21-8-legacy-entrypoint-makefile-source-removal.md` | create | delivery report |
| cli | `source/main.c` | delete | deletion-ready entrypoint sentinel |
| cli | `source/cmd/ai` | delete | obsolete compatibility family |
| cli | `source/cmd/query` | delete | obsolete compatibility shim |
| cli | `source/cmd/dispatch.c` | delete | orphaned residual glue after entrypoint removal |
| cli | `scripts/check-no-source-dependency.sh` | update | block recreation of newly deleted paths |
| cli | `MIGRATION_MAP.md` | update | reflect expanded guardrail coverage |
| yai | `Makefile` | update | remove `CLI_SOURCE`, `source/main.c`, and shell-theme Makefile anchors |

## Deletion Decision

| Legacy area | Active build reference? | Deletion-ready? | Delete in V21.8? | Reason |
| ----------- | ----------------------- | --------------- | ---------------- | ------ |
| `source/main.c` | yes | yes | yes | only active role was the residual `yai/Makefile` sentinel/entrypoint anchor; useful semantics were already extracted in V21.3/V21.4 |
| `source/assets/shell` | yes | no | no | blocked by `yai/tests/harness/yai/test_cli_surface_contract.sh` even after Makefile cleanup |
| `source/cmd/dispatch.c` | no | yes | yes | orphaned legacy dispatcher once `source/main.c` is removed; no active Rust/Cargo/Makefile dependency |
| `source/cmd/root.h` | no | no | no | still included by retained residual families |
| `source/cmd/ai` | no | yes | yes | compatibility-only removed-command wrapper; no active dependency |
| `source/cmd/inspect` | no | no | no | still contains runtime inspection wrapper logic not explicitly drained in this wave |
| `source/cmd/models` | no | no | no | still contains non-trivial model surface wrapper logic not explicitly drained in this wave |
| `source/cmd/query` | no | yes | yes | compatibility shim with no active dependency and no remaining ownership value |
| `source/cmd/skills` | no | no | no | thin residual family but not explicitly drained or validated for deletion in V21.8 |
| `source/cmd/flow` | no | no | no | heavy blocked semantic area from V21.3/V21.4 |
| `source/cmd/knowledge` | no | no | no | heavy blocked semantic area from V21.3/V21.4 |
| `source/cmd/case` | no | no | no | heavy partial surface and still contains direct shell-asset path assumptions |
| `source/README.md` | no | no | no | useful quarantine banner while residual source remains |
| `source/MIGRATION_MAP.md` | no | no | no | local historical residue retained until final source removal |

## Deleted Paths

| Deleted path | Reason | Validation |
| ------------ | ------ | ---------- |
| `cli/source/main.c` | residual sentinel/entrypoint anchor removed after Makefile cleanup | file absent after deletion; guardrail blocks recreation |
| `cli/source/cmd/ai` | obsolete compatibility-only wrapper family | subtree absent after deletion; guardrail blocks recreation |
| `cli/source/cmd/query` | obsolete compatibility shim family | subtree absent after deletion; guardrail blocks recreation |
| `cli/source/cmd/dispatch.c` | orphaned legacy central dispatcher | file absent after deletion; guardrail blocks recreation |

## Remaining Residuals

| Remaining path | Reason retained | Future wave |
| -------------- | --------------- | ----------- |
| `cli/source/assets/shell` | retained by test harness reference to `yai-top-render.py` | V21.9/follow-up |
| `cli/source/cmd/flow` | blocked semantic mass | V21.9/follow-up |
| `cli/source/cmd/knowledge` | blocked semantic mass | V21.9/follow-up |
| `cli/source/cmd/case` | heavy partial case/query surface | V21.9/follow-up |
| `cli/source/cmd/inspect` | runtime inspection wrapper residue | V21.9/follow-up |
| `cli/source/cmd/models` | model surface wrapper residue | V21.9/follow-up |
| `cli/source/cmd/skills` | thin residual family not yet explicitly drained | V21.9/follow-up |
| `cli/source/cmd/root.h` | shared residual glue header for retained families | V21.9/follow-up |
| `cli/source/README.md` | quarantine banner while source remains | V21.9/follow-up |
| `cli/source/MIGRATION_MAP.md` | local historical residue while source remains | V21.9/follow-up |

## Makefile Reference Cleanup

| Reference | Before | After | Result |
| --------- | ------ | ----- | ------ |
| `CLI_SOURCE` | present | absent | pass |
| `source/main.c` | present | absent | pass |
| `source/assets/shell` | present | absent | pass |
| deleted command-family paths | absent | absent | pass |
| generic `cli/source` docs references | historical/current | historical/current | historical |

## Guardrail Status

| Guard | Status | Notes |
| ----- | ------ | ----- |
| block V21.5 deleted paths | active | `source/out`, `source/shared` |
| block V21.7 deleted paths | active | residual command families deleted in V21.7 |
| block V21.8 deleted paths | active | `source/main.c`, `source/cmd/ai`, `source/cmd/query`, `source/cmd/dispatch.c` |
| block all `source/` existence | not active | residual source still exists |
| block Cargo/src/tests dependencies | active | required |

## Full Absence Status

```text
source/ fully removed: no
full absence guardrail active: no
partial guardrail active: yes
ready for V21.9 final absence guardrail: no
```

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f Documentation/cli/legacy-entrypoint-makefile-source-removal.md` | pass | new doc |
| api | `test -f Documentation/waves/v21-8-legacy-entrypoint-makefile-source-removal.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| api | `git diff --check` | pass | required |
| cli | `scripts/check-no-source-dependency.sh` | pass | required |
| cli | `cargo fmt --check` | pass | required |
| cli | `cargo test` | pass | warnings only; tests passed |
| cli | `cargo build` | pass | warnings only |
| cli | `git diff --check` | pass | required |
| cli | post-deletion source inspection | pass | `source/main.c`, `source/cmd/ai`, `source/cmd/query`, and `source/cmd/dispatch.c` absent; residual source recorded |
| cli | dependency regression scan | pass | no `Cargo.toml`/`src`/`tests` dependency on `source/` |
| yai | `make info` | pass | required |
| yai | `make yai` | pass | `Nothing to be done for 'yai'` |
| yai | `git diff --check` | pass | required |
| sdk | `git diff --check` | not run | not touched |
| loom | `git diff --check` | not run | not touched |

## Findings

### Finding A - Entrypoint Anchor Removed Or Blocked

`source/main.c` was removed after its Makefile sentinel role was eliminated.

### Finding B - Makefile Source Anchors Removed Or Narrowed

`yai/Makefile` no longer points to `CLI_SOURCE`, `source/main.c`, or
`source/assets/shell`.

### Finding C - Full Absence Status Is Truthful

V21.8 does not claim full source absence because residual source still remains.

### Finding D - V21.9 Can Enforce Absence Or Target Final Blockers

V21.9 must resolve the remaining shell-asset/test-harness blocker and the
retained residual domain families before full absence can be enforced.

## V21.8 Completion Checklist

* [x] `Documentation/cli/legacy-entrypoint-makefile-source-removal.md` exists
* [x] `Documentation/waves/v21-8-legacy-entrypoint-makefile-source-removal.md` exists
* [x] deletion decision table completed
* [x] source/main.c removed or blocker recorded
* [x] source/assets/shell removed or blocker recorded
* [x] remaining deletion-ready residuals removed
* [x] yai/Makefile source references removed or narrowed truthfully
* [x] guardrail expanded
* [x] Rust CLI cargo validation passes
* [x] yai make validation passes
* [x] no source files moved
* [x] no runtime behavior added
* [x] no API/SDK implementation added
* [x] no session canonicalization added
* [x] full absence status recorded truthfully
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
