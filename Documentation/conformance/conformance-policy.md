# Conformance Policy

API conformance validates protocol artifacts and documentation boundaries.

## Scope

Conformance checks may validate:

- operation registry and action descriptor consistency
- request, response, readiness, error, and stream contracts
- operation-to-transport mapping
- schemas and fixtures
- transport contract readiness
- OpenAPI projection compatibility

## Policy

Conformance proves API contract consistency. It does not prove runtime feature completeness, SDK package quality, or Console UX behavior unless those surfaces are explicitly checking their API boundary consumption.
