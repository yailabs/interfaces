# Operation Grammar

Canonical operation form:
- `family.resource.verb`
- `family.verb` when family is the resource.

Public family model includes: auth, identity, session, client, system, case, conversation, prompting, workflow, governance, control, knowledge, state, skills, providers, models, agents, orchestrator, analytics, output.

High-level compositions: chat, guide, plan, act, gate, proof, recall.

Constraints:
- `workflow` replaces public `flow`.
- `orchestrator` replaces public `orchestration` grammar.
- root `policy.*` is forbidden; use `governance.policy.*`.
- runtime/system service lifecycle start/stop/restart operations are forbidden.
