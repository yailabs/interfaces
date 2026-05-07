# Local IPC RPC Security v1

## Purpose

Freeze the minimum security posture for the primary native-local transport.

## Security Baseline

- same-machine only
- no LAN
- no TCP by default
- same-user default access
- socket or pipe permission enforcement required
- runtime-owned endpoint file or pipe lifecycle
- version handshake required
- local client identity required before sensitive operations
- no default world-writable socket
- no remote exposure
- no provider credentials sent over client-runtime transport

## Boundary

- Socket and pipe permissions are runtime-owned implementation details later.
- API owns the security contract the implementation must satisfy.
- Provider/model transport remains separate from `local_ipc_rpc`.
