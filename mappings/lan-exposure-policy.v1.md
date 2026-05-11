# LAN Exposure Policy v1

## Purpose

This policy prevents API.02 from quietly turning local runtime operations into
default network-exposed operations.

## Baseline

- `lan_secure` is controlled and disabled by default.
- No operation implies automatic `0.0.0.0` bind.
- Pairing is required before any LAN client may use a mapped operation.
- Token, certificate, or equivalent proof is required.
- Device allowlist and revocation posture are required.

## Mapping Rule

- Only operations marked `allowed_with_pairing` may include `lan_secure` in
  `allowed_transports`.
- Operations marked `blocked_by_default` must not imply LAN availability.
- API.02 keeps write, mutating, stream, platform-remote, and compatibility
  surfaces off LAN by default.

## Current Intent

- Read-oriented local runtime inspection surfaces may later travel over
  `lan_secure` when pairing and runtime enforcement exist.
- API.02 does not implement pairing, listeners, or LAN execution.

See also:
- `../transports/lan-secure.v1.md`
- `../transports/lan-secure/README.md`
- `../Documentation/lan-secure-remote-https-boundary.md`
