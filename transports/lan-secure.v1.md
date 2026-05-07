# LAN Secure v1

## Purpose

Define `lan_secure` as the explicit opt-in transport class for multi-machine
local-network runtime access.

API.07 verticalizes this transport into a dedicated contract subtree so
runtime, SDK, and client surfaces can align on pairing, discovery, endpoint
binding, allowlist, revocation, and operation exposure posture later without
turning Local HTTP Loopback into implicit LAN exposure.

## Bindings

- RPC over TCP/TLS
- HTTPS on a local network
- secure WebSocket only where justified

## Boundary Split

- `lan_secure` is controlled runtime exposure for another trusted machine on a
  local network.
- `lan_secure` is not `local_http_loopback`.
- `lan_secure` is not `remote_https`.
- `lan_secure` is not provider/model transport.
- `lan_secure` is not anonymous LAN or public internet exposure.

## Classification

- status: controlled
- class: paired secure local-network transport

## Ownership

- API owns: contract and security requirements
- Runtime owns: gated listener, pairing enforcement, token/certificate checks,
  allowlist, revocation, dispatch into runtime boundary adapters
- SDK owns: paired client behavior and secure client transport handling

## Security Baseline

- disabled by default
- no automatic `0.0.0.0` bind
- no wildcard LAN exposure
- explicit bind address required
- pairing required
- token or certificate required
- TLS or equivalent secure channel required
- device allowlist required
- revocation required
- operation exposure policy required

## Contract Surfaces

- `lan-secure/README.md`
- `lan-secure/pairing.v1.md`
- `lan-secure/discovery.v1.md`
- `lan-secure/endpoint-binding.v1.md`
- `lan-secure/security.v1.md`
- `lan-secure/device-allowlist.v1.md`
- `lan-secure/revocation.v1.md`
- `lan-secure/operation-exposure.v1.md`
- `lan-secure/errors.v1.md`
- `lan-secure/conformance-profile.v1.md`

## Non-goals

- not default local runtime execution
- not a replacement for local IPC RPC
- not Local HTTP Loopback on a wider bind address
- not Remote HTTPS platform transport
- no LAN listener implementation is added by this document
