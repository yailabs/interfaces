# Runtime Resolution Model

Runtime resolution is the SDK client-side process of finding or configuring an API transport endpoint. It is not runtime implementation truth.

Identity/account/auth posture reaches the local runtime as a bounded access projection under `../yai/src/runtime/access`; SDK runtime resolution must not treat platform identity as local runtime ownership.

## SDK Responsibilities

- Resolve explicit configured endpoints or local runtime connection paths.
- Surface unavailable, denied, blocked, or not configured status honestly.
- Preserve API readiness and error semantics in package-specific results.
- Avoid direct runtime adapter imports for product paths.

## Delegation

Runtime implementation, lifecycle, governance, and enforcement truth belongs to `../yai/Documentation`. SDK documents only client-side resolution and package behavior.
