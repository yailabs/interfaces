# SDK Workspace Scientific Control Path

This note documents the scientific workspace path in the canonical chain:

`cli -> sdk -> yai`

## SDK responsibilities

- forward scientific workspace control-calls without embedding runtime policy logic
- preserve runtime decision/evidence/execution payload fields
- keep workspace binding mediation in SDK context APIs
- preserve family-aware runtime semantics in replies:
  - execution-facing state (`exec`)
  - data/record persistence state (`data`)
  - graph truth/materialization state (`graph`)
  - knowledge support/transient state (`knowledge`)

## Non-responsibilities

- no scientific policy decision logic in SDK
- no resolver duplication from `yai`
- no command topology ownership that belongs to `law`

## Scientific flow reference

1. CLI sets workspace and declared scientific specialization.
2. CLI sends `yai.workspace.run` with experiment tokens.
3. SDK forwards control-call to runtime.
4. Runtime resolves scientific specialization/effect.
5. SDK returns structured reply; CLI renders scientific summaries.

## Required pass-through fields

- `decision.family_id`
- `decision.specialization_id`
- `decision.effect`
- `resolution_trace.*`
- `scientific.*` summaries from runtime
- execution mode metadata (`requested/effective/degraded`)
