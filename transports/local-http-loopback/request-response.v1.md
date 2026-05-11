# Local HTTP Loopback Request and Response v1

## Purpose

Freeze how `local_http_loopback` carries API.03 envelopes.

## Carriage

- HTTP carries API.03 request envelopes.
- HTTP carries API.03 response envelopes.
- `application/json` is the required content type for v1.

## Separation Rule

- `local_http_loopback` must not carry Local Event Stream frames as normal
  response envelopes.
- Realtime stream transport remains separate under `local_event_stream`.
- HTTP request and response posture remains request-response only in API.05.
