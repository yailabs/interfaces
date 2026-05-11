# LAN Secure Device Allowlist v1

## Purpose

Define device allowlist posture for `lan_secure`.

## Rules

- device allowlist is required
- allowlist decisions remain separate from operation authorization
- non-allowed devices must fail before operation dispatch
- allowlist status must be revocable

## Boundary

- API.07 documents allowlist posture only
- no allowlist storage or enforcement implementation is added here
