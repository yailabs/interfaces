# SDK Versioning and Release Policy

- SDK release claims require matching package-level validation evidence.
- C build contract must be deterministic (`make check-config`).
- TypeScript validation must run via `npm run typecheck`.
- Python validation must pass `py_compile` checks.

If any package gate is blocked, client migration gate remains blocked.
