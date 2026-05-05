# V5 - Principal Model

## Status

* Delivery: V5
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: identity model documentation + local-dev principal alignment
* Previous delivery: V4 - Local Dev Auth
* Next delivery: V6 - Root User Case

## Purpose

V5 stabilizes the canonical identity vocabulary:

```text
principal
account_ref
auth_context
entitlement_ref
machine_authorization_ref
case_ref
```

V5 prepares the root case work in V6 but does not create `case://user`.

## Scope

* principal model documented;
* local-dev principal model documented;
* account_ref boundary documented;
* auth_context boundary documented;
* entitlement_ref boundary documented;
* machine_authorization_ref boundary documented;
* case_ref remains null until V6;
* session remains legacy compatibility only.

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `docs/identity/principal-model.md` | create | canonical identity model |
| api | `docs/waves/v5-principal-model.md` | create | delivery report |
| cli | `src/commands/auth.rs` | implementation wording | align local-dev output with principal/auth_context vocabulary |
| cli | `README.md` | docs | align local-dev principal vocabulary |

## Principal Model

| Concept | Canonical meaning | V5 local-dev value | Owner |
| ------- | ----------------- | ------------------ | ----- |
| principal | authenticated actor identity | `local-dev:<value>` | V/auth plane |
| account_ref | external account reference | null | E/account platform |
| auth_context | resolved authorization posture | local-dev posture/documented | V auth/runtime boundary |
| entitlement_ref | entitlement reference | null | E entitlement platform |
| machine_authorization_ref | machine authorization reference | null | E/platform or future machine auth |
| case_ref | governed work boundary | null until V6 | V case plane |

## Local Dev Identity Shape

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

Actual local path from V4:

```text
~/.yai/auth/local-dev.json
```

or, when `YAI_CONFIG_HOME` is set:

```text
$YAI_CONFIG_HOME/auth/local-dev.json
```

## Boundary Rules

```text
principal != account_ref
principal != session
auth_context != runtime health
auth_context != session
account_ref may be null in local-dev
entitlement_ref may be null in local-dev
machine_authorization_ref may be null in local-dev
case_ref remains null until V6
session remains legacy compatibility only
```

## Command Behavior After V5

| Command | Expected behavior after V5 |
| ------- | -------------------------- |
| `yai auth login` | production login still unavailable/planned |
| `yai auth login --local-dev` | creates local-dev marker with canonical principal shape |
| `yai auth status` | reports principal and null refs truthfully |
| `yai auth logout` | clears local-dev marker without touching runtime/session/case |

## Deferred to Later Waves

| Deferred item | Future wave |
| ------------- | ----------- |
| root `case://user` creation after login | V6 |
| case URI grammar | V7 |
| case tree model | V8 |
| canonical case commands | V9 |
| active case out of session | V10 |
| operator context plane | V11 |
| runtime sealed enforcement | V14 |
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
| api | `test -f docs/waves/v4-local-dev-auth.md` | pass | baseline |
| api | `test -f docs/identity/principal-model.md` | pass | new identity doc |
| api | `test -f docs/waves/v5-principal-model.md` | pass | new report |
| cli | `cargo fmt --check` | pass | CLI source touched |
| cli | `cargo test` | pass | binary compiled as required |
| cli | `YAI_CONFIG_HOME=/tmp/yai-v5-auth-test cargo run -- auth login --local-dev` | pass | local-dev marker created |
| cli | `YAI_CONFIG_HOME=/tmp/yai-v5-auth-test cargo run -- auth status` | pass | reports local-dev principal/auth context and null refs |
| cli | `YAI_CONFIG_HOME=/tmp/yai-v5-auth-test cargo run -- auth logout` | pass | clears marker without touching runtime/session/case |
| sdk | docs validation | not run | no SDK files touched in V5 |
| loom | docs validation | not run | no Loom files touched in V5 |

## Post-Edit Scans

API scan:

```bash
cd ~/Developer/YAI/api
rg -n "principal|account_ref|auth_context|entitlement_ref|machine_authorization_ref|case_ref|local-dev|session remains legacy" docs/identity docs/waves
```

Result: matches in V5 identity docs and V5 report.

CLI scan:

```bash
cd ~/Developer/YAI/cli
rg -n "principal|account_ref|auth_context|entitlement_ref|machine_authorization_ref|case_ref|local-dev|Session remains legacy|Session: legacy" src README.md MIGRATION_MAP.md
```

Result: matches in local-dev auth implementation and CLI README.

Forbidden scan:

```bash
rg -n "account_ref: [^n]|entitlement_ref: [^n]|machine_authorization_ref: [^n]|case://user created|Root case: created|session created|session updated|production account connected|Supabase login|device login complete" ~/Developer/YAI/api ~/Developer/YAI/cli ~/Developer/YAI/sdk ~/Developer/YAI/loom
```

Result: no new fake account/entitlement/machine/case/session claims. Matches, if
any, are negative/deferred policy text.

## Findings

### Finding A - Principal Is Now Explicit

V5 defines the principal as the authenticated actor identity. In local-dev, the
principal format is `local-dev:<value>`.

### Finding B - Account Is External

V5 does not create account_ref. External account identity remains in E waves.

### Finding C - Auth Context Is Not Runtime Health

V5 distinguishes auth_context from runtime lifecycle, runtime health and runtime
readiness.

### Finding D - Case Ref Remains Deferred

V5 does not create `case://user`. V6 owns root case creation.

### Finding E - Session Remains Legacy

V5 does not revive session as an identity model. Session remains legacy
compatibility only.

## V5 Completion Checklist

* [x] `docs/identity/principal-model.md` exists
* [x] `docs/waves/v5-principal-model.md` exists
* [x] principal model documented
* [x] local-dev principal format documented
* [x] account_ref boundary documented
* [x] auth_context boundary documented
* [x] entitlement_ref boundary documented
* [x] machine_authorization_ref boundary documented
* [x] case_ref deferred to V6
* [x] session remains legacy compatibility
* [x] local-dev marker remains truthful
* [x] no production login implemented
* [x] no Supabase/device/OAuth implemented
* [x] no account_ref created
* [x] no entitlement_ref created
* [x] no machine_authorization_ref created
* [x] no case://user created
* [x] no active case selected
* [x] no session mutation added
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched

## Pass Criteria

* [x] V5 report exists
* [x] principal identity model doc exists
* [x] local-dev principal shape is documented and aligned
* [x] account_ref/auth_context/entitlement_ref/machine_authorization_ref/case_ref meanings are clear
* [x] local-dev marker remains local-only
* [x] no production account behavior is introduced
* [x] no root case is created
* [x] no session ownership is revived
* [x] validation results are recorded truthfully
* [x] unrelated working-tree changes are untouched
