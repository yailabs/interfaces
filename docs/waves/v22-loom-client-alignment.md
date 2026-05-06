# V22 - Loom Client Alignment

## Status

* Delivery: V22
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: Loom client alignment audit + docs/UX wording alignment + optional truthful posture display refinement
* Previous delivery: V21.9 - Final CLI Source Removal / Absence Guardrail
* Next delivery: V23 - VS Code Client Alignment

## Purpose

V22 aligns Loom as a governed long-lived client, not a domain owner.

## Scope

* Loom auth/case/session/readiness assumptions audited;
* Loom long-lived client role documented;
* session ownership language removed or qualified;
* auth/case/operator/readiness boundaries documented;
* entitlement/license/machine/gate boundary documented;
* forbidden E object boundary documented;
* CLI source absence verified;
* no backend/E/runtime control implementation added.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `docs/client/loom-client-alignment.md` | create | Loom client alignment model |
| api | `docs/waves/v22-loom-client-alignment.md` | create | delivery report |
| loom | `docs/runtime-readiness.md` | docs | align attach/detach and session wording with client connection model |
| loom | `docs/sdk-first-client-contract.md` | docs | document client connection posture and E/license boundary |
| loom | `src/app/commands.rs` | UX wording | avoid `attached` as canonical session truth |
| loom | `src/command/registry.rs` | UX wording | classify attach/detach as client connection requests |
| loom | `src/command/router.rs` | UX wording | report client connection posture instead of session ownership |
| loom | `src/tui/screens/client_shell.rs` | UX wording | render client posture label |
| loom | `src/yai/posture.rs` | UX wording | qualify legacy session compatibility in boundary notes |
| loom | `src/yai/sdk.rs` | UX wording | map SDK posture to client connection labels |
| loom | `src/yai/session.rs` | UX wording | retain legacy attached compatibility while displaying client connection labels |

Pre-existing unrelated worktree note: `loom/README.md` was already modified before
V22 and was left untouched by this delivery.

## Loom Audit Summary

| Area | Finding | Action |
| ---- | ------- | ------ |
| auth wording | LoginShell/auth copy already treats production auth as unavailable or dev-bypass only | documented auth posture boundary; no auth implementation added |
| case wording | Loom currently says cases are unavailable until backend case surface is wired | retained truthful unavailable state; no case client added |
| active case/operator context | no active-case ownership implementation found in Loom | documented `operator_context.active_case_ref` as owner |
| runtime readiness | Loom fetches runtime posture through SDK and exposes unavailable/degraded states | retained SDK-bound posture; documented readiness projection boundary |
| session wording | active TUI copy used `session`, `attached`, and `SessionMutation` labels | changed visible labels to client connection and legacy session compatibility |
| client attach/detach | `/attach` and `/detach` remain unavailable/not implemented when backend support is missing | reworded as client connect/disconnect requests only |
| entitlement/license/machine gate language | no live Loom implementation found | documented future refs/leases/`runtime_gate_decision` consumption boundary |

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
| runtime_gate_decision | future consumed decision only |
| pricing/billing/provider identity | must not consume |

## CLI Source Absence Check

```text
cli/source/ exists: no
full absence guardrail active: yes
Rust src/ is the only CLI implementation: yes
```

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f docs/client/loom-client-alignment.md` | pass | new client doc |
| api | `test -f docs/waves/v22-loom-client-alignment.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| api | `git diff --check` | pass | required |
| loom | `cargo fmt --check` | pass | source wording touched |
| loom | `cargo test` | pass | 0 tests |
| loom | `cargo build` | pass | build succeeded |
| loom | `git diff --check` | pass | required |
| cli | `test ! -e source` | pass | source absence confidence |
| cli | `scripts/check-no-source-dependency.sh` | pass | source absence guard |
| cli | `cargo fmt --check` | pass | required source absence confidence |
| cli | `cargo test` | pass | warnings only; tests passed |
| cli | `cargo build` | pass | warnings only; build passed |
| cli | `git diff --check` | pass | required |
| sdk | `git diff --check` | pass | not touched |
| yai | `make info` | pass | source absence cross-check |
| yai | `make yai` | pass | source absence cross-check |
| yai | `git diff --check` | pass | not touched |

## Post-Edit Scans

| Repo | Scan | Result | Notes |
| ---- | ---- | ------ | ----- |
| api | `rg -n "Loom Client Alignment|long-lived client|does not own domain truth|operator_context.active_case_ref|runtime_gate_decision|license_lease|machine_authorization_ref|Supabase user object|billing provider object|legacy session" docs/client docs/waves` | pass | V22 docs carry required boundary language |
| loom | `rg -n "session attached|session detached|session selected|client logged in|runtime ready because UI|Loom owns|operator_context.active_case_ref|auth posture|readiness projection|sealed|blocked|legacy session|entitlement|license|lease|machine|runtime_gate_decision" README.md docs src` | pass | no unqualified old wording; remaining matches are required boundary terms |
| all | forbidden ownership/backend scan | pass | matches are limited to V22 wording-rule anti-pattern examples; no false ownership/backend claims introduced |

## Findings

### Finding A - Loom Is A Long-Lived Client

Loom is a governed long-lived client/TUI, not a domain owner.

### Finding B - Session Is Not Loom Truth

Loom must not use session as canonical auth/case/runtime truth.

### Finding C - Loom Observes Operator Context

Active case is owned by operator context; Loom observes/displays it.

### Finding D - Loom Consumes E Gates Only As Refs/Decisions

Future entitlement/license/machine authorization data must be consumed as safe
refs, leases and gate decisions, not commercial/provider/account objects.

### Finding E - V23 Can Align VS Code

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
