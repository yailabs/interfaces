# Ownership Map

| Path | Status | Ownership note |
| --- | --- | --- |
| `contracts/` | observed | API contract grammar |
| `schemas/` | observed | schema surfaces |
| `envelopes/` | observed | request/response envelope grammar |
| `errors/` | observed | API error surfaces |
| `transports/` | observed | transport contract material |
| `openapi/` | observed | OpenAPI projection material |
| `projections/`, `mappings/`, `registry/`, `lifecycle/` | observed | projection and classification roots |
| `conformance/`, `fixtures/`, `examples/` | observed | support and validation material |
| `.agents/` | canonical | agent control-plane instructions |

- `external`: runtime implementation belongs to `../yai`.
- `unknown`: deeper domain ownership inside uninspected fixture subtrees must be verified before editing.
