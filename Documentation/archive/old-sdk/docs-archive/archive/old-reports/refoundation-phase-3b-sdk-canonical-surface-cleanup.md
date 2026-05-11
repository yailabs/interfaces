# Refoundation Phase 3B — SDK Canonical Surface Cleanup / Typed Operation Constants Patch

## Verdict

Phase 3B updates the SDK public surface story so TypeScript and Rust no longer present legacy API grammar as canonical. Canonical operation constants now follow `../api/registry/api-operations.v1.json`, while legacy names remain only as explicit compatibility aliases where preserving downstream imports is safer than removal.

## Files Changed

- `README.md`
- `Documentation/standards/family-availability.md`
- `Documentation/reports/refoundation-phase-3b-sdk-canonical-surface-cleanup.md`
- `packages/typescript/src/client.ts`
- `packages/typescript/src/index.ts`
- `packages/typescript/src/operations.ts`
- `packages/typescript/src/surfaces/agent.ts`
- `packages/typescript/src/surfaces/agents.ts`
- `packages/typescript/src/surfaces/base.ts`
- `packages/typescript/src/surfaces/case.ts`
- `packages/typescript/src/surfaces/control.ts`
- `packages/typescript/src/surfaces/conversation.ts`
- `packages/typescript/src/surfaces/flow.ts`
- `packages/typescript/src/surfaces/governance.ts`
- `packages/typescript/src/surfaces/knowledge.ts`
- `packages/typescript/src/surfaces/models.ts`
- `packages/typescript/src/surfaces/orchestrator.ts`
- `packages/typescript/src/surfaces/output.ts`
- `packages/typescript/src/surfaces/prompting.ts`
- `packages/typescript/src/surfaces/providers.ts`
- `packages/typescript/src/surfaces/records.ts`
- `packages/typescript/src/surfaces/runtime.ts`
- `packages/typescript/src/surfaces/state.ts`
- `packages/typescript/src/surfaces/supervisor.ts`
- `packages/typescript/src/surfaces/system.ts`
- `packages/typescript/src/surfaces/workflow.ts`
- `packages/rust/README.md`
- `packages/rust/src/client.rs`
- `packages/rust/src/operations.rs`
- `packages/rust/src/surfaces/case.rs`
- `packages/rust/src/surfaces/conversation.rs`
- `packages/rust/src/surfaces/mod.rs`
- `packages/rust/src/surfaces/models.rs`
- `packages/rust/src/surfaces/prompting.rs`
- `packages/rust/src/surfaces/provider.rs`
- `packages/rust/src/surfaces/providers.rs`
- `packages/rust/src/surfaces/runtime.rs`
- `packages/rust/src/surfaces/session.rs`
- `packages/rust/src/surfaces/system.rs`
- `packages/rust/src/transport.rs`

## Canonical Surfaces Added

### TypeScript

- `system`
- `conversation`
- `prompting`
- `workflow`
- `knowledge`
- `state`
- `providers`
- `models`
- `agents`
- `orchestrator`
- `output`

### Rust

- `system`
- `providers`
- `conversation`
- `prompting`

## Compatibility Aliases Retained

### TypeScript

- `client.runtime` -> `client.system`
- `client.flow` -> `client.workflow`
- `client.records` -> `client.state`
- `client.supervisor` -> `client.control`
- `client.agent` -> `client.agents`

Legacy TypeScript operation identifiers that are absent from the canonical API registry were moved under `YAI_COMPAT_OPERATIONS` and are no longer the primary SDK constants.

### Rust

- `client.runtime().status_inspect()` -> canonical `system.status`
- `client.provider().list_inspect()` -> canonical `providers.list`
- `client.case().current_inspect()` -> canonical `case.current`
- `client.models().list_inspect()` -> canonical `models.list`
- `client.session().status_inspect()` -> canonical `session.status`

Rust keeps method-name compatibility only. Canonical operation ids are now API-present ids.

## Operation Constant Alignment

Canonical constants now use API-present operation ids, including:

- `system.status`
- `system.check`
- `system.runtime.inspect`
- `case.current`
- `case.list`
- `case.show`
- `case.records.tail`
- `conversation.current`
- `conversation.messages.send`
- `prompting.context.assemble`
- `workflow.list`
- `workflow.show`
- `workflow.steps.pending`
- `workflow.runs.watch`
- `governance.posture`
- `governance.policy.resolve`
- `control.decisions.explain`
- `control.gates.list`
- `control.gates.show`
- `knowledge.lineage.trace`
- `knowledge.query`
- `state.records.query`
- `state.records.tail`
- `providers.list`
- `providers.probe`
- `models.list`
- `models.capabilities.show`
- `agents.list`
- `agents.trace`
- `orchestrator.routes.resolve`
- `output.show`
- `session.current`
- `session.status`

Removed from canonical use:

- `runtime.status.inspect`
- `records.projection.list`
- `flow.binding.readiness.inspect`
- `control.readiness.inspect`
- `agent.orchestration.entry.propose`

## Remaining Drift

- TypeScript still exports legacy names for compatibility, but they are explicit wrappers instead of canonical first-path surfaces.
- C remains compat/native-heavy and still needs a dedicated boundary plan.
- Python remains intentionally thin and does not yet expose the canonical family set.

## Validation

Phase 3B validation is expected to include:

- TypeScript `npm run build`
- Rust `cargo check`
- C `make`
- Python `py_compile`
- drift grep proving old names survive only in compatibility code/comments

## Recommended Next Phase

- `Phase 3C — SDK Compat Isolation / C SDK Boundary Plan` if C drift still blocks CLI work
- otherwise `Phase 4A — CLI Rust Migration Plan against canonical SDK`
