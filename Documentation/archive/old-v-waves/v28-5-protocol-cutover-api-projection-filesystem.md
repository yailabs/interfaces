# V28.5 — Protocol Cutover / API Projection Filesystem Canonicalization

## Status

* Delivery: V28.5
* Status: done
* Track: V — Protocol/API boundary corrective wave
* Repo branch: `refoundation/phase-01`
* Repo change type: protocol filesystem cutover + API projection redefinition
* Previous delivery: V28 — Logout / Seal Policy
* Next delivery: V29 — Case Evidence Binding

## Purpose

V28.5 separates canonical protocol ownership from API projection ownership.

## Scope

Record:

* `yai/protocols` created;
* old `yai/specs` compatibility status recorded;
* `api` filesystem classified;
* API projection filesystem documented;
* C contract artifacts classified but not blindly moved;
* safe protocol material mirrored into `yai/protocols`;
* API protocol conformance rewired to validate canonical `yai/protocols` files and detect mirror drift in `api`;
* validation run;
* no runtime/API/SDK behavior implemented.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| yai | `protocols/**` | create/copy | canonical protocol root |
| yai | `specs/README.md` | update | old specs compatibility pointer |
| yai | `README.md` | update | point canonical spec ownership at `protocols/` |
| api | `README.md` | update | redefine API as projection |
| api | `Documentation/api-source-of-truth.md` | update | clarify API exposure vs protocol meaning |
| api | `Documentation/protocol-api-boundary.md` | create | explicit protocol/API ownership boundary and target API shape |
| api | `contracts/README.md` | update | classify C helper contracts as separate audit |
| api | `conformance/check_logout_seal_policy.py` | update | validate canonical protocol files and assert API mirror alignment |
| api | `conformance/check_case_evidence_binding.py` | update | validate canonical protocol files and assert API mirror alignment |
| api | `registry/README.md` | update | define registry as API grammar, not protocol meaning |
| api | `openapi/README.md` | update | define OpenAPI as projection, not protocol owner |
| api | `conformance/README.md` | update | define API-owned vs protocol-mirror checks |
| api | `conformance/CHECKLIST.md` | update | add mirror drift and ownership checks |
| api | `Documentation/api-projection-filesystem.md` | create | API projection definition |
| api | `Documentation/waves/v28-5-protocol-cutover-api-projection-filesystem.md` | create | delivery report |
| yai | `Documentation/system/README.md` | update | switch normative system-doc references from `specs/` to `protocols/` |
| yai | `Documentation/system/architecture/README.md` | update | switch architecture normative references from `specs/` to `protocols/` |

## Protocol Filesystem Result

| Path | Status | Notes |
| ---- | ------ | ----- |
| `yai/protocols` | created | canonical protocol root created in V28.5 |
| `yai/specs` | compat pointer/still active | compatibility mirror retained because active refs remain |
| `yai/protocols/naming` | present | copied from `specs/naming` |
| `yai/protocols/ontology` | present | copied from `specs/ontology`; internal path updated to `protocols/...` |
| `yai/protocols/registry` | present | copied from `specs/registry` |
| `yai/protocols/system` | present | copied from `specs/system` |
| `yai/protocols/topology` | present | copied from `specs/topology` |
| protocol schemas | moved partially | V28/V29 protocol-neutral schemas mirrored into `protocols/schemas`; broader schema split deferred |
| protocol fixtures | moved partially | V28/V29 protocol-neutral fixtures mirrored into `protocols/fixtures` |
| protocol conformance | moved partially | V28/V29 protocol-neutral conformance mirrored into `protocols/conformance` |

## API Filesystem Result

| API path | Target role | Result |
| -------- | ----------- | ------ |
| `openapi/` | API projection | keep |
| `registry/api-*.json` | API operation registry/projection | keep |
| `schemas/` | protocol canonical or API schema mirror | mirror/deferred |
| `fixtures/` | protocol canonical or API projection fixtures | mirror/deferred |
| `conformance/check_api_contracts.py` | API conformance | keep |
| `conformance/check_operation_registry.py` | API registry conformance | keep |
| `contracts/*.c/*.h` | legacy C contract audit | classified |
| `Documentation/waves` | historical delivery reports | keep |
| `Documentation/execution` | protocol docs / API docs split | deferred/split |

## C Contract Artifact Classification

| Path | Classification | Action |
| ---- | -------------- | ------ |
| `contracts/foundation/*.c/*.h` | `legacy_c_contract_audit` | keep in `api/contracts` pending ABI/reference decision |
| `contracts/identity/*.c/*.h` | `legacy_c_contract_audit` | keep in `api/contracts` pending ABI/reference decision |
| `contracts/runtime/*.c/*.h` | `legacy_c_contract_audit` | keep in `api/contracts` pending ABI/reference decision |

Record:
Do not move C contracts into protocols without separate ABI/reference decision.

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| yai | `test -d protocols` | pass | canonical protocol root |
| yai | `find protocols -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | protocol JSON |
| yai | `make info` | pass | required |
| yai | `make yai` | pass | required |
| yai | `git diff --check` | pass | required |
| api | `test -f Documentation/api-projection-filesystem.md` | pass | API filesystem doc |
| api | `test -f Documentation/waves/v28-5-protocol-cutover-api-projection-filesystem.md` | pass | report |
| api | `python3 conformance/check_api_contracts.py` | pass | API conformance |
| api | `python3 conformance/check_logout_seal_policy.py` | pass | reads canonical `yai/protocols` and fails on API mirror drift |
| api | `python3 conformance/check_case_evidence_binding.py` | pass | reads canonical `yai/protocols` and fails on API mirror drift |
| api | `find schemas -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | schema JSON |
| api | `find fixtures -name '*.json' -print0 | xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | fixture JSON |
| api | `git diff --check` | pass | required |
| cli | `test ! -e source` | pass | source absence |
| cli | `scripts/check-no-source-dependency.sh` | pass | source guard |
| sdk | `git diff --check` | not run | repo not touched |
| loom | `git diff --check` | not run | repo not touched |

## Findings

### Finding A — Protocol Root Exists

Record:
`yai/protocols` exists as canonical protocol root.

### Finding B — API Is Projection

Record:
`api` is defined as API projection over protocols, not protocol source.

### Finding C — C Contracts Need Separate Audit

Record:
C `.c/.h` contract artifacts are not blindly moved into protocols.

### Finding D — V29 Can Use Correct Protocol Destination

Record:
Case evidence binding now has a canonical protocol destination in
`yai/protocols`, while `api` can retain mirrors for API projection and
validation.

## V28.5 Completion Checklist

* [x] `yai/protocols/README.md` exists
* [x] `yai/protocols/protocol-filesystem.v1.md` exists
* [x] `yai/protocols/MIGRATION_FROM_SPECS.md` exists
* [x] existing `yai/specs` content migrated or compatibility status recorded
* [x] `api/Documentation/api-projection-filesystem.md` exists
* [x] `api/Documentation/waves/v28-5-protocol-cutover-api-projection-filesystem.md` exists
* [x] api filesystem classification table completed
* [x] C contract artifacts classified
* [x] protocol vs API ownership rules documented
* [x] no runtime behavior added
* [x] no API endpoint behavior added
* [x] no SDK behavior added
* [x] CLI source absence guard remains passing
* [x] validation results recorded truthfully
* [x] unrelated working-tree changes left untouched
