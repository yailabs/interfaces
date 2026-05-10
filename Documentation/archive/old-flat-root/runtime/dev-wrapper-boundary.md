# Dev Wrapper Boundary

## Status

* Delivery: V18
* Status: active boundary model
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Purpose

Separate development wrappers from canonical runtime/service control.

## Definition

`dev-wrapper` is the canonical V18 term for a development/ops bootstrap
surface used to build, run, install, inspect, or locally supervise runtime
artifacts during development.

A `dev-wrapper` is not the canonical product control plane.

## Classification

| Surface | Classification | Domain owner? |
| ------- | -------------- | ------------- |
| `make yai` | `dev-wrapper/build` | no |
| `make info` | `dev-wrapper/inspection` | no |
| `make install` | `dev-wrapper/install` | no |
| `make install-service` | `dev-wrapper/service-bootstrap` | no |
| `launchd` / `systemd` unit | `service-manager` / ops | no domain ownership |
| installed `yai` CLI | canonical user command | command surface only |
| runtime carrier binary | service/internal runtime | no user/domain ownership |
| future `yai runtime control ...` | future control plan | V19+ |

## Boundary Rules

```text
dev-wrapper != canonical CLI command model
dev-wrapper != service manager
dev-wrapper != runtime readiness
dev-wrapper != authorization
dev-wrapper != auth login
dev-wrapper != case selection
dev-wrapper != operator context
dev-wrapper != shell/client attach
dev-wrapper != session
make/install-service can affect process installation or service bootstrap, but
does not make operational actions authorized
```

## Canonical Operator Flow

```bash
which yai
yai ...
```

Do not present Makefile/script/launchd commands as canonical domain commands.

## Local Interpretation

V18 keeps these distinctions explicit:

* successful `make yai` means the repository build surface produced the local
  runtime artifact; it does not imply auth posture, case posture, operator
  context, readiness, or authorization;
* successful `make install-service` means a host bootstrap/install surface
  completed; it does not imply the runtime is unsealed or operationally ready;
* a service manager may own process lifecycle, but it does not become the auth,
  case, shell, or session authority surface;
* installed `yai` remains the user-facing command surface even when repository
  build or service bootstrap surfaces exist nearby.

## Deferred

| Deferred item | Future wave |
| ------------- | ----------- |
| runtime control plan | V19 |
| SDK runtime surface alignment | V20 |
| CLI SDK-first wiring | V21 |
| detach semantics | V26 |
| logout policy | V27 |
