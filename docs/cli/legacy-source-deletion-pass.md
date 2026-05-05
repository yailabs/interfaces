# Legacy Source Deletion Pass

## Status

* Delivery: V21.5
* Status: active deletion pass
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Purpose

Delete deletion-ready legacy C `cli/source/` material after extraction.

## Deletion Principle

```text
Delete only after useful semantics are extracted and build references are
removed or proven irrelevant.
```

## Deleted Areas

| Deleted path | Reason | Prior extraction artifact |
| ------------ | ------ | ------------------------- |
| `source/out` | Rendering stubs had no remaining runtime/core or API/SDK semantic value, and the only broader build references were in an unused legacy Makefile inventory list removed in V21.5 | `docs/cli/legacy-runtime-core-extraction.md`, `docs/cli/legacy-api-sdk-surface-extraction.md` |
| `source/shared` | Legacy argv/path/help/passthrough helpers were already drained into Rust CLI/config surfaces; no Cargo or active yai build dependency remained | `docs/cli/legacy-runtime-core-extraction.md`, `docs/cli/legacy-api-sdk-surface-extraction.md` |

## Remaining Areas

| Remaining path | Reason retained | Future action |
| -------------- | --------------- | ------------- |
| `source/main.c` | Monolithic legacy entrypoint still acts as a residual quarantine sentinel in `yai/Makefile` and still mixes blocked domains | retain through residual deletion follow-up, then remove with remaining CLI source tree |
| `source/cmd/runtime` | runtime family wrappers still remain partially blocked even after semantic extraction | V21.6+ follow-up or later deletion pass after residual cleanup |
| `source/cmd/provider` | provider family shapes preserved, but subtree still remains part of retained residual legacy command tree | V21.6+ follow-up or later deletion pass |
| `source/cmd/agent` | agent grammar preserved, but subtree still remains part of retained residual legacy command tree | V21.6+ follow-up or later deletion pass |
| `source/cmd/flow` | heavy blocked semantic area from V21.3/V21.4 | later deletion after additional residual cleanup |
| `source/cmd/govern` | governance wrappers remain partial residuals | later deletion after residual cleanup |
| `source/cmd/knowledge` | heavy blocked semantic area from V21.3/V21.4 | later deletion after additional residual cleanup |
| `source/cmd/analytics` | thin but still retained with residual command family | later deletion pass |
| `source/cmd/logs` | records/evidence tail surface still retained with residual command family | later deletion pass |
| `source/cmd/case` | large partial case surface remains retained | later deletion pass |
| `source/cmd/session` | session remains explicitly non-canonical but not yet physically deleted | later deletion/deprecation pass |
| `source/assets/shell` | residual legacy shell assets not in current deletion set | evaluate in later cleanup wave |
| `source/MIGRATION_MAP.md` | local legacy map retained as historical residue | keep until final `source/` removal |
| `source/README.md` | quarantine banner still needed while any legacy source remains | keep until final `source/` removal |

## Build References

| Reference | Status after V21.5 | Notes |
| --------- | ------------------ | ----- |
| `yai/Makefile` `CLI_SOURCE` | retained | generic residual pointer remains while any quarantined legacy source exists |
| `YAI_CLI_CANONICAL_SRCS` | removed | unused legacy inventory list removed with deleted-path cleanup |
| Rust Cargo references | none | `Cargo.toml` does not depend on `source/` |
| Rust `src/` references | none | dependency regression scan remains clean |
| Rust tests references | none | dependency regression scan remains clean |

## Next

| Wave | Purpose |
| ---- | ------- |
| V21.6 | Add absence guardrail / prevent source recreation |
| V22 | Loom client alignment after CLI cleanup branch |
