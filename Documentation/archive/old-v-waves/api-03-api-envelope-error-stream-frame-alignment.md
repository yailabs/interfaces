# API.03 — API Envelope / Error / Stream Frame Alignment

## Status

- Delivery: API.03
- Status: done
- Track: API / Transport / SDK / Runtime alignment
- Repo branch: `refoundation/phase-01`
- Repo change type: envelope/error/stream-frame contract alignment
- Previous delivery: API.02 — Operation-to-Transport Mapping / Dispatch Contract
- Next delivery: API.04 — Local IPC RPC Contract Verticalization

## Purpose

API.03 defines the API wire envelope, error, operation result, readiness, and
stream frame model before implementation. The wave freezes the transport-facing
grammar that runtime listeners and SDK transports will carry later without
implementing those listeners or transports now.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| `api` | `envelopes/README.md` | modified | freeze envelope boundary vocabulary |
| `api` | `envelopes/api-envelope-model.v1.md` | added | define base transport-facing envelope fields |
| `api` | `envelopes/request-envelope.v1.md` | added | define canonical request envelope |
| `api` | `envelopes/response-envelope.v1.md` | added | define canonical terminal response envelope |
| `api` | `envelopes/readiness-envelope.v1.md` | added | define readiness/status projection envelope |
| `api` | `errors/README.md` | modified | freeze API error boundary vocabulary |
| `api` | `errors/api-error-model.v1.md` | added | define canonical API error object |
| `api` | `errors/error-code-registry.v1.json` | added | freeze API.03 error code metadata |
| `api` | `errors/error-http-status-map.v1.json` | added | freeze HTTP status projection for API errors |
| `api` | `errors/error-transport-map.v1.md` | added | separate transport failure from operation failure |
| `api` | `lifecycle/README.md` | modified | align lifecycle/result vocabulary to API.03 |
| `api` | `lifecycle/operation-result-model.v1.md` | added | define normalized `result` payload model |
| `api` | `schemas/envelope.v1.schema.json` | modified | align base API envelope schema |
| `api` | `schemas/request-envelope.v1.schema.json` | modified | align request envelope schema |
| `api` | `schemas/response-envelope.v1.schema.json` | modified | align response envelope schema |
| `api` | `schemas/error.v1.schema.json` | modified | align error schema with category/flag model |
| `api` | `schemas/operation-result.v1.schema.json` | modified | align result posture vocabulary |
| `api` | `schemas/readiness-envelope.v1.schema.json` | modified | align readiness/status envelope |
| `api` | `schemas/watch-event.v1.schema.json` | modified | align stream frame identity and terminal semantics |
| `api` | `registry/api-envelopes.v1.json` | modified | register canonical envelope/error/frame requirements |
| `api` | `registry/api-errors.v1.json` | modified | preserve string-list compatibility while adding API.03 metadata |
| `api` | `mappings/operation-dispatch-contract.v1.md` | modified | align dispatch flow to request/response envelopes and stream handoff |
| `api` | `mappings/streamable-operation-policy.v1.md` | modified | separate stream frames from response envelopes |
| `api` | `conformance/check_api_envelope_error_stream.py` | added | validate API.03 schema/registry/mapping alignment |
| `api` | `conformance/README.md` | modified | register the new API.03 conformance checker |
| `api` | `Documentation/api-envelope-error-stream-model.md` | added | summarize the API.03 wire model |
| `api` | `Documentation/waves/api-03-api-envelope-error-stream-frame-alignment.md` | added | record wave scope and validation |
| `yai` | `runtime/boundary/api/README.md` | modified | align runtime boundary to normalized request/response envelope ownership |
| `yai` | `runtime/boundary/transport/README.md` | modified | align runtime transport boundary to frame-to-envelope conversion role |
| `yai` | `runtime/connections/README.md` | modified | align connection observation to request/stream identity without semantic ownership |
| `sdk` | `README.md` | modified | state SDK consumes API.03 envelope/error/frame grammar |
| `sdk` | `generated/README.md` | modified | keep generated outputs as projections, not grammar source-of-truth |
| `sdk` | `packages/rust/README.md` | modified | align Rust SDK docs to API.03 envelope ownership |
| `sdk` | `packages/typescript/README.md` | modified | align TypeScript SDK docs to API.03 envelope ownership |

## Existing Schema Audit

| Schema | Result | Notes |
| ------ | ------ | ----- |
| `schemas/envelope.v1.schema.json` | aligned | base wire fields frozen; request/response envelope transport enum excludes `local_event_stream` as a generic carrier |
| `schemas/request-envelope.v1.schema.json` | aligned | `operation_id` and `request_id` remain required; `stream_request`, `timeout_ms`, and `cancellation_ref` added as envelope controls |
| `schemas/response-envelope.v1.schema.json` | aligned | finite status vocabulary and result/error terminal exclusivity added |
| `schemas/error.v1.schema.json` | aligned | required category and transport/operation/guard flags frozen |
| `schemas/operation-result.v1.schema.json` | aligned | result posture aligned to API.03 status vocabulary while keeping payload flexible |
| `schemas/readiness-envelope.v1.schema.json` | aligned | richer readiness envelope frozen while preserving current simplified projection compatibility |
| `schemas/watch-event.v1.schema.json` | aligned | stream frame identity, event class, heartbeat, retry, and terminal semantics frozen separately from response envelopes |

## Envelope Model Result

Record:
- base envelope fields: `schema`, `envelope_id`, `operation_id`, `request_id`, `correlation_id`, `client`, optional `case_ref`, optional `principal_ref`, `transport`, `created_at`, optional `metadata`
- request envelope fields: base envelope plus required `input` and optional `idempotency_key`, `stream_request`, `timeout_ms`, `cancellation_ref`
- response envelope fields: base envelope plus required `status` and optional `result`, `error`, `warnings`, `records`, `evidence_refs`, `readiness`, `stream_ref`
- readiness/status relation: readiness remains an explicit API-facing projection payload and does not become implicit runtime truth
- terminal result/error rule: terminal response envelopes carry exactly one of `result` or `error`
- no behavior implementation: yes

## Error Model Result

Record:
- error categories: `validation`, `unauthorized`, `forbidden`, `not_found`, `conflict`, `rate_limited`, `unavailable`, `timeout`, `cancelled`, `unsupported`, `runtime_sealed`, `transport`, `internal`
- error-code registry: `errors/error-code-registry.v1.json`
- HTTP status map: `errors/error-http-status-map.v1.json`
- transport vs operation error distinction: explicit through `transport_error`, `operation_error`, and `guard_error`
- runtime sealed / unavailable distinction: explicit through separate codes such as `runtime_sealed`, `runtime_unavailable`, and `provider_unavailable`

## Stream Frame Result

Record:
- stream frame fields: `schema`, `stream_id`, `event_id`, `operation_id`, `request_id`, `sequence`, `event_type`, `created_at`, optional `data`, optional `error`, `terminal`, `heartbeat`, optional `retry_after_ms`, optional `resume_token`
- event_type classes: `stream.open`, `stream.heartbeat`, `stream.data`, `stream.warning`, `stream.error`, `stream.cancelled`, `stream.closed`
- terminal frame semantics: terminal stream frames explicitly classify closed, cancelled, or error posture
- heartbeat/reconnect posture: heartbeat and reconnect metadata are frozen through `heartbeat`, `retry_after_ms`, and `resume_token`
- separation from response envelope: stream frames are not modeled as normal response envelopes; `local_event_stream` carries stream frames only

## Transport Relationship

Record:
- `local_ipc_rpc` carries request/response envelopes and RPC stream frames
- `local_http_loopback` carries request/response envelopes
- `local_event_stream` carries stream frames only
- `provider_transport_boundary` is excluded

## Runtime/SDK Compatibility Notes

Record:
- SDK simplified envelopes remain migration-era implementation until later SDK waves
- current `HttpTransport` and `YAI_API_ENDPOINT` wiring in SDK, CLI, and Loom remain implementation reality rather than API.03 grammar ownership
- runtime boundary docs are aligned to request/response envelope and stream handoff ownership, but runtime behavior is unchanged
- CLI and Loom behavior is unchanged
- out-of-scope legacy docs such as `Documentation/REQUEST_RESPONSE_MODEL.md` and `conformance/CHECKLIST.md` still reflect older wording and remain deferred drift for a later cleanup wave

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| `api` | `find envelopes errors lifecycle schemas registry mappings conformance docs -maxdepth 3 -type f | sort` | pass | confirmed API.03 surfaces and checker/report files exist |
| `api` | `python3 - <<'PY' ... json.load(...) ... PY` over envelope/error/registry/mapping files | pass | parsed `schemas/envelope.v1.schema.json`, `schemas/request-envelope.v1.schema.json`, `schemas/response-envelope.v1.schema.json`, `schemas/error.v1.schema.json`, `schemas/operation-result.v1.schema.json`, `schemas/readiness-envelope.v1.schema.json`, `schemas/watch-event.v1.schema.json`, `registry/api-envelopes.v1.json`, `registry/api-errors.v1.json`, and `mappings/operation-transport-map.v1.json` |
| `api` | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| `api` | `python3 conformance/check_operation_registry.py` | pass | `conformance: ok` |
| `api` | `python3 conformance/check_operation_transport_mapping.py` | pass | `operation-transport-map: ok` |
| `api` | `python3 conformance/check_api_envelope_error_stream.py` | pass | `api-envelope-error-stream: ok` |
| `api` | `find schemas registry errors -name '*.json' -print0 \| xargs -0 -n1 python3 -m json.tool >/dev/null` | pass | all touched JSON files parse |
| `api` | `git diff --check` | pass | required |
| `yai` | `git diff --check` | pass | touched boundary docs only |
| `sdk` | `rg -n "YaiEnvelope\|envelope\|error\|status\|transport\|watch\|stream\|response\|request\|operation_id\|HttpTransport" README.md generated packages/rust packages/typescript 2>/dev/null \|\| true` | pass | audit confirmed simplified SDK envelope types and current HTTP transport remain compatibility-era implementation |
| `sdk` | `git diff --check` | pass | touched docs only |
| `cli` | `test ! -e source` | pass | required source-absence guard |
| `cli` | `scripts/check-no-source-dependency.sh` | pass | required |
| `cli` | `git diff --check` | pass | repo untouched by API.03 |
| `loom` | `rg -n "envelope\|error\|status\|operation_id\|transport\|stream\|watch\|posture" README.md src tests 2>/dev/null \|\| true` | pass | audit confirmed no API.03 behavior changes were required |
| `loom` | `git diff --check` | pass | repo untouched by API.03 |
| `all` | `rg -n "SDK defines envelope grammar\|CLI defines envelope grammar\|Loom defines envelope grammar\|API implements runtime envelope normalization\|API implements listener\|runtime owns API schema source of truth\|stream frames are response envelopes\|provider transport is client envelope transport\|HTTP error equals operation error" ../api ../yai ../sdk ../cli ../loom 2>/dev/null \|\| true` | pass/classified | matches appeared only inside wave-report command text in `api/Documentation/waves/api-02-operation-to-transport-mapping-dispatch-contract.md` and this API.03 wave report; no positive ownership claims found |

## Non-Implementation Confirmation

Record:
- no runtime listener
- no runtime envelope normalizer implementation
- no SDK encoder/decoder implementation
- no CLI/Loom behavior change
- no OpenAPI route expansion
- no provider/model behavior change
