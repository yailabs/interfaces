# LAN Secure Contract

`api/transports/lan-secure/` holds the verticalized API.07 contract for the
`lan_secure` transport class.

Purpose:
- define controlled opt-in local-network access to a local YAI runtime
- freeze pairing, discovery, endpoint binding, allowlist, revocation, and
  operation exposure posture before implementation
- keep LAN exposure separate from loopback-local browser access and from
  Remote HTTPS platform traffic

Boundary:
- `lan_secure` is disabled by default.
- `lan_secure` requires explicit enablement and explicit bind address.
- `lan_secure` is not `local_http_loopback`.
- `lan_secure` is not `remote_https`.
- `lan_secure` is not provider/model transport.

Required posture:
- pairing required
- device allowlist required
- revocation required
- TLS, token, certificate, or equivalent secure channel posture required
- operation exposure policy required
- no automatic `0.0.0.0`

Out of scope:
- no LAN listener
- no pairing implementation
- no allowlist implementation
- no revocation implementation
