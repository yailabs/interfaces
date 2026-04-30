# agent family contract (wave 15 proposal-entry scaffold)

Status: scaffolded (proposal-entry-ready)

This family exposes runtime-owned orchestration entry semantics:
- request accepted (`received`/`pending`)
- context bound
- proposal/plan readiness
- execution deferred posture

It does not claim:
- provider/model execution
- tool execution
- autonomous mutation
- governance/supervisor approval

Contract envelope (conceptual):
- schema: `api.agent.orchestration.entry.v1`
- status: `pending|unavailable|blocked|error|ready`
- result_kind: `proposal|plan|readiness_summary|deferred_execution|unavailable`
