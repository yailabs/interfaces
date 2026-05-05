# CLI Legacy Source Quarantine

## Status

* Delivery: V21.2
* Status: active quarantine
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Purpose

Quarantine `cli/source/` until it can be extracted and deleted.

## Quarantine Policy

```text
cli/source/ is quarantined legacy C material.

It is not the canonical CLI.
It must not be used for new CLI behavior.
It must not be used as runtime/domain ownership.
It must not be used as session authority.
It must not be imported or depended on by Rust `src/`.
It exists only as extraction/migration reference until deletion.

Final target:
  cli/source/ is removed completely after useful logic is extracted.
```

This quarantine builds on the V21.1 extraction map: the Rust CLI under
`cli/src/` remains canonical, while `cli/source/` stays available only so
runtime/core, API, and SDK knowledge can be extracted in later waves before
deletion.

## Dependency Rule

```text
No new dependency from Rust `src/`, tests, or Cargo build metadata may point to
cli/source/.
```

The current Cargo CLI build remains clean under this rule:

* `cli/Cargo.toml` points the installed binary at `src/main.rs`
* no `build.rs` exists in `cli/`
* Rust `src/` and `tests/` do not currently point at `source/`

Broader legacy references outside Cargo remain recorded separately and are not
silently removed by V21.2.

## Allowed Uses While Quarantined

| Use | Allowed | Notes |
| --- | ------- | ----- |
| extraction reference | yes | until migrated |
| migration notes | yes | temporary |
| historical reference | yes | clearly marked legacy |
| new CLI behavior | no | use Rust `src/` |
| runtime/domain ownership | no | belongs outside CLI |
| session authority | no | session non-canonical |
| build dependency | no | except existing broader legacy references recorded separately |

## Known Residuals

| Residual | Status | Future wave |
| -------- | ------ | ----------- |
| `yai/Makefile` references `cli/source` | recorded | V21.3/V21.5 |
| `source/main.c` monolithic entrypoint | recorded | V21.3/V21.5 |
| `source/cmd/logs` weak classification | follow-up | V21.3/V21.4 |
| useful runtime/provider/agent/flow knowledge may exist | extract first | V21.3/V21.4 |

## Deletion Roadmap

| Wave | Action |
| ---- | ------ |
| V21.3 | extract runtime/core candidates |
| V21.4 | extract API/SDK candidates |
| V21.5 | delete migrated/obsolete source subtrees |
| V21.6 | add absence guardrail |
