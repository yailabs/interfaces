# V15 - Runtime Readiness Projection

## Status

* Delivery: V15
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: runtime readiness projection documentation + local CLI status/readiness output alignment
* Previous delivery: V14 - Runtime Sealed Enforcement
* Next delivery: V16 - Allowed/Blocked Surfaces

## Purpose

V15 aligns local status output to canonical readiness projection fields:

```text
operationalReadiness
sealReason
```

## Scope

Record:

* readiness projection model documented;
* local status output aligned where implemented;
* runtime lifecycle/health/readiness separated from operational authorization;
* runtime transport unavailable reported separately;
* session ignored as authorization source;
* no production backend added;
* no full runtime transport implemented.

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `Documentation/runtime/runtime-readiness-projection.md` | create | readiness projection model |
| api | `Documentation/waves/v15-runtime-readiness-projection.md` | create | delivery report |
| cli | `src/output/readiness.rs` | create | local readiness projection helper |
| cli | `src/output/mod.rs` | update | expose readiness helper |
| cli | `src/output/render.rs` | update | runtime readiness rendering |
| cli | `src/commands/runtime.rs` | update | runtime status readiness projection |
| cli | `src/commands/auth.rs` | update | auth status readiness wording alignment |
| cli | `src/commands/case.rs` | update | case status readiness wording alignment |
| cli | `tests/output_snapshot.rs` | update | runtime status JSON snapshot alignment |
| cli | `README.md` | update | V15 readiness wording |
| cli | `MIGRATION_MAP.md` | update | runtime/case/auth readiness notes |
| sdk | `README.md` | update | readiness boundary clarification |
| loom | `README.md` | update | readiness boundary clarification |

## Projection Fields

| Field | Status after V15 | Notes |
| ----- | ---------------- | ----- |
| `lifecycle` | implemented | projected from runtime transport envelope when available; `unavailable` when transport is unavailable |
| `health` | implemented | projected from runtime transport envelope when available; `unavailable` when transport is unavailable |
| `readiness` | implemented | projected from runtime transport envelope when available; `unavailable` when transport is unavailable |
| `operationalReadiness` | implemented | projected locally from auth/root/tree/operator posture |
| `sealReason` | implemented | explicit local reason such as `missing_auth_context` or `missing_operator_context` |
| `authPosture` | implemented | `unauthenticated`, `local-dev`, or `authenticated` |
| `casePosture` | implemented | local CLI uses `unavailable`, `missing_root`, `root_present/missing_tree`, or `root_present/tree_present` |
| `operatorContextPosture` | implemented | local CLI uses `unavailable`, `active_case_missing`, or `active_case_present` |
| `clientPosture` | implemented | local CLI projects `cli-one-shot` |
| `sessionPosture` | implemented | local CLI projects `legacy_ignored` |

## Local State Projection

| Local state | operationalReadiness | sealReason | Observed result |
| ----------- | -------------------- | ---------- | --------------- |
| no auth | sealed | `missing_auth_context` | projected in `yai auth status`, `yai case status`, and `yai runtime status` |
| auth only | blocked | `missing_operator_context` | current local-dev login ensures root/tree, so observed as auth/root/tree/no active |
| auth + root/tree + no active case | blocked | `missing_operator_context` | projected after `yai auth login --local-dev` |
| auth + root/tree + active case | ready | `none` | projected after `yai case open` + `yai case enter` |
| runtime transport unavailable | transport unavailable | separate lifecycle/transport | lifecycle/health/readiness stay `unavailable`; local auth/case/operator posture remains visible |

## Runtime Status Output

Installed `yai runtime status` now reports:

```text
Runtime status:
Lifecycle: unavailable
Health: unavailable
Readiness: unavailable
Transport: runtime_transport_unavailable

Operational readiness: <local projection>
Seal reason: <local projection>

Auth posture: <local projection>
Case posture: <local projection>
Operator context posture: <local projection>
Client posture: cli-one-shot
Session posture: legacy_ignored
```

Required note:

```text
runtime_transport_unavailable does not imply operational authorization and does
not replace local auth/case/operator posture.
```

## Boundary Rules

Record:

```text
runtime running != runtime authorized
runtime healthy != operational actions allowed
client attached != login
auth login != shell
case selected != session
session is not a readiness source
```

## Installed CLI Validation

| Check | Result | Notes |
| ----- | ------ | ----- |
| installed CLI path | verify locally with `which yai` | installed CLI must resolve in the current shell |
| canonical smoke command form | `yai` | verify with `which yai`, then use plain `yai ...` |
| primary smoke uses `cargo run` | no | required |
| primary smoke uses `YAI_CONFIG_HOME` | no | required |
| primary smoke uses `YAI_ACCOUNT_USERNAME` | no | required |

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f Documentation/runtime/runtime-readiness-projection.md` | pass | new runtime doc |
| api | `test -f Documentation/waves/v15-runtime-readiness-projection.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| cli | `cargo fmt --check` | pass | formatting clean after V15 changes |
| cli | `cargo test` | pass | warnings only; runtime JSON snapshot updated for V15 projection |
| cli | `cargo build` | pass | warnings only |
| cli | `cargo install --path . --force` | pass | installed CLI |
| shell | `yai auth status` | pass | projected `Auth posture: unauthenticated`, `Operational readiness: sealed`, `Seal reason: missing_auth_context` |
| shell | no-auth `yai case status` | pass | projected `Operational readiness: sealed`, `Seal reason: missing_auth_context`, exit `0` |
| shell | `yai runtime status` | pass | transport unavailable reported separately from local readiness posture, exit `4` |
| shell | `yai auth login --local-dev` | pass | setup local-dev auth/root/tree, exit `0` |
| shell | `yai case status` | pass | projected `blocked` + `missing_operator_context` after auth/root/tree/no active, exit `0` |
| shell | `yai case open projects/readiness-check` | pass | setup case boundary, exit `0` |
| shell | `yai case enter projects/readiness-check` | pass | selected active case, exit `0` |
| shell | `yai case status` | pass | projected `ready` + `none` after active case selection, exit `0` |
| shell | cleanup `yai case leave` / `yai case close projects/readiness-check` / `yai auth logout` | pass | cleanup returned exit `0` for all three commands |
| sdk | docs validation | not run | docs-only unless touched substantially |
| loom | docs validation | not run | docs-only unless touched substantially |

Additional observed output:

* `yai runtime status --format json` returned V15 projection fields including `operationalReadiness`, `sealReason`, `authPosture`, `casePosture`, `operatorContextPosture`, `clientPosture`, `sessionPosture`, and `transport`.
* `which yai` resolved to the installed CLI in the validation shell.

## Findings

### Finding A - Readiness Projection Exists

Record:
V15 defines canonical readiness projection fields.

### Finding B - Operational Readiness Is Separate

Record:
Operational readiness is separate from lifecycle, health and transport status.

### Finding C - Seal Reason Is Explicit

Record:
Blocked or sealed posture now has explicit seal reasons.

### Finding D - Runtime Transport Is Separate

Record:
`runtime_transport_unavailable` is a transport or lifecycle issue, not auth
success or failure.

### Finding E - V16 Can Define Allowed/Blocked Surfaces

Record:
With projection fields in place, V16 can define the allowed/blocked surface
matrix.

## V15 Completion Checklist

* [x] `Documentation/runtime/runtime-readiness-projection.md` exists
* [x] `Documentation/waves/v15-runtime-readiness-projection.md` exists
* [x] readiness projection fields documented
* [x] `operationalReadiness` documented
* [x] `sealReason` documented
* [x] auth/case/operator/client/session postures documented
* [x] local status output aligned where scoped
* [x] runtime transport unavailable reported separately
* [x] runtime health does not grant authorization
* [x] session is not a readiness source
* [x] no production auth added
* [x] no Supabase/database integration added
* [x] no account_ref/entitlement_ref/machine_authorization_ref added
* [x] no SDK runtime client implementation added
* [x] no Loom behavior implementation added
* [x] installed CLI validation used
* [x] primary smoke does not use cargo run
* [x] primary smoke does not use YAI_CONFIG_HOME
* [x] primary smoke does not use YAI_ACCOUNT_USERNAME
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
