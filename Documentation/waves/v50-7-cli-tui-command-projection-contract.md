# V50.7 — CLI / TUI Command Projection Contract

## Status

* Delivery: V50.7
* Status: done
* Track: V — CLI/API/SDK/runtime/TUI command canon
* Repo branch: `refoundation/phase-01`
* Repo change type: docs-only command/action projection contract
* Previous delivery: V50.6 — Canonical YAI Command System
* Next delivery: V51 — API Registry Refactor

## Purpose

V50.7 defines the shared projection contract so that CLI commands, Loom/TUI
actions, SDK methods, API operations, and runtime action keys all project from
the same canonical primitive: `action_id`.

V50.6 remains the command-system and operational-cycle document.
V50.7 adds the explicit projection layer that V50.6 was still missing.

## Scope

Record:

* canonical primitive is `action_id`
* CLI commands are projections, not the source of truth
* TUI actions/menus/panels are projections, not the source of truth
* shared descriptor fields defined
* shared CLI/TUI action matrix defined
* TUI locations and interaction kinds defined
* command palette model defined
* shared output contract defined
* forbidden TUI actions defined
* cross-repo projection anchors recorded
* no CLI behavior implemented
* no TUI behavior implemented
* no API registry refactor performed
* no SDK/runtime behavior implemented
* CLI source absence verified

## Files Changed

| Repo | File | Change |
| ---- | ---- | ------ |
| `api` | `Documentation/cli/cli-tui-command-projection-contract.md` | created |
| `api` | `Documentation/cli/canonical-yai-command-system.md` | updated with CLI/TUI projection pointer |
| `api` | `Documentation/waves/v50-7-cli-tui-command-projection-contract.md` | created |

## Repos Audited

| Repo | Branch | Surfaces audited | Key finding |
| ---- | ------ | ---------------- | ----------- |
| `api` | `refoundation/phase-01` | `docs`, `registry`, `schemas`, `fixtures`, `conformance` | `api` already had the conceptual bridge for V50.7: `command-projection-model.md`, `api-operation-model.md`, projection-aware operation schema fields, and operation-composition seeds. |
| `cli` | `refoundation/phase-01` | `src`, `tests`, `docs`, `README.md`, `MIGRATION_MAP.md` | Current Rust CLI still mixes canonical commands, compatibility aliases, UX-only shell actions, and placeholder families; it needed a deeper projection contract instead of another flat command table. |
| `sdk` | `refoundation/phase-01` | `README.md`, `docs`, `packages` | SDK already exposes richer typed families and canonical API-present operation ids than the current CLI string surface, confirming that command strings cannot be the primitive. |
| `yai` | `refoundation/phase-01` | `README.md`, `Documentation`, `state`, `packaging`, `tests`, `Makefile` | `yai` contains the deeper authority model: `operation -> case_action -> controlled_act`, plus state/lineage/materialization/projection boundaries that action descriptors must preserve. |
| `loom` | `refoundation/phase-01` | `README.md`, `docs`, `src` | Loom already behaves like a projection consumer: slash-command registry, command palette, disabled/unavailable reasons, login shell/account gate, and client shell/runtime posture views. |

## Canonical Projection Decisions

* `action_id` is the canonical primitive.
* CLI command strings are projections.
* TUI labels, panels, menus, and palette entries are projections.
* API operations remain transport contracts, not domain ownership.
* SDK methods remain typed consumption surfaces, not domain ownership.
* runtime action keys remain runtime-local identifiers and should only be filled
  when verified.
* shared output truth is one envelope shape rendered differently by CLI and TUI.

## Loom / TUI Alignment Notes

The Loom audit gave concrete support for the V50.7 model:

* `loom/src/command/registry.rs` already models command id, route, availability,
  effect, confirmation, and backend dependency.
* `loom/src/tui/overlays/palette.rs` already shows visible-but-disabled command
  entries with explicit reasons.
* `loom/src/tui/screens/login.rs` already acts like an `auth_panel` /
  `account_panel` projection.
* `loom/src/tui/screens/client_shell.rs` already acts like a `home` /
  `runtime_panel` / `operator_context` overview.

This means Loom should not invent a separate TUI-only command domain; it should
consume the shared action descriptor model.

## CLI Source Absence Check

```text
cli/source/ exists: no
full absence guardrail active: yes
Rust src/ is the only CLI implementation: yes
```

## Validation

| Repo | Command | Result |
| ---- | ------- | ------ |
| `api` | `test -f Documentation/cli/cli-tui-command-projection-contract.md` | pass |
| `api` | `test -f Documentation/cli/canonical-yai-command-system.md` | pass |
| `api` | `test -f Documentation/waves/v50-7-cli-tui-command-projection-contract.md` | pass |
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

CLI validation note:

* `cargo test` and `cargo build` pass with pre-existing Rust warnings about
  unused fields/variants in CLI compatibility/help surfaces. No new CLI code was
  added in V50.7.

## Completion Checklist

* [x] `Documentation/cli/cli-tui-command-projection-contract.md` exists
* [x] `Documentation/cli/canonical-yai-command-system.md` updated with CLI/TUI projection pointer
* [x] `Documentation/waves/v50-7-cli-tui-command-projection-contract.md` exists
* [x] canonical primitive is `action_id`
* [x] CLI commands documented as projections
* [x] TUI actions documented as projections
* [x] TUI locations and interaction kinds defined
* [x] command palette model defined
* [x] shared output contract defined
* [x] forbidden TUI actions defined
* [x] action families mapped
* [x] no CLI behavior implemented
* [x] no TUI behavior implemented
* [x] no API registry refactor performed
* [x] no SDK/runtime behavior implemented
* [x] CLI source absence verified
