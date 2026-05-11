# Protocol API Boundary

The protocol/API boundary is the contract between client-facing interface
artifacts and runtime/system implementation.

Interfaces owns:

- operation identity and semantics;
- request, response, readiness, and stream envelope models;
- error shape and status mapping;
- transport contracts;
- schema and registry artifacts;
- compatibility mappings and lifecycle models.

YAI runtime owns implementation behavior behind those contracts. Console owns
terminal UX over those contracts. Web/account/product surfaces own their own
product workflows.

OpenAPI is projection. It can describe HTTP-facing protocol projections, but it
does not replace the protocol registry, schema, mapping, or contract sources.
