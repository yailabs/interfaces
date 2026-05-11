# Operation Model

An API operation is the stable protocol unit exposed to clients and implemented by runtime adapters.

## Grammar Relationship

Operations use the canonical grammar documented in `operations/operation-grammar.md`. The registry stores families, verbs, operation records, projections, and action descriptors.

## Operation Record

An operation record identifies:

- operation id
- family and verb
- request and response schema relationship
- projection and action descriptor relationship
- allowed transports and streamability
- conformance expectations

## Runtime Boundary

Runtime handlers implement operation behavior, but handler internals are not API documentation authority. API authority stops at the operation contract, mapping, envelope, error, and conformance boundary.
