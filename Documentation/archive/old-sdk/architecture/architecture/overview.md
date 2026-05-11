# SDK Architecture Overview

The SDK repository is the typed client and language package authority for YAI consumers. It turns API protocol contracts into usable package surfaces while preserving the boundary between SDK package behavior, API protocol truth, runtime/system truth, and terminal UX truth.

## Boundary Summary

- Protocol, operation grammar, transport, envelope, and error truth belong to `../api/Documentation`.
- Runtime, system, and governance truth belong to `../yai/Documentation`.
- Terminal command and TUI UX truth belongs to `../console/Documentation`.
- SDK owns typed client consumption and package behavior only.

## Canonical SDK Model

- Language packages consume API contracts and expose typed client behavior.
- SDK transports are client-side adapters to API transports; they do not define transport grammar.
- Generated surfaces are projections over API artifacts, not independent protocol sources.
- SDK compatibility exists to protect consumers while avoiding revival of retired product surfaces.
- Package release claims require package validation evidence.
