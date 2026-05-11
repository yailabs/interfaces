# V50.5 — Canonical CLI Command Surface Audit

## Status

* Delivery: V50.5
* Status: done
* Track: V — CLI/API/SDK/runtime command canon
* Repo branch: `refoundation/phase-01`
* Repo change type: canonical CLI command inventory audit docs
* Previous delivery: V50 — Logout / Revocation / Lease Invalidation
* Next delivery: V51 — API Registry Refactor

## Purpose

V50.5 defines the official canonical CLI command inventory audit before V51.

The source of truth is:

* `api/Documentation/cli/canonical-cli-command-inventory.md`

This wave is documentation-only.

## Scope

Record:

* command families audited across `api`, `cli`, `sdk`, `yai`, and `loom`
* canonical target commands recorded beyond what is implemented today
* implemented vs target vs legacy vs deprecated vs forbidden classified
* API/SDK/CLI/runtime/Loom divergences recorded
* required posture/gates and future test priorities documented
* session legacy classified as non-canonical
* dev-wrapper commands classified outside canonical CLI
* no CLI behavior implemented
* no API registry refactor performed
* no SDK behavior implemented
* CLI source absence verified

## Files Changed

| Repo | File | Change |
| ---- | ---- | ------ |
| `api` | `Documentation/cli/canonical-cli-command-inventory.md` | created |
| `api` | `Documentation/waves/v50-5-canonical-cli-command-surface-audit.md` | created |

## Repos Audited

| Repo | Branch | Surfaces audited | Key finding |
| ---- | ------ | ---------------- | ----------- |
| `api` | `refoundation/phase-01` | `registry`, `schemas`, `docs`, `fixtures`, `conformance` | Registry and docs seed many more canonical families than the current Rust CLI exposes. |
| `cli` | `refoundation/phase-01` | `src`, `tests`, `README.md`, `docs`, `MIGRATION_MAP.md` | Rust CLI currently implements `auth`, `case`, `runtime`, `shell`, `session`, `provider`, `models`, `doctor`, and `version`; the rest is scaffold or absent. |
| `sdk` | `refoundation/phase-01` | `packages`, `docs`, `README.md` | SDK already exposes or names many canonical families (`system`, `workflow`, `governance`, `control`, `knowledge`, `state`, `agents`) that the CLI does not yet surface. |
| `yai` | `refoundation/phase-01` | `README.md`, `Documentation`, `packaging`, `tests`, `Makefile` | Runtime docs strongly separate auth/case/operator/runtime truth from client, shell, session, and dev-wrapper surfaces. |
| `loom` | `refoundation/phase-01` | `README.md`, `docs`, `src` | Loom reinforces shell/client UX boundaries and keeps auth/case/runtime truth external, but still carries compatibility posture language. |

## Key Decisions

* `api/Documentation/cli/canonical-cli-command-inventory.md` is the single canonical command inventory.
* `session` remains legacy compatibility only and must not revive as canonical domain grammar.
* `runtime status` is a current compatibility surface; `system status` is the canonical target.
* `flow`, singular `provider`, singular `agent`, and root `records` are divergence surfaces, not clean canonical endpoints.
* root `policy`, root `query`, and root `inspect` are not acceptable canonical public CLI families.
* runtime lifecycle `start/stop/restart` remains outside canonical public CLI and belongs to service/bootstrap or host-manager boundaries.

## CLI Source Absence Check

```text
cli/source/ exists: no
full absence guardrail active: yes
Rust src/ is the only CLI implementation: yes
```

## Validation

| Repo | Command | Result |
| ---- | ------- | ------ |
| `api` | `test -f Documentation/cli/canonical-cli-command-inventory.md` | pass |
| `api` | `test -f Documentation/waves/v50-5-canonical-cli-command-surface-audit.md` | pass |
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

* [x] `Documentation/cli/canonical-cli-command-inventory.md` exists
* [x] `Documentation/waves/v50-5-canonical-cli-command-surface-audit.md` exists
* [x] canonical seed commands included
* [x] command families expanded beyond seed
* [x] implemented vs target vs legacy classified
* [x] API/SDK/CLI/runtime/Loom divergences recorded
* [x] P0/P1/P2/P3 test priority skeleton created
* [x] session legacy classified as non-canonical
* [x] dev-wrapper commands classified outside canonical CLI
* [x] no CLI behavior implemented
* [x] no API registry refactor performed
* [x] no SDK behavior implemented
* [x] CLI source absence guard verified
