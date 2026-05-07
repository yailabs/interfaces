# LAN Secure Errors v1

## Purpose

Freeze LAN transport and security error posture for `lan_secure`.

## Required Error Categories

- `lan_disabled`
- `pairing_required`
- `pairing_rejected`
- `device_not_allowed`
- `device_revoked`
- `insecure_channel`
- `bind_not_allowed`
- `operation_not_exposed_on_lan`
- `token_required`
- `token_rejected`
- `runtime_unavailable`

## Rules

- LAN transport or security failure remains distinct from runtime operation
  failure
- pairing or allowlist failure must not be flattened into generic operation
  denial
- runtime sealed or guard failures remain operation or guard errors after
  dispatch, not LAN transport errors
