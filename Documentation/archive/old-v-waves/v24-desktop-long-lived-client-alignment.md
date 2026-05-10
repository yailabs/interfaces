# V24 — Desktop / Long-Lived Client Alignment

## Status

* Delivery: V24
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: Desktop / long-lived client contract documentation + optional docs alignment
* Previous delivery: V23 — VS Code Client Alignment
* Next delivery: V25 — Case-bound Jobs

## Purpose

V24 defines Desktop and similar persistent clients as governed long-lived
clients, not domain owners.

## Scope

Record:

* Desktop/long-lived client assumptions audited;
* Desktop long-lived client contract documented;
* local UI state/domain truth boundary documented;
* reconnect/resume boundary documented;
* auth/case/operator/readiness boundaries documented;
* records/evidence/knowledge ownership boundaries documented;
* entitlement/license/machine/gate boundary documented;
* forbidden E object boundary documented;
* CLI source absence verified;
* no backend/E/runtime control implementation added.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `Documentation/client/desktop-long-lived-client-alignment.md` | create | Desktop / long-lived client contract |
| api | `Documentation/waves/v24-desktop-long-lived-client-alignment.md` | create | delivery report |
| yai | `Documentation/operator/desktop/README.md` | update | truthful desktop workspace boundary |
| yai | `Documentation/operator/desktop/desktop-tauri-runbook.md` | update | remove stale in-tree desktop assumptions |
| yai | `Documentation/operator/desktop/workspace-integration.md` | update | remove stale `cli/source` and desktop ownership drift |
| yai | `packaging/windows/desktop-boundary/README.md` | update | cross-link runtime/Desktop boundary to V24 client contract |

## Desktop / App Audit Summary

| Area | Finding | Action |
| ---- | ------- | ------ |
| repo presence | not present | documented that no standalone Desktop/app repo exists in the selected workspace |
| auth wording | no active Desktop code to audit; only runbooks/operator docs existed | aligned docs to posture-only wording |
| case/workspace/window wording | workspace docs risked implying shell/workspace integration is a domain surface | clarified that workspace/window state is client state only |
| active case/operator context | Desktop docs did not point cleanly at operator-context ownership | documented `operator_context.active_case_ref` boundary |
| runtime readiness | stale runbook language implied GUI shell/runtime coupling | reframed as observed runtime/readiness posture only |
| memory/knowledge/records wording | no active Desktop implementation present | documented non-ownership in V24 contract |
| session wording | baseline `api` is partial: V23 docs are missing, and historical session surfaces still exist elsewhere | recorded Desktop session as legacy compatibility only |
| entitlement/license/machine gate language | no active Desktop code, but no canonical Desktop contract existed | documented refs/leases/gate-decisions-only boundary |

## Ownership Boundary

| Concern | Desktop role after V24 |
| ------- | ---------------------- |
| auth truth | observes/does not own |
| root case | observes/does not own |
| active_case_ref | observes operator context/does not own |
| local UI/window state | owns local client state only |
| records/evidence/knowledge | observes/displays governed state; does not own |
| runtime lifecycle | observes/does not control |
| readiness projection | displays/does not fabricate |
| session | legacy compatibility only |
| entitlement/license/machine refs | future consumed refs only |
| runtime_gate_decision | future consumed decision only |
| pricing/billing/provider identity | must not consume |

## Reconnect / Resume Rules

| Scenario | Desktop behavior |
| -------- | ---------------- |
| app reopen | re-read posture; do not invent auth/readiness |
| runtime transport unavailable | display unavailable transport truthfully |
| license lease expired | display sealed/blocked posture when projected |
| machine unauthorized | display blocked posture when projected |
| active case missing | display missing operator context; do not select by itself |
| job running elsewhere | defer to execution lease/job status surfaces in V25/V26 |

## CLI Source Absence Check

Record:

```text
cli/source/ exists: no
full absence guardrail active: yes
Rust src/ is the only CLI implementation: yes
```

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f Documentation/client/desktop-long-lived-client-alignment.md` | pass | new client doc |
| api | `test -f Documentation/waves/v24-desktop-long-lived-client-alignment.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| api | `git diff --check` | pass | required |
| cli | `test ! -e source` | pass | source absence confidence |
| cli | `scripts/check-no-source-dependency.sh` | pass | source absence guard |
| cli | `cargo fmt --check` | not run | cli not touched |
| cli | `cargo test` | not run | cli not touched |
| sdk | validation | not run | docs-only unless touched |
| loom | validation | not run | docs-only unless touched |
| yai | `make info` | pass | touched docs cross-check |
| yai | `make yai` | pass | touched docs cross-check |
| yai | `git diff --check` | pass | required because yai docs were touched |
| desktop/app | validation | not present | no standalone Desktop/app repo found in selected workspace |

## Findings

### Finding A — Desktop Is A Long-Lived Client

Record:
Desktop is a governed long-lived app client, not a domain owner.

### Finding B — UI State Is Not Domain Truth

Record:
Window/view/cache/workspace state does not own auth, case, readiness, memory or
license truth.

### Finding C — Desktop Observes Operator Context

Record:
Active case is owned by operator context; Desktop observes/displays it.

### Finding D — Desktop Consumes E Gates Only As Refs/Decisions

Record:
Future entitlement/license/machine authorization data must be consumed as safe
refs, leases and gate decisions, not commercial/provider/account objects.

### Finding E — V25 Can Define Case-bound Jobs

Record:
With client roles aligned, V25 can bind jobs to cases rather than clients,
sessions or windows.

## V24 Completion Checklist

* [x] `Documentation/client/desktop-long-lived-client-alignment.md` exists
* [x] `Documentation/waves/v24-desktop-long-lived-client-alignment.md` exists
* [x] Desktop/app assumptions audited
* [x] Desktop long-lived client role documented
* [x] UI state/domain truth boundary documented
* [x] reconnect/resume boundary documented
* [x] workspace/case boundary documented
* [x] auth ownership boundary documented
* [x] case ownership boundary documented
* [x] active_case_ref/operator context boundary documented
* [x] runtime lifecycle/readiness boundary documented
* [x] records/evidence/knowledge ownership boundary documented
* [x] session legacy boundary documented
* [x] entitlement/license/machine/gate boundary documented
* [x] forbidden E object boundary documented
* [x] no production auth added
* [x] no Supabase/database integration added
* [x] no entitlement/machine/license implementation added
* [x] no runtime control implementation added
* [x] no session mutation added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched

## Residual Baseline Note

The V24 baseline is partially ahead of the recorded repository state:

* `Documentation/client/vscode-client-alignment.md` is missing;
* `Documentation/waves/v23-vscode-client-alignment.md` is missing.

V24 therefore progresses from the accepted sequence in the delivery box while
recording that the V23 documentation artifact is not yet present in `api`.
