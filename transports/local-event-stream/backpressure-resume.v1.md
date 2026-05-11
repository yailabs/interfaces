# Local Event Stream Backpressure and Resume v1

## Purpose

Define slow-consumer, dropped-event, and resumability posture for event
streams.

## Rules

- slow consumer posture must be explicit
- dropped event posture must be explicit
- buffer overflow posture must be explicit
- resumable and non-resumable stream classes must be explicit
- terminal error behavior must be explicit

## Contract Guidance

- resumable streams should use `resume_token` or `last_event_id` posture
- non-resumable streams must close with explicit terminal posture rather than
  silent loss
- provider/model raw payloads must never be exposed as a backpressure shortcut
