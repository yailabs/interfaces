# Local Event Stream Errors and Terminal Events v1

## Purpose

Preserve the distinction between stream transport failure, operation stream
error, normal closure, and cancellation.

## Rules

- stream transport error and operation stream error are distinct
- terminal error frame must include `error`
- stream closed normally must be terminal without implying operation failure
- heartbeat timeout is transport or connection posture, not automatically
  operation failure
- terminal stream frames close streams; they are not normal operation responses
