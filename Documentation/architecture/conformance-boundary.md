# Conformance Boundary

Conformance checks protocol integrity and SDK package alignment.

Protocol conformance verifies that registries, schemas, mappings, transports,
envelopes, errors, fixtures, OpenAPI projections, and contracts remain mutually
consistent.

Package conformance verifies that SDK packages consume the protocol without
defining it. Package checks may compile, typecheck, test, inspect provenance,
and compare generated or package-facing constants against canonical inputs.

INTF.6 owns guardrails, provenance, and package validation hardening for
residual package checks discovered during INTF.4.
