# Execution Domain

The execution domain documents API-facing projections for jobs, agents, providers, flows, knowledge, evidence, analytics, limits, and compute boundaries.

## Absorbed Semantics

- Case-bound jobs and detach/continuation behavior.
- Execution leases and runtime gate checks.
- Agent, provider, flow, knowledge, evidence, records, and analytics bindings.
- Case/job/flow limit boundaries and local or cloud compute exposure boundaries.
- Local provider and model access boundaries.

## Runtime Boundary

Execution implementation truth belongs to YAI runtime documentation. API owns only the operation, schema, fixture, mapping, envelope, error, and conformance projection.

## Artifact References

- `schemas/case-job-flow-limit-boundary.v1.schema.json`
- `schemas/agent-authority-binding.v1.schema.json`
- `schemas/provider-authority-binding.v1.schema.json`
- `schemas/flow-binding.v1.schema.json`
- `schemas/knowledge-binding.v1.schema.json`
- `schemas/analytics-binding.v1.schema.json`
- `fixtures/case-job-flow-limit-boundary/`
