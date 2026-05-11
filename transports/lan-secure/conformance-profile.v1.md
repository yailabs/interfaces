# LAN Secure Conformance Profile v1

## Purpose

Define the minimum contract claims that a future `lan_secure`
implementation must satisfy.

## Required Contract Areas

- disabled-by-default posture
- no automatic `0.0.0.0`
- explicit bind address
- pairing required
- device allowlist required
- revocation required
- TLS, token, certificate, or equivalent secure channel posture
- operation exposure policy
- explicit separation from Local HTTP Loopback and Remote HTTPS

## Out of Scope for API.07

- no LAN listener implementation
- no pairing implementation
- no allowlist implementation
- no revocation implementation
