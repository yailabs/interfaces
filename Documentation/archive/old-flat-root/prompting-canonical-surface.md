# Prompting Canonical Surface

## Decision

`prompting` is a first-class canonical public API family.

It is not:
- a compatibility alias for `conversation`
- a sub-surface of `agents`
- a synonym for model/provider execution
- a synonym for workflow execution

Prompting exists to expose prompt-oriented assembly and inspection contracts as
their own governed family.

## Canonical resources

Canonical public prompting resources are:
- `context`
- `templates`
- `previews`
- `traces`

Future/deferred resource families may include:
- `instructions`
- `roles`
- `profiles`

Those future resources are not current canonical operations unless and until
they are added to the operation registry intentionally.

## Current canonical operation

Current canonical prompting operation:
- `prompting.context.assemble`

Current implementation truth:
- canonical family: yes
- canonical public surface: yes
- runtime handler readiness: `partial`
- boundary behavior: deterministic context projection only
- records emitted: yes
- evidence emitted: no

What it does now:
- assembles prompt-related context projection from runtime/knowledge backing
- stays conversation-bound where request/context selection matters
- preserves governance boundary posture

What it does not do now:
- no prompt stack renderer
- no template renderer
- no role/instruction stack materializer
- no model-ready prompt generation
- no provider execution
- no model execution
- no assistant reply generation

## Planned and deferred prompting operations

Planned canonical prompting operations already seeded in the registry:
- `prompting.templates.render`
- `prompting.previews.render`
- `prompting.traces.replay`

These remain planned/deferred surfaces, not implemented execution claims.

Planned extensions suitable for later proposal waves:
- `prompting.traces.show`
- `prompting.traces.export`
- `prompting.instructions.*`
- `prompting.roles.*`

Those extensions should remain deferred until the API intentionally defines
their contract and runtime truth.

## Family separation

### Prompting vs conversation

`conversation` owns conversation lifecycle, current conversation visibility, and
message intake/persistence.

`prompting` owns prompt-oriented context assembly and future prompt inspection or
rendering contracts.

Conversation may supply inputs or bindings used by prompting, but prompting is
not the conversation family.

### Prompting vs agents

`agents` owns agent listing, planning, execution, and tracing posture.

`prompting` may prepare context used by agents, but it must not be collapsed
into agent execution or agent orchestration.

### Prompting vs models and providers

`models` and `providers` own inventory, capability, connectivity, and execution
adjacent posture.

`prompting` must not imply provider dispatch, model invocation, or successful
prompt execution. Prompt preparation is distinct from inference or provider
selection.

### Prompting vs workflow

`workflow` owns composition, execution, steps, and runs.

`prompting` may contribute prompt context to workflow-driven or guided behavior,
but it does not own workflow execution semantics.

## SDK Phase 3B target

Phase 3B should expose a minimal canonical prompting client around:
- `prompting.context.assemble`

Phase 3B may carry typed placeholders or planned compat notes for:
- `prompting.templates.render`
- `prompting.previews.render`
- `prompting.traces.replay`

Phase 3B should not claim:
- template rendering is implemented
- preview rendering is implemented
- trace replay is implemented end-to-end
- model/provider execution through prompting

## Contract posture summary

- `prompting` is first-class and public
- `prompting.context.assemble` is current and partial
- render/replay-oriented prompting operations remain planned/deferred
- prompting is distinct from conversation, agents, models, providers, and workflow
