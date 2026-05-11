# API Plane Surface Model

Public API surface is operation-family based.

Canonical mappings:
- public `system` -> runtime posture/inspection projections
- public `workflow` -> implementation may still reference `../yai/flow` internally
- public `state` -> `state.records.*` operations (root `records` is not a public plane)
- public `orchestrator` -> implementation may still reference `../yai/orchestration` internally
- public `control` -> internal control plane

Compatibility names (`flow`, root `records`, `orchestration`, CLI-style aliases) are not canonical public surface keys.
