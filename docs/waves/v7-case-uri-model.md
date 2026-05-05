# V7 - Case URI Model

## Status

* Delivery: V7
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: case URI grammar documentation + root naming correction
* Previous delivery: V6 - Root User Case
* Next delivery: V8 - Case Tree Model

## Purpose

V7 defines canonical case URI grammar:

```text
case://<account-username>
case://me
case://<account-username>/<nested-path>
case://me/<nested-path>
```

For the current workspace example:

```text
case://francesco
case://me
case://francesco/projects/site-e0-cleanup
case://me/projects/site-e0-cleanup
```

V7 does not create nested cases and does not implement the full case command
model.

## Scope

* case URI grammar defined;
* `case://<account-username>` canonical root defined;
* `case://francesco` recorded as the current workspace example;
* `case://me` alias defined;
* `case://user` reclassified as placeholder/provisional, not persisted;
* nested path syntax defined;
* normalization rules defined;
* invalid URI rules defined;
* no nested case persistence added;
* no active case selection added;
* session remains legacy compatibility only.

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `docs/case/case-uri-model.md` | create/update | canonical case URI grammar |
| api | `docs/case/root-user-case.md` | update | mark `case://user` provisional and document concrete root |
| api | `docs/waves/v6-root-user-case.md` | update | record V6 naming correction |
| api | `docs/waves/v7-case-uri-model.md` | create/update | delivery report |
| cli | `src/commands/auth.rs` | implementation correction | persist `case://<account-username>` instead of placeholder `case://user` |
| cli | `README.md` | docs | document account-username root case naming |
| cli | `MIGRATION_MAP.md` | docs | update auth migration note |

## URI Grammar

```text
case-uri        = "case://" case-authority [ "/" case-path ]

case-authority  = account-username | "me"

account-username = path-segment

case-path       = path-segment *( "/" path-segment )

path-segment    = lowercase token containing:
                  a-z
                  0-9
                  "-"
                  "_"
                  "."
```

Canonical root form:

```text
case://<account-username>
```

Current workspace example:

```text
case://francesco
```

Alias:

```text
case://me resolves to case://<account-username> for the current principal.
In this workspace, case://me resolves to case://francesco.
```

Placeholder/provisional form:

```text
case://user
```

`case://user` is not the canonical persisted root case value.

## Normalization Rules

| Input | Normalized | Notes |
| ----- | ---------- | ----- |
| `case://francesco` | `case://francesco` | current workspace root |
| `case://me` | `case://francesco` | current principal alias |
| `case://francesco/` | `case://francesco` | trailing root slash collapsed |
| `case://me/` | `case://francesco` | alias + trailing slash collapsed |
| `case://francesco/projects/demo` | `case://francesco/projects/demo` | nested path |
| `case://me/projects/demo` | `case://francesco/projects/demo` | alias nested path |

## Invalid URI Rules

| Invalid form | Reason |
| ------------ | ------ |
| non-`case://` scheme | wrong scheme |
| `case://user` as persisted value | placeholder/provisional, not concrete account username |
| empty authority | invalid authority |
| empty path segment | ambiguous path |
| `.` or `..` path segment | traversal/dot segment forbidden |
| uppercase path segment | non-canonical |
| spaces | non-canonical |
| query string | forbidden |
| fragment | forbidden |

## Root Case Compatibility

V6 initially used `case://user` as a provisional placeholder in docs and marker
behavior. V7 corrects the persisted local root marker to
`case://<account-username>`.

For local-dev, the CLI reads the username slug from:

```text
YAI_ACCOUNT_USERNAME
YAI_LOCAL_DEV_USER_SLUG
YAI_USER_SLUG
USER / USERNAME fallback
```

The account username is normalized to the case URI lowercase token grammar.

V7 does not delete existing root case markers automatically. A fresh local-dev
login writes the corrected root marker and auth marker.

## Command Behavior After V7

| Command | Expected behavior after V7 |
| ------- | -------------------------- |
| `yai auth login --local-dev` | ensures `case://<account-username>` |
| `yai auth status` | reports concrete root case |
| `yai auth logout` | clears auth marker but retains root case marker |
| `yai case ...` | not expanded by V7 |

## Boundary Rules

```text
case://<account-username> != session
case://me != new root case
case://user != canonical persisted root
case URI != account_ref
case URI != entitlement_ref
case URI != machine_authorization_ref
case URI != shell/client attach
case URI != runtime readiness
case URI != active case selection
nested URI path != persisted nested case until V8/V9
```

## Deferred to Later Waves

| Deferred item | Future wave |
| ------------- | ----------- |
| nested case tree persistence | V8 |
| canonical case commands | V9 |
| active case out of session | V10 |
| operator context plane | V11 |
| shell/client attach model | V13 |
| runtime sealed enforcement | V14 |
| case-bound jobs | V24 |
| case evidence binding | V28 |
| knowledge binding | V29 |

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f docs/waves/v0-command-reality-audit.md` | pass | baseline |
| api | `test -f docs/adr/ADR-V1-session-death-decision.md` | pass | baseline |
| api | `test -f docs/compat/session-legacy-containment.md` | pass | baseline |
| api | `test -f docs/waves/v2-legacy-session-containment.md` | pass | baseline |
| api | `test -f docs/waves/v3-auth-command-model.md` | pass | baseline |
| api | `test -f docs/waves/v4-local-dev-auth.md` | pass | baseline |
| api | `test -f docs/identity/principal-model.md` | pass | baseline |
| api | `test -f docs/waves/v5-principal-model.md` | pass | baseline |
| api | `test -f docs/case/root-user-case.md` | pass | baseline |
| api | `test -f docs/waves/v6-root-user-case.md` | pass | baseline |
| api | `test -f docs/case/case-uri-model.md` | pass | new URI doc |
| api | `test -f docs/waves/v7-case-uri-model.md` | pass | new report |
| cli | `cargo fmt --check` | pass | run because every wave recompiles/checks CLI |
| cli | `cargo test` | pass | run because every wave recompiles/checks CLI |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v7-uri-test cargo run -- auth login --local-dev` | pass | smoke check; root case `case://francesco` |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v7-uri-test cargo run -- auth status` | pass | root case `case://francesco` reported |
| sdk | docs validation | not run | SDK not touched in V7 |
| loom | docs validation | not run | Loom not touched in V7 |

## Post-Edit Scans

```bash
cd ~/Developer/YAI/api
rg -n "case://<account-username>|case://francesco|case://me|case URI|Case URI|placeholder|provisional|nested path|session remains legacy" docs/case docs/waves
```

Result: matches in V7 docs.

```bash
rg -n "case://francesco|case://me|case://francesco/projects|case://me/projects|nested path|case URI|case://user.*placeholder|case://user.*provisional" ~/Developer/YAI/api ~/Developer/YAI/cli ~/Developer/YAI/sdk ~/Developer/YAI/loom
```

Result: matches in V7 docs and touched CLI docs.

Forbidden scan:

```bash
rg -n "nested case created|project case created|active case selected|case://me root marker|case://me created|session created|session updated|case URI grants entitlement|case URI authorizes machine|case://user.*canonical root" ~/Developer/YAI/api ~/Developer/YAI/cli ~/Developer/YAI/sdk ~/Developer/YAI/loom
```

Result: no new fake nested-case, active-case, session, entitlement, machine
authorization, or canonical `case://user` claims from V7. Matches, if any, are
negative/deferred/provisional policy text.

## Findings

### Finding A - Case URI Grammar Exists

V7 defines the canonical syntax for concrete account-username roots and nested
case references.

### Finding B - `case://me` Is an Alias

`case://me` resolves to the current principal root, such as
`case://francesco`. It is not a separate persisted root case.

### Finding C - `case://user` Is Provisional

`case://user` is a generic placeholder / legacy provisional form. It must not be
persisted as the concrete root case value.

### Finding D - Nested Paths Are Names Only

Nested URI paths are valid names, but V7 does not persist nested cases. V8 owns
case tree persistence.

### Finding E - URI Does Not Select Active Case

A URI reference does not itself select active case. V10 owns operator context
active case refactor.

### Finding F - V8 Can Build the Case Tree

With URI grammar fixed, V8 can implement or document the nested case tree model.

## V7 Completion Checklist

* [x] `docs/case/case-uri-model.md` exists
* [x] `docs/waves/v7-case-uri-model.md` exists
* [x] `case://<account-username>` defined as canonical root form
* [x] `case://francesco` recorded as workspace example
* [x] `case://me` defined as alias
* [x] `case://user` classified as placeholder/provisional
* [x] nested path grammar defined
* [x] normalization rules defined
* [x] invalid URI rules defined
* [x] root case compatibility with V6 correction recorded
* [x] no nested case persistence added
* [x] no active case selection added
* [x] no session mutation added
* [x] no production auth added
* [x] no account_ref/entitlement_ref/machine_authorization_ref added
* [x] no SDK case client implementation added
* [x] no Loom behavior implementation added
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched

## Pass Criteria

* [x] V7 report exists
* [x] case URI model doc exists
* [x] concrete root and `case://me` semantics are clear
* [x] nested path grammar is clear
* [x] invalid forms are documented
* [x] V6 root marker naming is corrected
* [x] no nested cases are created
* [x] no active case is selected
* [x] no session ownership is revived
* [x] validation results are recorded truthfully
* [x] unrelated working-tree changes are untouched
