# Runtime Implementation Boundary

`../yai/runtime/boundary/api` implements runtime handlers for operations declared in `../api`.

Runtime metadata in `yai` may track implementation readiness and capability only.
Runtime metadata must not become a parallel canonical command registry.
