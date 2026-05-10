# A1 - Console Canonicalization / Legacy CLI-Loom Drain

## Status

* Delivery: A1
* Status: done
* Track: A - Console canonicalization / legacy CLI-Loom drain
* Repo branch: `refoundation/phase-01` for `api`, `yai`, `sdk`, `cli`, `loom`; `console` remains on `main`
* Change type: naming/canonicalization cleanup; docs + product identity + active help/copy
* Next delivery: A2 - Operation Transport Mapping Drift Reconciliation

## Purpose

Console is now the canonical terminal client. CLI and Loom remain as legacy,
compatibility, or historical names only.

A1 avoids transport, runtime, SDK API, and default behavior changes. The only
runtime-adjacent code edits are naming/copy/manifest updates and a compatibility
environment alias where Console replaces Loom as the canonical variable name.

## Files Changed

| Repo | Area | Change |
| ---- | ---- | ------ |
| api | `Documentation/client/console-client-alignment.md` | Added active Console client model. |
| api | `Documentation/client/loom-client-alignment.md` | Retained V22 path as historical compatibility note. |
| api | `Documentation/client/*`, `Documentation/cli/*`, `Documentation/sdk/*`, `Documentation/*source*` | Reworded active references from Loom/CLI as canonical clients to Console plus legacy compatibility. |
| api | `Documentation/*boundary*`, `Documentation/local-ipc-rpc-contract.md`, `Documentation/transport-boundary-model.md` | Repointed active native terminal target language to Console; kept legacy CLI/Loom only as compatibility behavior wording. |
| api | `Documentation/waves/a-series-map.md` | Added A-series map with A1 and A2. |
| yai | README, architecture, operator, packaging, runtime boundary docs | Repointed active boundary language to `../console`; marked `../cli`/`../loom` as legacy-compatible external surfaces. |
| sdk | manifests, README, standards/guides/package docs | Updated client targets and consumer language to `console`/`yai-console`; retained legacy `loom`/`yai-cli` keys for compatibility. |
| cli | README, PRODUCT, manifest, help/copy | Marked CLI as legacy-compatible scriptable command surface; Console is canonical terminal client. |
| loom | `LICENSE` | Kept `yailabs/loom` as legacy compatibility history and recorded `yailabs/console` as canonical terminal client repository target after the remote Console cutover. |
| console | product/docs/manifests, Cargo package/lock, active TUI copy/internal type names, launcher | Canonicalized product identity to YAI Console and added `yai-console`; `yai-loom` remains a legacy launcher. |

Remote realignment note: the `../loom` branch already contains the active
Console cutover, including `Documentation/`, `console.manifest.json`, and
`src/client/*`. A1 kept that remote topology instead of reintroducing stale
pre-cutover paths.

## Classification

| Classification | Decision |
| -------------- | -------- |
| `active_should_rename` | Active README/product/architecture/operator/package docs that treated CLI/Loom as canonical client identities were rewritten to Console. |
| `historical_keep` | Existing V0-V23 wave reports, ADRs, audits, and legacy reports retain historical CLI/Loom wording. |
| `compatibility_keep` | `yai`, `yai-cli`, `yai-loom`, `YAI_LOOM_DEV_BYPASS_AUTH`, manifest legacy keys, and existing compatibility docs remain with explicit legacy labels where the compatibility surface still exists. |
| `tombstone_keep` | Loom client alignment path remains as a historical/tombstone doc that points to Console alignment. |
| `code_symbol_keep_for_now` | SDK C handshake metadata `yai-cli` remains unchanged to avoid SDK/runtime compatibility risk. Console keeps legacy `yai-loom` launcher/manifest aliases for compatibility. |
| `code_symbol_rename_now` | Console Rust internal `LoomSdk`/`LoomPalette` symbols became `ConsoleSdk`/`ConsolePalette`; visible copy became YAI Console. The remote `../loom` branch already carries its own Console topology cutover. |
| `needs_followup` | A2 should reconcile operation transport mapping drift; future packaging work can decide when to retire legacy launchers/env aliases. |

## Remote Rebase Note

After `git fetch origin` and `git pull --rebase --autostash`, `api`, `sdk`,
`yai`, and `loom` were realigned with their upstream `refoundation/phase-01`
heads. `api` and `sdk` moved to the remote `Documentation/` docs topology; A1
was reintegrated only into active `Documentation/` paths. Stale local `docs/`
paths from pre-pull worktrees were dropped.

`yai` had advanced by 7 remote commits and `loom` by 3 remote commits. `yai`
A1 edits were replayed on top of the new remote docs/runtime/build surfaces.
`loom` remote had already cut over to Console topology, so A1 kept the remote
code/docs/manifest topology and retained only the compatibility-history license
correction.

The remote already contains
`Documentation/waves/a1-operation-transport-mapping-drift-reconciliation.md`.
That accepted report is not renamed here; the A-series map records A2 as the
forward transport-mapping slot.

## Compatibility Notes

- `YAI_CONSOLE_DEV_BYPASS_AUTH=1` is canonical for Console dev bypass.
- `YAI_LOOM_DEV_BYPASS_AUTH=1` remains accepted as a legacy alias in
  `../console`.
- `./yai-console` is canonical in `../console`.
- `./yai-loom` remains a compatibility launcher in `../console`.
- No transport behavior, runtime behavior, SDK API behavior, or default switch was intentionally changed.

## Validation

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `git diff --check` | pass | Required gate. |
| yai | `git diff --check && make -j4 && make -j4 yai` | pass | `make -j4 yai` reported nothing to do after successful build. |
| sdk | `cargo test --manifest-path packages/rust/Cargo.toml && git diff --check` | pass | 11 unit tests and 8 local IPC RPC integration tests passed after remote realignment. |
| cli | `test ! -e source && scripts/check-no-source-dependency.sh && git diff --check` | pass | `source/` remains absent. |
| loom | `cargo fmt --check && cargo test && cargo build && git diff --check` | pass | Remote branch now carries Console topology; 25 Rust tests passed. |
| console | `cargo fmt --check && cargo test && cargo build && git diff --check` | pass | Added handling for SDK `TransportContract` error variant introduced by remote SDK changes. |

## Completion Check

- Active docs converge on Console.
- Active code/help/manifest language converges on Console where safe.
- CLI/Loom remain only as historical, compatibility, tombstone, or deferred code-symbol terms.
- A-series map records A1 and A2.
