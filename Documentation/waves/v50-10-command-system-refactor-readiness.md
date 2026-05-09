# V50.10 — Command System Refactor Readiness

## Status

* Delivery: V50.10
* Status: done
* Track: V — CLI/API/SDK/runtime/TUI action canon
* Repo branch: `refoundation/phase-01`
* Repo change type: docs-only cross-repo refactor readiness plan
* Previous delivery: V50.9 — Canonical Action Descriptor Registry Seed
* Next delivery: V51 — API Registry Refactor

## Purpose

Turn the V50.9 action registry seed into a verified cross-repo readiness map
for V51+.

## Scope

Record:

* the V50.9 action registry seed was consumed as the canonical input
* a cross-repo readiness matrix now classifies every seeded action by API/SDK/CLI/TUI/runtime/backend path
* V51 registry normalization scope is now explicit
* SDK readiness gaps are recorded
* CLI parser/output/test gaps are recorded
* Loom/TUI panel/action readiness is recorded
* runtime/backend reconnection gaps are recorded
* forbidden and legacy locks are recorded
* no CLI, TUI, SDK, API registry, or runtime behavior was implemented

## Files Changed

| File | Change |
| ---- | ------ |
| `api/Documentation/cli/command-system-refactor-readiness.md` | created |
| `api/Documentation/waves/v50-10-command-system-refactor-readiness.md` | created |

## Repo Evidence

| Repo | Key evidence used |
| ---- | ----------------- |
| `api` | `Documentation/cli/canonical-yai-command-system.md`, `Documentation/cli/cli-tui-command-projection-contract.md`, `Documentation/cli/capability-command-recovery.md`, `Documentation/cli/canonical-action-descriptor-registry.md`, `registry/yai-actions.v1.json`, verified `openapi/yai-api.v1.yaml` operation ids such as `workflow.list`, `workflow.runs.watch`, `providers.list`, `providers.probe`, `models.list`, `models.capabilities.show`, `knowledge.lineage.trace`, `state.records.query`, `state.records.tail`, and `agents.list` |
| `cli` | `README.md`, `MIGRATION_MAP.md`, `src/commands/auth.rs`, `src/commands/case.rs`, `src/commands/runtime.rs`, `src/commands/shell.rs`, `src/commands/session.rs`, `src/commands/provider.rs`, `src/commands/models.rs` |
| `sdk` | `README.md`, `packages/rust/src/operations.rs`, Rust client/surface modules, TypeScript `surfaces/workflow.ts`, `surfaces/control.ts`, `surfaces/governance.ts`, `surfaces/knowledge.ts`, `surfaces/providers.ts`, `surfaces/models.ts`, `surfaces/agents.ts`, and package layout showing Rust/TypeScript/C plus a currently non-verified Python surface |
| `yai` | `README.md`, `Documentation/architecture/controlled-act-lifecycle.md`, `include/orchestration/flow.h`, `state/materialization/materialize_runtime.c`, `state/substrate/lmdb_store.c`, `state/substrate/duckdb_store.c`, plus explicit working-tree drift around knowledge/lineage/materialization moves |
| `loom` | `README.md`, `src/command/registry.rs`, command palette and runtime-readiness docs proving that Loom currently projects only a small slash-command set and still needs canonical `action_id` mapping |

## Readiness Highlights

| Area | V50.10 outcome |
| ---- | -------------- |
| action registry consumed | yes |
| cross-repo readiness matrix created | yes |
| V51 API registry refactor scope prepared | yes |
| SDK readiness gaps recorded | yes |
| CLI parser/output/test gaps recorded | yes |
| Loom/TUI panel/action readiness recorded | yes |
| runtime/backend reconnection gaps recorded | yes |
| forbidden/legacy lock recorded | yes |
| test readiness matrix created | yes |

## Key Findings

* `system.status` is already the real underlying operation for the current CLI compatibility surface `yai runtime status`.
* `auth`, `case`, and `shell` already prove truthful local CLI behavior patterns and should be used as the migration standard for later families.
* `case.close` is implemented in the current Rust CLI local surface, but the V50.9 registry seed still marks it as `planned`. V51 should normalize that metadata drift.
* `provider.list` and `models.list` are real but shallow current surfaces; the rest of the provider/model lifecycle still needs registry and backend reconnection.
* `workflow`, `materialize`, `state`, and `lineage` have stronger backend/API anchors than the current CLI/TUI surfaces suggest.
* `loom` currently exposes only `/help`, `/status`, `/runtime`, `/runtime-ipc`, `/attach`, and `/detach`; almost every canonical family still needs `action_id`-backed TUI projection.
* `yai` currently has pre-existing working-tree drift around knowledge/lineage/materialization paths. V50.10 records that drift instead of pretending the backend topology is already stable.

## CLI Source Absence Check

```text
cli/source/ exists: no
full absence guardrail active: yes
Rust src/ is the only CLI implementation: yes
```

## Validation

| Repo | Command | Result |
| ---- | ------- | ------ |
| `api` | `test -f Documentation/cli/command-system-refactor-readiness.md` | pass |
| `api` | `test -f Documentation/waves/v50-10-command-system-refactor-readiness.md` | pass |
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

* `api/conformance/check_yai_actions_registry.py` is still absent. V50.10 relies on the existing V50.9 JSON validation path plus `check_api_contracts.py`.
* `cli` validation still emits pre-existing Rust warnings in compatibility/help surfaces, but all required checks passed.
* V50.10 did not update the V50.6-V50.9 source documents or the JSON registry seed because the readiness wave did not require pointer corrections.

## Completion Checklist

* [x] `Documentation/cli/command-system-refactor-readiness.md` exists
* [x] `Documentation/waves/v50-10-command-system-refactor-readiness.md` exists
* [x] action registry consumed
* [x] cross-repo readiness matrix created
* [x] V51 API registry refactor scope prepared
* [x] SDK readiness gaps recorded
* [x] CLI parser/output/test gaps recorded
* [x] Loom/TUI panel/action readiness recorded
* [x] runtime/backend reconnection gaps recorded
* [x] forbidden/legacy lock recorded
* [x] test readiness matrix created
* [x] no CLI behavior implemented
* [x] no TUI behavior implemented
* [x] no API registry refactor performed
* [x] no SDK/runtime behavior implemented
* [x] CLI source absence guard remains passing
* [x] unrelated working-tree changes left untouched
