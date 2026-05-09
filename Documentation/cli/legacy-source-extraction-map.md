# CLI Legacy Source Extraction Map

## Status

* Delivery: V21.1
* Status: active extraction map
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Purpose

Map `cli/source/` for extraction and eventual deletion.

## Final Direction

```text
cli/source/ must be removed completely after useful logic is extracted.
```

## Current Topology

| Path | Meaning | Canonical status |
| ---- | ------- | ---------------- |
| `src/` | Rust CLI | canonical current CLI |
| `source/` | legacy C CLI/migration substrate | non-canonical; extraction target |
| `Documentation/` | CLI docs | documentation |
| `tests/` | Rust CLI tests | canonical validation |
| `target/` | generated build output | generated/non-architecture |

## Build Inclusion

The current Rust CLI build is cargo-only:

* `cli/Cargo.toml` points the installed binary at `src/main.rs`.
* no `build.rs` exists in `cli/`.
* `rg` over `Cargo.toml`, `src/`, and `tests/` found no build-time inclusion of `source/`.

That means `source/` is not part of the installed Rust CLI build.

However, `source/` is still build-active outside Cargo:

* `yai/Makefile` defines `CLI_SOURCE := $(CLI_REPO)/source`
* `yai/Makefile` defines `YAI_CLI_CANONICAL_SRCS := ...` with many `source/cmd/*`,
  `source/out/*`, and `source/shared/*` files
* `yai/Makefile` also copies `source/assets/shell/*` into runtime/share surfaces

So V21.1 records two truths at once:

* `source/` is not part of the canonical Rust CLI build
* `source/` is still referenced by the broader repository build and cannot be
  deleted blindly

Recorded drift:

* `cli/source/README.md` correctly labels the tree as legacy, but its path note
  says the official Rust CLI lives under `../cli/src`; relative to `cli/source/`
  the current canonical path is `../src`
* V21.1 records that drift but does not fix it because `source/README.md` is
  outside the allowed edit scope for this wave

## Extraction Ownership Rules

```text
CLI owns:
  command parsing
  UX/help
  output rendering
  one-shot invocation
  local config/state only where scoped
  SDK/API calls

CLI must not own:
  provider execution
  agent authority
  flow execution
  knowledge store semantics
  analytics domain
  runtime lifecycle
  runtime readiness truth
  auth/account backend
  entitlement
  governed execution
  memory/state/lineage/control core semantics
  recall semantics
  session as domain

API owns:
  contracts
  operation registry
  schemas
  transport-visible surfaces

SDK owns:
  typed clients
  transport wrappers
  typed request/response surfaces

yai/core owns:
  runtime implementation
  service lifecycle
  governed execution substrate
  state/memory/lineage/control substrate
  records/evidence/knowledge runtime storage
  provider/agent/flow execution substrate

E track owns:
  account backend
  Supabase/provider auth
  entitlement
  machine authorization
  release access
```

## Extraction Map

`Compiled?` below means "present in the current broader repo build graph outside
Cargo", not "used by the installed Rust CLI".

| Legacy path | Domain | Current role | Compiled? | Target owner | Extraction action | Deletion wave |
| ----------- | ------ | ------------ | --------- | ------------ | ----------------- | ------------- |
| `source/main.c` | CLI entrypoint | monolithic legacy C entrypoint with runtime/session/case/provider knowledge mixed into one file | unknown | remove_later | mine only for migration reference; do not preserve as architecture | V21.x |
| `source/cmd/dispatch.c` | CLI dispatch | legacy command router | yes | remove_later | keep only as dispatch reference while subtrees are extracted | V21.x |
| `source/cmd/session` | session | legacy CLI/session model and shell/session glue | yes | remove_later | treat as compatibility specimen only; do not promote session as domain | V21.x |
| `source/cmd/runtime` | runtime | legacy runtime command/status path | yes | sdk/api | extract transport-visible status/control-plan semantics to SDK/API; keep CLI client-only | V21.x |
| `source/cmd/case` | case | legacy case command surface plus runtime/watch/runtime-state projection | yes | yai/api/sdk | split case substrate knowledge into `yai`; keep transport contracts in API/SDK; keep Rust CLI UX local | V21.x |
| `source/cmd/provider` | provider | legacy provider command family | yes | sdk/api | extract typed provider surfaces to SDK/API; delete CLI-owned provider behavior | V21.x |
| `source/cmd/models` | models | legacy model listing/resolution CLI surface | yes | sdk/api | keep only typed SDK/API projection; delete C command handlers later | V21.x |
| `source/cmd/agent` | agent | legacy agent command surface with runtime-env seeding and execution vocabulary | yes | yai/api/sdk | extract governed execution semantics outside CLI; leave only thin client UX if needed | V21.x |
| `source/cmd/flow` | flow | legacy orchestration/execution command surface | yes | yai/api/sdk | extract orchestration/runtime semantics to core and API/SDK | V21.x |
| `source/cmd/govern` | governance | legal/intake/authority/review/publication CLI bridge | yes | yai/api | extract governance/control semantics outside CLI | V21.x |
| `source/cmd/knowledge` | knowledge | legacy knowledge/memory/lineage/records/query CLI bridge | yes | yai/api/sdk | extract substrate semantics to `yai`; keep transport-visible query surfaces in API/SDK | V21.x |
| `source/cmd/analytics` | analytics | legacy analytics query surface | yes | api/sdk | align to canonical analytics/state/records contracts; remove CLI-owned domain logic | V21.x |
| `source/cmd/inspect` | runtime inspect | legacy inspect/runtime bridge | yes | sdk/api | merge surviving inspect semantics into canonical system/runtime SDK/API surfaces | V21.x |
| `source/cmd/ai` | prompting/AI | legacy AI root surface | yes | api/sdk | decide whether to map to prompting/AI contracts or retire as obsolete grammar | V21.x |
| `source/cmd/query` | query compatibility | legacy umbrella query entrypoint | yes | remove_later | map survivors to canonical command families; delete compatibility root | V21.x |
| `source/cmd/logs` | logs | minimal legacy root with unclear surviving ownership | yes | unknown_needs_followup | inspect whether this belongs to records/state/runtime diagnostics or should be dropped | V21.x |
| `source/cmd/skills` | skills | legacy skills root surface | yes | yai/api/sdk | extract skills/runtime bindings outside CLI | V21.x |
| `source/assets/shell` | shell UX | legacy shell prompt/render/session assets | yes | cli/Documentation/remove | salvage only assets that still serve canonical shell UX; delete session-bound legacy pieces | V21.x |
| `source/out` | output rendering | C text/json/table/tsv/shell rendering layer | yes | remove_later | do not port C renderers; Rust output layer is canonical | V21.x |
| `source/shared` | shared C helpers | argv/flags/help/io/paths/strings helpers for legacy CLI | yes | cli/remove_later | extract only tiny helpers if Rust still lacks them; otherwise delete with dependents | V21.x |

## Deletion Strategy

| Stage | Purpose |
| ----- | ------- |
| V21.1 | map and classify |
| V21.2 | quarantine source and block new dependencies |
| V21.3 | extract runtime/core candidates |
| V21.4 | extract API/SDK surface candidates |
| V21.5 | delete migrated source subtrees |
| V21.6 | add absence guardrail |

## Non-Deletion Rule For V21.1

```text
V21.1 does not delete source files.
Deletion begins only after extraction targets are documented and validated.
```
