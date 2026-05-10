# API Operation Model

API owns operation grammar. Runtime implements handlers.

Canonical model:
- `family.resource.verb`
- operation contracts in `registry/api-operations.v1.json`

Runtime/service lifecycle start/stop/restart is explicitly excluded from API operation grammar.
