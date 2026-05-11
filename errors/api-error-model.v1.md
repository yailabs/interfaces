# API Error Model v1

## Purpose

Freeze the canonical API error object carried inside response envelopes and
stream error frames.

## Required Fields

- `code`
- `message`
- `category`
- `retryable`
- `transport_error`
- `operation_error`
- `guard_error`

## Optional Fields

- `details`
- `cause`
- `refs`

## Required Categories

- `validation`
- `unauthorized`
- `forbidden`
- `not_found`
- `conflict`
- `rate_limited`
- `unavailable`
- `timeout`
- `cancelled`
- `unsupported`
- `runtime_sealed`
- `transport`
- `internal`

## Boundary Rule

- Transport failure is not the same thing as operation failure.
- Guard or sealed posture failure is not the same thing as raw transport
  failure.
- Provider/model transport errors are not exposed as raw provider transport
  frames in the client-runtime API.
