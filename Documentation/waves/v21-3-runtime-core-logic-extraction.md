# V21.3 - Runtime/Core Logic Extraction

## Status

* Delivery: V21.3
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: runtime/core semantic extraction documentation + migration planning
* Previous delivery: V21.2 - CLI Legacy Source Quarantine
* Next delivery: V21.4 - API/SDK Surface Extraction

## Purpose

V21.3 extracts runtime/core/domain semantics from quarantined `cli/source/`
without deleting or moving source files.

## Scope

Record:

* legacy runtime/core areas inspected;
* useful semantics extracted to Documentation/spec artifacts;
* target owners assigned;
* deletion readiness recorded;
* no source deleted;
* no source moved;
* no behavior changed.

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `Documentation/cli/legacy-runtime-core-extraction.md` | create | extracted runtime/core semantics |
| api | `Documentation/waves/v21-3-runtime-core-logic-extraction.md` | create | delivery report |
| yai | `Documentation/legacy-cli-runtime-core-extraction.md` | create | runtime/core extraction target |

## Extraction Summary

| Legacy area | Target owner | Extracted artifact | Deletion readiness |
| ----------- | ------------ | ------------------ | ------------------ |
| `source/main.c` | `yai/core` + `api` | `Documentation/cli/legacy-runtime-core-extraction.md`, `Documentation/legacy-cli-runtime-core-extraction.md` | blocked |
| `source/shared` | `cli` | `Documentation/cli/legacy-runtime-core-extraction.md` | partial |
| `source/out` | `cli` | `Documentation/cli/legacy-runtime-core-extraction.md` | partial |
| `source/cmd/runtime` | `yai/core` + `api` | `Documentation/cli/legacy-runtime-core-extraction.md` | partial |
| `source/cmd/provider` | `api` + `sdk` + `yai/core` | `Documentation/cli/legacy-runtime-core-extraction.md` | partial |
| `source/cmd/agent` | `yai/core` + `api` + `sdk` | `Documentation/cli/legacy-runtime-core-extraction.md` | partial |
| `source/cmd/flow` | `yai/core` + `api` | `Documentation/cli/legacy-runtime-core-extraction.md`, `Documentation/legacy-cli-runtime-core-extraction.md` | blocked |
| `source/cmd/govern` | `yai/core` + `api` | `Documentation/cli/legacy-runtime-core-extraction.md` | partial |
| `source/cmd/knowledge` | `yai/core` + `api` | `Documentation/cli/legacy-runtime-core-extraction.md`, `Documentation/legacy-cli-runtime-core-extraction.md` | blocked |
| `source/cmd/analytics` | `api` + `sdk` + `yai/core` | `Documentation/cli/legacy-runtime-core-extraction.md` | partial |
| `source/cmd/logs` | `yai/core` + `api` + `sdk` | `Documentation/cli/legacy-runtime-core-extraction.md` | partial |

## Deletion Readiness

Record:

* `source/shared` and `source/out` are semantically close to disposable, but
  still wait on broader build-reference cleanup in V21.5.
* `source/cmd/provider`, `source/cmd/govern`, `source/cmd/runtime`,
  `source/cmd/agent`, `source/cmd/analytics`, and `source/cmd/logs` are
  partially documented now, but still need typed API/SDK extraction in V21.4.
* `source/main.c`, `source/cmd/flow`, and `source/cmd/knowledge` remain blocked
  because they still carry dense runtime/core/state/lineage/governance
  semantics.
* `yai/Makefile` build references remain recorded and unchanged; V21.3 does not
  hide them.

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f Documentation/cli/legacy-runtime-core-extraction.md` | pass | new extraction doc |
| api | `test -f Documentation/waves/v21-3-runtime-core-logic-extraction.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | available |
| yai | `test -f Documentation/legacy-cli-runtime-core-extraction.md` | pass | new core extraction doc |
| yai | `make info` | pass | `yai` doc touched |
| yai | `make yai` | pass | `yai` doc touched |
| cli | source inspection commands | pass | runtime/core source families inspected and cross-checked |
| cli | `cargo fmt --check` | pass | validation run even though CLI code was unchanged |
| cli | `cargo test` | pass | warnings only |
| cli | `cargo build` | pass | warnings only |
| sdk | validation | not run | untouched |
| loom | validation | not run | untouched |

## Findings

### Finding A - Runtime/Core Semantics Extracted

Record:
Useful runtime/core semantics have been preserved outside the CLI source tree.

### Finding B - CLI Does Not Own These Domains

Record:
Runtime, provider, agent, flow, governance, knowledge, analytics, logs/records
and state/control semantics do not belong in CLI implementation.

### Finding C - Deletion Readiness Is Now Visible

Record:
Each reviewed area has a deletion readiness classification.

### Finding D - V21.4 Can Extract API/SDK Surfaces

Record:
Concepts requiring typed contracts or client surfaces move to V21.4.

## V21.3 Completion Checklist

* [x] `Documentation/cli/legacy-runtime-core-extraction.md` exists
* [x] `Documentation/waves/v21-3-runtime-core-logic-extraction.md` exists
* [x] `yai/Documentation/legacy-cli-runtime-core-extraction.md` exists
* [x] runtime/core legacy areas inspected
* [x] semantics extracted into Documentation/spec artifacts
* [x] target owners assigned
* [x] deletion readiness recorded
* [x] no source files deleted
* [x] no source files moved
* [x] no behavior changed
* [x] no runtime implementation added
* [x] no API/SDK implementation added
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched

## Pass Criteria

* V21.3 report exists
* runtime/core extraction docs exist
* reviewed legacy areas have target owners and deletion readiness
* useful semantics are preserved outside `cli/source/`
* no files are deleted or moved
* no behavior changes are introduced

## Fail Criteria

* V21.3 deletes legacy source
* V21.3 moves legacy source
* V21.3 implements runtime/provider/agent/flow behavior
* V21.3 treats CLI as owner of runtime/core domains
* V21.3 hides unknowns
* V21.3 edits unrelated files
