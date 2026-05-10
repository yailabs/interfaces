# V0 - Command Reality Audit

## Status

* Delivery: V0
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: documentation/audit report
* Previous delivery: Master plan loaded
* Next delivery: V1 - Session Death Decision

## Purpose

V0 freezes the real current command, API, SDK, CLI, runtime and client surfaces
before any session removal or auth/case refactor work begins.

This wave is intentionally documentation-only.

## Master Decision

`session` is no longer a canonical YAI domain entity.

Canonical target flow:

```text
auth login
  -> principal/account context
  -> root case case://user
  -> nested cases
  -> governed work
```

Legacy `session` commands may remain temporarily only as:

* compatibility bridge;
* migration bridge;
* debug/dev shim.

They must not own:

* auth;
* client lifecycle;
* active case;
* work;
* permissions;
* harness.

## Branch Note

The delivery box named `feature/refactor-8`. After `git fetch --all --prune`,
that branch was not present locally or remotely in `api`, `cli`, `sdk`, or
`loom`. The available refactor branch in all four repos was
`feature/topology-refactor-8`, and the user confirmed that as the correct
branch. All audit commands below ran on `feature/topology-refactor-8`.

## Repos Audited

| Repo | Path | Branch | Status | Notes |
| ---- | ---- | ------ | ------ | ----- |
| api | `~/Developer/YAI/api` | `feature/topology-refactor-8` | inspected | Canonical API registry/schema/OpenAPI source; report file created here. |
| cli | `~/Developer/YAI/cli` | `feature/topology-refactor-8` | inspected | Rust CLI plus legacy C migration source. |
| sdk | `~/Developer/YAI/sdk` | `feature/topology-refactor-8` | inspected | TS/Rust/C SDK surfaces; Rust consumed by CLI/Loom. |
| loom | `~/Developer/YAI/loom` | `feature/topology-refactor-8` | inspected | Rust TUI/client consuming Rust SDK. |

## Current Command Inventory

| Repo | Surface | Current command/API | Location | Current behavior | Target classification |
| ---- | ------- | ------------------- | -------- | ---------------- | --------------------- |
| api | API | `auth.login`, `auth.logout`, `auth.status`, `auth.whoami` | `registry/api-operations.v1.json`, `registry/api-surfaces.v1.json` | Contract entries exist; handler readiness is planned in observed registry lines. | canonical, partial |
| api | API | `session.attach`, `session.current`, `session.detach`, `session.status` | `registry/api-operations.v1.json`, `registry/api-families.v1.json` | Session is exposed as public family with attach/current/detach/status projections. | legacy |
| api | API | `case.current`, `case.list`, `case.show`, `case.records.tail`, `case.create`, `case.tree`, `case.use` | `registry/api-operations.v1.json`, `openapi/yai-api.v1.yaml` | Case family exists; root/open/enter/leave/close target vocabulary is not explicit. | canonical, partial |
| api | API/runtime posture | `system.status`, `system.runtime.inspect`, runtime service schema | `schemas/runtime-service-status.v1.schema.json`, `registry/api-operations.v1.json` | Schema distinguishes lifecycle, readiness, health, sealed posture, operational readiness, active case posture. | canonical, partial |
| cli | CLI | `yai runtime status` | `src/app/cli.rs`, `src/commands/runtime.rs`, `src/sdk/runtime.rs` | SDK-wired, transport-gated status command; docs say rename to system is needed. | legacy |
| cli | CLI | `yai session status` | `src/app/cli.rs`, `src/commands/session.rs`, `src/sdk/runtime.rs` | SDK-wired session status; legacy source also carries attach/current/detach/active-case semantics. | legacy |
| cli | CLI | `yai case current` | `src/app/cli.rs`, `src/commands/case.rs`, `src/sdk/runtime.rs` | SDK-wired current-case command; broader legacy case surface remains in C source. | canonical, partial |
| cli | CLI | `yai auth ...` | `src/app/cli.rs`, `src/commands/auth.rs`, `MIGRATION_MAP.md` | Scaffold/unavailable; docs mark auth as planned and missing SDK/runtime maturity. | canonical, missing implementation |
| cli | CLI/dev shell | `yai session attach --user <username> --client cli`, shell/session assets | `source/main.c`, `source/cmd/session/*`, `source/assets/shell/*` | Legacy C path blends session bootstrap, user, client attach, active case, and shell UX. | dev shim / legacy |
| sdk | SDK | `client.session().status()`, `client.session().current()` | `packages/rust/src/surfaces/session.rs`, `packages/typescript/src/operations.ts` | Typed transport-backed session surface remains available. | legacy |
| sdk | SDK | `client.case().current()`, `case.list`, `case.show`, `case.records.tail` | `packages/rust/src/surfaces/case.rs`, `packages/typescript/src/operations.ts` | Case current/list/show records operations exist in SDK operation constants. | canonical, partial |
| sdk | SDK | runtime/system status surfaces | `packages/rust/src/surfaces/system.rs`, `packages/rust/src/surfaces/runtime.rs`, `packages/typescript/src/surfaces/system.ts` | Canonical system exists; runtime compatibility alias forwards to system status. | canonical plus legacy alias |
| sdk | SDK | auth clients | docs and search results | Auth was reported missing in SDK audit docs; no Rust auth surface observed. | unknown / missing |
| loom | TUI/client | `/status`, `/runtime`, `/attach`, `/detach` | `src/command/registry.rs`, `src/command/router.rs` | Product command UX over SDK posture; attach/detach are truthful unavailable/not implemented unless backend posture supports them. | dev shim / UX |
| loom | TUI/client | LoginShell/ClientShell | `src/tui/screens/login.rs`, `src/tui/screens/client_shell.rs`, `Documentation/runtime-readiness.md` | Auth/account gate is product posture; dev bypass can enter ClientShell without production auth. | dev shim |

## Session Inventory

| Repo | Location | Reference | Current meaning | Risk | Target classification |
| ---- | -------- | --------- | --------------- | ---- | --------------------- |
| api | `registry/api-families.v1.json`, `registry/api-operations.v1.json` | `session` family and `session.attach/current/detach/status` | Public API family for client-session attachment/status contracts. | High: public registry still teaches session as a family. | legacy |
| api | `contracts/runtime/session.c`, `contracts/runtime/session.h` | `yai_api_session_init`, `session_ref`, `scope_id`, `active` | Runtime contract helper carries session metadata. | Medium: may preserve session as envelope/runtime concept. | legacy |
| api | `schemas/request-envelope.v1.schema.json`, `Documentation/REQUEST_RESPONSE_MODEL.md` | `session` field | Request envelope includes session alongside client, case_ref, principal_ref. | High: envelope-level session can imply canonical domain ownership. | legacy / remove |
| api | `Documentation/source-api-readme.md`, `Documentation/versioning-and-compatibility.md`, `extraction/*` | session compatibility notes | Docs already call session compatibility/transitional in some places. | Low to medium: still visible but partially classified. | legacy |
| cli | `src/app/cli.rs`, `src/commands/session.rs`, `src/sdk/runtime.rs` | `yai session status` | Rust CLI status command against SDK session status. | Medium: public command remains. | legacy |
| cli | `source/main.c`, `source/cmd/session/*`, `source/assets/shell/*` | `session attach`, `session current`, `session detach`, `session active-case`, session shell bootstrap | Legacy C path appears to own/derive auth prompt, user session, active case, shell attachment, and runtime-session file behavior. | High: blends auth, client, active case, and shell. | dev shim / legacy / remove |
| cli | `source/cmd/case/surface.c` | user session reads and `case://user` legacy alias | Case surface reads current session and active case for GUI/session summaries. | High: active case can be session-derived. | legacy |
| sdk | `packages/rust/src/surfaces/session.rs`, `packages/typescript/src/operations.ts` | `session.current`, `session.status`, `SessionStatus.session_id` | Typed session clients and types. | Medium: SDK makes session easy to consume as canonical. | legacy |
| sdk | `Documentation/standards/family-availability.md` | session-oriented client usage compatibility-only | Docs warn new clients should prefer system/runtime posture plus client/operator context. | Low: already labeled compatibility. | legacy |
| loom | `src/yai/session.rs`, `src/yai/sdk.rs`, `src/command/router.rs` | session posture labels, attach/detach state | Client posture/UX state, not backend implementation. | Medium: product language still says session attached/unattached. | dev shim / legacy |

Observed session match count from `rg -c` line totals: api 81, cli 574,
sdk 31, loom 48, total 734 line matches. Counts are line-match summaries, not
unique semantic surfaces.

Required notes:

* `session` command surfaces: API registry has attach/current/detach/status; CLI has Rust `session status` and legacy C/session shell attach/current/detach/active-case/status/summary traces; Loom has `/attach` and `/detach` session posture UX.
* `session` API surfaces: API registry and projections expose `session.*`; request envelope contains `session`.
* SDK `session` clients/types: Rust `SessionSurface`, `SessionStatus`; TypeScript operation constants for session current/status.
* Docs teaching `session` as canonical: API `operation-grammar.md`; CLI README/command model/migration docs; SDK README/family availability; Loom product docs. Several newer docs already label it compatibility-only.
* Current ownership risk: legacy CLI/session paths and case surface indicate session can own or derive active case, auth prompt/user, client attach, shell bootstrap, runtime-session persistence, work/chat session state, and harness constraints.

## Auth Inventory

| Repo | Surface | Existing auth concept | Location | Current behavior | Gap vs target |
| ---- | ------- | --------------------- | -------- | ---------------- | ------------- |
| api | API | `auth.login`, `auth.logout`, `auth.status`, `auth.whoami`; principal current | `registry/api-operations.v1.json`, `registry/api-verbs.v1.json` | Registry-level contract exists; observed readiness is planned. | `--local-dev` not represented; implementation maturity unknown/planned. |
| cli | CLI | `yai auth ...` | `src/app/cli.rs`, `src/commands/auth.rs`, `MIGRATION_MAP.md` | Scaffold returns unavailable; migration docs say auth needs SDK/runtime maturity. | Missing implemented `login`, `login --local-dev`, `status`, `logout`. |
| cli | Legacy runtime/session | Prompted login/user attach | `source/main.c`, `source/cmd/session/substrate_entry_cli.c`, `source/cmd/runtime/auth.c` | Session attach prompts login/user and verifies password in legacy paths. | Auth is blended into session bootstrap, not canonical auth plane. |
| sdk | SDK | Account/auth posture references only in docs | `Documentation/guides/client-adoption.md`, `Documentation/standards/enterprise-sdk-standard.md` | SDK docs say SDK does not own login backend; auth missing in typed surfaces. | Missing typed auth clients. |
| loom | runtime/docs | LoginShell, auth labels, dev bypass | `src/yai/auth.rs`, `src/tui/screens/login.rs`, `Documentation/runtime-readiness.md` | Product gate blocks fake production auth; `YAI_LOOM_DEV_BYPASS_AUTH=1` allows dev entry. | No backend auth login/logout/status; local dev bypass is Loom-local UX, not canonical auth command. |

Target auth commands:

| Target command | Status |
| -------------- | ------ |
| `yai auth login` | partial scaffold in CLI/API registry; not implemented end-to-end |
| `yai auth login --local-dev` | missing as canonical command |
| `yai auth status` | API registry exists; CLI implemented status not observed |
| `yai auth logout` | API registry exists; CLI implemented logout not observed |

## Case Inventory

| Repo | Surface | Existing case concept | Location | Current behavior | Gap vs target |
| ---- | ------- | --------------------- | -------- | ---------------- | ------------- |
| api | API | `case.current`, `case.list`, `case.show`, `case.records.tail`, `case.create`, `case.tree`, `case.use` | `registry/api-operations.v1.json`, `openapi/yai-api.v1.yaml` | Case family is present and partly projected. | Target root/open/enter/leave/status/close command names not fully mapped. |
| api | Schema/runtime posture | active case posture/ref | `schemas/runtime-service-status.v1.schema.json`, `schemas/case-ref.v1.schema.json` | Runtime status schema includes activeCasePosture, activeCaseReason, activeCaseRef. | Root user case creation/selection policy not defined here. |
| cli | CLI | `yai case current` | `src/app/cli.rs`, `src/commands/case.rs`, `src/sdk/runtime.rs` | Rust CLI exposes current only. | Missing root/list/open/enter/leave/status/close in Rust CLI. |
| cli | Legacy C case runtime | broad `yai-cased`/case surface, `case://user` alias, active case env/session handling | `source/cmd/case/surface.c`, `source/cmd/session/session_shell_surface.c` | Rich case/watch/registry/process surface exists, but mixed with runtime internals and session. | Needs canonical command split and active case out of session. |
| sdk | SDK | `case.current`, `case.list`, `case.show`, `case.records.tail` | `packages/rust/src/surfaces/case.rs`, `packages/typescript/src/operations.ts` | Typed case surface exists for current/list/show/records. | Missing root/open/enter/leave/status/close naming and root case model. |
| loom | TUI/client | cases unavailable | `src/app/update.rs`, `src/tui/screens/client_shell.rs` | Cases page/command is disabled until backend case surface wired. | No client case tree UX yet. |

Target case commands:

| Target command | Status |
| -------------- | ------ |
| `yai case root` | missing |
| `yai case list` | API/SDK partial; CLI Rust not implemented |
| `yai case open <path>` | missing |
| `yai case enter <case>` | legacy C has enter-like semantics; canonical CLI missing |
| `yai case leave` | legacy C/session hints exist; canonical CLI missing |
| `yai case status` | partial via `case current` and runtime active case posture |
| `yai case close <case>` | missing/canonical not observed |

## Client/Shell Inventory

| Repo | Surface | Existing client/shell concept | Location | Current behavior | Gap vs target |
| ---- | ------- | ----------------------------- | -------- | ---------------- | ------------- |
| api | API | `client` family and client refs | `registry/api-families.v1.json`, `schemas/client-ref.v1.schema.json`, `schemas/client-surface-status.v1.schema.json` | API has client-related contract vocabulary. | No explicit `shell` command model. |
| cli | CLI/Shell | shell/session assets, client attach flags | `source/assets/shell/*`, `source/main.c`, `source/cmd/session/*` | Legacy session attach uses `--client cli`; shell assets mediate active session behavior. | Attach/detach is domain-owning in legacy paths; must become shell/client UX only. |
| sdk | SDK | transport client and C client lifecycle | `packages/rust/src/client.rs`, `packages/c/include/yai_sdk/client.h`, `packages/c/src/client/client.c` | SDK owns transport/client open/close/invoke mechanics. | Does not define canonical shell/client attach commands. |
| loom | TUI/client | LoginShell, ClientShell, `/attach`, `/detach` | `src/command/registry.rs`, `src/command/router.rs`, `src/tui/screens/*` | Attach/detach are UX/posture commands and explicitly unavailable if backend unsupported. | Should migrate language from session attach to client/shell attach once canonical target lands. |

Current shell/client attach is mixed:

* CLI legacy session attach is domain-owning or at least domain-influencing.
* Loom attach/detach is mostly UX/connection posture and does not implement backend ownership.
* SDK client open/close is transport lifecycle, not operator auth/case lifecycle.

## Runtime Readiness / Sealed Posture Inventory

| Repo | Surface | Current readiness/lifecycle concept | Location | Current behavior | Gap vs target |
| ---- | ------- | ----------------------------------- | -------- | ---------------- | ------------- |
| api | API/schema | lifecycle/readiness/health/sealed/operationalReadiness/activeCasePosture | `schemas/runtime-service-status.v1.schema.json` | Schema explicitly distinguishes service lifecycle, readiness, health, sealed posture, seal reason, operational readiness, active case posture. | Runtime implementation truth may lag schema; API registry still broad/planned. |
| api | API policy | forbidden runtime start/stop service lifecycle ops | `conformance/check_api_contracts.py`, `Documentation/api-operation-model.md`, `Documentation/operation-grammar.md` | API forbids runtime/system service lifecycle start/stop/restart. | Good target alignment, but consumer docs must keep distinction. |
| cli | CLI/runtime | `yai runtime status`, runtime-gated diagnostics, legacy `start/stop` docs | `src/commands/runtime.rs`, `Documentation/refoundation-phase-4a-cli-rust-migration-plan.md`, `source/main.c` | Rust status is SDK-gated; legacy C contains lifecycle/start/stop and runtime-owned logic. | Runtime status still named `runtime`; legacy lifecycle remains mixed. |
| sdk | SDK | system/runtime status and sealed readiness typed data | `packages/rust/src/surfaces/system.rs`, `packages/typescript/src/surfaces/system.ts`, `Documentation/standards/enterprise-sdk-standard.md` | SDK forwards status/readiness and must not treat healthy/alive as operational authority. | C SDK still has legacy runtime/workspace control-call grammar. |
| loom | TUI/client | runtime posture via SDK, truthful degraded/unavailable states | `src/yai/runtime.rs`, `src/yai/sdk.rs`, `Documentation/runtime-readiness.md` | Uses SDK status; blocks fake auth/session/case/provider/model readiness. | Still product-language session/account/auth posture; case unavailable. |

Target distinctions currently:

| Distinction | Current state |
| ----------- | ------------- |
| `runtime running != runtime authorized` | API/SDK docs and schema support this; CLI legacy may conflate. |
| `runtime healthy != operational actions allowed` | API schema supports operationalReadiness; SDK docs warn against conflation. |
| `client attached != login` | Loom mostly distinguishes; legacy CLI session attach can conflate. |
| `auth login != shell` | Target missing; legacy CLI blends prompted login into session shell. |
| `case selected != session` | API schema has active case posture, but legacy CLI/session shell can derive active case from session/env. |

## Current vs Target Command Matrix

| Target command | Current equivalent | Exists today | Location | Required future wave |
| -------------- | ------------------ | ------------ | -------- | -------------------- |
| `yai auth login` | API `auth.login`; CLI `auth` scaffold | partial | api registry, cli `src/commands/auth.rs` | V3/V4 |
| `yai auth login --local-dev` | Loom env dev bypass only | no/partial dev shim | loom `YAI_LOOM_DEV_BYPASS_AUTH` docs | V4 |
| `yai auth status` | API `auth.status`; Loom auth posture | partial | api registry, loom posture | V3 |
| `yai auth logout` | API `auth.logout` | partial | api registry | V3 |
| `yai case root` | `case://user` legacy alias/root handling | partial legacy | cli `source/cmd/case/surface.c` | V6/V9 |
| `yai case list` | API/SDK `case.list`; CLI planned docs | partial | api registry, sdk operations, cli docs | V8/V9 |
| `yai case open <path>` | no canonical equivalent observed | no | TBD | V8/V9 |
| `yai case enter <case>` | legacy case/session active case behavior | partial legacy | cli C source | V9/V10 |
| `yai case leave` | legacy session landing suggests `yai case leave` | partial/unknown | cli shell assets | V9/V10 |
| `yai case status` | `yai case current`; runtime active case posture | partial | cli Rust, API schema | V9/V10 |
| `yai case close <case>` | no canonical equivalent observed | no | TBD | V9 |
| `yai shell` | Loom ClientShell/LoginShell; legacy session shell | partial dev/UX | loom, cli `source/assets/shell` | V13 |
| `yai shell list` | no canonical equivalent observed | no | TBD | V13 |
| `yai shell attach <shell_id>` | legacy `session attach`; Loom `/attach` posture | partial legacy/dev | cli legacy, loom command registry | V13 |
| `yai shell detach` | legacy session detach; Loom `/detach` posture | partial legacy/dev | cli legacy, loom command registry | V13 |
| `yai client list` | API client family only | partial contract | api registry/schemas | V12/V13 |
| `yai client attach <client_id>` | legacy `session attach --client`; Loom `/attach` | partial legacy/dev | cli legacy, loom | V12/V13 |
| `yai client detach` | legacy session detach; Loom `/detach` | partial legacy/dev | cli legacy, loom | V12/V13 |

## Findings

### Finding A - Current Session Ownership

Current `session` appears to own or influence:

* auth: legacy CLI prompts login/user in session attach paths.
* active case: legacy session shell reads/writes active/current case fields and env.
* client lifecycle: `session attach --client cli` and Loom session attached/unattached posture.
* runtime authorization: legacy session guard functions gate commands.
* work/jobs/flows: CLI legacy chat/work fields carry `chat_session_id`, `current_work_id`, and session state.
* permissions: source shows session guards and mediated shell restrictions.
* harness: shell assets and runtime-session file shape are session-rooted.

Target classification: legacy/dev shim now; remove domain ownership in V1/V2/V10/V13/V42.

### Finding B - Missing Auth Surface

API registry has auth operations, but CLI/SDK/Loom do not yet expose a complete
canonical auth command flow:

```bash
yai auth login
yai auth login --local-dev
yai auth status
yai auth logout
```

CLI auth is scaffold/unavailable. SDK auth clients are missing. Loom has a
LoginShell and dev bypass but no canonical backend auth command implementation.

### Finding C - Missing Case Surface

Current canonical case support is mostly current/list/show/records-tail at API/SDK
level and `yai case current` in CLI. Target commands are missing or only legacy:

```bash
yai case root
yai case list
yai case open
yai case enter
yai case leave
yai case status
yai case close
```

The root `case://user` concept exists as legacy alias/handling in CLI C case code,
but not as the canonical auth-login-created root case flow.

### Finding D - Runtime Readiness Ambiguity

API schema and SDK docs distinguish lifecycle, health, readiness, sealed posture,
operational readiness, authorization, and active case. Legacy CLI/runtime C paths
still mix runtime start/stop/status, session attach, active case, readiness, watch,
and shell behavior. The ambiguity is therefore implementation and UX drift, not
absence of a schema vocabulary.

### Finding E - SDK/API/CLI Alignment Gap

Rust CLI is mostly SDK-first for core status commands, but:

* CLI still uses legacy public vocabulary (`runtime`, `session`) and compat operation IDs.
* CLI legacy C source directly couples to runtime/API adapter internals.
* SDK Rust/TS align to API operation constants for many surfaces, but auth clients are missing.
* C SDK still exposes legacy runtime/workspace command grammar and low-level transport details.

### Finding F - Docs/Public Model Drift

Docs still teach `session` in public family/command/client language across API,
CLI, SDK, and Loom. Some docs already mark session as transitional or
compatibility-only, but the model is not consistently replaced with auth,
operator context, case, and client/shell boundaries.

## Risk Register

| Risk | Impact | Future wave | Notes |
| ---- | ------ | ----------- | ----- |
| `session` owns active case | high | V1/V2/V10 | Legacy CLI/session shell and case code carry active/current case via session/env. |
| auth commands missing | high | V3/V4 | API registry only; CLI scaffold; SDK missing auth clients. |
| root case missing | high | V6 | `case://user` exists as legacy alias, not login-created canonical root. |
| case tree missing | medium | V7/V8/V9 | API has case.tree/create/use; CLI target commands not present. |
| runtime health/readiness conflated | medium | V14/V15/V16/V17 | Schema distinguishes; legacy CLI/runtime UX still mixes lifecycle/readiness/session. |
| CLI coupled to runtime internals | high | V21 | Rust CLI is SDK-first, but legacy `source/` directly includes runtime/API adapter headers. |
| docs teach legacy session model | high | V43/V45/V46 | Public docs and registry still expose session as a family/client surface. |

## Commands Run

Exact command families run in each repo:

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `git status --short` | pass | Clean before report creation. |
| cli | `git status --short` | pass | Clean. |
| sdk | `git status --short` | pass | Clean. |
| loom | `git status --short` | pass | Clean. |
| api | `git branch --show-current` | pass | `feature/topology-refactor-8`. |
| cli | `git branch --show-current` | pass | `feature/topology-refactor-8`. |
| sdk | `git branch --show-current` | pass | `feature/topology-refactor-8`. |
| loom | `git branch --show-current` | pass | `feature/topology-refactor-8`. |
| api | `git fetch --all --prune` | pass after escalation | Used only to check missing `feature/refactor-8`; no source changes. |
| cli | `git fetch --all --prune` | pass after escalation | Same. |
| sdk | `git fetch --all --prune` | pass after escalation | Same. |
| loom | `git fetch --all --prune` | pass after escalation | Same. |
| api | `pwd` | pass | `/Users/francescomaiomascio/Developer/YAI/api`. |
| cli | `pwd` | pass | `/Users/francescomaiomascio/Developer/YAI/cli`. |
| sdk | `pwd` | pass | `/Users/francescomaiomascio/Developer/YAI/sdk`. |
| loom | `pwd` | pass | `/Users/francescomaiomascio/Developer/YAI/loom`. |
| api | `find . -maxdepth 3 -type f \| sort \| sed 's#^\./##' \| head -300` | pass | File inventory captured. |
| cli | `find . -maxdepth 3 -type f \| sort \| sed 's#^\./##' \| head -300` | pass | File inventory captured. |
| sdk | `find . -maxdepth 3 -type f \| sort \| sed 's#^\./##' \| head -300` | pass | File inventory captured. |
| loom | `find . -maxdepth 3 -type f \| sort \| sed 's#^\./##' \| head -300` | pass | File inventory captured. |
| api | `rg -n "\bsession\b|\bSession\b|\bSESSION\b|user_session|session_id|sessionId|sessionRef|active_session" .` | matches | Registry/contracts/docs/session references. |
| cli | same session command | matches | Heavy legacy and Rust session references. |
| sdk | same session command | matches | Rust/TS session clients and docs. |
| loom | same session command | matches | Product posture and attach/detach references. |
| api | `rg -n "\bauth\b|\bAuth\b|\bAUTH\b|login|logout|principal|account_ref|auth_context|entitlement_ref|machine_authorization_ref" .` | matches | API auth/principal registry entries. |
| cli | same auth command | matches | Auth scaffold plus legacy login/session prompt paths. |
| sdk | same auth command | matches | Docs only; no full typed auth surface observed. |
| loom | same auth command | matches | LoginShell/auth posture/dev bypass. |
| api | `rg -n "\bcase\b|\bCase\b|\bCASE\b|case://|case_ref|caseRef|active_case|activeCase|root case|nested case" .` | matches | Case registry/OpenAPI/schema. |
| cli | same case command | matches | Rust `case current`, legacy C case surface, `case://user`. |
| sdk | same case command | matches | Rust/TS case surfaces and active-case readiness docs. |
| loom | same case command | matches | Cases unavailable and Documentation/product boundaries. |
| api | `rg -n "command|commands|subcommand|arg|args|clap|commander|yargs|cobra|click|attach|detach|status|login|logout|open|enter|leave|close|root|list" .` | matches | Verbs/registry/OpenAPI. |
| cli | same CLI inventory command | matches | Clap command tree, Rust commands, legacy C commands. |
| sdk | same CLI inventory command | matches | SDK client and legacy C SDK command ids. |
| loom | same CLI inventory command | matches | Slash command registry/router. |
| api | `rg -n "route|router|endpoint|handler|registry|api|openapi|swagger|http|GET|POST|PUT|PATCH|DELETE" .` | matches | Registry/OpenAPI/schema. |
| cli | same API inventory command | matches | SDK HTTP endpoint and legacy API adapter includes. |
| sdk | same API inventory command | matches | API source model and HTTP transport. |
| loom | same API inventory command | matches | SDK endpoint and command registry. |
| api | `rg -n "runtime|lifecycle|readiness|ready|health|healthy|sealed|unsealed|operationalReadiness|sealReason|controlPlan|start|stop|degraded" .` | matches | Runtime status schema and lifecycle conformance. |
| cli | same runtime inventory command | matches | Rust runtime status plus legacy runtime/case readiness. |
| sdk | same runtime inventory command | matches | Runtime/system status and transport. |
| loom | same runtime inventory command | matches | SDK posture and readiness docs. |
| api | `rg -n "client|Client|SDK|sdk|transport|request|response|status|runtime|auth|case|session" .` | matches | API client/SDK boundary and request envelope. |
| cli | same SDK/client command | matches | SDK adapter and legacy source. |
| sdk | same SDK/client command | matches | SDK client/transport/surfaces. |
| loom | same SDK/client command | matches | Loom SDK client and posture. |
| api | `rg -n "\bsession\b|\bSession\b|\bauth\b|\bcase://user\b|\bcase\b|runtime|sealed|readiness|CLI|SDK|API" README* docs . --glob "*.md"` | matches | Public docs drift and compatibility notes. |
| cli | same docs command | matches | CLI docs drift and migration notes. |
| sdk | same docs command | matches | SDK docs drift and compatibility notes. |
| loom | same docs command | matches | Loom product docs and readiness model. |

`rg` returning matches is not a failure. No destructive commands were run. Build/test
was not required and was not run.

## V0 Completion Checklist

* [x] all involved repos checked out on `feature/topology-refactor-8`
* [x] repo existence and branch status recorded
* [x] current command surfaces inventoried
* [x] session references inventoried and classified
* [x] auth surfaces inventoried
* [x] case surfaces inventoried
* [x] client/shell surfaces inventoried
* [x] runtime readiness/lifecycle surfaces inventoried
* [x] SDK/API/CLI alignment gaps recorded
* [x] Documentation/public model drift recorded
* [x] no source code changed
* [x] no behavior changed
* [x] no unrelated files staged

## Pass Criteria

* [x] `Documentation/waves/v0-command-reality-audit.md` exists
* [x] report identifies all repos inspected
* [x] report records current branch as `feature/topology-refactor-8`
* [x] report documents current session surfaces
* [x] report documents current auth gaps
* [x] report documents current case gaps
* [x] report documents current runtime/readiness gaps
* [x] report documents current SDK/API/CLI alignment gaps
* [x] report classifies `session` references as canonical/legacy/dev shim/remove/unknown
* [x] no source code files changed
* [x] no unrelated files staged

