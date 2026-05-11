# SDK Workspace Digital Control Path

This note documents the digital workspace path in the canonical chain:

`cli -> sdk -> yai`

## SDK responsibilities

- forward digital workspace control-calls without embedding runtime policy logic
- preserve runtime decision/evidence/execution payload fields
- preserve sink-target and outbound control summaries in reply payloads
- preserve family-aware runtime semantics in replies:
  - execution-facing state (`exec`)
  - data/record persistence state (`data`)
  - graph truth/materialization state (`graph`)
  - knowledge support/transient state (`knowledge`)

## Non-responsibilities

- no digital policy decision logic in SDK
- no resolver duplication from `yai`
- no command topology ownership that belongs to `law`

## Digital flow reference

1. CLI sets workspace and declared digital specialization.
2. CLI sends `yai.workspace.run` with outbound/retrieval/publication/distribution tokens.
3. SDK forwards control-call to runtime.
4. Runtime resolves digital specialization/effect.
5. SDK returns structured reply; CLI renders digital summaries.

## Required pass-through fields

- `decision.family_id`
- `decision.specialization_id`
- `decision.effect`
- `resolution_trace.*`
- `digital.*` summaries from runtime
- execution mode metadata (`requested/effective/degraded`)
