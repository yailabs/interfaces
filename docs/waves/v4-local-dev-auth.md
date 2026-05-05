# V4 - Local Dev Auth

## Status

* Delivery: V4
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: local-dev auth CLI implementation + documentation/report
* Previous delivery: V3 - Auth Command Model
* Next delivery: V5 - Principal Model

## Purpose

V4 introduces:

```bash
yai auth login --local-dev
```

as a local development auth path.

V4 creates a tracked local principal, but does not implement production account
auth.

## Scope

* local-dev auth marker added;
* `yai auth login --local-dev` implemented;
* `yai auth status` reports local-dev/unauthenticated posture truthfully;
* `yai auth logout` clears local-dev marker truthfully;
* no production auth was added;
* no account_ref was created;
* no entitlement_ref was created;
* no machine_authorization_ref was created;
* no case://user was created.

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `docs/waves/v4-local-dev-auth.md` | create | delivery report |
| cli | `src/app/cli.rs` | implementation | add `--local-dev` flag to `yai auth login` |
| cli | `src/commands/auth.rs` | implementation | local-dev auth marker/status/logout behavior |
| cli | `src/output/render.rs` | compile repair | import public `RuntimeServiceStatus` path so CLI binary compiles |
| cli | `src/sdk/runtime.rs` | compile repair | import public `RuntimeServiceStatus` path so CLI binary compiles |
| cli | `README.md` | docs | document local-dev auth command behavior |
| cli | `MIGRATION_MAP.md` | docs | record V4 auth implementation scope |
| sdk | `README.md` | docs | local-dev boundary documentation |
| loom | `README.md` | docs | local-dev boundary documentation |

## Local Auth State

| Field | Value |
| ----- | ----- |
| state path | `~/.yai/auth/local-dev.json`, or `$YAI_CONFIG_HOME/auth/local-dev.json` when `YAI_CONFIG_HOME` is set |
| schema/name | `yai.auth.local-dev.v1` |
| mode | `local-dev` |
| principal format | `local-dev:<value>` |
| production account | none |
| entitlement | none |
| machine authorization | none |
| root case creation | none |
| session mutation | none |

Marker shape:

```json
{
  "schema": "yai.auth.local-dev.v1",
  "mode": "local-dev",
  "principal": "local-dev:<value>",
  "source": "cli",
  "account_ref": null,
  "entitlement_ref": null,
  "machine_authorization_ref": null,
  "case_ref": null
}
```

## Command Surface

| Command | Status after V4 | Behavior | Notes |
| ------- | --------------- | -------- | ----- |
| `yai auth login` | present | planned/unavailable unless local-dev flag used | no fake production login |
| `yai auth login --local-dev` | implemented | creates local-dev auth marker | local development only |
| `yai auth status` | implemented/updated | reports local-dev or unauthenticated | not runtime/session status |
| `yai auth logout` | implemented/updated | clears local-dev marker | does not stop runtime/cases/jobs |

## Boundary Rules

```text
local-dev auth != production account login
local-dev auth != entitlement
local-dev auth != machine authorization
local-dev auth != case://user creation
local-dev auth != active case selection
local-dev auth != shell/client attach
local-dev auth != runtime readiness
local-dev auth != session
```

## Deferred to Later Waves

| Deferred item | Future wave |
| ------------- | ----------- |
| principal/account_ref/auth_context stabilization | V5 |
| root `case://user` creation after login | V6 |
| case URI grammar | V7 |
| case tree model | V8 |
| canonical case commands | V9 |
| active case out of session | V10 |
| sealed runtime enforcement | V14 |
| SDK auth clients | V38 |
| external account provider/device login | E2/E6/E9 |
| entitlement evaluation | E18/E19/E20 |

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f docs/waves/v0-command-reality-audit.md` | pass | baseline |
| api | `test -f docs/adr/ADR-V1-session-death-decision.md` | pass | baseline |
| api | `test -f docs/compat/session-legacy-containment.md` | pass | baseline |
| api | `test -f docs/waves/v2-legacy-session-containment.md` | pass | baseline |
| api | `test -f docs/waves/v3-auth-command-model.md` | pass | baseline |
| api | `test -f docs/waves/v4-local-dev-auth.md` | pass | new report |
| cli | `cargo fmt --check` | pass | initial run reported wrapping for V4 code; formatting was corrected and check passed |
| cli | `cargo test` | pass | V2/V3 baseline compile issue resolved by importing `RuntimeServiceStatus` from `surfaces::system` |
| cli | `cargo run -- auth --help` or equivalent | pass | command help shows canonical auth commands and local-dev flag guidance |
| cli | `cargo run -- auth login --local-dev` or equivalent | pass | creates local-dev marker and prints no production account/entitlement/machine authorization/case |
| cli | `cargo run -- auth status` or equivalent | pass | reports unauthenticated before login, local-dev after login, unauthenticated after logout |
| cli | `cargo run -- auth logout` or equivalent | pass | clears local-dev marker and does not modify runtime/jobs/cases/shell/client |
| sdk | docs validation | not run | README-only change; no obvious fast documented command |
| loom | docs validation | not run | README-only change; no Rust source changed in Loom |

## Required Post-Edit Scans

CLI scan:

```bash
cd ~/Developer/YAI/cli
rg -n "local-dev|local_dev|Local-dev|local development auth|local-dev auth|principal|Production account: none|No case://user was created|Session: legacy" src README.md MIGRATION_MAP.md
```

Result: matches in changed auth implementation and CLI docs.

Cross-repo scan:

```bash
rg -n "local-dev auth|local development auth|local-dev:<|No production account|No entitlement|No machine authorization|No case://user" ~/Developer/YAI/api ~/Developer/YAI/cli ~/Developer/YAI/sdk ~/Developer/YAI/loom
```

Result: matches in V4 docs, CLI implementation, CLI README, SDK README and Loom
README.

Forbidden scan:

```bash
rg -n "auth login succeeded|production account connected|token saved|Supabase login|device login complete|entitlement granted|machine authorized|case://user created|session created|session updated" ~/Developer/YAI/cli ~/Developer/YAI/api ~/Developer/YAI/sdk ~/Developer/YAI/loom
```

Result: no V4 fake production/account/session/case claims. Matches, if any, are
negative/deferred policy text such as no `case://user` creation.

## Findings

### Finding A - Local Dev Auth Exists

V4 introduces a local-only auth path for development use.

### Finding B - Local Dev Auth Is Not Account Auth

V4 does not connect production account identity, Supabase, OAuth, device login or
external account provider.

### Finding C - Local Dev Auth Does Not Create Root Case

V4 does not create `case://user`; V6 owns that wave.

### Finding D - Local Dev Auth Does Not Own Session

V4 does not mutate or revive `session` as an auth model. Session remains legacy
compatibility only.

### Finding E - V5 Can Stabilize Principal Model

With local-dev principal tracking in place, V5 can define/stabilize
principal/account_ref/auth_context semantics.

## V4 Completion Checklist

* [x] `docs/waves/v4-local-dev-auth.md` exists
* [x] `yai auth login --local-dev` implemented or truthfully wired
* [x] local-dev principal format recorded
* [x] local-dev marker path recorded
* [x] `yai auth status` reports local-dev or unauthenticated posture
* [x] `yai auth logout` clears local-dev marker or no-ops truthfully
* [x] no production login implemented
* [x] no Supabase/device/OAuth implemented
* [x] no account_ref created
* [x] no entitlement_ref created
* [x] no machine_authorization_ref created
* [x] no case://user created
* [x] no active case selected
* [x] no session mutation added
* [x] no runtime/job/case/shell lifecycle mutation added
* [x] no SDK auth client implementation added
* [x] no Loom behavior implementation added
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched

## Pass Criteria

* [x] V4 report exists
* [x] `yai auth login --local-dev` is available or truthfully wired in CLI
* [x] local-dev auth state is explicit and local-only
* [x] `yai auth status` distinguishes local-dev from unauthenticated
* [x] `yai auth logout` clears local-dev state or no-ops truthfully
* [x] no fake production auth is introduced
* [x] no root case is created
* [x] no session ownership is revived
* [x] no runtime/case/job/shell/client lifecycle is changed
* [x] validation results are recorded truthfully
* [x] unrelated working-tree changes are untouched
