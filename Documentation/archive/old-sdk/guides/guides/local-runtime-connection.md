# Local Runtime Connection

Local runtime connection is SDK client-side endpoint resolution.

## Rules

- Prefer explicit configured transports.
- Treat missing endpoint, missing permission, runtime unavailable, version mismatch, and denied status as typed SDK outcomes.
- Do not import runtime internals for product paths.
- Do not make local runtime availability implicit package truth.

Runtime implementation and lifecycle remain delegated to `../yai/Documentation`.
