# V40 — Machine Fingerprint Evidence Builder

## Status

* Delivery: V40
* Status: done
* Track: V — Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `refoundation/phase-01`
* Repo change type: machine fingerprint evidence docs + contract schema/fixtures + validation/conformance report
* Previous delivery: V39 — Local Machine Identity Store
* Next delivery: V41 — Machine Enrollment Client Flow

## Purpose

V40 defines privacy-bounded machine evidence for future enrollment without raw
hardware leakage.

## Scope

Record:

* machine fingerprint evidence vocabulary documented;
* evidence statuses documented;
* source policies documented;
* privacy/minimization/consent/confidence posture documented;
* enrollment use documented;
* forbidden raw hardware and secret fields documented;
* E/V boundary documented;
* JSON schema created;
* fixtures created;
* conformance script created or deviation recorded;
* no hardware probing/fingerprinting implemented;
* no hash/salt/signing implemented;
* no enrollment/authorization implemented;
* CLI source absence verified.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| api | `Documentation/execution/machine-fingerprint-evidence-builder.md` | create | machine evidence boundary |
| api | `Documentation/waves/v40-machine-fingerprint-evidence-builder.md` | create | delivery report |
| api | `schemas/machine-fingerprint-evidence-builder.v1.schema.json` | create | machine evidence schema |
| api | `fixtures/machine-fingerprint-evidence-builder/minimized-local-evidence.json` | create | representative evidence fixture |
| api | `fixtures/machine-fingerprint-evidence-builder/enrollment-ready-evidence.json` | create | representative evidence fixture |
| api | `fixtures/machine-fingerprint-evidence-builder/consent-required-evidence.json` | create | representative evidence fixture |
| api | `fixtures/machine-fingerprint-evidence-builder/rotated-identity-evidence.json` | create | representative evidence fixture |
| api | `fixtures/machine-fingerprint-evidence-builder/raw-hardware-rejected-evidence.json` | create | privacy rejection fixture |
| api | `fixtures/machine-fingerprint-evidence-builder/low-confidence-evidence.json` | create | low-confidence posture fixture |
| api | `conformance/check_machine_fingerprint_evidence_builder.py` | create | dependency-free fixture/schema check |
| yai | `Documentation/execution/machine-fingerprint-evidence-builder.md` | create | runtime/core evidence boundary record |

## Contract Artifacts

| Artifact | Status | Notes |
| -------- | ------ | ----- |
| machine fingerprint evidence doc | created | API execution contract added |
| JSON schema | created | dependency-free JSON schema artifact added |
| fixtures | created | six representative evidence fixtures added |
| conformance script | created | dependency-free fixture/schema checks added |
| yai runtime/core doc | created | runtime/core boundary recorded |

## Machine Fingerprint Evidence Model

| Concern | V40 policy |
| ------- | ---------- |
| `machine_fingerprint_evidence_ref` | evidence identity |
| `local_machine_identity_ref` | required |
| `local_machine_ref` | required |
| evidence kind/status | required |
| privacy posture | required |
| raw hardware | forbidden |
| salt/private key | forbidden |
| machine authorization | future E-owned relation |
| license lease | separate future relation |
| login/session/auth_context | not evidence ownership |

## Fixture Summary

| Fixture | Scenario | Expected invariant |
| ------- | -------- | ------------------ |
| `minimized-local-evidence.json` | minimized local evidence | required refs present |
| `enrollment-ready-evidence.json` | ready for enrollment | enrollment_ready posture |
| `consent-required-evidence.json` | consent required | consent_required posture |
| `rotated-identity-evidence.json` | rotated local identity | rotation posture |
| `raw-hardware-rejected-evidence.json` | raw hardware rejected | no raw hardware fields |
| `low-confidence-evidence.json` | low confidence | low confidence posture |

## CLI Source Absence Check

```text
cli/source/ exists: no
full absence guardrail active: yes
Rust src/ is the only CLI implementation: yes
```

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| api | `test -f Documentation/execution/machine-fingerprint-evidence-builder.md` | pass | new policy doc |
| api | `test -f Documentation/waves/v40-machine-fingerprint-evidence-builder.md` | pass | new report |
| api | `test -f schemas/machine-fingerprint-evidence-builder.v1.schema.json` | pass | schema |
| api | `test -f conformance/check_machine_fingerprint_evidence_builder.py` | pass | conformance |
| api | `python3 conformance/check_machine_fingerprint_evidence_builder.py` | pass | V40 conformance |
| api | `python3 conformance/check_local_machine_identity_store.py` | pass | V39 regression |
| api | `python3 conformance/check_cloud_compute_boundary.py` | pass | V38 regression |
| api | `python3 conformance/check_api_contracts.py` | pass | existing conformance |
| api | `find schemas -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | schema JSON |
| api | `find fixtures/machine-fingerprint-evidence-builder -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | fixtures JSON |
| api | `git diff --check` | pass | required |
| yai | `test -f Documentation/execution/machine-fingerprint-evidence-builder.md` | pass | new runtime/core doc |
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

### Finding A — Fingerprint Evidence Is Privacy-bounded

Record:
Machine fingerprint evidence is privacy-bounded evidence posture, not raw
hardware fingerprinting.

### Finding B — Evidence Does Not Grant Authorization

Record:
Machine fingerprint evidence does not grant machine authorization or license
lease by itself.

### Finding C — Raw Hardware And Secrets Are Forbidden

Record:
Raw serial, MAC address, hardware UUID, raw fingerprints, salts and private keys
are forbidden.

### Finding D — Enrollment Can Consume Safe Evidence Later

Record:
V41 can define enrollment client flow consuming safe evidence posture without raw
hardware leakage.

## V40 Completion Checklist

* [x] `Documentation/execution/machine-fingerprint-evidence-builder.md` exists
* [x] `Documentation/waves/v40-machine-fingerprint-evidence-builder.md` exists
* [x] `schemas/machine-fingerprint-evidence-builder.v1.schema.json` exists
* [x] fixtures exist
* [x] conformance script exists or deviation recorded
* [x] `yai/Documentation/execution/machine-fingerprint-evidence-builder.md` exists
* [x] evidence vocabulary documented
* [x] evidence statuses documented
* [x] source policies documented
* [x] privacy/minimization/consent/confidence posture documented
* [x] enrollment use documented
* [x] forbidden raw hardware and secret fields documented
* [x] E/V boundary documented
* [x] no hardware probing/fingerprinting implemented
* [x] no hash/salt/signing implementation added
* [x] no enrollment/authorization implemented
* [x] no secrets/keychain behavior added
* [x] no API endpoint added
* [x] no SDK machine evidence client added
* [x] no CLI behavior added
* [x] no session mutation added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
