# Local Event Stream

Local event stream carries streamable API events, progress, watch output, and terminal frames.

## Artifact References

- ``transports/local-event-stream.v1.md``
- ``transports/local-event-stream/``

## Contract Model

Event stream defines subscription, event type, frame, heartbeat, reconnect, resume, backpressure, terminal events, and redaction policy.

## Operation Relationship

Allowed operations are controlled by `mappings/operation-transport-map.v1.json` and related mapping policy. Transport docs describe how operations are carried; operation docs define what operations mean.
