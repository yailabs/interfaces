# Local HTTP Loopback Contract

## Purpose

API.05 defines `local_http_loopback` as the primary browser, dashboard, local
web UI, and developer/debug request-response transport contract before
implementation.

## Contract Summary

- binding: HTTP over loopback only
- allowed bind addresses: `127.0.0.1`, `::1`, `localhost`
- discovery order: explicit config, `YAI_LOCAL_HTTP_ENDPOINT`, discovery file,
  platform default, then `not_configured`
- route posture: invocation, metadata/readiness, local health/readiness,
  discovery, and optional stream pointer route
- request-response carriage: API.03 request envelopes and response envelopes
- browser-safe access posture: strict origin and CORS allowlist, local client
  token posture, no wildcard CORS
- security posture: same-machine, no LAN, no provider credential leakage

## Ownership

- API owns the `local_http_loopback` contract.
- Runtime implements the loopback server later.
- SDK TypeScript consumes the contract later.
- SDK Rust may keep HTTP as explicit override or dev transport later.
- Local Event Stream remains separate for realtime traffic.
