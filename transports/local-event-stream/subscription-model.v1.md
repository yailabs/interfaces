# Local Event Stream Subscription Model v1

## Purpose

Define the stream open or subscribe request posture for `local_event_stream`.

## Required Subscription Fields

- `operation_id`
- `request_id`
- `stream_id` optional or assigned by runtime later
- `filters` optional
- `resume_token` optional
- `last_event_id` optional
- `client_ref`
- `case_ref` optional

## Rules

- Streamable operation ids must come from the existing API.02 mapping and
  registry only.
- API.06 does not invent new stream operation ids.
- Current watchable operations are:
  - `case.records.tail`
  - `state.records.tail`
  - `workflow.runs.watch`
