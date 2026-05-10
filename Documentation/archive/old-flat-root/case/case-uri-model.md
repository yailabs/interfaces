# Case URI Model

## Status

* Delivery: V7
* Status: active grammar model
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Purpose

Define canonical YAI case URI grammar.

## Canonical Roots

| URI | Meaning |
| --- | ------- |
| `case://<account-username>` | canonical root user case for a concrete principal/account username |
| `case://me` | alias for current principal's root case |
| `case://francesco` | current workspace example root case |
| `case://user` | generic placeholder / legacy provisional form; not persisted |

## Grammar

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

Reserved root references:

```text
case://<account-username>
case://me
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
case://me resolves to case://<account-username> for the currently authenticated principal.
In this workspace, case://me resolves to case://francesco.
```

Nested case examples:

```text
case://francesco/projects/site-e0-cleanup
case://francesco/projects/runtime-identity
case://francesco/research/whitepaper
case://francesco/releases/preview
case://francesco/private/notes
```

Alias example:

```text
case://me/projects/site-e0-cleanup
  resolves to case://francesco/projects/site-e0-cleanup
```

## Normalization

| Input | Normalized |
| ----- | ---------- |
| `case://francesco` | `case://francesco` |
| `case://me` | `case://francesco` |
| `case://francesco/` | `case://francesco` |
| `case://me/` | `case://francesco` |
| `case://francesco/projects/demo` | `case://francesco/projects/demo` |
| `case://me/projects/demo` | `case://francesco/projects/demo` |

## Valid Examples

| URI | Classification |
| --- | -------------- |
| `case://francesco` | root |
| `case://me` | root alias |
| `case://francesco/projects/site-e0-cleanup` | nested path |
| `case://francesco/projects/runtime-identity` | nested path |
| `case://francesco/research/whitepaper` | nested path |
| `case://francesco/releases/preview` | nested path |
| `case://francesco/private/notes` | nested path |

## Invalid Examples

| URI | Reason |
| --- | ------ |
| `session://user` | wrong scheme |
| `case:user` | malformed scheme |
| `case:/user` | malformed scheme |
| `case://user` | placeholder/provisional authority, not persisted |
| `case://session` | invalid authority |
| `case://account` | invalid authority |
| `case://francesco//` | empty path segment |
| `case://francesco/../x` | traversal segment forbidden |
| `case://francesco/./x` | dot segment forbidden |
| `case://francesco/projects/ demo` | space forbidden |
| `case://francesco/projects/Demo` | uppercase forbidden |
| `case://francesco/projects/demo?x=1` | query forbidden |
| `case://francesco/projects/demo#x` | fragment forbidden |

## Resolution

`case://me` resolves to `case://<account-username>` for the currently authenticated
principal.

For the current workspace, `case://me` resolves to `case://francesco`.

In V7, resolution is grammar-level only. It does not create a nested case.

## Boundary Rules

```text
case://<account-username> != session
case://<account-username> != account_ref
case://<account-username> != principal
case://<account-username> != shell/client attach
case://<account-username> != runtime readiness
case://<account-username> is root harness
case://me is an alias, not a separate root
case://user is placeholder/provisional and must not be persisted
nested paths are names, not created cases until V8/V9
active case selection is not implied by a URI
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| nested case tree persistence | V8 |
| case commands | V9 |
| active case operator context | V10 |
| operator context plane | V11 |
| case-bound jobs | V24 |
| evidence binding | V28 |
| knowledge binding | V29 |
