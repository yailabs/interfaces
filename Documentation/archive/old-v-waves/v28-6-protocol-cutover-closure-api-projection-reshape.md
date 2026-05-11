# V28.6 — Protocol Cutover Closure / Specs Rename & API Projection Reshape

## Status

* Delivery: V28.6
* Status: done
* Track: V — Protocol/API boundary corrective wave
* Repo branch: `refoundation/phase-01`
* Repo change type: cutover closure + specs rename drain + API projection reshape
* Previous delivery: V28.5 — Protocol Cutover / API Projection Filesystem Canonicalization

## Purpose

Close the remaining ambiguity between `yai/specs` and `yai/protocols`, then
reshape `api` so it visibly presents as an API projection repository.

## Scope

Record:

* `yai/specs` audited for remaining duplicated compact protocol material;
* migrated compact protocol files drained from `yai/specs`;
* active ownership docs repointed from `specs/` to `protocols/` where safe;
* `api` projection roots created as README-only placeholders;
* API mirror/projection classifications tightened;
* validation run;
* no runtime, transport, SDK, CLI, or Loom behavior implemented.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| yai | `protocols/README.md` | update | record V28.6 closure |
| yai | `protocols/MIGRATION_FROM_SPECS.md` | update | record drain status |
| yai | `protocols/protocol-filesystem.v1.md` | update | define pointer-only compatibility state |
| yai | `specs/README.md` | update | pointer-only compatibility surface |
| yai | `specs/{naming,ontology,registry,system,topology}/*` | delete | remove duplicated compact protocol material after verification |
| yai | `README.md` | update | change `specs/` from mirror to pointer |
| yai | `Documentation/meta/**/*.md` | update | remove active `specs/` protocol ownership claims |
| yai | `Documentation/reference/README.md` | update | repoint normative ownership to `protocols/` |
| yai | `Documentation/system/architecture/traceability.md` | update | repoint active protocol ownership |
| yai | `Documentation/system/knowledge/README.md` | update | repoint related protocol refs |
| yai | `Documentation/system/topology/**/*.md` | update | repoint topology ownership to `protocols/` |
| yai | `Documentation/operator/deployment/deployment-guide.md` | update | repoint protocol registry failure note |
| api | `README.md` | update | define API as projection repo with mapping/transport roots |
| api | `Documentation/api-projection-filesystem.md` | update | record V28.6 projection shape |
| api | `Documentation/protocol-api-boundary.md` | update | mark current projection-root reality |
| api | `Documentation/waves/v28-6-protocol-cutover-closure-api-projection-reshape.md` | create | delivery report |
| api | `transports/README.md` | create | projection-root placeholder |
| api | `mappings/README.md` | create | projection-root placeholder |
| api | `projections/README.md` | create | projection-root placeholder |
| api | `examples/README.md` | create | projection-root placeholder |
| api | `tools/README.md` | create | projection-root placeholder |
| api | `schemas/README.md` | update | classify schema mirrors vs API-owned schemas |
| api | `fixtures/README.md` | create | classify fixture mirrors |
| api | `contracts/README.md` | update | keep C contracts as audit surface |
| api | `conformance/README.md` | update | classify API-owned vs protocol-mirror checks |
| api | `registry/README.md` | update | define registry as API exposure grammar |
| api | `openapi/README.md` | update | define OpenAPI as projection only |

## V28.6.A — Cutover Status Audit

| Path | Result | Notes |
| ---- | ------ | ----- |
| `yai/specs` | duplicated compact protocol material found | `naming/`, `ontology/`, `registry/`, `system/`, `topology/` still present before this wave |
| `yai/protocols` | canonical replacement present | all compact protocol families verified in canonical destination |

## V28.6.B — Drain `yai/specs`

| Path | Result | Notes |
| ---- | ------ | ----- |
| `yai/specs/README.md` | kept | compatibility pointer only |
| `yai/specs/naming/*` | removed | canonical replacement exists in `yai/protocols/naming/` |
| `yai/specs/ontology/*` | removed | canonical replacement exists in `yai/protocols/ontology/` |
| `yai/specs/registry/*` | removed | canonical replacement exists in `yai/protocols/registry/` |
| `yai/specs/system/*` | removed | canonical replacement exists in `yai/protocols/system/` |
| `yai/specs/topology/*` | removed | canonical replacement exists in `yai/protocols/topology/` |

## V28.6.C — Rewrite Stale Path References

Pass with limits.

- active ownership and topology docs were repointed from `specs/` to
  `protocols/` where those protocol roots exist now;
- historical migration/audit documents were left intact;
- unrelated legacy references to non-protocol `specs/...` families remain
  deferred because those target ownership decisions are outside this wave.

## V28.6.D / E — API Projection Reshape and Classification

Pass.

- `api/transports`, `api/mappings`, `api/projections`, `api/examples`, and
  `api/tools` now exist as README-only projection roots;
- `api/schemas`, `api/fixtures`, `api/conformance`, `api/contracts`,
  `api/registry`, and `api/openapi` are documented as projection, mirror, or
  audit surfaces rather than protocol owners.

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| yai | `find specs -maxdepth 2 -type f | sort` | pass | confirms README-only compatibility surface |
| yai | `find protocols -name '*.json' -print0 \| xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | protocol JSON |
| yai | `make -j4` | pass | build/validation target remained up to date |
| yai | `make -j4 yai` | pass | runtime target remained up to date |
| yai | `rg -n "specs/|protocols/" README.md Documentation protocols specs` | pass | ownership verification |
| api | `find . -maxdepth 2 \\( -path './transports' -o -path './mappings' -o -path './projections' -o -path './examples' -o -path './tools' \\)` | pass | projection roots present |
| api | `find schemas -name '*.json' -print0 \| xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | schema JSON |
| api | `find fixtures -name '*.json' -print0 \| xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | fixture JSON |
| api | `python3 conformance/check_api_contracts.py` | pass | API conformance |
| api | `python3 conformance/check_operation_registry.py` | pass | registry conformance |
| api | `python3 conformance/check_logout_seal_policy.py` | pass | protocol mirror drift check |
| api | `python3 conformance/check_case_evidence_binding.py` | pass | protocol mirror drift check |
| api | `rg -n "projection|mirror|protocols" README.md docs schemas fixtures contracts conformance registry openapi transports mappings projections examples tools` | pass | wording verification |

## Residual Drift

- legacy non-protocol `specs/...` references still exist in parts of `yai`
  outside this wave's safe ownership scope;
- `api/schemas`, `api/fixtures`, and `api/conformance` remain mixed
  projection/mirror surfaces until a later split wave decides which artifacts
  stay API-owned versus move fully behind projections.
