# Local HTTP Loopback Headers v1

## Purpose

Define the required header roles for `local_http_loopback`.

## Required Header Roles

- API version header
- request id header
- correlation id header
- local client token or equivalent future local credential header
- content type header
- accepted content type header
- optional idempotency key header

## Notes

- API.05 defines header roles and intent, not a runtime middleware
  implementation.
- Header grammar remains API-owned; SDK and runtime will consume it later.
