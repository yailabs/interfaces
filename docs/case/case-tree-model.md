# Case Tree Model

## Status

* Delivery: V8
* Status: active model
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Purpose

Define the nested case tree under the authenticated principal's root case.

## Root

| Concept | Value |
| ------- | ----- |
| Canonical form | `case://<account-username>` |
| Current example | `case://francesco` |
| Alias | `case://me` |
| Placeholder legacy/provisional form | `case://user` |

## Tree Shape

```text
case://<account-username>
  projects/
    site-e0-cleanup
    runtime-identity
  research/
    whitepaper
  releases/
    preview
  private/
    notes
```

Current example URIs:

```text
case://francesco/projects/site-e0-cleanup
case://francesco/projects/runtime-identity
case://francesco/research/whitepaper
case://francesco/releases/preview
case://francesco/private/notes
```

These examples define valid nested names. They are not persisted nested cases
until a case tree manifest or later case command creates them.

## Case Node Model

| Field | Meaning |
| ----- | ------- |
| `case_ref` | canonical case URI |
| `kind` | root-user-case, project-case, research-case, release-case, private-case, generic-case |
| `parent_case_ref` | parent case URI or null for root |
| `path` | path relative to root |
| `active` | false unless selected by operator context |
| `principal` | principal that owns the local root/tree |
| `created_by` | local creator/source if available |

## Manifest Shape

V8 implements a local root-only manifest at the same state root as the local-dev
auth marker:

```text
~/.yai/case/case-tree.json
```

or, when `YAI_CONFIG_HOME` is set:

```text
$YAI_CONFIG_HOME/case/case-tree.json
```

Current manifest shape:

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

The manifest contains only the root node in V8. It does not create project,
research, release or private nested cases.

## Boundary Rules

```text
case tree != session
case tree != account database
case tree != shell/client attach
case tree != runtime readiness
root case exists before nested cases
nested path names do not imply persisted nested cases unless present in the tree manifest
case tree existence does not imply active case selection
case://me is an alias, not a persisted node
case://user is placeholder/provisional, not persisted canonical value
session remains legacy compatibility only
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| case commands | V9 |
| active case operator context | V10 |
| operator context plane | V11 |
| shell/client attach model | V13 |
| runtime sealed enforcement | V14 |
| case-bound jobs | V24 |
| evidence binding | V28 |
| knowledge binding | V29 |
