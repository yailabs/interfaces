# Local Event Stream Security and Redaction v1

## Purpose

Freeze projection-safe stream payload posture for `local_event_stream`.

## Rules

- stream payloads must be projection-safe
- sensitive provider or model raw payloads must not be streamed directly
- provider credentials must never appear in stream payloads
- LAN remains blocked by default unless `lan_secure` is separately enabled
- browser streams must obey the same local origin and token posture as Local
  HTTP Loopback where applicable
- redaction posture may be declared explicitly in stream frames
