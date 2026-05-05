# Allowed / Blocked Surfaces

## Status

* Delivery: V16
* Status: active local surface matrix
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Purpose

Define which surfaces remain available while sealed and which surfaces are
blocked until required posture exists.

## Canonical Invocation

```bash
which yai
yai ...
```

`cargo run`, `YAI_CONFIG_HOME`, and `YAI_ACCOUNT_USERNAME` are not canonical
operator-flow requirements.

## Surface Categories

| Category | Meaning |
| -------- | ------- |
| `inspection_allowed` | non-mutating status/readiness/help surface |
| `auth_bootstrap_allowed` | auth-establishing command allowed while sealed |
| `cleanup_allowed` | safe cleanup/no-op mutation |
| `operational_requires_auth` | mutating command requires auth/root posture |
| `operational_requires_case` | mutating command requires target case boundary |
| `operational_requires_active_case` | command requires active case |
| `ux_unavailable_allowed` | truthful unavailable UX surface |
| `legacy_compatibility` | legacy surface; must not authorize |

## Matrix

| Surface | Category | Sealed behavior | Notes |
| ------- | -------- | --------------- | ----- |
| `yai --help` | `inspection_allowed` | allowed | non-mutating command discovery |
| `yai auth status` | `inspection_allowed` | allowed | non-mutating auth posture |
| `yai runtime status` | `inspection_allowed` | allowed | transport may be unavailable |
| `yai case status` | `inspection_allowed` | allowed | truthful local posture |
| `yai shell --help` | `inspection_allowed` | allowed | non-mutating help |
| `yai shell` | `ux_unavailable_allowed` | allowed if truthful | UX-only unavailable surface |
| `yai shell list` | `ux_unavailable_allowed` | allowed if truthful | UX-only unavailable surface |
| `yai shell attach <id>` | `ux_unavailable_allowed` | allowed if truthful | must not log in or select case |
| `yai shell detach` | `ux_unavailable_allowed` | allowed if truthful | must not log out or stop runtime |
| `yai auth login --local-dev` | `auth_bootstrap_allowed` | allowed | establishes local auth posture |
| `yai auth logout` | `cleanup_allowed` | allowed | cleanup mutation; V27 owns final logout policy |
| `yai case root` | `operational_requires_auth` | blocked if missing auth/root/tree | inspection shape, but governed by local auth/root posture in current CLI |
| `yai case list` | `operational_requires_auth` | blocked if missing auth/root/tree | lists governed case tree |
| `yai case open <path-or-uri>` | `operational_requires_auth` | blocked if missing auth/root/tree | mutates case tree |
| `yai case enter <case>` | `operational_requires_case` | blocked if missing auth/case | mutates operator context |
| `yai case leave` | `cleanup_allowed` | allowed/no-op | clears operator context if present |
| `yai case close <case>` | `operational_requires_case` | blocked if missing auth/case or if active | mutates case tree |
| `yai session ...` | `legacy_compatibility` | must not authorize | compatibility only |

## Rules

```text
health/status/readiness surfaces are allowed while sealed
operational mutation is blocked without required posture
auth bootstrap is allowed because it establishes auth posture
cleanup commands may be allowed if safe and truthful
session must not authorize blocked operations
shell/client presence must not authorize blocked operations
runtime health must not authorize blocked operations
```

## Readiness Interaction

`operationalReadiness` and `sealReason` explain why operational mutation is
allowed or blocked. They do not hide status/readiness/health inspection
surfaces.

`runtime_transport_unavailable` remains a transport/lifecycle visibility issue.
It does not replace local auth, case, or operator-context posture.

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| service lifecycle boundary | V17 |
| dev wrapper boundary | V18 |
| runtime control plan | V19 |
| SDK runtime surface alignment | V20 |
| CLI SDK-first wiring | V21 |
| logout policy | V27 |
