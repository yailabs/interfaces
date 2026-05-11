# LAN Secure Revocation v1

## Purpose

Define revocation posture for paired or allowed LAN clients.

## Rules

- revocation is required
- revoked devices or credentials must not remain implicitly trusted
- revocation failures remain distinct from normal runtime operation failure
- revocation posture must apply to pairing identity and device allowlist state

## Boundary

- API.07 documents revocation posture only
- no revocation implementation is added here
