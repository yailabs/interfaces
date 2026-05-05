# V21 - CLI SDK-first Wiring

## Status

* Delivery: V21
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: CLI SDK-first runtime wiring + documentation/report
* Previous delivery: V20 - SDK Runtime Surface Alignment
* Next delivery: V22 - Loom Alignment

## Purpose

V21 moves CLI runtime-facing surfaces toward SDK-first behavior.

## Scope

Record:

* CLI runtime status wiring inspected;
* SDK runtime/system surface consumed or gap recorded;
* local readiness projection preserved;
* runtime transport unavailable remains truthful;
* controlPlan remains plan/projection only;
* CLI remains one-shot client;
* no runtime control execution added.

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `docs/cli/cli-sdk-first-wiring.md` | create | CLI SDK-first model |
| api | `docs/waves/v21-cli-sdk-first-wiring.md` | create | delivery report |
| cli | `README.md` | update | runtime status SDK-first note |
| cli | `MIGRATION_MAP.md` | update | runtime row SDK-first note |
| cli | `src/app/cli.rs` | update | runtime help wording |
| cli | `src/commands/runtime.rs` | update | canonical system-status operation id |
| cli | `src/sdk/runtime.rs` | update | use Rust SDK system surface directly |
| cli | `src/output/readiness.rs` | update | SDK-first runtime operation id for fallback view |
| cli | `tests/output_snapshot.rs` | update | runtime status snapshot alignment |

## Wiring Decision

| Decision | Meaning |
| -------- | ------- |
| A | CLI runtime status now consumes Rust SDK runtime/system surface directly |

## Runtime Status Behavior

Current `yai runtime status` after V21:

* lifecycle/health/readiness come from Rust SDK `system.status` transport truth;
* transport unavailable is still surfaced as `runtime_transport_unavailable`;
* local `operationalReadiness` and `sealReason` remain composed by the CLI from
  local state;
* `controlPlan` is not yet surfaced by the CLI;
* fake execution claims remain absent.

## CLI / SDK Boundary

| Concern | Owner after V21 |
| ------- | --------------- |
| runtime lifecycle truth | SDK/API/transport |
| local readiness projection | CLI local projection using local state |
| controlPlan semantics | SDK/API model, plan-only |
| runtime control execution | not implemented |
| active_case_ref | operator context |
| case tree | case manifest |
| session | legacy compatibility only |

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f docs/cli/cli-sdk-first-wiring.md` | pass | new CLI doc |
| api | `test -f docs/waves/v21-cli-sdk-first-wiring.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | available and clean |
| sdk/rust | `cargo check` | not run | SDK source untouched in V21 |
| sdk/rust | `cargo test` | not run | SDK source untouched in V21 |
| cli | `cargo fmt --check` | pass | CLI source touched |
| cli | `cargo test` | pass | CLI source touched |
| cli | `cargo build` | pass | CLI source touched |
| cli | `cargo install --path . --force` | pass | installed CLI refreshed |
| shell | `which yai` | pass | installed CLI resolution |
| shell | `yai runtime status` | pass | SDK-first runtime status; truthful unavailable transport; exit `4` |
| shell | `yai auth status` | pass | local projection sanity |
| shell | `yai case status` | pass | local projection sanity |
| sdk/typescript | validation | not run | untouched |
| loom | validation | not run | untouched |
| yai | validation | not run | untouched |
