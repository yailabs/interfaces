# ADR-V1 - Session Death Decision

## Status

* ADR: ADR-V1
* Delivery: V1
* Status: accepted
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo: `api`
* Repo branch: `feature/topology-refactor-8`
* Repo change type: architecture decision record
* Previous delivery: V0 - Command Reality Audit
* Next delivery: V2 - Legacy Session Containment

## Context

V0 found that `session` is still present across API, CLI, SDK and Loom surfaces.

V0 approximate line-match summary:

| Repo | Session line matches | Notes |
| ---- | -------------------- | ----- |
| api | 81 | API registry/contracts/docs/request envelope references |
| cli | 574 | Rust CLI plus heavy legacy C session/shell/case coupling |
| sdk | 31 | Rust/TypeScript session clients/types/docs |
| loom | 48 | TUI posture, attach/detach, login/client shell language |

V0 found that legacy `session` currently risks owning or influencing:

* auth;
* active case;
* client lifecycle;
* runtime authorization;
* work/jobs/flows;
* permissions;
* harness.

This conflicts with the target YAI domain model.

## Decision

`session` is no longer a canonical YAI domain entity.

The canonical model is:

```text
auth login
  -> principal/account context
  -> root case case://user
  -> nested cases
  -> governed work
```

`session` must not own:

* auth;
* principal;
* account_ref;
* auth_context;
* entitlement_ref;
* machine_authorization_ref;
* root case;
* active case;
* operator context;
* client lifecycle;
* shell lifecycle;
* work;
* jobs;
* flows;
* agents;
* provider calls;
* records;
* evidence;
* knowledge;
* permissions;
* harness.

## Allowed Meaning of Session

After V1, `session` may only appear as:

| Allowed use | Meaning | Constraint |
| ----------- | ------- | ---------- |
| compatibility bridge | temporary support for old commands/API clients | must point users toward auth/case/shell/client |
| migration bridge | transitional mapping from old surfaces to new planes | must not create new domain ownership |
| debug/dev shim | local developer helper | must not be documented as public canonical model |
| historical docs/reference | old behavior explanation | must be clearly marked legacy/non-canonical |

## Forbidden Meaning of Session

After V1, `session` must not be used to mean:

| Forbidden use | Replacement |
| ------------- | ----------- |
| logged-in user | principal/auth context |
| account | account_ref |
| active work boundary | active case ref |
| root harness | `case://user` |
| current project | nested case path |
| shell connection | shell/client connection |
| client identity | client_ref/operator context |
| permission boundary | authorization/governance |
| job owner | case-bound job/lease |
| runtime readiness | sealed/readiness posture |

## New Ownership Model

| Concern | Canonical owner |
| ------- | --------------- |
| login/logout/status | auth plane |
| local dev identity | auth plane with local-dev principal |
| external account link | account_ref |
| entitlement | entitlement_ref |
| machine authorization | machine_authorization_ref |
| root operational harness | `case://user` |
| nested work containers | case tree |
| active case selection | operator context |
| CLI one-shot invocation | CLI client over SDK/API |
| long-lived shell connection | shell/client UX |
| runtime health | runtime lifecycle/health plane |
| runtime operational permission | sealed readiness + auth + operator context + case |
| jobs/flows/agents | case-bound governed execution |
| records/evidence/knowledge | case-bound persistence |

## Target Command Consequences

Deprecated canonical model:

```bash
yai session attach --user <username> --client cli
yai session detach
yai session status
```

These may remain only as legacy compatibility, migration bridge or debug/dev
shim.

Canonical auth commands:

```bash
yai auth login
yai auth login --local-dev
yai auth status
yai auth logout
```

Canonical case commands:

```bash
yai case root
yai case list
yai case open <path>
yai case enter <case>
yai case leave
yai case status
yai case close <case>
```

Canonical shell/client commands:

```bash
yai shell
yai shell list
yai shell attach <shell_id>
yai shell detach
```

or:

```bash
yai client list
yai client attach <client_id>
yai client detach
```

Shell/client attach is UX/connection only. It must not decide auth, active case,
permissions or work ownership.

## Runtime Sealed Posture Consequences

The following distinctions are mandatory:

```text
runtime running != runtime authorized
runtime healthy != operational actions allowed
client attached != login
auth login != shell
case selected != session
```

Operational actions require:

* identity/auth posture;
* operator context;
* case boundary;
* authorization.

Runtime may be alive, healthy and inspectable while sealed.

## API Consequences

API must eventually stop presenting `session` as a canonical family.

Future API work must:

* preserve `session.*` only as explicitly legacy/compatibility, if needed;
* move canonical auth operations into auth family;
* move canonical case operations into case family;
* expose operator context explicitly;
* avoid request envelopes that imply session-owned auth/case/work;
* avoid treating `session.current` as source of active case truth.

Relevant future waves:

* V34 - API Registry Refactor
* V35 - API Case Expansion
* V36 - API Auth Surfaces
* V37 - API Operator Context Surfaces
* V44 - Remove Session API Canon

## SDK Consequences

SDKs must eventually stop making `session` look canonical.

Future SDK work must:

* keep session clients only as legacy/compatibility if retained;
* add typed auth clients;
* add typed case-tree clients;
* add operator-context clients;
* ensure runtime/system readiness does not imply operational authority;
* avoid teaching new integrations to call `client.session()` as the main entry point.

Relevant future waves:

* V20 - SDK Runtime Surface Alignment
* V38 - SDK Auth Clients
* V39 - SDK Case Clients
* V47 - SDK Docs Alignment

## CLI Consequences

CLI must stop treating `session attach` as the canonical entry point.

Future CLI work must:

* expose `yai auth login/status/logout`;
* expose `yai auth login --local-dev`;
* expose `yai case root/list/open/enter/leave/status/close`;
* move active case out of session;
* classify old `yai session ...` commands as legacy/dev/compat;
* use SDK/API rather than runtime internals;
* avoid shell/client attach owning auth or case.

Relevant future waves:

* V2 - Legacy Session Containment
* V3 - Auth Command Model
* V4 - Local Dev Auth
* V9 - Case Commands
* V10 - Active Case Refactor
* V13 - Shell UX Model
* V21 - CLI SDK-first Wiring
* V40 - CLI Deprecation UX
* V41 - Migration Shim
* V42 - Remove Session Runtime Ownership
* V46 - CLI Command Docs

## Loom Consequences

Loom must represent itself as a client/operator UX, not a session owner.

Future Loom work must:

* keep LoginShell/auth posture truthful;
* distinguish dev bypass from canonical auth;
* represent attach/detach as UX/client posture only;
* use root case/auth/readiness when backend support exists;
* avoid teaching session as the main domain model.

Relevant future waves:

* V22 - Loom Alignment
* V12 - Client Connection Model
* V13 - Shell UX Model

## Documentation Consequences

Docs must stop teaching `session` as the canonical public model.

Future docs must:

* explain auth -> case://user -> nested cases;
* explain shell/client attach as connection UX only;
* explain runtime sealed posture;
* mark session docs as legacy/compatibility;
* avoid using session as harness/work/account/user synonym.

Relevant future waves:

* V43 - Remove Session Docs
* V45 - Runtime Identity Docs
* V46 - CLI Command Docs
* V47 - SDK Docs Alignment

## Compatibility Policy

Existing `session` surfaces may remain temporarily only if all of these are true:

* they are clearly marked legacy, compatibility, migration or debug/dev;
* they do not introduce new domain behavior;
* they do not own active case, auth, permissions or work;
* they point toward auth/case/shell/client replacements where user-facing;
* they are tracked for containment/removal in later V waves.

## Migration Rule

Every future `session` touch must classify the reference as one of:

| Classification | Meaning |
| -------------- | ------- |
| legacy | old public surface retained temporarily |
| compatibility | old client/command support |
| migration bridge | maps old behavior to new auth/case/operator/client planes |
| debug/dev shim | local-only helper |
| remove | should be deleted once replacement exists |
| historical | old docs or changelog context |
| forbidden | new canonical usage; must not be added |

No new `session` reference may be added without one of these classifications.

## Consequences

| Area | Consequence |
| ---- | ----------- |
| API | `session` can no longer be canonical registry family long-term |
| CLI | `session attach` is no longer canonical onboarding |
| SDK | `client.session()` cannot be taught as primary client surface |
| Loom | session posture must become client/operator/auth/case posture |
| Runtime | runtime state must not be owned by session |
| Case | active case must move to operator context |
| Auth | login/logout/status must live in auth plane |
| Docs | public model must say auth -> case, not session |
| Website | public copy must not teach session as domain |
| E platform | account/backend remains external and passes refs/context to core |

## V1 Completion Checklist

* [x] ADR file exists at `docs/adr/ADR-V1-session-death-decision.md`
* [x] ADR records V0 as previous delivery
* [x] ADR records `feature/topology-refactor-8`
* [x] ADR states `session` is non-canonical
* [x] ADR records canonical auth -> case://user -> nested cases model
* [x] ADR defines allowed `session` uses
* [x] ADR defines forbidden `session` meanings
* [x] ADR defines new ownership model
* [x] ADR records API consequences
* [x] ADR records SDK consequences
* [x] ADR records CLI consequences
* [x] ADR records Loom consequences
* [x] ADR records documentation consequences
* [x] ADR records compatibility policy
* [x] ADR records migration classification rule
* [x] no source code changed
* [x] no behavior changed
* [x] no unrelated files staged

## Pass Criteria

* [x] `docs/adr/ADR-V1-session-death-decision.md` exists
* [x] ADR clearly declares `session` non-canonical
* [x] ADR clearly says session must not own auth/client/active case/work/permissions/harness
* [x] ADR defines allowed legacy/compatibility/debug use
* [x] ADR defines canonical ownership by auth, case, operator context and client/shell planes
* [x] ADR links V1 consequences to later V waves
* [x] source code changes: none
* [x] build/test not required
* [x] unrelated working-tree changes untouched
