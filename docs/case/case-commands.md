# Case Commands

## Status

* Delivery: V9
* Status: active local CLI command model
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Purpose

Define canonical YAI case commands.

## Commands

| Command | V9 behavior |
| ------- | ----------- |
| `yai case root` | print root case |
| `yai case list` | list local case tree manifest |
| `yai case open <path-or-uri>` | ensure nested case in manifest |
| `yai case enter <case>` | present but active selection deferred to V10 |
| `yai case leave` | present but active clearing deferred to V10 |
| `yai case status` | show root/tree/active-case posture |
| `yai case close <case>` | close nested case; root cannot be closed |

## Root Rules

```text
root form: case://<account-username>
current example: case://francesco
alias: case://me
placeholder only: case://user
```

## Open And Close

`yai case open <path-or-uri>` creates or ensures a nested case entry in the local
case tree manifest. Accepted input forms include:

```text
projects/site-e0-cleanup
case://francesco/projects/site-e0-cleanup
case://me/projects/site-e0-cleanup
```

All normalize to the concrete current-principal root:

```text
case://francesco/projects/site-e0-cleanup
```

`yai case close <case>` removes nested case entries from the manifest. It must
not close the root case, delete the root marker, delete auth state, mutate
session or mutate active case.

## Case Node Kind Inference

| Path prefix | Kind |
| ----------- | ---- |
| `projects/` | `project-case` |
| `research/` | `research-case` |
| `releases/` | `release-case` |
| `private/` | `private-case` |
| other | `generic-case` |

## Active Case Boundary

```text
V9 does not select active case.
V10 introduces operator_context.active_case_ref.
Session must not own active case.
```

`yai case enter <case>` and `yai case leave` are visible command surfaces in V9,
but they return truthful unavailable/deferred messaging until V10.

## Session Boundary

```text
case commands do not mutate session.
session remains legacy compatibility only.
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| active case operator context | V10 |
| operator context plane | V11 |
| shell/client attach model | V13 |
| runtime sealed enforcement | V14 |
| case-bound jobs | V24 |
| evidence binding | V28 |
| knowledge binding | V29 |
