# Active Case Ref

## Status

* Delivery: A3
* Status: active topology vocabulary
* Track: A - system/work case boundary
* Repo branch: `refoundation/phase-01`

## Purpose

Define active case ownership outside legacy session and outside client
attachment.

## Decision

Active case is owned by:

```text
operator_context.active_case_ref
```

It is not owned by session.
It is not owned by client connection state.

## Local V10 Behavior

```text
yai case enter <case>
  -> validates case exists
  -> writes operator_context.active_case_ref

yai case leave
  -> clears operator_context.active_case_ref
```

The local operator context marker is stored at:

```text
~/.yai/operator/context.json
```

or, when `YAI_CONFIG_HOME` is set:

```text
$YAI_CONFIG_HOME/operator/context.json
```

Current local marker shape:

```json
{
  "schema": "yai.operator-context.active-case.v1",
  "source": "cli",
  "principal": "local-dev:francesco",
  "root_case_ref": "case://francesco",
  "active_case_ref": "case://francesco/projects/site-e0-cleanup"
}
```

After `yai case leave`, `active_case_ref` is set to null and the marker is
retained.

## Boundary Rules

```text
active case != session
active case != auth login
active case != root case creation
active case != shell/client attach
active case != client subject
active case != client connection
active case != system/root case
active case != runtime readiness
active case must reference an existing case
case enter does not create cases
case leave does not close cases
```

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| full operator context plane | V11 |
| client/shell attach distinction | V12/V13 |
| runtime sealed enforcement | V14 |
| logout policy with active case/job | V27 |
| case-bound jobs | V24 |
| evidence binding | V28 |
| knowledge binding | V29 |
