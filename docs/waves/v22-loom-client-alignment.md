# V22 — Loom Client Alignment

## Status

* Delivery: V22
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: Loom client alignment audit + docs/UX wording alignment + optional truthful posture display refinement
* Previous delivery: V21.9 — Final CLI Source Removal / Absence Guardrail
* Next delivery: V23 — VS Code Client Alignment

## Purpose

V22 aligns Loom as a governed long-lived client, not a domain owner.

## Scope

Record:

* Loom auth/case/session/readiness assumptions audited;
* Loom long-lived client role documented;
* session ownership language removed or qualified;
* auth/case/operator/readiness boundaries documented;
* E gate/ref consumption boundary documented;
* no backend/E/runtime control implementation added.
* repository reality diverged from the delivery-box branch expectation; the work was performed on verified branch `refoundation/phase-01`.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `docs/client/loom-client-alignment.md` | create | Loom client alignment model |
| api | `docs/waves/v22-loom-client-alignment.md` | create | delivery report |
| loom | `README.md` | update | align Loom client language |
| loom | `docs/product-boundary.md` | update | long-lived client boundary |
| loom | `docs/runtime-readiness.md` | update | truthful readiness/client wording |
| loom | `docs/sdk-first-client-contract.md` | update | SDK/Loom ownership boundary |
| loom | `src/app/commands.rs` | update | client posture wording |
| loom | `src/app/model.rs` | update | client posture state model |
| loom | `src/app/update.rs` | update | auth/client feedback wording |
| loom | `src/command/registry.rs` | update | command descriptions and categories |
| loom | `src/command/router.rs` | update | truthful client/runtime command feedback |
| loom | `src/tui/overlays/help.rs` | update | auth posture wording |
| loom | `src/tui/screens/login.rs` | update | auth/client gate wording |
| loom | `src/tui/screens/client_shell.rs` | update | client/runtime/operator wording |
| loom | `src/yai/posture.rs` | update | boundary notes wording |
| loom | `src/yai/sdk.rs` | update | client posture labels |
| loom | `src/yai/session.rs` | update | legacy session compatibility labels to client posture wording |

## Loom Audit Summary

| Area | Finding | Action |
| ---- | ------- | ------ |
| auth wording | LoginShell and help copy still implied `account login` ownership language | changed to `account posture` / `auth posture` wording |
| case wording | ClientShell said `cases` generically without operator-context boundary | changed to `operator context active case` wording |
| active case/operator context | no visible `operator_context.active_case_ref` pointer in Loom-specific docs | documented explicit operator-context ownership in Loom docs |
| runtime readiness | runtime posture existed but was mixed with session/client attachment language | qualified runtime as observed posture and kept readiness truthful |
| session wording | multiple UI and command strings still surfaced `session`, `attached`, `detached` | shifted to `client` / `runtime connection posture` wording and marked session as legacy compatibility only |
| client attach/detach | `/attach` and `/detach` looked session-owned | reframed as runtime connection posture commands |
| entitlement/license/machine gate language | no explicit Loom rule for future E consumption boundary | documented refs/gate-decision-only boundary |

## Ownership Boundary

| Concern | Loom role after V22 |
| ------- | ------------------- |
| auth truth | observes/does not own |
| root case | observes/does not own |
| active_case_ref | observes operator context/does not own |
| runtime lifecycle | observes/does not control |
| readiness projection | displays/does not fabricate |
| session | legacy compatibility only |
| entitlement/license/machine refs | future consumed refs only |
| pricing/billing/provider identity | must not consume |

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f docs/client/loom-client-alignment.md` | pass | new client doc |
| api | `test -f docs/waves/v22-loom-client-alignment.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| api | `git diff --check` | pass | required |
| loom | `cargo fmt --check` | pass | required if source touched |
| loom | `cargo test` | pass | 0 tests, build/test surface clean |
| loom | `cargo build` | pass | required if source touched |
| loom | `git diff --check` | pass | required if touched |
| cli | `test ! -e source` | pass | source absence confidence |
| cli | `scripts/check-no-source-dependency.sh` | pass | source absence guard |
| cli | `cargo fmt --check` | not run | cli not touched |
| cli | `cargo test` | not run | cli not touched |
| sdk | validation | not run | docs-only unless touched |
| yai | validation | not run | docs-only unless touched |

## Findings

### Finding A — Loom Is A Long-Lived Client

Record:
Loom is a governed long-lived client/TUI, not a domain owner.

### Finding B — Session Is Not Loom Truth

Record:
Loom must not use session as canonical auth/case/runtime truth.

### Finding C — Loom Observes Operator Context

Record:
Active case is owned by operator context; Loom observes/displays it.

### Finding D — Loom Consumes E Gates Only As Refs/Decisions

Record:
Future entitlement/license/machine authorization data must be consumed as safe
refs/gate decisions, not commercial/provider/account objects.

### Finding E — V23 Can Align VS Code

Record:
With Loom aligned, V23 can apply the same governed-client model to VS Code.

## V22 Completion Checklist

* [x] `docs/client/loom-client-alignment.md` exists
* [x] `docs/waves/v22-loom-client-alignment.md` exists
* [x] Loom current assumptions audited
* [x] Loom long-lived client role documented
* [x] auth ownership boundary documented
* [x] case ownership boundary documented
* [x] active_case_ref/operator context boundary documented
* [x] runtime lifecycle/readiness boundary documented
* [x] session legacy boundary documented
* [x] E gate/ref consumption boundary documented
* [x] no production auth added
* [x] no Supabase/database integration added
* [x] no entitlement/machine/license implementation added
* [x] no runtime control implementation added
* [x] no session mutation added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
