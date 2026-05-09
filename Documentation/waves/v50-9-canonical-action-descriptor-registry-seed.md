# V50.9 — Canonical Action Descriptor Registry Seed

## Status

* Delivery: V50.9
* Status: done
* Track: V — CLI/API/SDK/runtime/TUI action canon
* Repo branch: `refoundation/phase-01`
* Repo change type: docs + JSON registry seed only
* Previous delivery: V50.8 — Capability Command Recovery
* Next delivery: V50.10 — Command System Refactor Readiness

## Purpose

Create the first canonical `action_id` registry seed so CLI, Loom/TUI, SDK,
API, and runtime-aligned action surfaces all project from the same primitive.

## Scope

Record:

* a first canonical `action_id` registry seed in prose and JSON
* lifecycle-shaped action coverage rather than shallow `list/status` recovery
* family coverage across CLI, TUI, SDK, API, and runtime candidates
* explicit legacy alias mapping and forbidden-root representation
* pointer updates from V50.6, V50.7, and V50.8 into the registry seed
* no CLI, TUI, SDK, API, or runtime behavior implementation
* CLI source absence verification

## Files Changed

| File | Change |
| ---- | ------ |
| `api/Documentation/cli/canonical-action-descriptor-registry.md` | created |
| `api/registry/yai-actions.v1.json` | created |
| `api/Documentation/waves/v50-9-canonical-action-descriptor-registry-seed.md` | created |
| `api/Documentation/cli/canonical-yai-command-system.md` | updated with V50.9 registry pointer |
| `api/Documentation/cli/cli-tui-command-projection-contract.md` | updated with registry-seed extension |
| `api/Documentation/cli/capability-command-recovery.md` | updated to point recovered lifecycle slices into V50.9 |

## Seed Summary

| Registry property | Outcome |
| ----------------- | ------- |
| canonical primitive | `action_id` |
| machine-readable seed | `api/registry/yai-actions.v1.json` |
| lifecycle vocabulary attached | yes |
| CLI projections attached | yes |
| TUI projections attached | yes |
| API operation candidates attached | yes |
| SDK surface candidates attached | yes |
| runtime action key candidates attached where verified | yes |
| legacy aliases represented | yes |
| forbidden actions represented | yes |

## Repo Evidence

| Repo | Key evidence used |
| ---- | ----------------- |
| `api` | `registry/api-operations.v1.json`, `registry/api-operation-projections.v1.json`, execution docs, runtime gate fixtures, existing V50.6/V50.7/V50.8 docs |
| `cli` | `MIGRATION_MAP.md`, help registry, runtime/session/provider/models compatibility wording |
| `sdk` | `README.md`, Rust `surfaces/system.rs`, `surfaces/providers.rs`, `surfaces/models.rs`, TS `surfaces/workflow.ts`, `surfaces/agents.ts`, `surfaces/providers.ts`, `surfaces/models.ts` |
| `yai` | controlled-act lifecycle docs, `include/orchestration/flow.h`, `state/materialization/materialize_runtime.c` |
| `loom` | command registry and palette/screen anchors proving TUI is a projection, not a primitive |

## CLI Source Absence Check

```text
cli/source/ exists: no
full absence guardrail active: yes
Rust src/ is the only CLI implementation: yes
```

## Validation

| Repo | Command | Result |
| ---- | ------- | ------ |
| `api` | `test -f Documentation/cli/canonical-action-descriptor-registry.md` | pass |
| `api` | `test -f Documentation/waves/v50-9-canonical-action-descriptor-registry-seed.md` | pass |
| `api` | `test -f registry/yai-actions.v1.json` | pass |
| `api` | `python3 -m json.tool registry/yai-actions.v1.json >/dev/null` | pass |
| `api` | `python3 conformance/check_api_contracts.py` | pass |
| `api` | `git diff --check` | pass |
| `cli` | `test ! -e source` | pass |
| `cli` | `scripts/check-no-source-dependency.sh` | pass |
| `cli` | `cargo fmt --check` | pass |
| `cli` | `cargo test` | pass |
| `cli` | `cargo build` | pass |
| `cli` | `git diff --check` | pass |
| `yai` | `make info` | pass |
| `yai` | `make yai` | pass |
| `yai` | `git diff --check` | pass |
| `sdk` | `git diff --check` | pass |
| `loom` | `git diff --check` | pass |

## Notes

* `api/conformance/check_yai_actions_registry.py` was not created in V50.9.
  The registry seed is validated through `python3 -m json.tool` and bounded by
  the existing `check_api_contracts.py` pass.
* `cli` validation still emits pre-existing Rust warnings in compatibility/help
  surfaces, but all required checks passed without code changes in this wave.

## Completion Checklist

* [x] `Documentation/cli/canonical-action-descriptor-registry.md` exists
* [x] `registry/yai-actions.v1.json` exists
* [x] `Documentation/waves/v50-9-canonical-action-descriptor-registry-seed.md` exists
* [x] `canonical-yai-command-system.md` updated with V50.9 pointer
* [x] `cli-tui-command-projection-contract.md` updated with registry-seed note
* [x] `capability-command-recovery.md` updated with registry-seed implication
* [x] JSON registry validated
* [x] validation results recorded truthfully
* [x] no CLI behavior implemented
* [x] no TUI behavior implemented
* [x] no API registry refactor performed
* [x] no SDK/runtime behavior implemented
* [x] CLI source absence guard remains passing
* [x] unrelated working-tree changes left untouched
