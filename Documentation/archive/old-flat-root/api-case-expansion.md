# API Case Expansion

## Status

* Delivery: V52
* Branch: `refoundation/phase-01`
* Registry source: `api/registry`
* Action source: `api/registry/yai-actions.v1.json`

## Purpose

V52 expands the canonical API `case` surface so it matches the command-system
model, current Rust CLI case reality, the seeded action registry, SDK
direction, and the operator-context boundary already documented in
`Documentation/operator/active-case-ref.md` and
`Documentation/operator/operator-context-plane.md`.

## Non-goals

* no CLI parser behavior changes
* no CLI command implementation
* no SDK generation
* no TUI/Loom behavior implementation
* no runtime behavior
* no case storage implementation
* no operator-context implementation
* no API endpoint/server implementation
* no protocol cutover

## Canonical Case Principles

```text
case is canonical.
case is not session.
active case is operator context.
case operations must not imply session mutation.
case close must not imply evidence, knowledge, or record deletion by default.
case open does not imply active-case selection.
case enter and case leave mutate operator_context.active_case_ref, not session.
```

## Case Tree vs Active Case Boundary

| Concern | Canonical owner | API meaning |
| ------- | --------------- | ----------- |
| root case anchor | `case` | `case.root` resolves the authenticated principal root case |
| nested case inventory | `case` | `case.list`, `case.tree`, and `case.show` inspect case-tree state |
| ensure nested case entry | `case` | `case.open` ensures a case-tree entry exists |
| active case selection | `operator_context.active_case_ref` | `case.enter` and `case.leave` project operator-context mutation through the case grammar |
| active case posture | `operator_context.active_case_ref` + case tree | `case.status` reports root case, active case, and operator-context posture together |
| nested case closure | `case` | `case.close` removes a nested case-tree entry only; it is not semantic deletion |
| session compatibility | `session` legacy | case operations must not imply session mutation |

## Canonical Case Operations

| Operation | Status | Meaning |
| --------- | ------ | ------- |
| `case.root` | canonical | inspect root case anchor |
| `case.list` | canonical | list nested cases under the root case |
| `case.open` | canonical | ensure or normalize a nested case-tree entry |
| `case.enter` | canonical | bind active case in operator context |
| `case.leave` | canonical | clear active case from operator context |
| `case.status` | canonical | inspect root case plus active-case posture |
| `case.close` | canonical | close nested case-tree entry without semantic deletion |
| `case.current` | compatibility read model | inspect current case-style posture from older partial API naming |
| `case.show` | compatibility detail view | detailed case projection |
| `case.tree` | compatibility tree view | explicit case-tree projection |
| `case.create` | deprecated | older naming replaced by `case.open` |
| `case.use` | deprecated | older naming replaced by `case.enter` |

## Request / Response Envelope

V52 keeps request shape under:

```text
schemas/request-envelope.v1.schema.json#/properties/input
```

and introduces a dedicated case response envelope:

```text
schemas/case-operation.v1.schema.json
```

The response contract centers on:

* `operation_id`
* `outcome`
* `root_case_ref`
* `active_case_ref`
* `operator_context_owner`
* `session_mutated`
* `case_tree_mutated`
* `operator_context_mutated`
* `evidence_deleted`
* `knowledge_deleted`
* `records_deleted`
* `cases`
* `warnings`
* `next_actions`

The envelope makes the non-goals explicit:

* `session_mutated` is always `false`
* `evidence_deleted` is always `false`
* `knowledge_deleted` is always `false`
* `records_deleted` is always `false`

This is the V52 contract guard against treating `case.close` as destructive
semantic deletion.

## Registry Alignment

V52 aligns the `case` family across the registry in four ways:

1. `api-operations.v1.json` now contains the full canonical command-model case
   set: `root`, `list`, `open`, `enter`, `leave`, `status`, `close`.
2. `api-surfaces.v1.json` exposes those operations as the public `case` surface.
3. `api-operation-projections.v1.json` records `case.create -> case.open` and
   `case.use -> case.enter` as deprecated compatibility mappings.
4. `yai-actions.v1.json` now maps the canonical `case.*` action_ids to the new
   API operation candidates instead of leaving them as `none verified`.

## Compatibility and Deferred Items

| Legacy or partial surface | V52 decision |
| ------------------------- | ------------ |
| `case.create` | deprecated compatibility alias to `case.open` |
| `case.use` | deprecated compatibility alias to `case.enter` |
| `case.current` | compatibility read model retained because older API/SDK surfaces already reference it |
| `context.*` | V54 now defines explicit `operator_context.*` API surfaces; public CLI may still prefer `case enter`, `case leave`, and `case status` |
| `case.records.tail` | retained as the watch boundary; V52 does not replace it |
| `case.graph.show` | retained; V52 does not redefine graph payloads |

## V53+ Handoff

* V53 — API Auth Surfaces
* V54 — API Operator Context
* V55 — Entitlement
* V56 — Machine Authorization
* V57 — Runtime Gate Decision

V52 deliberately stops at API registry, schema, fixtures, and conformance. It
does not implement runtime handlers, CLI behavior, SDK clients, or storage.
