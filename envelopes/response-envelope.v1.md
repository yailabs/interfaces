# Response Envelope v1

## Purpose

Define the canonical terminal response shape returned by request/response API
transports.

## Required Fields

- all base envelope fields from `api-envelope-model.v1.md`
- `status`

## Optional Fields

- `system_call_ref`
- `client_subject_ref`
- `client_connection_ref`
- `client_attachment_ref`
- `system_root_context_ref`
- `work_case_ref`
- `control_admission_ref`
- `result`
- `error`
- `warnings`
- `records`
- `evidence_refs`
- `readiness`
- `stream_ref`

## Rules

- A terminal response envelope must contain either `result` or `error`.
- A response envelope must not carry both `result` and `error` as the primary
  terminal payload.
- Non-terminal stream delivery uses stream event frames, not response envelopes.
- `stream_ref` is an acknowledgement/ref handoff, not a stream event frame.
- A5 adds call-context projection fields to API envelopes.
- A5 does not implement runtime admission/materialization.
- `system_call_ref` is echoed if known or may be created by later runtime
  admission/materialization.
- `control_admission_ref` is a future hook and remains optional in A5.
- `work_case_ref`, when present, does not merge system lineage with work-case
  lineage.

## Status Vocabulary

- `ok`: operation completed successfully
- `accepted`: operation accepted and may continue through a stream or follow-on
  boundary
- `partial`: operation returned a truthful partial result
- `unavailable`: operation could not complete because a required runtime/API
  dependency was unavailable
- `blocked`: operation was guarded or sealed
- `invalid`: request shape or operation preconditions were invalid
- `failed`: operation reached a terminal failure inside API/runtime semantics
