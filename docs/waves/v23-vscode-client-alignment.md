# V23 - VS Code Client Alignment

## Status

* Delivery: V23
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: VS Code client alignment model + docs/report + optional existing extension audit
* Previous delivery: V22 - Loom Client Alignment
* Next delivery: V24 - Desktop / Long-Lived Client Alignment

## Purpose

V23 aligns VS Code as a governed editor client, not a domain owner.

## Scope

* VS Code/editor client assumptions audited;
* VS Code long-lived editor-client role documented;
* editor/workspace/case boundary documented;
* auth/case/operator/readiness boundaries documented;
* entitlement/license/machine/gate boundary documented;
* forbidden E object boundary documented;
* CLI source absence verified;
* no backend/E/runtime control implementation added.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `docs/client/vscode-client-alignment.md` | create | VS Code client alignment model |
| api | `docs/waves/v23-vscode-client-alignment.md` | create | delivery report |

No SDK, CLI, Loom, YAI, or VS Code extension files were changed in V23.

## VS Code / Extension Audit Summary

| Area | Finding | Action |
| ---- | ------- | ------ |
| repo presence | present at `../vscode`, clean worktree, branch `main` instead of expected `refoundation/phase-01` | audit-only; no files changed in optional repo |
| auth wording | README says the extension is an external client/integration surface and does not own runtime/account/case/governance truth | retained; V23 API doc defines auth posture ownership |
| case/workspace wording | extension has workspace case binding flows and local `workspaceState` binding storage | documented workspace/editor context as VS Code client state only, not case ownership |
| active case/operator context | extension currently calls `caseEnter(binding.caseId)` during bootstrap to align DevHost/backend checks | recorded as residual extension assumption; future selected extension wave must route through operator-context-safe contract |
| runtime readiness | extension checks runtime health and renders offline/degraded states; some copy says to start backend manually | documented readiness projection boundary; no runtime lifecycle implementation added |
| session wording | extension references `sessionStatus`, `active yai user session`, and session boundary/provider posture | recorded as residual wording/model issue for selected extension alignment |
| entitlement/license/machine gate language | no live entitlement/license/machine implementation found | documented future refs/leases/`runtime_gate_decision` consumption boundary |

## Ownership Boundary

| Concern | VS Code role after V23 |
| ------- | ---------------------- |
| auth truth | observes/does not own |
| root case | observes/does not own |
| active_case_ref | observes operator context/does not own |
| workspace/editor context | owns local editor state only |
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
| api | `test -f docs/client/vscode-client-alignment.md` | pass | new client doc |
| api | `test -f docs/waves/v23-vscode-client-alignment.md` | pass | new report |
| api | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| api | `git diff --check` | pass | required |
| cli | `test ! -e source` | pass | source absence confidence |
| cli | `scripts/check-no-source-dependency.sh` | pass | source absence guard |
| cli | `cargo fmt --check` | pass | source absence confidence |
| cli | `cargo test` | pass | warnings only; tests passed |
| cli | `cargo build` | pass | warnings only; build passed |
| cli | `git diff --check` | pass | required |
| sdk | `git diff --check` | pass | not touched |
| loom | `git diff --check` | pass | V22 changes present; not touched by V23 |
| yai | `make info` | pass | source absence cross-check |
| yai | `make yai` | pass | source absence cross-check |
| yai | `git diff --check` | pass | not touched |
| vscode/extension | validation | not run | repo present but not touched; branch `main` does not match V23 branch |

## Post-Edit Scans

| Repo | Scan | Result | Notes |
| ---- | ---- | ------ | ----- |
| api | `rg -n "VS Code Client Alignment|long-lived editor client|workspace bound to case_ref|operator_context.active_case_ref|runtime_gate_decision|license_lease|machine_authorization_ref|Supabase user object|billing provider object|legacy session" docs/client docs/waves` | pass | V23 docs carry required boundary language |
| all | forbidden ownership/backend scan | pass | matches are limited to V23 wording-rule anti-pattern examples; no false ownership/backend claims introduced |

## Findings

### Finding A - VS Code Is A Long-Lived Editor Client

VS Code is a governed long-lived editor client, not a domain owner.

### Finding B - Workspace Is Not Case Ownership

Editor workspace/folder/window state may bind to case refs, but it does not own
cases.

### Finding C - VS Code Observes Operator Context

Active case is owned by operator context; VS Code observes/displays it.

### Finding D - VS Code Consumes E Gates Only As Refs/Decisions

Future entitlement/license/machine authorization data must be consumed as safe
refs, leases and gate decisions, not commercial/provider/account objects.

### Finding E - V24 Can Generalize Desktop Client

With Loom and VS Code aligned at the client-model level, V24 can define the
general desktop/long-lived client contract. The existing `vscode` extension repo
still needs a selected-branch follow-up before its active implementation can be
claimed fully wording-aligned.

## V23 Completion Checklist

* [x] `docs/client/vscode-client-alignment.md` exists
* [x] `docs/waves/v23-vscode-client-alignment.md` exists
* [x] VS Code/editor assumptions audited
* [x] VS Code long-lived client role documented
* [x] workspace/case boundary documented
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
