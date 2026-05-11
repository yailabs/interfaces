# Stream Frame Model

Stream frames carry ordered API events for watch, progress, subscription, or terminal stream behavior.

## Frame Semantics

A stream frame identifies event type, sequence or cursor position, payload, error or terminal state, and metadata needed for redaction, resume, and backpressure.

## Artifact References

- `schemas/watch-event.v1.schema.json`
- `transports/local-event-stream/event-frame.v1.schema.json`
- `transports/local-event-stream/event-types.v1.json`
- `transports/local-event-stream/backpressure-resume.v1.md`
- `transports/local-event-stream/heartbeat-reconnect.v1.md`
