# Transport Model

The transport model defines how the same API operation contract is carried across local, remote, compatibility, and test transports.

## Transport Families

- Local IPC RPC is the preferred local structured request/response transport.
- Local HTTP loopback exposes local API operations through loopback HTTP routes.
- Local event stream carries watch, progress, and event frames.
- LAN secure remote and remote HTTPS define controlled remote exposure boundaries.
- Subprocess stdio compatibility exists for compatibility clients only.
- In-process test transport exists for conformance and harness use.

## Mapping Rule

Operations do not choose transports by client convenience. `mappings/operation-transport-map.v1.json` and the mapping policy documents define allowed dispatch paths.

## Artifact Boundary

Transport artifact files under `transports/` remain outside `Documentation`. They are indexed from `reference/transport-artifact-index.md` and summarized in `transports/transport-contract-index.md`.
