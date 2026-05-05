# V10.5 - Canonical CLI Install and Invocation

## Status

* Delivery: V10.5
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: CLI install/canonical invocation hardening + documentation/report
* Previous delivery: V10 - Active Case Refactor
* Next delivery: V11 - Operator Context Plane

## Purpose

V10.5 makes installed `yai` the primary accepted CLI path.

## Scope

Record:

* installed CLI invocation documented;
* canonical smoke path uses `yai ...`;
* `cargo run` demoted to dev/debug only;
* `YAI_CONFIG_HOME=/tmp/...` demoted to isolated test/debug only;
* `YAI_ACCOUNT_USERNAME=...` removed from primary smoke;
* `~/.yai` is canonical local state;
* real account backend remains deferred;
* Supabase/database integration remains deferred.

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `docs/cli/canonical-cli-invocation.md` | create | canonical installed CLI workflow |
| api | `docs/waves/v10-5-canonical-cli-install-and-invocation.md` | create | delivery report |
| cli | `README.md` | docs | canonical installed CLI path |

## Canonical CLI Path

Install method:

```bash
cargo install --path . --force
```

Installed command verification:

```bash
which yai
yai --help
```

Important path finding:

```text
plain which yai -> /usr/local/bin/yai
which yai after CLI install resolved to the installed CLI in the validation shell
```

`/usr/local/bin/yai` is the runtime carrier in this workspace. The canonical
operator flow is: install the CLI, verify `which yai`, then use plain `yai ...`.

## Canonical Smoke

The canonical smoke used installed `yai`, normal `~/.yai` state, no `cargo run`,
no `YAI_CONFIG_HOME`, and no `YAI_ACCOUNT_USERNAME`.

| Command | Result | Notes |
| ------- | ------ | ----- |
| `yai --help` | pass | installed Rust CLI help |
| `yai auth login --local-dev` | pass | derived `local-dev:francescomaiomascio`; no env username |
| `yai auth status` | pass | reads canonical `~/.yai` state |
| `yai case root` | pass | root `case://francescomaiomascio` |
| `yai case list` | pass | tree from canonical state |
| `yai case open projects/site-e0-cleanup` | pass | created nested case |
| `yai case enter projects/site-e0-cleanup` | pass | set operator context active case |
| `yai case status` | pass | active case shown |
| `yai case leave` | pass | active case cleared |
| `yai case close projects/site-e0-cleanup` | pass | nested case removed |
| `yai auth logout` | pass | auth cleared truthfully |

## Dev/Test-Only Tools

```text
cargo run --quiet --        debug/development only
YAI_CONFIG_HOME=/tmp/...    isolated test only
YAI_ACCOUNT_USERNAME=...    override/debug only, not primary smoke
```

## Boundary Rules

```text
canonical command path uses installed yai
canonical state path is ~/.yai
local-dev auth remains temporary until real account backend exists
real account login remains deferred
Supabase/database remains deferred
API/SDK must align to installed CLI semantics
session remains legacy compatibility only
```

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| cli | `cargo fmt --check` | pass | exact |
| cli | `cargo test` | pass | exact; warnings only |
| cli | `cargo build` | pass | exact; warnings only |
| cli | `cargo install --path . --force` | pass | installed CLI successfully |
| cli | `which yai` | pass | resolved to the installed CLI in the validation shell |
| cli | `yai --help` | pass | installed Rust CLI |
| cli | canonical smoke commands | pass | no `cargo run`, no `YAI_CONFIG_HOME`, no `YAI_ACCOUNT_USERNAME` |
| api | baseline docs checks | pass | V0-V10 docs present |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| api | `test -f docs/cli/canonical-cli-invocation.md` | pass | new doc |
| api | `test -f docs/waves/v10-5-canonical-cli-install-and-invocation.md` | pass | new report |
| sdk | validation | not run | no SDK files changed |
| yai | `make info` | pass | build metadata printed |
| yai | `make yai` | pass | nothing to be done |
| loom | validation | not run | no Loom files changed |

## Post-Edit Scans

```bash
rg -n "cargo run --quiet|YAI_CONFIG_HOME|YAI_ACCOUNT_USERNAME|canonical smoke|installed yai|which yai|~/.yai" api cli sdk yai loom
```

Result: pass; remaining `cargo run` or env references are classified as
debug/test-only or are historical delivery records.

```bash
rg -n "primary smoke.*cargo run|canonical.*YAI_CONFIG_HOME|canonical.*YAI_ACCOUNT_USERNAME|production account connected|Supabase login complete|device login complete|entitlement granted" api cli sdk yai loom
```

Result: pass; matches are older forbidden-scan command strings or negative V10.5
text saying the canonical smoke does not use env/cargo. There are no new claims
that env/cargo are the primary canonical flow and no fake production
account/backend claims.

## Findings

### Finding A - Installed CLI Is Canonical

The accepted command path is now installed `yai`, not repo-local `cargo run`.

### Finding B - Env Overrides Are Debug Only

`YAI_CONFIG_HOME` and `YAI_ACCOUNT_USERNAME` may remain useful for isolated
tests, but are not canonical user flow.

### Finding C - Real Account Backend Still Deferred

This wave does not implement Supabase/database/account login. It prepares the CLI
surface for it.

### Finding D - V11 Can Continue Safely

With canonical CLI invocation fixed, V11 can model operator context without
depending on development-only execution assumptions.

## V10.5 Completion Checklist

* [x] `docs/cli/canonical-cli-invocation.md` exists
* [x] `docs/waves/v10-5-canonical-cli-install-and-invocation.md` exists
* [x] installed `yai` path documented
* [x] primary smoke uses `yai ...`
* [x] primary smoke does not use `cargo run`
* [x] primary smoke does not use `YAI_CONFIG_HOME=/tmp/...`
* [x] primary smoke does not use `YAI_ACCOUNT_USERNAME=...`
* [x] env overrides documented as debug/test-only
* [x] canonical local state path documented as `~/.yai`
* [x] production auth not claimed
* [x] Supabase/database not claimed
* [x] API/SDK/CLI alignment implications recorded
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
