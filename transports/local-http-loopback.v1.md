# Local HTTP Loopback v1

## Purpose

Define `local_http_loopback` as the primary browser/dashboard/dev transport for
local runtime access.

API.05 verticalizes this transport into a dedicated contract subtree so runtime
and SDK can implement discovery, route handling, headers, origin/CORS, local
token posture, and error separation later without inventing divergent rules.

## Binding

- HTTP over `127.0.0.1`
- HTTP over `::1`
- HTTP over `localhost`

## Classification

- status: primary now
- class: local browser-friendly request/response transport

## Ownership

- API owns: route contract, request/response envelope, headers, CORS/origin
  policy, local auth/token mapping, error mapping
- Runtime owns: loopback server, router, binding policy, dispatch into
  `runtime/boundary/api`
- SDK owns: browser-compatible HTTP client and optional Rust HTTP override

## Contract Surfaces

- `local-http-loopback/README.md`
- `local-http-loopback/discovery.v1.md`
- `local-http-loopback/route-model.v1.md`
- `local-http-loopback/request-response.v1.md`
- `local-http-loopback/headers.v1.md`
- `local-http-loopback/origin-cors-policy.v1.md`
- `local-http-loopback/local-client-token.v1.md`
- `local-http-loopback/security.v1.md`
- `local-http-loopback/errors.v1.md`
- `local-http-loopback/platform-bindings.v1.md`
- `local-http-loopback/conformance-profile.v1.md`

## Primary Users

- dashboard/web/browser surfaces
- local debug clients
- development tooling that benefits from browser-compatible transport

## Security Baseline

- bind to loopback only by default
- strict origin/CORS posture
- local client token or equivalent required before sensitive operations
- no LAN exposure by default
- same-machine by default
- no raw provider credential exposure
- no provider/model direct transport through browser

## Non-goals

- not the only canonical YAI transport
- not the required native local transport for Rust CLI/Loom
- no HTTP server implementation is added by this document
