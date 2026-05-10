# API.05 — Local HTTP Loopback Contract Verticalization

## Status

* Delivery: API.05
* Status: done
* Track: API / Transport / SDK / Runtime alignment
* Repo branch: `refoundation/phase-01`
* Repo change type: Local HTTP Loopback contract verticalization
* Previous delivery: API.04 — Local IPC RPC Contract Verticalization
* Next delivery: API.06 — Local Event Stream Contract Verticalization

## Purpose

API.05 defines Local HTTP Loopback as the primary browser, dashboard, local web
UI, and developer/debug transport contract before implementation.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| `api` | `transports/local-http-loopback.v1.md` | modified | expand the root Local HTTP Loopback contract and link the verticalized subtree |
| `api` | `transports/local-http-loopback/README.md` | added | create the Local HTTP Loopback contract root |
| `api` | `transports/local-http-loopback/discovery.v1.md` | added | define endpoint discovery order and result classes |
| `api` | `transports/local-http-loopback/route-model.v1.md` | added | define route posture without implementing routes |
| `api` | `transports/local-http-loopback/request-response.v1.md` | added | freeze HTTP carriage of API.03 request and response envelopes |
| `api` | `transports/local-http-loopback/headers.v1.md` | added | define required header roles |
| `api` | `transports/local-http-loopback/origin-cors-policy.v1.md` | added | define strict local-origin and no-wildcard CORS posture |
| `api` | `transports/local-http-loopback/local-client-token.v1.md` | added | define local token posture for sensitive operations |
| `api` | `transports/local-http-loopback/security.v1.md` | added | define loopback-only security posture |
| `api` | `transports/local-http-loopback/errors.v1.md` | added | preserve HTTP transport vs operation error distinction |
| `api` | `transports/local-http-loopback/platform-bindings.v1.md` | added | freeze loopback-only binding addresses |
| `api` | `transports/local-http-loopback/conformance-profile.v1.md` | added | define minimum contract claims for future implementations |
| `api` | `Documentation/local-http-loopback-contract.md` | added | summarize the API.05 contract |
| `api` | `Documentation/waves/api-05-local-http-loopback-contract-verticalization.md` | added | record scope and validation |
| `api` | `conformance/check_local_http_loopback_contract.py` | added | validate Local HTTP Loopback contract structure and wording |
| `api` | `conformance/README.md` | modified | register the new API.05 conformance checker |
| `api` | `mappings/transport-selection-policy.v1.md` | modified | cross-link browser selection policy to Local HTTP Loopback contract docs |
| `api` | `mappings/operation-dispatch-contract.v1.md` | modified | cross-link dispatch ownership to API.05 Local HTTP Loopback contract |
| `api` | `transports/README.md` | modified | cross-link the verticalized HTTP Loopback subtree |
| `yai` | `runtime/boundary/service/README.md` | modified | align future service exposure to loopback-only default |
| `yai` | `runtime/boundary/transport/README.md` | modified | align HTTP request normalization ownership |
| `yai` | `runtime/boundary/api/README.md` | modified | make Local HTTP Loopback dispatch explicit and transport-agnostic after normalization |
| `yai` | `runtime/connections/README.md` | modified | document HTTP observation scope without CORS ownership |
| `sdk` | `generated/README.md` | modified | keep generated HTTP artifacts as API contract projections only |
| `sdk` | `packages/typescript/README.md` | modified | align browser/dashboard HTTP target ownership |
| `sdk` | `packages/rust/README.md` | modified | keep Rust HTTP as override or dev transport only |

## Existing Surface Audit

| Surface | Result | Notes |
| ------- | ------ | ----- |
| `api/transports/local-http-loopback.v1.md` | updated | pre-existing root contract now points to a verticalized subtree |
| `yai/runtime/boundary/service` | documented | remains the future loopback service exposure boundary |
| `yai/runtime/boundary/transport` | documented | remains the future request normalization boundary for HTTP |
| `sdk/packages/typescript` | documented | current browser/client wording already pointed to loopback and event stream; now made contract-specific |
| `sdk/packages/rust` | documented | current `HttpTransport` remains migration-era override or dev transport |
| `cli` | untouched | still reflects migration-era HTTP transport wiring through SDK |
| `loom` | untouched | still reflects migration-era endpoint/backend wording |

## Contract Result

Record:
- binding: HTTP over loopback only
- allowed bind addresses: `127.0.0.1`, `::1`, `localhost`
- forbidden default binding: `0.0.0.0`, LAN interface, public interface, wildcard host exposure
- discovery order: explicit config, `YAI_LOCAL_HTTP_ENDPOINT`, runtime discovery file, platform default loopback port or registry, then `not_configured`
- route posture: operation invocation, metadata/readiness, local health/readiness, discovery, and optional stream discovery pointer route
- request-response carriage: API.03 request envelopes and response envelopes over `application/json`
- header roles: API version, request id, correlation id, local client token, content type, accepted content type, optional idempotency key
- origin/CORS posture: local-origin allowlist only, no wildcard CORS, no broad reflection
- token posture: local client token or equivalent required before sensitive operations
- error distinction: HTTP transport or security failure remains separate from operation, guard, or runtime failure carried inside API.03 response envelopes

## Security Result

Record:
- same-machine only by default
- loopback-only binding
- no LAN by default
- no wildcard CORS
- no provider credential leakage
- no provider/model direct transport through browser

## Runtime/SDK Ownership Result

Record:
- API owns contract
- runtime will implement loopback server later
- SDK TypeScript will implement browser-facing client behavior later
- SDK Rust may retain HTTP as explicit override or dev transport
- CLI/Loom behavior unchanged

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| `api` | `find transports/local-http-loopback* transports mappings schemas errors envelopes conformance docs -maxdepth 4 -type f | sort` | pass | confirmed Local HTTP Loopback subtree, checker, and wave report exist |
| `api` | `rg -n "local_http_loopback\|HTTP\|loopback\|127.0.0.1\|::1\|localhost\|CORS\|origin\|token\|request-response\|header\|route\|LAN\|provider transport\|implementation" README.md transports mappings schemas errors envelopes conformance docs 2>/dev/null \|\| true` | pass | audit confirmed contract vocabulary and pre-existing HTTP transport references |
| `yai` | `find runtime/boundary/service runtime/boundary/transport runtime/boundary/api runtime/connections -maxdepth 3 -type f | sort` | pass | confirmed pre-existing runtime service and boundary surfaces |
| `yai` | `rg -n "HTTP\|loopback\|127.0.0.1\|::1\|localhost\|local_http_loopback\|CORS\|origin\|token\|request_id\|client_ref\|connection\|provider transport\|implementation" runtime/boundary/service runtime/boundary/transport runtime/boundary/api runtime/connections README.md 2>/dev/null \|\| true` | pass | audit confirmed documentation alignment points |
| `sdk` | `rg -n "local_http_loopback\|HTTP\|loopback\|YaiTransport\|HttpTransport\|transport\|origin\|CORS\|token\|header\|envelope\|stream\|YAI_API_ENDPOINT" README.md generated packages/typescript packages/rust 2>/dev/null \|\| true` | pass | audit confirmed TypeScript loopback target and Rust HTTP migration-era reality |
| `cli` | `test ! -e source` | pass | required source-absence guard |
| `cli` | `scripts/check-no-source-dependency.sh` | pass | required |
| `cli` | `rg -n "HttpTransport\|YAI_API_ENDPOINT\|local_http_loopback\|HTTP\|loopback\|transport\|runtime" README.md src tests 2>/dev/null \|\| true` | pass | current CLI still reflects migration-era HTTP transport wiring |
| `loom` | `rg -n "HttpTransport\|YAI_API_ENDPOINT\|local_http_loopback\|HTTP\|loopback\|transport\|runtime\|backend" README.md src tests 2>/dev/null \|\| true` | pass | current Loom still reflects migration-era endpoint or backend wording |
| `api` | `python3 conformance/check_api_contracts.py` | pass | `api-contracts: ok` |
| `api` | `python3 conformance/check_operation_registry.py` | pass | `conformance: ok` |
| `api` | `python3 conformance/check_operation_transport_mapping.py` | pass | `operation-transport-map: ok` |
| `api` | `python3 conformance/check_api_envelope_error_stream.py` | pass | `api-envelope-error-stream: ok` |
| `api` | `python3 conformance/check_local_http_loopback_contract.py` | pass | `local-http-loopback-contract: ok` |
| `api` | `git diff --check` | pass | required |
| `yai` | `git diff --check` | pass | required |
| `sdk` | `git diff --check` | pass | docs-only touches |
| `cli` | `git diff --check` | pass | untouched |
| `loom` | `git diff --check` | pass | untouched |
| `all` | `rg -n "HTTP server implemented\|router implemented\|CORS middleware implemented\|SDK implements local_http_loopback\|dashboard defaults switched\|provider transport is local_http_loopback\|LAN enabled by default\|API implements HTTP server\|API owns loopback listener lifecycle" ../api ../yai ../sdk ../cli ../loom 2>/dev/null \|\| true` | pass/classified | matches appeared only inside the API.05 checker forbidden-phrase list and wave-report command text; no positive implementation claims found |

## Non-Implementation Confirmation

Record:
- no HTTP server
- no router implementation
- no CORS middleware implementation
- no local client token implementation
- no runtime listener implementation
- no SDK `LocalHttpLoopbackTransport`
- no dashboard, CLI, or Loom behavior change
