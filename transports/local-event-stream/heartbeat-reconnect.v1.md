# Local Event Stream Heartbeat and Reconnect v1

## Purpose

Freeze long-lived stream liveness and reconnect posture.

## Rules

- heartbeat is required for long-lived streams
- reconnect semantics must be documented
- resume token posture must be explicit
- `last_event_id` posture must be explicit where SSE-style clients apply
- missing resume support must be explicit, not implicit

## Notes

- heartbeat timeout is transport or connection posture, not automatically
  operation failure
- reconnect behavior is client and runtime implementation later; API.06 defines
  the contract only
