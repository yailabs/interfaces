# LAN Secure Endpoint Binding v1

## Purpose

Freeze LAN binding posture for `lan_secure` without implementing listeners.

## Rules

- explicit bind address is required
- automatic `0.0.0.0` is prohibited
- wildcard LAN exposure is prohibited
- public internet exposure is prohibited
- TLS or equivalent secure channel is required for LAN transport carriage
- Local HTTP Loopback must not be treated as LAN by widening its bind address

## Boundary

- API.07 defines endpoint posture only
- no TCP, TLS, HTTPS, or WebSocket listener is added here
