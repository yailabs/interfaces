# SDK Final Demo Matrix Convergence (14/14)

Canonical chain remains:

`cli -> sdk -> yai`

## SDK obligations in final matrix

- preserve workspace descriptors and execution mode metadata
- preserve scientific and digital vertical summaries
- preserve decision/evidence/trace fields from runtime replies
- avoid policy or command-topology duplication in CLI

## Validation pointers

- `tools/sh/check_api_boundaries.sh`
- `build/tests/workspace_smoke`
- `build/tests/models_contract_smoke`
- `build/tests/sdk_smoke`

## Final matrix handoff

SDK remains the mediation layer used by all runbooks in:
- `yai/Documentation/runbooks/demos/demo-execution-runbook.md`
- `yai/Documentation/runbooks/qualification/core-qualification-runbook.md`
- `yai/Documentation/runbooks/qualification/core-qualification-runbook.md`
- `yai/Documentation/runbooks/remediation/core-remediation-runbook.md`


Model contract guardrail:
- typed runtime/workspace/binding/governance model extraction must remain valid across demo scenarios.
