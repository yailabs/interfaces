# Principal Model

## Status

* Delivery: V5
* Status: canonical identity vocabulary
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Previous delivery: V4 - Local Dev Auth
* Next delivery: V6 - Root User Case

## Purpose

This document defines the canonical identity vocabulary used by YAI core,
runtime, API, SDK, CLI and Loom.

V5 documents the model. It does not implement production account auth, external
entitlements, machine authorization, root case creation or runtime enforcement.

## Canonical Concepts

| Concept | Canonical meaning | V5 local-dev value | Owner |
| ------- | ----------------- | ------------------ | ----- |
| principal | authenticated actor identity | `local-dev:<value>` | V/auth plane |
| account_ref | external account reference | null | E/account platform |
| auth_context | resolved authorization posture | local-dev posture/documented | V auth/runtime boundary |
| entitlement_ref | entitlement reference | null | E entitlement platform |
| machine_authorization_ref | machine authorization reference | null | E/platform or future machine auth |
| case_ref | governed work boundary | null until V6 | V case plane |

## Definitions

### principal

The principal is the authenticated actor identity known to core/runtime.

In V4/V5 local-dev, the principal format is:

```text
local-dev:<value>
```

The principal is not an account, not a session, not runtime health and not a case
boundary.

### account_ref

`account_ref` is an external account reference.

It may be null in local-dev. It is owned by the E track/account platform, not by
the local CLI runtime.

### auth_context

`auth_context` is the resolved authorization posture presented to runtime and
clients.

In V5, this is documented as local-dev posture for local-dev auth. V5 does not
implement full runtime enforcement.

`auth_context` is not runtime lifecycle, runtime health, runtime readiness or
session status.

### entitlement_ref

`entitlement_ref` is an external entitlement reference.

It is null in local-dev. It is owned by the E entitlement/release platform.

### machine_authorization_ref

`machine_authorization_ref` is an external or local machine authorization
reference.

It is null in V5 local-dev unless a future wave explicitly introduces a machine
authorization model.

### case_ref

`case_ref` is the governed work boundary.

It remains null until V6 creates or ensures `case://user`. It is not session.

## Local Dev Marker

The V4 marker remains valid in V5:

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

Default path:

```text
~/.yai/auth/local-dev.json
```

When `YAI_CONFIG_HOME` is set:

```text
$YAI_CONFIG_HOME/auth/local-dev.json
```

## Boundary Language

The principal is the authenticated actor identity.
The account_ref is an external account reference, not the principal itself.
The auth_context is the resolved authorization posture, not runtime health.
The case_ref is the governed work boundary, not session.
Local-dev auth may have a principal without account_ref, entitlement_ref,
machine_authorization_ref or case_ref.

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

## Deferred

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
