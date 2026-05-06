# API Projection Filesystem

## Status

* Delivery: V28.5
* Repo: `api`
* Role: API projection over canonical YAI protocols

## Purpose

Define `api` as API projection, not protocol source of truth.

## Canonical Rule

```text
api projects yai/protocols into API surfaces.
api does not own protocol meaning.
```

## API Owns

```text
openapi/
registry/api-*.json
API operation registry
API projection docs
HTTP/transport request-response mapping
API-specific conformance
```

## API Does Not Own

```text
transport-neutral protocol meaning
runtime behavior
SDK client behavior
E business/account backend
raw provider identity
pricing/billing objects
```

## Migration Map

| Path | Current role | Target owner | Classification | Action |
| ---- | ------------ | ------------ | -------------- | ------ |
| `api/schemas` | mixed protocol contracts plus API-facing schema projection | split: `yai/protocols` + `api` | `protocol_canonical_move_later` | keep API copies as mirrors now; V28/V29 protocol-neutral schemas mirrored into `yai/protocols/schemas`; broader split deferred because OpenAPI and registry refs still point here |
| `api/fixtures` | protocol fixtures for logout/evidence examples | `yai/protocols` | `protocol_canonical_move_now` | mirrored to `yai/protocols/fixtures`; API copies retained as projection/validation mirrors |
| `api/conformance/check_logout_seal_policy.py` | protocol conformance consumer | `yai/protocols` | `conformance_protocol_move` | canonical checker mirrored into `yai/protocols/conformance`; API wrapper now validates canonical protocol files and fails on API mirror drift |
| `api/conformance/check_case_evidence_binding.py` | protocol conformance consumer | `yai/protocols` | `conformance_protocol_move` | canonical checker mirrored into `yai/protocols/conformance`; API wrapper now validates canonical protocol files and fails on API mirror drift |
| `api/conformance/check_api_contracts.py` | API conformance | `api` | `conformance_api_keep` | keep in `api` |
| `api/conformance/check_operation_registry.py` | API registry conformance | `api` | `conformance_api_keep` | keep in `api` |
| `api/registry` | API projection registry | `api` | `api_projection_keep` | keep in `api` |
| `api/openapi` | HTTP/API projection | `api` | `api_projection_keep` | keep in `api` |
| `api/contracts/*.c/*.h` | C contract artifacts | audit | `legacy_c_contract_audit` | keep in place; classify in a separate ABI/reference wave before any move |
| `api/docs/execution` | protocol-facing doctrine mirrored inside API repo | split | `protocol_canonical_move_later` | keep as API-side mirror for now; eventual canonical protocol doc destination should be under `yai/protocols` or an explicitly split protocol-doc surface |
| `api/docs/runtime` | mixed runtime boundary and API projection docs | split | `api_projection_refactor_later` | keep; classify doc-by-doc later |
| `api/docs/waves` | historical delivery reports | `api` | `wave_report_keep` | keep in `api` |

## Filesystem Notes

`api` remains the right owner for:

- HTTP projection
- OpenAPI transport exposure
- API family/verb/operation registry
- API-specific compatibility and contract-release checks
- mirror verification that `api/schemas`, `api/fixtures`, and protocol-facing conformance stay aligned with `yai/protocols`

`api` is no longer the right canonical owner for transport-neutral protocol
meaning such as logout/evidence contract semantics once those can live safely in
`yai/protocols`.

See also:

- `docs/protocol-api-boundary.md`
