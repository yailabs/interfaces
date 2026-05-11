# Local IPC RPC Platform Bindings v1

## Purpose

Freeze the physical binding posture for `local_ipc_rpc` without implementing
platform listeners.

## Bindings

- macOS and Linux: Unix domain socket
- Windows: named pipe

## Exposure

- same-machine only
- no LAN
- no TCP by default
- no HTTP required
- no provider/model access bypass

## Endpoint Lifecycle

- runtime owns endpoint file or pipe lifecycle later
- SDK discovers and opens endpoints later
- API.04 does not implement socket creation, named pipe creation, or endpoint
  cleanup
