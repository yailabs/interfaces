# V50.8 — Capability Command Recovery / Backend Surface Rehydration

## Status

* Delivery: V50.8
* Status: done
* Track: V — CLI/API/SDK/runtime command canon
* Repo branch: `refoundation/phase-01`
* Repo change type: docs-only command capability recovery and lifecycle reconstruction
* Previous delivery: V50.7 — CLI / TUI Command Projection Contract
* Next delivery: V51 — API Registry Refactor

## Purpose

Recover the full command lifecycle for capability families that had become too
shallow in earlier flat audits and projection-only documents.

## Scope

Record:

* lifecycle recovery for `provider`, `model`, `agent`, `workflow`, `job`,
  `skills`, `knowledge`, `state`, `lineage`, `records`, `evidence`,
  `materialize`, `intake`, `query`, `logs`, and runtime/system diagnostics
* backend surface rehydration using verified `api`, `sdk`, `yai`, `cli`, and
  `loom` anchors
* explicit statement that `list/status/readiness` is not sufficient lifecycle
  recovery
* required pointers from V50.6 and V50.7 into the V50.8 recovery doc
* no CLI, TUI, SDK, API, or runtime behavior implementation
* CLI source absence verification

## Files Changed

| File | Change |
| ---- | ------ |
| `api/Documentation/cli/capability-command-recovery.md` | created |
| `api/Documentation/cli/canonical-yai-command-system.md` | updated with V50.8 lifecycle-depth pointer and final-decision note |
| `api/Documentation/cli/cli-tui-command-projection-contract.md` | updated with capability lifecycle coverage rule and V50.8 pointer |
| `api/Documentation/waves/v50-8-capability-command-recovery.md` | created |

## Recovery Summary

| Family cluster | Recovery outcome |
| -------------- | ---------------- |
| provider/model | recovered as inspect/check/run/gate families, not list/status only |
| agent/workflow/job | recovered as full governed execution families with watch/evidence/lineage/cancel/explain depth |
| skills | recovered as registry/routing/admissibility family, not list/inspect only |
| materialize/intake | recovered as plan/run/status/outputs families |
| knowledge/state/lineage/records/evidence | recovered as deeper data-and-aftermath families, not static nouns |
| query/logs | root forms remain too vague; recovery is scoped rather than root revival |
| runtime/system diagnostics | recovered as inspect/check/watch/explain diagnostic family; lifecycle control remains forbidden |

## Repo Evidence

| Repo | Key evidence used |
| ---- | ----------------- |
| `api` | execution boundary docs, runtime gate registry, runtime readiness projection, and existing CLI/TUI canon docs |
| `sdk` | `operations.ts`, `workflow.ts`, `state.ts`, `knowledge.ts` showing deeper canonical operations |
| `yai` | controlled-act lifecycle, flow model header, materialization runtime, workflow readiness slice, state materialization direct-cut audit |
| `cli` | `MIGRATION_MAP.md` and `src/sdk/runtime.rs` proving current public slice remains shallow |
| `loom` | command registry/palette/screen audit confirming TUI projection exists but is not the canonical primitive |

## CLI Source Absence Check

```text
cli/source/ exists: no
full absence guardrail active: yes
Rust src/ is the only CLI implementation: yes
```

## Validation

| Repo | Command | Result |
| ---- | ------- | ------ |
| `api` | `test -f Documentation/cli/capability-command-recovery.md` | pass |
| `api` | `test -f Documentation/cli/canonical-yai-command-system.md` | pass |
| `api` | `test -f Documentation/cli/cli-tui-command-projection-contract.md` | pass |
| `api` | `test -f Documentation/waves/v50-8-capability-command-recovery.md` | pass |
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

## Completion Checklist

* [x] `Documentation/cli/capability-command-recovery.md` exists
* [x] `Documentation/waves/v50-8-capability-command-recovery.md` exists
* [x] `canonical-yai-command-system.md` updated with V50.8 pointer
* [x] `cli-tui-command-projection-contract.md` updated with lifecycle coverage rule
* [x] capability families reconstructed beyond readiness/list/status
* [x] backend surface rehydration documented truthfully
* [x] no CLI behavior implemented
* [x] no TUI behavior implemented
* [x] no API registry refactor performed
* [x] no SDK/runtime behavior implemented
* [x] CLI source absence guard remains passing
* [x] unrelated working-tree changes left untouched
