# LAN Secure Security v1

## Purpose

Freeze the minimum security posture for `lan_secure`.

## Rules

- disabled by default
- pairing required
- device allowlist required
- revocation required
- token, certificate, or equivalent proof required
- TLS or equivalent secure channel required
- sensitive operations still pass the runtime guard chain
- provider credentials must never be exposed as LAN transport payloads

## Boundary

- API.07 adds no LAN security implementation
