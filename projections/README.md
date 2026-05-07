# Projections

`api/projections/` is the documentation root for API-facing projection models.

Typical contents for later waves may include operation projections, payload
shape guidance, and projection release notes.

SDK client packages consume these projections through SDK-owned client
transports. This root does not own transport implementation.

Test-only `in_process_test` and compatibility-only
`subprocess_stdio_compat` do not redefine projection ownership or become
canonical projection transports.

This root is intentionally documentation-only in V28.6/API.01.
