# Local HTTP Loopback Conformance Profile v1

## Purpose

Define the minimum contract claims that a future `local_http_loopback`
implementation must satisfy.

## Required Contract Areas

- loopback-only discovery and binding posture
- route posture
- API.03 request-envelope and response-envelope carriage
- header roles and `application/json` content type
- strict local-origin and no-wildcard CORS posture
- local client token posture for sensitive operations
- separation of transport failure from operation failure

## Out of Scope for API.05

- HTTP server implementation
- router implementation
- CORS middleware implementation
- local client token implementation
- SDK `LocalHttpLoopbackTransport`
- dashboard, CLI, or Loom behavior changes
