# Root User Case

## Status

* Delivery: V6
* Status: active local-dev model
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Definition

`case://<account-username>` is the canonical root operational case for the authenticated
principal.

For the current local-dev principal used in this workspace, the concrete root
case is:

```text
case://francesco
```

`case://user` is a generic placeholder / legacy provisional form. It is not the
canonical persisted root case value.

It is the root harness for nested cases, jobs, flows, agents, evidence, records,
knowledge and governed work.

## V6 Local-Dev Behavior

In V6, local-dev auth ensures a local root case marker:

```text
yai auth login --local-dev
  -> principal local-dev:<account-username>
  -> auth_context local-dev
  -> root case case://<account-username>
```

For the current workspace example, the account username is `francesco` and the
auth marker records `case_ref: case://francesco`. The root case marker is local and inspectable.
Logout clears local-dev auth but does not delete the root case marker.

## Boundary Rules

```text
case://<account-username> != session
case://<account-username> != account_ref
case://<account-username> != shell/client attach
case://<account-username> != production entitlement
case://<account-username> != active case selection unless an operator context explicitly selects it
case://<account-username> is the root harness, not a nested project case
case://user is placeholder/provisional and must not be persisted as the concrete root
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| case URI grammar | V7 |
| nested case tree | V8 |
| case commands | V9 |
| active case operator context | V10 |
| operator context plane | V11 |
| case-bound jobs | V24 |
| evidence binding | V28 |
| knowledge binding | V29 |
