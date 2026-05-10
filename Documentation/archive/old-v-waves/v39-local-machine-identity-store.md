# V39 — Local Machine Identity Store

## Status

* Delivery: V39
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: local machine identity store docs + contract schema/fixtures + validation/conformance report
* Previous delivery: V38 — Cloud Compute Boundary
* Next delivery: V40 — Machine Fingerprint Evidence Builder

## Purpose

V39 defines local runtime machine identity posture without raw hardware leakage.

## Scope

Record:

* local machine identity vocabulary documented;
* store status documented;
* identity status documented;
* storage posture documented;
* rotation posture documented;
* privacy posture documented;
* evidence builder relationship documented;
* enrollment readiness documented;
* E/V boundary documented;
* JSON schema created;
* fixtures created;
* conformance script created or deviation recorded;
* no identity generation implemented;
* no persistence implemented;
* no hardware probing/fingerprinting implemented;
* no enrollment/authorization implemented;
* CLI source absence verified.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `Documentation/execution/local-machine-identity-store.md` | create | local machine identity boundary |
| api | `Documentation/waves/v39-local-machine-identity-store.md` | create | delivery report |
| api | `schemas/local-machine-identity-store.v1.schema.json` | create | local machine identity schema |
| api | `fixtures/local-machine-identity-store/new-local-identity.json` | create | representative identity fixture |
| api | `fixtures/local-machine-identity-store/existing-local-identity.json` | create | representative identity fixture |
| api | `fixtures/local-machine-identity-store/rotated-local-identity.json` | create | representative identity fixture |
| api | `fixtures/local-machine-identity-store/revoked-local-identity.json` | create | representative identity fixture |
| api | `fixtures/local-machine-identity-store/no-raw-hardware-fields.json` | create | privacy boundary fixture |
| api | `fixtures/local-machine-identity-store/reboot-continuity-posture.json` | create | continuity posture fixture |
| api | `conformance/check_local_machine_identity_store.py` | create | dependency-free fixture/schema check |
| yai | `Documentation/execution/local-machine-identity-store.md` | create | runtime/core identity boundary record |

## Contract Artifacts

| Artifact | Status | Notes |
| -------- | ------ | ----- |
| local machine identity doc | created | API execution contract added |
| JSON schema | created | dependency-free JSON schema artifact added |
| fixtures | created | six representative identity posture fixtures added |
| conformance script | created | dependency-free fixture/schema checks added |
| yai runtime/core doc | created | runtime/core boundary recorded |

## Local Machine Identity Model

| Concern | V39 policy |
| ------- | ---------- |
| `local_machine_identity_ref` | required |
| `local_machine_ref` | required |
| `machine_identity_store_ref` | required |
| store status | required |
| local identity | privacy-bounded |
| raw hardware identity | forbidden |
| machine authorization | E-owned future relation |
| license lease | separate future relation |
| auth_context | separate |
| session | no ownership |

## Fixture Summary

| Fixture | Scenario | Expected invariant |
| ------- | -------- | ------------------ |
| `new-local-identity.json` | newly created identity posture | required refs present |
| `existing-local-identity.json` | loaded local identity posture | loaded status |
| `rotated-local-identity.json` | rotated identity posture | rotation status |
| `revoked-local-identity.json` | revoked local identity posture | authorization not granted |
| `no-raw-hardware-fields.json` | privacy boundary | no forbidden hardware keys |
| `reboot-continuity-posture.json` | reboot continuity posture | identity is not login/session |

## CLI Source Absence Check

```text
cli/source/ exists: no
full absence guardrail active: yes
Rust src/ is the only CLI implementation: yes
```

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f Documentation/execution/local-machine-identity-store.md` | pass | new policy doc |
| api | `test -f Documentation/waves/v39-local-machine-identity-store.md` | pass | new report |
| api | `test -f schemas/local-machine-identity-store.v1.schema.json` | pass | schema |
| api | `test -f conformance/check_local_machine_identity_store.py` | pass | conformance |
| api | `python3 conformance/check_local_machine_identity_store.py` | pass | V39 conformance |
| api | `python3 conformance/check_cloud_compute_boundary.py` | pass | V38 regression |
| api | `python3 conformance/check_local_model_provider_access_boundary.py` | pass | V37 regression |
| api | `python3 conformance/check_runtime_gate_registry.py` | pass | V35 regression |
| api | `python3 conformance/check_api_contracts.py` | pass | existing conformance |
| api | `find schemas -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | schema JSON |
| api | `find fixtures/local-machine-identity-store -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | fixtures JSON |
| api | `git diff --check` | pass | required |
| yai | `test -f Documentation/execution/local-machine-identity-store.md` | pass | new runtime/core doc |
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

### Finding A — Local Machine Identity Is Privacy-bounded

Record:
Local machine identity is a privacy-bounded local runtime posture, not raw
hardware identity.

### Finding B — Local Identity Does Not Grant Authorization

Record:
Local machine identity does not grant machine authorization or license lease by
itself.

### Finding C — Raw Hardware Is Forbidden

Record:
Raw serial, MAC address, hardware UUID and raw hardware fingerprint are forbidden
as canonical identity.

### Finding D — Continuity Is Not Login

Record:
Local machine identity may survive reboot but is not login, auth_context,
session or client attachment.

### Finding E — V40 Can Build Evidence

Record:
V40 can define privacy-bounded machine fingerprint evidence using local identity
posture without exposing raw hardware.

## V39 Completion Checklist

* [x] `Documentation/execution/local-machine-identity-store.md` exists
* [x] `Documentation/waves/v39-local-machine-identity-store.md` exists
* [x] `schemas/local-machine-identity-store.v1.schema.json` exists
* [x] fixtures exist
* [x] conformance script exists or deviation recorded
* [x] `yai/Documentation/execution/local-machine-identity-store.md` exists
* [x] local machine identity vocabulary documented
* [x] store status documented
* [x] identity status documented
* [x] storage posture documented
* [x] rotation posture documented
* [x] privacy posture documented
* [x] evidence builder relationship documented
* [x] enrollment readiness documented
* [x] E/V boundary documented
* [x] no identity generation implemented
* [x] no persistence implemented
* [x] no hardware probing/fingerprinting implemented
* [x] no enrollment/authorization implemented
* [x] no secrets/keychain behavior added
* [x] no API endpoint added
* [x] no SDK machine identity client added
* [x] no CLI behavior added
* [x] no session mutation added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
