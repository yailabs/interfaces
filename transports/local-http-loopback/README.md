# Local HTTP Loopback Contract

`api/transports/local-http-loopback/` holds the verticalized API.05 contract
for the `local_http_loopback` transport class.

Purpose:
- define the primary browser, dashboard, local web UI, and dev/debug
  request-response transport contract
- freeze discovery, route posture, headers, origin/CORS, local token posture,
  security, and error separation before implementation
- keep Local Event Stream separate for realtime delivery

Primary clients:
- dashboard web
- local browser UI
- TypeScript SDK in browser-compatible contexts
- developer/debug tools
- curl/Postman-like local inspection
- optional Rust SDK override or dev transport

Boundary:
- API defines the contract only.
- Runtime implements the loopback server later.
- SDK TypeScript consumes the contract later.
- SDK Rust may use it as explicit override or dev transport later.
- No HTTP server, router, CORS middleware, or token implementation is added
  here.
