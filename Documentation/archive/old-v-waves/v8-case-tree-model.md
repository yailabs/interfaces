# V8 - Case Tree Model

## Status

* Delivery: V8
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: case tree model documentation + optional local case tree manifest/index
* Previous delivery: V7 - Case URI Model
* Next delivery: V9 - Case Commands

## Purpose

V8 defines the nested case tree model under:

```text
case://<account-username>
```

Current local example:

```text
case://francesco
```

V8 does not implement the full case command model.

## Scope

Record:

* case tree model defined;
* root case is `case://<account-username>`;
* current example root is `case://francesco`;
* `case://me` remains alias;
* `case://user` is placeholder/provisional only;
* local case tree manifest/index added;
* no nested project cases were created;
* no active case selection added;
* session remains legacy compatibility only.

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `Documentation/case/case-tree-model.md` | create | canonical case tree model |
| api | `Documentation/waves/v8-case-tree-model.md` | create | delivery report |
| cli | `src/commands/auth.rs` | implementation | create root-only local case tree manifest after local-dev auth |
| cli | `README.md` | docs | document local case tree manifest boundary |
| cli | `MIGRATION_MAP.md` | docs | record V8 local manifest behavior |

## Case Tree Root

| Concept | Value |
| ------- | ----- |
| canonical root form | `case://<account-username>` |
| current example root | `case://francesco` |
| alias | `case://me` |
| non-canonical placeholder | `case://user` |

## Case Tree Manifest

| Field | Value |
| ----- | ----- |
| manifest implemented | yes |
| manifest path | `~/.yai/case/case-tree.json` or `$YAI_CONFIG_HOME/case/case-tree.json` |
| schema | `yai.case.tree.v1` |
| root_case_ref | `case://<account-username>` |
| current root_case_ref | `case://francesco` |
| nested cases created by V8 | no |
| active case selected | no |

Actual manifest JSON shape observed with
`YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v8-tree-test`:

```json
{
  "schema": "yai.case.tree.v1",
  "root_case_ref": "case://francesco",
  "principal": "local-dev:francesco",
  "cases": [
    {
      "case_ref": "case://francesco",
      "kind": "root-user-case",
      "parent_case_ref": null,
      "path": "",
      "active": false
    }
  ]
}
```

## Boundary Rules

```text
case tree != session
case tree != account database
case tree != shell/client attach
case tree != runtime readiness
case tree does not imply active case selection
case://me is an alias, not a persisted node
case://user is placeholder/provisional, not persisted canonical value
nested paths are only persisted cases when present in the tree manifest
```

## Command Behavior After V8

| Command | Expected behavior after V8 |
| ------- | -------------------------- |
| `yai auth login --local-dev` | still ensures root case; also ensures empty root-only tree manifest |
| `yai auth status` | still reports root case and active case none |
| `yai auth logout` | still clears auth marker; root/tree markers are retained |
| `yai case ...` | not expanded by V8 |

## Deferred to Later Waves

| Deferred item | Future wave |
| ------------- | ----------- |
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
| api | `test -f Documentation/waves/v0-command-reality-audit.md` | pass | baseline |
| api | `test -f Documentation/adr/ADR-V1-session-death-decision.md` | pass | baseline |
| api | `test -f Documentation/compat/session-legacy-containment.md` | pass | baseline |
| api | `test -f Documentation/waves/v2-legacy-session-containment.md` | pass | baseline |
| api | `test -f Documentation/waves/v3-auth-command-model.md` | pass | baseline |
| api | `test -f Documentation/waves/v4-local-dev-auth.md` | pass | baseline |
| api | `test -f Documentation/identity/principal-model.md` | pass | baseline |
| api | `test -f Documentation/waves/v5-principal-model.md` | pass | baseline |
| api | `test -f Documentation/case/root-user-case.md` | pass | baseline |
| api | `test -f Documentation/waves/v6-root-user-case.md` | pass | baseline |
| api | `test -f Documentation/case/case-uri-model.md` | pass | baseline |
| api | `test -f Documentation/waves/v7-case-uri-model.md` | pass | baseline |
| api | `test -f Documentation/case/case-tree-model.md` | pass | new tree doc |
| api | `test -f Documentation/waves/v8-case-tree-model.md` | pass | new report |
| cli | `cargo fmt --check` | pass | exact result |
| cli | `cargo test` | pass | exact result; warnings only |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v8-tree-test cargo run --quiet -- auth login --local-dev` | pass | root case and root-only tree manifest reported |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v8-tree-test cargo run --quiet -- auth status` | pass | root case reported; active case none |
| cli | inspect root marker JSON | pass | `case_ref: case://francesco` |
| cli | inspect case tree manifest JSON | pass | root-only `yai.case.tree.v1` manifest exists |
| cli | `YAI_ACCOUNT_USERNAME=francesco YAI_CONFIG_HOME=/tmp/yai-v8-tree-test cargo run --quiet -- auth logout` | pass | auth marker cleared; root/tree markers retained |
| sdk | docs validation | not run | no SDK files changed |
| loom | docs validation | not run | no Loom files changed |

## Findings

### Finding A - Case Tree Model Exists

V8 defines the nested case tree model under `case://<account-username>`.

### Finding B - Root Is Username-Based

The canonical root is not `case://user`; it is `case://<account-username>`.
For this local workspace, the example root is `case://francesco`.

### Finding C - `case://me` Remains Alias

`case://me` resolves to the current principal's root case and is not persisted
as a separate node.

### Finding D - No Active Case Yet

V8 does not select active case. V10 owns active case operator context.

### Finding E - V9 Can Add Case Commands

With URI grammar and tree model established, V9 can introduce canonical case
commands.

## V8 Completion Checklist

* [x] `Documentation/case/case-tree-model.md` exists
* [x] `Documentation/waves/v8-case-tree-model.md` exists
* [x] root form documented as `case://<account-username>`
* [x] current example documented as `case://francesco`
* [x] `case://me` alias documented
* [x] `case://user` placeholder/provisional status documented
* [x] case node model documented
* [x] manifest shape documented or implemented truthfully
* [x] no broad case command model implemented
* [x] no active case selection added
* [x] no session mutation added
* [x] no production auth added
* [x] no account_ref/entitlement_ref/machine_authorization_ref added
* [x] no SDK case client implementation added
* [x] no Loom behavior implementation added
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
