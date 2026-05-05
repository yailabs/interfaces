# V21.1 - CLI Legacy Source Extraction Map

## Status

* Delivery: V21.1
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: legacy source extraction audit + migration map
* Previous delivery: V21 - CLI SDK-first Wiring
* Next delivery: V21.2 - CLI Legacy Source Quarantine

## Purpose

V21.1 maps the legacy C `cli/source/` tree so it can be extracted and deleted.

## Scope

Record:

* `source/` topology inspected;
* build inclusion checked;
* major subtrees classified;
* ownership targets assigned;
* deletion strategy defined;
* no source deleted;
* no behavior changed.

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `docs/cli/legacy-source-extraction-map.md` | create | extraction map |
| api | `docs/waves/v21-1-cli-legacy-source-extraction-map.md` | create | delivery report |

## Build Inclusion Result

| Check | Result | Notes |
| ----- | ------ | ----- |
| `source/` referenced by Cargo | no | `cli/Cargo.toml` builds `src/main.rs` only |
| `source/` compiled by build.rs | no | no `build.rs` exists in `cli/` |
| `source/` referenced by Rust `src/` | no | `rg` over `Cargo.toml`, `src/`, and `tests/` found no build inclusion |
| `source/` referenced by tests | no | Rust tests execute `CARGO_BIN_EXE_yai` and do not include `source/` |
| `source/` required for installed CLI | no | installed Rust CLI comes from Cargo `src/main.rs` |

Important cross-repo note:

* `source/` is still referenced by `yai/Makefile` through `CLI_SOURCE` and
  `YAI_CLI_CANONICAL_SRCS`
* `source/assets/shell` is still copied by `yai/Makefile`
* deletion must therefore be staged across `cli` and `yai`, not treated as a
  local Cargo-only cleanup

Recorded drift:

* `cli/source/README.md` already says the tree is legacy, but its relative path
  note still points at `../cli/src` instead of the current canonical `../src`
* V21.1 records that mismatch and leaves it untouched because it is outside the
  allowed edit scope for this wave

## Legacy Source Inventory

| Path | Classification | Target owner | Extraction action |
| ---- | -------------- | ------------ | ----------------- |
| `source/cmd/session` | `legacy_cli_reference` | `remove_later` | keep only as compatibility specimen; remove after session compatibility is fully displaced |
| `source/cmd/runtime` | `sdk_surface_candidate` | `sdk/api` | extract runtime status/control semantics to SDK/API and delete CLI-local C path |
| `source/cmd/case` | `backend_domain_candidate` | `yai/api/sdk` | separate case substrate logic from transport surface and delete CLI-owned runtime/case logic |
| `source/cmd/provider` | `sdk_surface_candidate` | `sdk/api` | keep only typed provider transport surfaces |
| `source/cmd/agent` | `backend_domain_candidate` | `yai/api/sdk` | move governed agent execution semantics outside CLI |
| `source/cmd/flow` | `backend_domain_candidate` | `yai/api/sdk` | move orchestration/execution semantics outside CLI |
| `source/cmd/knowledge` | `backend_domain_candidate` | `yai/api/sdk` | move knowledge/memory/lineage semantics outside CLI |
| `source/cmd/govern` | `backend_domain_candidate` | `yai/api` | move governance/control semantics outside CLI |
| `source/cmd/analytics` | `api_surface_candidate` | `api/sdk` | align query surface to canonical analytics/state/records contracts |
| `source/cmd/models` | `sdk_surface_candidate` | `sdk/api` | keep only typed model transport surfaces |
| `source/cmd/skills` | `backend_domain_candidate` | `yai/api/sdk` | move skills/runtime bindings outside CLI |
| `source/assets/shell` | `migration_reference` | `cli/docs/remove` | salvage only assets still useful to canonical shell UX |
| `source/shared` | `migration_reference` | `cli/remove_later` | inspect helpers only after dependent subtrees are classified |

## Extraction Plan

| Priority | Source area | Target repo/surface | Reason |
| -------- | ----------- | ------------------- | ------ |
| P0 | session | remove/legacy docs | session is non-canonical |
| P1 | runtime | yai/api/sdk | runtime belongs outside CLI |
| P1 | provider/agent/flow | yai/api/sdk | governed execution domain |
| P1 | knowledge/govern/analytics | yai/api/sdk | memory/state/control domain |
| P2 | shell assets | cli/docs/remove | shell UX only |
| P3 | shared helpers | cli/remove_later | inspect after dependents classified |

## Deletion Roadmap

| Wave | Action |
| ---- | ------ |
| V21.2 | quarantine `source/`; document non-canonical status |
| V21.3 | extract runtime/core candidates |
| V21.4 | extract API/SDK candidates |
| V21.5 | delete extracted source subtrees |
| V21.6 | add guardrail preventing new `source/` dependency |

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f docs/cli/legacy-source-extraction-map.md` | pass | new doc |
| api | `test -f docs/waves/v21-1-cli-legacy-source-extraction-map.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | available |
| cli | `cargo fmt --check` | pass | docs-only wave; kept build green |
| cli | `cargo test` | pass | docs-only wave; kept build green |
| cli | `cargo build` | pass | docs-only wave; kept build green |
| cli | topology inspection commands | pass | `src/`, `source/`, `docs/`, `tests/`, and build inclusion inspected |
| sdk | validation | not run | untouched |
| yai | validation | not run | untouched |
| loom | validation | not run | untouched |

## Findings

### Finding A - source/ Is Non-Canonical

Record:
The Rust `src/` tree is the current canonical CLI. `source/` is legacy and must
be extracted/deleted.

### Finding B - Deletion Requires Extraction

Record:
`source/` cannot be safely deleted until useful runtime/API/SDK/core knowledge
is extracted.

### Finding C - CLI Must Not Own Domains

Record:
Provider, agent, flow, knowledge, governance, analytics, memory, state, lineage
and control semantics do not belong in CLI implementation.

### Finding D - V21.2 Can Quarantine source/

Record:
After mapping, V21.2 can explicitly quarantine `source/` and block new
dependencies.
