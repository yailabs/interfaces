# V50.6 — Canonical YAI Command System

## Status

* Delivery: V50.6
* Status: done
* Track: V — CLI/API/SDK/runtime command canon
* Repo branch: `refoundation/phase-01`
* Repo change type: docs-only system command reconstruction
* Previous delivery: V50.5 — Canonical CLI Command Surface Audit
* Next delivery: V51 — API Registry Refactor

## Purpose

V50.6 reconstructs the canonical YAI command system as an operational system,
not a flat CLI inventory.

The authoritative source of truth is now:

* `api/Documentation/cli/canonical-yai-command-system.md`

V50.5 remains a preliminary flat inventory only.

## Scope

Record:

* operational cycle mapped
* command-system layers defined
* state / knowledge / lineage / materialization command groups reconstructed
* SHM / LMDB / DuckDB / Ladybug audited and classified
* policy-pack / intake / materialization flow restored
* governance / policy / control boundaries defined
* provider / model / agent / workflow / job command groups rebuilt
* too-vague root commands classified
* lost legacy capabilities mapped to new canonical owners
* API / SDK / CLI / runtime / Loom divergence recorded
* no CLI behavior implemented
* no API registry refactor performed
* no SDK/runtime behavior implemented
* CLI source absence verified

## Files Changed

| Repo | File | Change |
| ---- | ---- | ------ |
| `api` | `Documentation/cli/canonical-yai-command-system.md` | created |
| `api` | `Documentation/cli/canonical-cli-command-inventory.md` | updated to mark V50.5 as preliminary and point to V50.6 |
| `api` | `Documentation/waves/v50-6-canonical-yai-command-system.md` | created |

## Repos Audited

| Repo | Branch | Surfaces audited | Key finding |
| ---- | ------ | ---------------- | ----------- |
| `api` | `refoundation/phase-01` | `docs`, `registry`, `schemas`, `fixtures`, `conformance`, `openapi`, `contracts`, `extraction` | API registry already seeds more canonical families than the current Rust CLI exposes, and the API docs already describe command projection, family ownership, and execution/license/runtime boundaries. |
| `cli` | `refoundation/phase-01` | `src`, `tests`, `docs`, `README.md`, `MIGRATION_MAP.md` | Rust CLI implements a narrow surface (`auth`, `case`, `runtime`, `shell`, `session`, `provider`, `models`, `doctor`, `version`) while keeping many future groups as placeholders or migration notes. |
| `sdk` | `refoundation/phase-01` | `packages`, `docs`, `generated`, `conformance`, `README.md` | TypeScript SDK already exposes richer canonical families (`workflow`, `governance`, `control`, `knowledge`, `state`, `agents`, `orchestrator`) than the Rust CLI; Rust keeps compatibility aliases for legacy grammar. |
| `yai` | `refoundation/phase-01` | `README.md`, `Documentation`, `state`, `packaging`, `tests`, `Makefile` | `yai` contains the strongest architectural truth for the operational cycle, controlled-act lifecycle, state/knowledge/lineage separation, materialization flow, and storage/projection/ladybug boundaries. |
| `loom` | `refoundation/phase-01` | `README.md`, `docs`, `src` | Loom reinforces the rule that client/shell/session posture is not runtime/case/auth truth and behaves as an observing client/TUI rather than a domain owner. |

## Reconstruction Highlights

* `system` is the canonical public diagnostic root; `runtime` is retained as a truthful compatibility surface.
* `workflow` is the canonical target grammar; `flow` is a migration/compatibility surface.
* `session` remains legacy compatibility only and must not revive as the canonical domain.
* `policy-pack`, `intake`, `materialize`, `excerpt`, `state`, and `lineage` are restored as first-class target command groups even though they are absent from the current Rust CLI parser.
* `records` should converge under `state`, not remain a competing semantic root.
* `Documentation/audits/refoundation-map-v3.md` is now reflected in the command system: data-plane commands are interpreted along the experiential spine `case -> records/state -> lineage -> memory -> recall -> control`, with `memory` reserved as a later public-access layer rather than a premature V50.6 root command.
* `query`, `inspect`, `logs`, and root `policy` are too vague as canonical public roots.
* `SHM` is live runtime state, `LMDB` is durable substrate, `DuckDB` is derived query/projection, and `Ladybug` remains a future lineage-inspection boundary rather than a public root.

## V50.5 Handling

V50.5 is not deleted. It is retained as:

* a preliminary flat inventory
* a cross-check for current implementation coverage
* a migration appendix for V50.6

V50.6 is the only authoritative command-system source of truth.

## CLI Source Absence Check

```text
cli/source/ exists: no
full absence guardrail active: yes
Rust src/ is the only CLI implementation: yes
```

## Validation

| Repo | Command | Result |
| ---- | ------- | ------ |
| `api` | `test -f Documentation/cli/canonical-yai-command-system.md` | pass |
| `api` | `test -f Documentation/waves/v50-6-canonical-yai-command-system.md` | pass |
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

* [x] `Documentation/cli/canonical-yai-command-system.md` exists
* [x] `Documentation/waves/v50-6-canonical-yai-command-system.md` exists
* [x] `Documentation/cli/canonical-cli-command-inventory.md` updated to point at V50.6
* [x] operational cycle mapped
* [x] command groups reconstructed
* [x] state / knowledge / lineage / materialization commands defined
* [x] SHM / LMDB / DuckDB / Ladybug audited
* [x] policy-pack / intake / materialization flow restored
* [x] governance / policy / control boundaries defined
* [x] provider / model / agent / workflow / job / case / control groups rebuilt
* [x] too-vague commands classified
* [x] lost legacy capabilities mapped to new canonical owners
* [x] API / SDK / runtime / backend divergence recorded
* [x] no CLI behavior implemented
* [x] no API registry refactor performed
* [x] no SDK/runtime behavior implemented
* [x] CLI source absence guard verified
