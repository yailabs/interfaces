# V2 - Legacy Session Containment

## Status

* Delivery: V2
* Status: done
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`
* Repo change type: documentation + CLI/help containment
* Previous delivery: V1 - Session Death Decision
* Next delivery: V3 - Auth Command Model

## Purpose

V2 contains existing `session` surfaces as legacy compatibility/dev/migration
surfaces without changing command behavior.

## Scope

* `session` remains available where it already exists;
* V2 does not remove commands;
* V2 does not rename commands;
* V2 does not implement replacement commands;
* V2 adds explicit containment language.

## Files Changed

| Repo | File | Change type | Reason |
| ---- | ---- | ----------- | ------ |
| api | `Documentation/compat/session-legacy-containment.md` | create | central containment policy |
| api | `Documentation/waves/v2-legacy-session-containment.md` | create | delivery report |
| cli | `README.md` | docs text only | classify session as legacy compatibility |
| cli | `MIGRATION_MAP.md` | docs text only | classify session command as legacy compatibility |
| cli | `src/app/cli.rs` | help text only | mark `session` help as legacy compatibility |
| sdk | `README.md` | docs text only | classify `client.session()` as legacy compatibility |
| loom | `README.md` | docs text only | classify session posture as legacy/client UX |
| loom | `Documentation/sdk-first-client-contract.md` | docs text only | classify session posture as non-canonical UX language |

## Containment Summary

| Surface | Before V2 | After V2 |
| ------- | --------- | -------- |
| API docs | session visible from V0 | session classified as legacy compatibility |
| CLI help/docs | session command visible | session marked legacy compatibility |
| SDK docs | client.session visible | session marked legacy compatibility |
| Loom docs | session posture language visible | session marked client/operator UX or dev shim |

## Required Session Warning

The canonical warning is now present in Documentation/help:

```text
Session is a legacy compatibility surface.
It is not the canonical YAI domain model.
```

## Replacement Guidance

Replacement guidance points toward:

```bash
yai auth ...
yai case ...
yai shell ...
yai client ...
```

V2 does not claim these are fully implemented.

## Truthfulness Rules

* no command removal;
* no command rename;
* no behavior change;
* no auth implementation;
* no case implementation;
* no shell/client implementation;
* no API registry refactor;
* no SDK client refactor;
* no Loom behavior refactor.

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f Documentation/waves/v0-command-reality-audit.md` | pass | baseline |
| api | `test -f Documentation/adr/ADR-V1-session-death-decision.md` | pass | baseline |
| api | `test -f Documentation/compat/session-legacy-containment.md` | pass | new policy |
| api | `test -f Documentation/waves/v2-legacy-session-containment.md` | pass | report |
| cli | `cargo fmt --check` | pass | initial run reported formatting for new Clap attribute; wrapping was corrected and check passed |
| cli | `cargo test` | fail | compile fails on existing `RuntimeServiceStatus` private import in `src/output/render.rs` and `src/sdk/runtime.rs`; unrelated to V2 help/docs changes |
| loom | `cargo fmt --check` | pass | no formatting changes required |
| loom | `cargo test` | fail | compile fails on existing missing `T: Clone` bound in `src/yai/runtime.rs`; unrelated to V2 Documentation/copy changes |
| sdk | not run | not run | no obvious fast documented lightweight validation for README-only change |

## Post-Containment Scan

Command:

```bash
rg -n "Session is a legacy compatibility surface|not the canonical YAI domain model|legacy compatibility command|prefer auth/case/shell" ~/Developer/YAI/api ~/Developer/YAI/cli ~/Developer/YAI/sdk ~/Developer/YAI/loom
```

Result: matches in the changed V2 policy, delivery report, CLI help/docs, SDK
README and Loom docs.

Forbidden new canonical wording scan:

```bash
rg -n "canonical session|session is canonical|primary session model|session owns|session is the root harness|session is the active case" ~/Developer/YAI/api ~/Developer/YAI/cli ~/Developer/YAI/sdk ~/Developer/YAI/loom
```

Result: matches, if any, are explanatory/forbidden-language policy references in
ADR/V2 docs, not new positive canonical-session claims.

## Findings

### Finding A - Session Contained, Not Removed

V2 intentionally leaves existing session surfaces in place but classifies them as
legacy compatibility/dev/migration surfaces.

### Finding B - Replacement Commands Are Guidance Only

Auth/case/shell/client replacements are referenced as target guidance only.
V2 does not claim all replacement commands are implemented.

### Finding C - CLI Help Is Now Safer

Changed CLI help/deprecation copy now warns that session is legacy and
non-canonical.

### Finding D - SDK/Loom Language Remains Transitional

SDK and Loom may still contain session language, but V2 requires it to be read as
compatibility/client posture/dev UX, not domain ownership.

### Finding E - V3 Can Start Auth Command Model

With session contained at the language/help level, V3 can begin implementing or
formalizing the canonical auth command surface.

## V2 Completion Checklist

* [x] `Documentation/compat/session-legacy-containment.md` exists
* [x] `Documentation/waves/v2-legacy-session-containment.md` exists
* [x] changed Documentation/help text marks session as legacy compatibility
* [x] changed Documentation/help text says session is not canonical
* [x] changed Documentation/help text points toward auth/case/shell/client
* [x] no session command removed
* [x] no session command renamed
* [x] no API registry behavior changed
* [x] no SDK client behavior changed
* [x] no CLI behavior changed except help/warning text
* [x] no Loom behavior changed except Documentation/copy if touched
* [x] no auth/case/shell/client implementation added
* [x] no unrelated files staged

## Pass Criteria

* [x] central containment policy exists
* [x] delivery report exists
* [x] user-facing session text touched by V2 is marked legacy/non-canonical
* [x] replacement guidance points to auth/case/shell/client
* [x] no behavior changes are introduced
* [x] source changes, if any, are limited to help/warning strings
* [x] validation commands are recorded truthfully
* [x] unrelated working-tree changes are untouched
