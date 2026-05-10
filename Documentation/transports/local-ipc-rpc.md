# Local IPC RPC

Local IPC RPC is the preferred structured local request/response transport for API operations.

## Artifact References

- ``transports/local-ipc-rpc.v1.md``
- ``transports/local-ipc-rpc/``
- ``transports/local-ipc-rpc/frame.v1.schema.json``

## Contract Model

IPC carries request and response envelopes with handshake, framing, cancellation, timeout, streaming, platform binding, and security rules.

## Operation Relationship

Allowed operations are controlled by `mappings/operation-transport-map.v1.json` and related mapping policy. Transport docs describe how operations are carried; operation docs define what operations mean.
