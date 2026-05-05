# Refoundation Phase 2C — Prompting Canonical Surface Plan

## Scope

Stabilized prompting as a first-class canonical API family without expanding
runtime claims or changing sibling repositories.

## What changed

- added `docs/prompting-canonical-surface.md`
- clarified prompting family metadata in `registry/api-families.v1.json`
- linked prompting plane metadata to the new canonical surface doc in
  `registry/api-plane-surfaces.v1.json`
- added prompting separation reminders to `conformance/CHECKLIST.md`

## Current canonical prompting posture

Prompting is a canonical first-class public family.

Current canonical operation:
- `prompting.context.assemble`

Current truth:
- canonical: yes
- runtime readiness: `partial`
- deterministic context projection: yes
- template rendering: no
- prompt stack rendering: no
- model-ready prompt generation: no
- provider/model execution: no

## Planned and deferred prompting posture

Registry-seeded but planned/deferred prompting operations:
- `prompting.templates.render`
- `prompting.previews.render`
- `prompting.traces.replay`

Future candidate planning only, not added in this phase:
- `prompting.traces.show`
- `prompting.traces.export`
- `prompting.instructions.*`
- `prompting.roles.*`

## Separation decisions

- prompting is not conversation lifecycle
- prompting is not agents execution
- prompting is not models/providers execution
- prompting is not workflow execution

## SDK impact

Phase 3B now has a clear minimal canonical prompting target:
- expose typed `prompting.context.assemble`

Phase 3B may carry planned/deferred prompting surface stubs only if clearly
marked non-implemented and non-executing:
- `prompting.templates.render`
- `prompting.previews.render`
- `prompting.traces.replay`

## Not changed

- no `yai` implementation changes
- no `sdk` implementation changes
- no new public schema family for controlled action
- no new prompting operation ids added
- no fake implementation/readiness claims added

## Recommended next phase

Phase 3B — SDK Canonical Surface Cleanup / Typed Operation Constants Patch
