# Source Plane SDK Model

## Purpose

Define the canonical SDK surface for source-plane operations so consumers do not
need to build raw control-call JSON by hand.

This slice introduces typed request/reply wrappers for:

- `yai.source.enroll`
- `yai.source.attach`
- `yai.source.emit`
- `yai.source.status`
- source summary read path (`yai.workspace.query` family `source`)

## Public header

- `include/yai_sdk/source.h`

Recommended include:

```c
#include <yai_sdk/public.h>
```

## Typed API entrypoints

- `yai_sdk_source_enroll(...)`
- `yai_sdk_source_attach(...)`
- `yai_sdk_source_emit(...)`
- `yai_sdk_source_status(...)`
- `yai_sdk_source_summary(...)`

## Typed reply parse helpers

- `yai_sdk_source_enroll_reply_from_sdk(...)`
- `yai_sdk_source_attach_reply_from_sdk(...)`
- `yai_sdk_source_emit_reply_from_sdk(...)`
- `yai_sdk_source_status_reply_from_sdk(...)`
- `yai_sdk_source_summary_from_sdk(...)`

These parse canonical `yai.exec.reply.v1` envelopes from `yai_sdk_reply_t`.

## Mediation model

Source-plane replies expose mediation data (when returned by runtime), mapped to:

- `yai_sdk_source_mediation_state_t`

This keeps owner/daemon routing and gate state readable for CLI/tooling without
forcing runtime-internal JSON parsing.

## SW-2 distribution model exposure

Source enroll/attach/status typed replies now include distributed delegated
scope state:

- `source_enrollment_grant_id`
- `source_policy_snapshot_id`
- `source_capability_envelope_id`
- `policy_snapshot_version`
- `distribution_target_ref`
- delegated scopes (`observation`, `mediation`, `enforcement`)

These fields are exposed via:

- `yai_sdk_source_distribution_state_t`
- `reply.distribution` in enroll/attach/status typed reply structs

## Compatibility posture

- Raw `yai_sdk_client_call_json(...)` remains available.
- Source-plane typed wrappers are the preferred path for new consumers.
- This slice is transport-agnostic at API level and currently targets the same
  runtime ingress used by the rest of SDK.

## Example

- `examples/05_source_plane_typed.c`

## Limits (v1)

- Source list/inspect uses summary-first query parsing.
- Advanced filtering/pagination is deferred.
- Runtime command stability still governs payload detail evolution.

## DX-1 extension: governed inspect/query summaries

SDK model now includes typed operational summary parsing hooks for source/edge,
mesh coordination/authority, and transport/ingress/overlay summary families.

These hooks are intended to consume owner-side QG summaries without forcing
client-side ad-hoc JSON stitching.
