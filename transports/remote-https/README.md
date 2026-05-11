# Remote HTTPS Contract

`api/transports/remote-https/` holds the verticalized API.07 contract for the
`remote_https` transport class.

Purpose:
- define the platform/account/update/license/machine/future capability
  boundary
- freeze remote-platform posture before implementation
- keep platform Remote HTTPS separate from LAN runtime exposure, Local HTTP
  Loopback, and provider/model HTTP transport

Boundary:
- `remote_https` is not default local runtime execution
- `remote_https` is not `lan_secure`
- `remote_https` is not `local_http_loopback`
- `remote_https` is not provider/model transport
- local-first runtime remains the baseline

Allowed platform or future uses:
- account login support
- `auth_context` refresh
- machine authorization
- license lease refresh
- release or update metadata
- account posture projection
- future hosted capability boundary

Out of scope:
- no Remote HTTPS client implementation
- no account/auth platform call
- no machine or license implementation
- no hosted compute implementation
