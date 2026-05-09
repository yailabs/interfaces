# LAN Secure and Remote HTTPS Boundary

## Purpose

API.07 separates `lan_secure` from `remote_https` so local-network runtime
exposure is never confused with YAI platform/account/update/future remote
capability traffic.

## Boundary Split

| Boundary | Role | Default posture | Notes |
| -------- | ---- | --------------- | ----- |
| Local IPC RPC | same-machine native local | primary native | CLI and Loom target default |
| Local HTTP Loopback | same-machine browser/dev | primary browser/dev | not LAN |
| Local Event Stream | realtime projection | primary realtime | not response envelope |
| LAN Secure | paired local-network runtime access | disabled | explicit opt-in only |
| Remote HTTPS | platform/account/update/future capability | controlled/future | not default runtime execution |
| Provider Transport | runtime -> provider/model | separate | not client-runtime |

## Key Rules

- Local HTTP Loopback is not LAN.
- LAN Secure is disabled by default and requires pairing, allowlist, and
  revocation.
- Remote HTTPS is not default local runtime execution.
- Provider transport is not YAI Remote HTTPS.
- Provider HTTP APIs are provider/model transport, not platform Remote HTTPS.
- Hosted compute is not implemented by API.07.
