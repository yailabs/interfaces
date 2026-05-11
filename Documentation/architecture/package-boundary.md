# Package Boundary

Official SDK packages belong under `interfaces/packages/` after SDK drain.

## Current Phase

YAI Interfaces is `pre-sdk-drain`. Package source still lives in `../sdk`.
INTF.2 does not move SDK packages.

## Package Scope After Drain

- `packages/rust/`: Rust client package behavior.
- `packages/python/`: Python client package behavior.
- `packages/typescript/`: TypeScript client package behavior.
- `packages/c/`: C client package behavior and compatibility posture.

## Package Rules

- Packages consume interface protocol and conformance definitions.
- Packages declare supported protocol and conformance versions.
- Packages do not define protocol truth.
- Packages must keep compatibility aliases explicit and non-canonical.
- Package release claims require package-local validation and interface
  conformance evidence.
