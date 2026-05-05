# V16 - Allowed / Blocked Surfaces

## Status

* Delivery: V16
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: allowed/blocked surface matrix documentation + local CLI classification/alignment
* Previous delivery: V15 - Runtime Readiness Projection
* Next delivery: V17 - Service Lifecycle Boundary

## Purpose

V16 defines the explicit allowed/blocked surface matrix.

## Scope

Record:

* allowed/blocked matrix documented;
* local CLI surfaces classified;
* inspection/status/readiness surfaces remain allowed while sealed;
* operational mutation surfaces remain blocked without required posture;
* auth bootstrap/cleanup exceptions documented;
* session does not authorize any blocked surface;
* shell/client presence does not authorize any blocked surface;
* no lifecycle/runtime control behavior added.

## Canonical Invocation

Record:

```bash
which yai
yai ...
```

Record:

* primary smoke uses `cargo run`: no
* primary smoke uses `YAI_CONFIG_HOME`: no
* primary smoke uses `YAI_ACCOUNT_USERNAME`: no
* path-bound `PATH=... yai` form reintroduced as canonical: no
* absolute installed CLI path reintroduced as canonical: no

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `docs/runtime/allowed-blocked-surfaces.md` | create | allowed/blocked matrix |
| api | `docs/waves/v16-allowed-blocked-surfaces.md` | create | delivery report |
| cli | `README.md` | docs | surface category alignment |
| cli | `MIGRATION_MAP.md` | docs | surface matrix alignment |
| cli | `src/app/cli.rs` | help text | command classification wording |

## Surface Matrix

| Surface | Category | Sealed behavior | Implemented result |
| ------- | -------- | --------------- | ------------------ |
| `yai auth status` | `inspection_allowed` | allowed | pass; reports sealed `missing_auth_context` when unauthenticated |
| `yai runtime status` | `inspection_allowed` | allowed | pass; reports lifecycle/health/readiness unavailable and separate local readiness posture |
| `yai case status` | `inspection_allowed` | allowed | pass; reports truthful sealed or ready posture without mutating state |
| `yai auth login --local-dev` | `auth_bootstrap_allowed` | allowed | pass; establishes local auth/root/tree posture |
| `yai auth logout` | `cleanup_allowed` | allowed | pass; clears auth marker and leaves root/tree markers intact |
| `yai case open` | `operational_requires_auth` | blocked without auth | pass; blocked unauthenticated, allowed after login |
| `yai case enter` | `operational_requires_case` | blocked without case | pass; blocked unauthenticated, allowed after case exists |
| `yai case leave` | `cleanup_allowed` | allowed/no-op | pass; clears active case without touching session |
| `yai case close` | `operational_requires_case` | blocked without case or if active | pass; blocked while target case is active, allowed after leave |
| `yai shell ...` | `ux_unavailable_allowed` | allowed if truthful | pass; truthful unavailable UX surface, exit `5` |
| `yai session ...` | `legacy_compatibility` | must not authorize | observed as legacy compatibility inspection; unavailable over missing runtime transport, exit `4` |

## Block Message Behavior

Current local CLI block messages:

```text
Operational action blocked: runtime is sealed for this command.
Reason: missing auth context.
Use `yai auth login --local-dev` for local development auth.
Runtime health/status does not imply operational authorization.
Session was not used.
```

```text
Operational action blocked: runtime is sealed for this command.
Reason: case boundary not found.
Use `yai case open <path-or-uri>` before selecting or closing this case.
Session was not used.
```

```text
Operational action blocked: active case safety.
Reason: target case is currently active.
Run `yai case leave` before closing this case.
Session was not used.
```

## Readiness Interaction

Record:

```text
operationalReadiness and sealReason explain why operational mutation is allowed
or blocked. They do not hide status/readiness/health inspection surfaces.
```

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f docs/runtime/allowed-blocked-surfaces.md` | pass | new runtime doc |
| api | `test -f docs/waves/v16-allowed-blocked-surfaces.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| cli | `cargo fmt --check` | pass | after formatting `src/app/cli.rs` |
| cli | `cargo test` | pass | warnings only |
| cli | `cargo build` | pass | warnings only |
| cli | `cargo install --path . --force` | pass | installed CLI successfully |
| shell | `which yai` | pass | resolved to the installed CLI in the current shell |
| shell | `yai auth status` | pass | inspection allowed; unauthenticated projected as sealed `missing_auth_context` |
| shell | no-auth `yai case status` | pass | inspection allowed; truthful sealed posture |
| shell | no-auth `yai case open projects/surface-check` | pass | expected blocked, exit `6` |
| shell | no-auth `yai case enter projects/surface-check` | pass | expected blocked, exit `6` |
| shell | no-auth `yai shell` | pass | UX unavailable allowed, exit `5` |
| shell | `yai auth login --local-dev` | pass | auth bootstrap allowed, exit `0` |
| shell | `yai case open projects/surface-check` | pass | allowed after auth, exit `0` |
| shell | `yai case enter projects/surface-check` | pass | allowed after case exists, exit `0` |
| shell | `yai case close projects/surface-check` | pass | expected blocked while active, exit `6` |
| shell | `yai case leave` | pass | cleanup allowed, exit `0` |
| shell | `yai case close projects/surface-check` | pass | allowed after leave, exit `0` |
| shell | cleanup `yai auth logout` | pass | cleanup allowed, exit `0`; root/tree markers retained by current CLI behavior |
| sdk | docs validation | not run | docs-only unless touched substantially |
| loom | docs validation | not run | docs-only unless touched substantially |

## Findings

### Finding A - Matrix Exists

Record:
V16 defines the local allowed/blocked surface matrix.

### Finding B - Inspection Remains Allowed

Record:
Health/status/readiness surfaces remain available while sealed if truthful and
non-mutating.

### Finding C - Operational Mutation Is Blocked

Record:
Mutating operational surfaces are blocked without required posture.

### Finding D - Auth Bootstrap And Cleanup Are Explicit

Record:
Auth bootstrap and cleanup commands are allowed exceptions with constrained
meaning.

### Finding E - Canonical Invocation Stayed Clean

Record:
V16 preserves the normalized command form:

```bash
which yai
yai ...
```

No path-bound invocation is reintroduced as the canonical operator flow.

### Finding F - V17 Can Separate Service Lifecycle

Record:
With surfaces classified, V17 can cleanly separate runtime lifecycle from
readiness/authorization.

## V16 Completion Checklist

* [x] `docs/runtime/allowed-blocked-surfaces.md` exists
* [x] `docs/waves/v16-allowed-blocked-surfaces.md` exists
* [x] surface categories documented
* [x] local CLI surfaces classified
* [x] inspection/status/readiness surfaces allowed while sealed
* [x] operational mutation blocked without posture
* [x] auth bootstrap exception documented
* [x] cleanup exception documented
* [x] shell UX unavailable surfaces allowed only if truthful
* [x] legacy session classified and not authorization source
* [x] runtime health not authorization source
* [x] no lifecycle/start/stop behavior added
* [x] no production auth added
* [x] no Supabase/database integration added
* [x] no account_ref/entitlement_ref/machine_authorization_ref added
* [x] no SDK runtime/client implementation added
* [x] no Loom behavior implementation added
* [x] installed CLI validation used
* [x] primary smoke does not use cargo run
* [x] primary smoke does not use YAI_CONFIG_HOME
* [x] primary smoke does not use YAI_ACCOUNT_USERNAME
* [x] path-bound `PATH=... yai` form not reintroduced as canonical
* [x] absolute CLI path not reintroduced as canonical
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
