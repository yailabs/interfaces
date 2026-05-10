# API Operator Context Surfaces

## Status

* Delivery: V54
* Branch: `refoundation/phase-01`
* API family: `operator_context`
* Previous: V53 — API Auth Surfaces

## Purpose

V54 creates the canonical API `operator_context` surface so active-case
selection posture no longer remains hidden inside session, client, shell, or
raw case operations.

It formalizes the boundary already described in:

* `Documentation/operator/operator-context-plane.md`
* `Documentation/operator/active-case-ref.md`
* `Documentation/api-case-expansion.md`

## Non-goals

* no CLI parser behavior changes
* no CLI command implementation
* no SDK generation
* no TUI/Loom behavior implementation
* no runtime behavior
* no operator context storage implementation
* no case storage implementation
* no API endpoint/server implementation
* no protocol cutover

## Canonical Operator-Context Operations

| Operation | action_id | CLI projection | Meaning | Owns active_case_ref? | Owns auth/runtime/job/evidence/knowledge? |
| --------- | --------- | -------------- | ------- | --------------------- | ----------------------------------------- |
| `operator_context.status` | `context.status` | `yai case status` | inspect current operator selection posture | yes | no |
| `operator_context.current` | `context.current` | future explicit `yai context status` or SDK/TUI context view | inspect current operator-context projection directly | yes | no |
| `operator_context.active_case.set` | `context.switch` | `yai case enter <case>` | set `operator_context.active_case_ref` to a selected case | yes | no |
| `operator_context.active_case.clear` | `context.clear` | `yai case leave` | clear `operator_context.active_case_ref` | yes | no |

## No-Session Boundary

```text
operator_context owns active_case_ref.
session does not own active_case_ref.
client does not own active_case_ref.
shell does not own active_case_ref.
case does not own active_case_ref directly.
case.enter / case.leave / case.status are public CLI projections over
operator_context updates and reads.
```

This keeps the operator selection boundary explicit:

* `case` owns case-tree existence and hierarchy
* `operator_context` owns current active-case selection
* `session` remains legacy compatibility only
* `client` and `shell` remain transport/UX surfaces only

## Operator Context vs Auth / Runtime / Work

`operator_context` is deliberately narrow.

It does not:

* authenticate a principal
* authorize actions
* issue or inspect entitlement
* issue or inspect machine authorization
* issue or inspect license lease
* start, stop, or unseal runtime
* own jobs, workflows, agents, provider calls, or model execution
* own evidence, records, knowledge, lineage, or analytics

`operator_context` only expresses current operator selection posture with
`active_case_ref` as the canonical mutable field.

## Projection Relationship

V54 keeps public CLI language stable while correcting API ownership:

| Public surface | V54 canonical API owner |
| -------------- | ----------------------- |
| `yai case enter <case>` | `operator_context.active_case.set` |
| `yai case leave` | `operator_context.active_case.clear` |
| `yai case status` | `operator_context.status` |
| future `yai context status` | `operator_context.current` or `operator_context.status` |

This means CLI case verbs remain truthful operator-facing projections while the
API registry now exposes the proper domain family explicitly.

## Request / Response Envelope

V54 introduces:

```text
schemas/operator-context-operation.v1.schema.json
```

The response contract centers on:

* `operation_id`
* `action_id`
* `request_kind`
* `operation_status`
* `root_case_ref`
* `active_case_ref`
* `operator_context_ref`
* `operator_context_owner`
* `selection_mutated`
* `session_mutated`
* `client_mutated`
* `shell_mutated`
* `runtime_mutated`
* `auth_mutated`
* `safe_projection`

Guard rails in the schema and fixtures make the boundary explicit:

* `operator_context_owner` is always `operator_context.active_case_ref`
* `session_mutated` is always `false`
* `client_mutated` is always `false`
* `shell_mutated` is always `false`
* `runtime_mutated` is always `false`
* `auth_mutated` is always `false`

## Registry Changes

V54 changes the registry in four ways:

1. `api-families.v1.json` now contains canonical `operator_context` family
   metadata.
2. `api-operations.v1.json` adds `operator_context.status`,
   `operator_context.current`, `operator_context.active_case.set`, and
   `operator_context.active_case.clear`.
3. `api-surfaces.v1.json` exposes the new surface entries as public API
   projections.
4. `api-operation-projections.v1.json` records bridge mappings from public
   `case.*` and `context.*` action_ids into explicit `operator_context`
   operations.

## Schema / Fixtures / Conformance

V54 adds:

* `schemas/operator-context-operation.v1.schema.json`
* `fixtures/operator-context-operation/operator-context-status.json`
* `fixtures/operator-context-operation/operator-context-current.json`
* `fixtures/operator-context-operation/active-case-set.json`
* `fixtures/operator-context-operation/active-case-clear.json`
* `conformance/check_operator_context_operations.py`

The conformance layer rejects:

* session ownership fields
* client ownership fields
* shell ownership fields
* runtime ownership fields
* work/evidence/knowledge/analytics ownership fields
* direct active-case ownership claims by `session`, `client`, or `shell`

## SDK / CLI / Loom Handoff

V54 does not add behavior, but it prepares the next layers cleanly:

* SDK clients can later add typed `operator_context` methods without reviving
  session semantics.
* CLI can keep `case enter`, `case leave`, and `case status` as public grammar
  while projecting to explicit `operator_context` APIs.
* Loom/TUI can later surface a context panel, disabled placeholders, or status
  badges from `context.*` action_ids without inventing hidden session ownership.

## V55 Handoff

V55 follows with API entitlement surfaces.
