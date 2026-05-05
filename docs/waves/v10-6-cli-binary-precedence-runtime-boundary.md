# V10.6 - CLI Binary Precedence / Runtime Carrier Boundary

## Status

* Delivery: V10.6
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: install/path/binary-boundary hardening + documentation/report
* Previous delivery: V10.5 - Canonical CLI Install and Invocation
* Next delivery: V11 - Operator Context Plane

## Purpose

V10.6 resolves or classifies the conflict where plain `which yai` resolves to
the runtime carrier instead of the installed CLI.

## Scope

Record:

* CLI/runtime binary ownership documented;
* `which yai` behavior recorded before and after;
* canonical `yai` invocation points to the installed CLI after `which yai`
  verification;
* local plain-PATH collision is explicitly documented as temporary residual;
* runtime carrier boundary documented;
* primary smoke remains installed-CLI based;
* no production backend added.

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `docs/cli/cli-runtime-binary-boundary.md` | create | CLI/runtime binary boundary |
| api | `docs/waves/v10-6-cli-binary-precedence-runtime-boundary.md` | create | delivery report |
| api | `docs/cli/canonical-cli-invocation.md` | update | cross-link/residual closure |
| cli | `README.md` | docs | CLI install precedence |

## Binary Resolution

| Check | Before | After | Result |
| ----- | ------ | ----- | ------ |
| `which yai` | `/usr/local/bin/yai` | `/usr/local/bin/yai` without PATH correction | residual |
| `which -a yai` | included both runtime carrier and installed CLI entries | same family of entries | recorded |
| CLI binary path | installed CLI binary present in shell resolution | installed CLI binary present in validation shell | recorded |
| runtime carrier path | `/usr/local/bin/yai` local conflict; intended runtime service path `/usr/local/libexec/yai/runtime` | conflict classified; intended boundary documented | residual |

## Decision

```text
B - temporary PATH precedence required; tracked residual
```

Product direction remains:

```text
A - CLI owns `yai`; runtime carrier moved/renamed/not user-facing
```

Residual:

```text
/usr/local/bin/yai still shadowed the CLI in the historical local shell.
Future packaging must resolve this by making CLI own `yai`.
```

## Canonical Smoke

The canonical smoke used installed `yai`, normal `~/.yai` state, no `cargo run`, no `YAI_CONFIG_HOME`, and no
`YAI_ACCOUNT_USERNAME`.

| Command | Result | Notes |
| ------- | ------ | ----- |
| `which yai` | residual/pass | historical plain shell resolved `/usr/local/bin/yai`; validation shell resolved the installed CLI |
| `yai --help` | pass | installed CLI shows auth/case commands |
| `yai auth status` | pass | installed CLI; unauthenticated before login |
| `yai auth login --local-dev` | pass | installed CLI, no env |
| `yai case status` | pass | installed CLI, no env |
| `yai case root` | pass | installed CLI, no env |

## Boundary Rules

```text
user-facing yai command belongs to CLI
runtime carrier is not the canonical user command
service manager may invoke runtime binary directly
cargo run remains debug-only
YAI_CONFIG_HOME remains test isolation only
YAI_ACCOUNT_USERNAME remains debug override only
```

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| cli | `cargo fmt --check` | pass | exact |
| cli | `cargo test` | pass | exact; warnings only |
| cli | `cargo build` | pass | exact; warnings only |
| cli | `cargo install --path . --force` | pass | exact; reinstalled the CLI |
| shell | `which -a yai` | pass | showed both runtime-carrier and installed-CLI entries |
| shell | `which yai` | residual | plain shell resolves `/usr/local/bin/yai` |
| shell | `which yai` in validation shell | pass | resolved to the installed CLI |
| shell | `yai --help` | pass | CLI help with auth/case commands |
| shell | `yai auth status` | pass | installed CLI |
| shell | canonical installed smoke | pass | no cargo/env auth username/config home |
| api | `test -f docs/cli/cli-runtime-binary-boundary.md` | pass | new doc |
| api | `test -f docs/waves/v10-6-cli-binary-precedence-runtime-boundary.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| yai | `make info` | pass | build metadata printed |
| yai | `make yai` | pass | nothing to be done |
| sdk | validation | not run | no SDK files changed |
| loom | validation | not run | no Loom files changed |

## Post-Edit Scans

```bash
rg -n "/usr/local/bin/yai|\\.cargo/bin/yai|which yai|runtime carrier|CLI owns|user-facing yai|cargo run|YAI_CONFIG_HOME|YAI_ACCOUNT_USERNAME" api cli yai sdk loom
```

Result: pass; references are classified as canonical install, runtime boundary,
historical records or debug/test-only.

```bash
rg -n "canonical smoke.*cargo run|canonical.*YAI_CONFIG_HOME|canonical.*YAI_ACCOUNT_USERNAME|runtime carrier owns user-facing yai|production account connected|Supabase login complete|device login complete|entitlement granted" api cli yai sdk loom
```

Result: pass; matches are negative/residual text or older forbidden-scan command
strings, not new primary-canonical env/cargo flow or fake backend claims.

## Findings

### Finding A - Binary Collision Resolved or Classified

The `/usr/local/bin/yai` versus installed-CLI collision is explicitly
tracked as a temporary residual.

### Finding B - CLI Owns User Command

The product direction is that the CLI owns the user-facing `yai` command.

### Finding C - Runtime Carrier Is Not UX

The runtime carrier must be service/internal, not the primary user command.

### Finding D - V11 Can Continue

Operator context work can proceed with the command-path ambiguity documented and
bounded.

## V10.6 Completion Checklist

* [x] `docs/cli/cli-runtime-binary-boundary.md` exists
* [x] `docs/waves/v10-6-cli-binary-precedence-runtime-boundary.md` exists
* [x] binary collision documented
* [x] CLI/runtime binary ownership documented
* [x] `which yai` behavior recorded
* [x] `yai --help` behavior recorded
* [x] canonical installed smoke run without `cargo run`
* [x] canonical installed smoke run without `YAI_CONFIG_HOME`
* [x] canonical installed smoke run without `YAI_ACCOUNT_USERNAME`
* [x] runtime carrier boundary documented
* [x] residual recorded if unresolved
* [x] no production backend claimed
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
