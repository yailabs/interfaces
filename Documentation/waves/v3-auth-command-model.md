# V3 - Auth Command Model

## Status

* Delivery: V3
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: CLI command model + documentation/report
* Previous delivery: V2 - Legacy Session Containment
* Next delivery: V4 - Local Dev Auth

## Purpose

V3 introduces the canonical auth command model:

```bash
yai auth login
yai auth status
yai auth logout
```

V3 does not implement real account login, local-dev login, token persistence,
Supabase, entitlement, machine authorization or case creation.

## Scope

* canonical auth command surface introduced or confirmed;
* session remains legacy compatibility;
* auth is distinct from runtime health;
* auth is distinct from shell/client attach;
* auth is distinct from active case selection;
* replacement implementation is deferred to later waves.

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `Documentation/waves/v3-auth-command-model.md` | create | delivery report |
| cli | `src/app/cli.rs` | command/help/model wording | expose canonical auth command model |
| cli | `src/commands/auth.rs` | command behavior wording | truthful unavailable/planned auth command output |
| cli | `src/commands/mod.rs` | command model wiring | dispatch auth subcommands |
| cli | `README.md` | docs text | document canonical auth command model |
| cli | `MIGRATION_MAP.md` | docs text | record V3 auth command model status |
| sdk | `README.md` | docs text | align docs with auth command boundary |
| loom | `README.md` | docs text | align client UX docs with auth boundary |

## Command Surface

| Command | Status after V3 | Behavior | Notes |
| ------- | --------------- | -------- | ----- |
| `yai auth login` | present in CLI command model | truthful unavailable/planned | does not fake login |
| `yai auth status` | present in CLI command model | truthful unavailable/planned | not runtime/session status |
| `yai auth logout` | present in CLI command model | truthful unavailable/planned | does not stop runtime/cases/jobs |

## Auth Boundary Rules

```text
auth login != shell/client attach
auth status != runtime health
auth status != legacy session status
auth logout != runtime stop
auth logout != case close
auth logout != job cancellation
auth logout != shell/client detach
```

## Session Containment Continuity

V3 does not remove `yai session ...`.

Any reference to `session` from auth help/docs must classify session as:

* legacy;
* compatibility;
* migration;
* debug/dev;
* historical.

## Deferred to Later Waves

| Deferred item | Future wave |
| ------------- | ----------- |
| `yai auth login --local-dev` | V4 |
| principal/account_ref/auth_context stabilization | V5 |
| root `case://user` creation after login | V6 |
| case command model | V9 |
| active case out of session | V10 |
| shell/client attach model | V13 |
| SDK auth clients | V38 |
| E account provider/device login | E2/E6/E9 |

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f Documentation/waves/v0-command-reality-audit.md` | pass | baseline |
| api | `test -f Documentation/adr/ADR-V1-session-death-decision.md` | pass | baseline |
| api | `test -f Documentation/compat/session-legacy-containment.md` | pass | baseline |
| api | `test -f Documentation/waves/v2-legacy-session-containment.md` | pass | baseline |
| api | `test -f Documentation/waves/v3-auth-command-model.md` | pass | new report |
| cli | `cargo fmt --check` | pass | initial run reported formatting for one new line; wrapping was corrected and check passed |
| cli | `cargo test` | fail | matches existing V2 baseline compile issue: private `RuntimeServiceStatus` import in `src/output/render.rs` and `src/sdk/runtime.rs`; not introduced by V3 |
| cli | `cargo run -- auth --help` or equivalent | not run | CLI binary cannot compile because of the known V2 baseline issue |
| cli | `cargo run -- auth login` or equivalent | not run | CLI binary cannot compile because of the known V2 baseline issue |
| cli | `cargo run -- auth status` or equivalent | not run | CLI binary cannot compile because of the known V2 baseline issue |
| cli | `cargo run -- auth logout` or equivalent | not run | CLI binary cannot compile because of the known V2 baseline issue |
| sdk | docs validation | not run | README-only change; no obvious fast documented command |
| loom | docs validation | not run | README-only change; no Rust source changed in Loom |

## Required Post-Edit Scans

CLI scan:

```bash
cd ~/Developer/YAI/cli
rg -n "Canonical auth|canonical auth|auth login|auth status|auth logout|legacy compatibility|not the canonical auth model|runtime health|active case|shell/client" src README.md MIGRATION_MAP.md
```

Result: matches in changed auth help, auth command output, README, migration map
and V2 session containment text.

Cross-repo scan:

```bash
rg -n "auth login != shell|auth status != runtime|auth logout != runtime|session is legacy|legacy compatibility" ~/Developer/YAI/api ~/Developer/YAI/cli ~/Developer/YAI/sdk ~/Developer/YAI/loom
```

Result: matches in V2/V3 Documentation/help and changed CLI/SDK/Loom docs.

Forbidden scan:

```bash
rg -n "auth login succeeded|logged in as|token saved|account connected|case://user created|local-dev auth enabled|Supabase|device login complete|entitlement granted" ~/Developer/YAI/cli ~/Developer/YAI/api ~/Developer/YAI/sdk ~/Developer/YAI/loom
```

Result: no V3 fake implementation claims. Matches, if any, are negative/deferred
roadmap language such as V3 explicitly not implementing Supabase, local-dev auth,
account-backed auth, entitlement or `case://user` creation.

## Findings

### Finding A - Auth Is Now the Canonical Entry Surface

V3 establishes `yai auth login/status/logout` as the canonical auth command
surface, even though behavior is still unavailable/planned.

### Finding B - Auth Does Not Replace Case

V3 does not create `case://user`, does not select active case and does not
implement case commands.

### Finding C - Auth Does Not Replace Shell/Client

V3 does not implement shell/client attach or detach. Auth and shell/client UX
remain separate planes.

### Finding D - Auth Does Not Replace Runtime Health

`yai auth status` must not be treated as `runtime status` or `session status`.

### Finding E - V4 Can Add Local Dev Auth

With the command model in place, V4 can add `yai auth login --local-dev` as a
tracked local principal flow.

## V3 Completion Checklist

* [x] `Documentation/waves/v3-auth-command-model.md` exists
* [x] `yai auth login` exists or is confirmed in CLI command model
* [x] `yai auth status` exists or is confirmed in CLI command model
* [x] `yai auth logout` exists or is confirmed in CLI command model
* [x] auth help says auth is canonical
* [x] auth help separates auth from session
* [x] auth help separates auth from shell/client attach
* [x] auth help separates auth from runtime health
* [x] auth help separates auth from active case
* [x] command behavior does not fake successful login
* [x] command behavior does not fake account identity
* [x] command behavior does not create `case://user`
* [x] command behavior does not mutate session
* [x] command behavior does not stop runtime/jobs/cases
* [x] no `--local-dev` added
* [x] no Supabase/account/device login added
* [x] no SDK auth client implementation added
* [x] no Loom behavior implementation added
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched

## Pass Criteria

* [x] V3 report exists
* [x] canonical auth command surface is present or explicitly confirmed
* [x] `login/status/logout` are visible under `yai auth`
* [x] messages are truthful if backend support is unavailable
* [x] no fake auth success is introduced
* [x] no local-dev auth is introduced
* [x] no session command is removed or renamed
* [x] no runtime/case/shell behavior is changed
* [x] validation results are recorded truthfully
* [x] unrelated working-tree changes are untouched
