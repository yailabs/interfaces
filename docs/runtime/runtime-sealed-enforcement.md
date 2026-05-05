# Runtime Sealed Enforcement

## Status

* Delivery: V14
* Status: active local enforcement model
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Purpose

Define V14 sealed posture enforcement.

## Core Rule

```text
runtime running != runtime authorized
runtime healthy != operational actions allowed
client attached != login
auth login != shell
case selected != session
```

## Local CLI Enforcement

| Surface | Allowed while sealed | Operational |
| ------- | -------------------- | ----------- |
| `yai auth status` | yes | no |
| `yai runtime status` | yes | no |
| `yai case status` | yes, truthful posture | no/inspection |
| `yai case open` | no | yes |
| `yai case enter` | no | yes |
| `yai case close` | no | yes |
| `yai shell ...` | yes if truthful-unavailable | no domain mutation |

## Required Posture

| Requirement | Owner |
| ----------- | ----- |
| auth context | auth plane |
| root case | case plane |
| case tree | case plane |
| active_case_ref | operator context |
| client invocation | client plane |
| shell UX | shell plane |
| session | legacy compatibility only |

## Boundary Rules

```text
sealed posture != runtime stopped
sealed posture != failed health check
sealed posture != session detached
sealed posture is an authorization/governance posture
session must not unseal runtime
shell attach must not unseal runtime
client connection must not unseal runtime
```

## Local V14 Behavior

Operational CLI actions are blocked when local posture is missing.

Truthful block language:

```text
Operational action blocked: runtime is sealed for this command.
Reason: missing auth context.
Use `yai auth login --local-dev` for local development auth.
Runtime health/status does not imply operational authorization.
Session was not used.
```

Other local block variants:

```text
Reason: missing root case.
Reason: case boundary not found.
Operational action blocked: active case safety.
```

`yai case status` remains readable while sealed and must report posture without
pretending that runtime health or local shell/client presence grants governed
authority.

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| runtime readiness projection | V15 |
| allowed/blocked surface matrix | V16 |
| service lifecycle boundary | V17 |
| SDK runtime surface alignment | V20 |
| CLI SDK-first wiring | V21 |
| logout policy | V27 |
