# V41 — Machine Enrollment Client Flow

## Status

* Delivery: V41
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: machine enrollment client flow docs + contract schema/fixtures + validation/conformance report
* Previous delivery: V40 — Machine Fingerprint Evidence Builder
* Next delivery: V42 — Machine Authorization Consumption

## Purpose

V41 defines local runtime/client-side machine enrollment request posture without
implementing enrollment.

## Scope

Record:

* enrollment request vocabulary documented;
* enrollment intents documented;
* enrollment channels documented;
* enrollment statuses documented;
* account confirmation/browser/device code postures documented;
* privacy/consent posture documented;
* blocked reasons and next actions documented;
* E/V boundary documented;
* JSON schema created;
* fixtures created;
* conformance script created or deviation recorded;
* no browser/device/polling/callback implementation;
* no machine authorization issuance;
* no license lease issuance;
* CLI source absence verified.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `docs/execution/machine-enrollment-client-flow.md` | create | machine enrollment client flow |
| api | `docs/waves/v41-machine-enrollment-client-flow.md` | create | delivery report |
| api | `schemas/machine-enrollment-client-flow.v1.schema.json` | create | enrollment flow schema |
| api | `fixtures/machine-enrollment-client-flow/local-client-enrollment-request.json` | create | representative enrollment fixture |
| api | `fixtures/machine-enrollment-client-flow/browser-confirmation-required.json` | create | representative enrollment fixture |
| api | `fixtures/machine-enrollment-client-flow/device-code-pending.json` | create | representative enrollment fixture |
| api | `fixtures/machine-enrollment-client-flow/enrollment-blocked-missing-auth.json` | create | blocked enrollment fixture |
| api | `fixtures/machine-enrollment-client-flow/enrollment-blocked-privacy-review.json` | create | privacy review fixture |
| api | `fixtures/machine-enrollment-client-flow/enrollment-completed-with-authorization-ref.json` | create | observed authorization relation fixture |
| api | `conformance/check_machine_enrollment_client_flow.py` | create | dependency-free fixture/schema check |
| yai | `Documentation/execution/machine-enrollment-client-flow.md` | create | runtime/core enrollment boundary record |

## Contract Artifacts

| Artifact | Status | Notes |
| -------- | ------ | ----- |
| machine enrollment client doc | created | API execution contract added |
| JSON schema | created | dependency-free JSON schema artifact added |
| fixtures | created | six representative enrollment fixtures added |
| conformance script | created | dependency-free fixture/schema checks added |
| yai runtime/core doc | created | runtime/core boundary recorded |

## Enrollment Client Model

| Concern | V41 policy |
| ------- | ---------- |
| `machine_enrollment_request_ref` | request identity |
| `local_machine_identity_ref` | required |
| `local_machine_ref` | required |
| fingerprint evidence | optional safe evidence ref |
| browser handoff | posture only |
| device code | posture only |
| account confirmation | E/platform-owned |
| `machine_authorization_ref` | optional future relation |
| `license_lease_ref` | separate future relation |
| login/session/auth_context | not enrollment ownership |

## Fixture Summary

| Fixture | Scenario | Expected invariant |
| ------- | -------- | ------------------ |
| `local-client-enrollment-request.json` | local client starts request | required refs present |
| `browser-confirmation-required.json` | browser handoff needed | browser posture present |
| `device-code-pending.json` | device code flow pending | device posture present |
| `enrollment-blocked-missing-auth.json` | missing auth | blocked reason present |
| `enrollment-blocked-privacy-review.json` | privacy review needed | privacy blocked reason |
| `enrollment-completed-with-authorization-ref.json` | E-issued auth ref observed | auth ref is relation, not V issuance |

## CLI Source Absence Check

```text
cli/source/ exists: no
full absence guardrail active: yes
Rust src/ is the only CLI implementation: yes
```

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f docs/execution/machine-enrollment-client-flow.md` | pass | new policy doc |
| api | `test -f docs/waves/v41-machine-enrollment-client-flow.md` | pass | new report |
| api | `test -f schemas/machine-enrollment-client-flow.v1.schema.json` | pass | schema |
| api | `test -f conformance/check_machine_enrollment_client_flow.py` | pass | conformance |
| api | `python3 conformance/check_machine_enrollment_client_flow.py` | pass | V41 conformance |
| api | `python3 conformance/check_machine_fingerprint_evidence_builder.py` | pass | V40 regression |
| api | `python3 conformance/check_local_machine_identity_store.py` | pass | V39 regression |
| api | `python3 conformance/check_api_contracts.py` | pass | existing conformance |
| api | `find schemas -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | schema JSON |
| api | `find fixtures/machine-enrollment-client-flow -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | fixtures JSON |
| api | `git diff --check` | pass | required |
| yai | `test -f Documentation/execution/machine-enrollment-client-flow.md` | pass | new runtime/core doc |
| yai | `make info` | pass | yai touched |
| yai | `make yai` | pass | yai touched |
| yai | `git diff --check` | pass | yai touched |
| cli | `test ! -e source` | pass | source absence confidence |
| cli | `scripts/check-no-source-dependency.sh` | pass | source absence guard |
| cli | `cargo fmt --check` | not run | cli not touched |
| cli | `cargo test` | not run | cli not touched |
| sdk | validation | not run | docs-only unless touched |
| loom | validation | not run | docs-only unless touched |

## Findings

### Finding A — Enrollment Request Is Not Authorization

Record:
Machine enrollment request does not grant machine authorization or license lease
by itself.

### Finding B — Account Confirmation Is E-owned

Record:
Account confirmation, approval/rejection and machine_authorization_ref issuance
belong to E/platform.

### Finding C — Enrollment Uses Safe Evidence

Record:
Enrollment may reference privacy-bounded evidence but must not carry raw hardware
identity.

### Finding D — Client Flow Is Contract-only

Record:
V41 defines browser/device/account confirmation posture without implementing
browser handoff, device code, polling or callback server.

### Finding E — V42 Can Consume Authorization

Record:
V42 can now define how runtime consumes machine_authorization_ref after E issues
it.

## V41 Completion Checklist

* [x] `docs/execution/machine-enrollment-client-flow.md` exists
* [x] `docs/waves/v41-machine-enrollment-client-flow.md` exists
* [x] `schemas/machine-enrollment-client-flow.v1.schema.json` exists
* [x] fixtures exist
* [x] conformance script exists or deviation recorded
* [x] `yai/Documentation/execution/machine-enrollment-client-flow.md` exists
* [x] enrollment vocabulary documented
* [x] enrollment statuses documented
* [x] browser/device/account confirmation posture documented
* [x] privacy/consent posture documented
* [x] blocked reasons and next actions documented
* [x] E/V boundary documented
* [x] no browser/device/polling/callback implementation
* [x] no machine authorization issuance
* [x] no license lease issuance
* [x] no hardware probing/fingerprinting implemented
* [x] no secrets/keychain behavior added
* [x] no API endpoint added
* [x] no SDK machine enrollment client added
* [x] no CLI behavior added
* [x] no session mutation added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
