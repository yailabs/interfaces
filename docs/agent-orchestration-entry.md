# Agent Orchestration Entry Contract

Schema: `api.agent.orchestration.entry.v1`

Request shape (contract-level):
- request_id (optional/symbolic)
- case_ref (optional)
- subject_ref (optional)
- client_ref (optional)
- intent_kind
- prompt_or_instruction (optional)
- source
- refs

Result shape (contract-level):
- status
- result_kind
- message
- proposal_ref
- plan_ref
- record_ref
- trace_ref
- flow_binding_ref
- provider_status
- model_status
- governance_status
- control_status (legacy alias: `supervisor_status`)
- warnings

Wave 15 posture:
- proposal/planning/readiness only
- execution deferred
- no provider/model/tool execution claim
