# Transport Consumption Model

SDK transports are client-side adapters that consume API transport contracts.

## Model

- Rust native local clients target explicit Local IPC RPC transport when configured.
- TypeScript browser/local-web clients target Local HTTP Loopback and Local Event Stream when configured.
- Python follows package maturity and explicit configured transports.
- C remains native/compat-heavy and transitional until its public surface is partitioned further.

## Boundary

SDK transports do not define transport grammar, runtime listeners, LAN policy, remote hosting policy, or stream frame semantics. Those belong to `../api/Documentation` and API artifacts, with runtime implementation truth in `../yai/Documentation`.
