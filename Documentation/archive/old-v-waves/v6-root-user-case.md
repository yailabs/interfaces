# V6 - Root User Case

## Status

* Delivery: V6
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: local root case marker implementation + documentation/report
* Previous delivery: V5 - Principal Model
* Next delivery: V7 - Case URI Model

## Purpose

V6 creates or ensures:

```text
case://<account-username>
```

after successful local-dev auth.

V6 creates the root operational harness but does not implement nested cases or
the full case command model.

Correction after V7: the earlier `case://user` wording is provisional
placeholder language. The persisted local root case is
`case://<account-username>`. For the current workspace, that value is
`case://francesco`.

## Scope

* local root case marker added;
* `yai auth login --local-dev` ensures `case://<account-username>`;
* auth marker now records `case_ref: case://<account-username>`;
* `yai auth status` reports root case truthfully;
* logout does not delete root case marker;
* no nested cases were implemented;
* no active case operator context was implemented;
* session remains legacy compatibility only.

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `Documentation/case/root-user-case.md` | create | root user case model |
| api | `Documentation/waves/v6-root-user-case.md` | create | delivery report |
| cli | `src/commands/auth.rs` | implementation | ensure local root case after local-dev auth |
| cli | `README.md` | docs | document V6 root case marker behavior |
| cli | `MIGRATION_MAP.md` | docs | update auth migration status |

## Root Case State

| Field | Value |
| ----- | ----- |
| root case ref | `case://francesco` in this workspace; `case://<account-username>` generally |
| root case marker path | `~/.yai/case/root-user.json`, or `$YAI_CONFIG_HOME/case/root-user.json` |
| auth marker `case_ref` | `case://francesco` in this workspace |
| principal | `local-dev:francesco` in this workspace |
| account_ref | null |
| entitlement_ref | null |
| machine_authorization_ref | null |
| active case selected | no |
| session mutation | none |

## Root Case Marker Shape

Actual marker shape:

```json
{
  "schema": "yai.case.root-user.v1",
  "case_ref": "case://francesco",
  "kind": "root-user-case",
  "principal": "local-dev:francesco",
  "source": "cli-local-dev-auth",
  "parent_case_ref": null,
  "active": false
}
```

The V6 verification run observed the same shape at:

```text
/tmp/yai-v6-root-case-test/case/root-user.json
```

## Command Behavior After V6

| Command | Expected behavior after V6 |
| ------- | -------------------------- |
| `yai auth login` | production login still unavailable/planned |
| `yai auth login --local-dev` | creates local-dev auth marker and ensures `case://<account-username>` |
| `yai auth status` | reports principal, auth_context and root case |
| `yai auth logout` | clears auth marker; root case marker is not deleted |

## Boundary Rules

```text
case://<account-username> != session
case://<account-username> != account_ref
case://<account-username> != entitlement_ref
case://<account-username> != machine_authorization_ref
case://<account-username> != shell/client attach
case://<account-username> != active case selection unless operator context explicitly selects it
case://<account-username> is root harness, not nested project case
case://user is placeholder/provisional and must not be persisted
```

## Deferred to Later Waves

| Deferred item | Future wave |
| ------------- | ----------- |
| case URI grammar beyond placeholder `case://user` | V7 |
| nested case tree model | V8 |
| canonical case commands | V9 |
| active case out of session | V10 |
| operator context plane | V11 |
| shell/client attach model | V13 |
| runtime sealed enforcement | V14 |
| case-bound jobs | V24 |
| case evidence binding | V28 |
| knowledge binding | V29 |
| external account/provider auth | E2/E6/E9 |
| entitlement evaluation | E18/E19/E20 |

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f Documentation/waves/v0-command-reality-audit.md` | pass | baseline |
| api | `test -f Documentation/adr/ADR-V1-session-death-decision.md` | pass | baseline |
| api | `test -f Documentation/compat/session-legacy-containment.md` | pass | baseline |
| api | `test -f Documentation/waves/v2-legacy-session-containment.md` | pass | baseline |
| api | `test -f Documentation/waves/v3-auth-command-model.md` | pass | baseline |
| api | `test -f Documentation/waves/v4-local-dev-auth.md` | pass | baseline |
| api | `test -f Documentation/identity/principal-model.md` | pass | baseline |
| api | `test -f Documentation/waves/v5-principal-model.md` | pass | baseline |
| api | `test -f Documentation/case/root-user-case.md` | pass | new case doc |
| api | `test -f Documentation/waves/v6-root-user-case.md` | pass | new report |
| cli | `cargo fmt --check` | pass | exact result |
| cli | `cargo test` | pass | exact result; warnings only |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v6-root-case-test cargo run -- auth login --local-dev` | pass | output reports root case `case://francesco` |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v6-root-case-test cargo run -- auth status` | pass | reports `Root case: case://francesco` and `Active case: none` |
| cli | inspect auth marker JSON | pass | verified `case_ref: case://francesco` |
| cli | inspect root case marker JSON | pass | verified `yai.case.root-user.v1` marker exists |
| cli | `YAI_CONFIG_HOME=/tmp/yai-v6-root-case-test cargo run -- auth logout` | pass | clears auth marker and reports root marker retained |
| cli | post-logout root marker check | pass | root marker retained; auth marker cleared |
| sdk | docs validation | not run | SDK not touched in V6 |
| loom | docs validation | not run | Loom not touched in V6 |

## Post-Edit Scans

```bash
cd ~/Developer/YAI/api
rg -n "case://user|root operational case|root harness|Root User Case|session|active case|operator context" Documentation/case Documentation/waves
```

Result: matches in V6 root case docs and delivery report.

```bash
cd ~/Developer/YAI/cli
rg -n "case://user|Root case|root case|case_ref|root-user-case|yai.case.root-user.v1|Session remains legacy|Session: legacy" src README.md MIGRATION_MAP.md
```

Result: matches in changed CLI implementation/docs.

Forbidden scan:

```bash
rg -n "case://user created by Supabase|production account connected|entitlement granted|machine authorized|active case selected|session created|session updated|nested case created|project case created" ~/Developer/YAI/api ~/Developer/YAI/cli ~/Developer/YAI/sdk ~/Developer/YAI/loom
```

Result: no new fake production, entitlement, machine authorization, session or
nested-case claims from V6. Any matches are negative/deferred policy text.

## Findings

### Finding A - Root Case Exists

V6 ensures `case://<account-username>` after local-dev auth.

### Finding B - Root Case Is the Harness

`case://<account-username>` is the root operational harness for future nested
cases and governed work. In this workspace, that is `case://francesco`.

### Finding C - Root Case Is Not Session

V6 does not revive session. Session remains legacy compatibility only.

### Finding D - Root Case Is Not Active Case Selection

V6 does not select active case. V10 owns active case operator context.

### Finding E - V7 Can Define Case URI Grammar

With the concrete root present, V7 defines URI grammar including `case://me` and
nested paths.

## V6 Completion Checklist

* [x] `Documentation/case/root-user-case.md` exists
* [x] `Documentation/waves/v6-root-user-case.md` exists
* [x] local root case marker exists after `yai auth login --local-dev`
* [x] auth marker records `case_ref: case://francesco` in this workspace
* [x] `yai auth status` reports `Root case: case://francesco` in this workspace
* [x] root case marker path recorded
* [x] logout root marker policy recorded
* [x] no nested cases implemented
* [x] no active case operator context implemented
* [x] no production login implemented
* [x] no Supabase/device/OAuth implemented
* [x] no account_ref created
* [x] no entitlement_ref created
* [x] no machine_authorization_ref created
* [x] no session mutation added
* [x] no runtime/job/shell lifecycle mutation added
* [x] no SDK case client implementation added
* [x] no Loom behavior implementation added
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched

## Pass Criteria

* [x] V6 report exists
* [x] root user case doc exists
* [x] `yai auth login --local-dev` ensures `case://<account-username>`
* [x] auth marker has `case_ref: case://francesco` in this workspace
* [x] root case marker exists and is local-only
* [x] `yai auth status` reports root case truthfully
* [x] root case is not represented as session
* [x] no nested case tree is implemented
* [x] no active case overclaim is introduced
* [x] no production account behavior is introduced
* [x] validation results are recorded truthfully
* [x] unrelated working-tree changes are untouched
