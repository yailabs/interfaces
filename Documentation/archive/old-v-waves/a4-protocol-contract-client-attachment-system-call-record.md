# A4 — Protocol Contract for Client Attachment + System Call Record

## Status

Delivery: A4
Status: done
Track: A-series / API projection
Repo branch: refoundation/phase-01
Previous delivery: A3 — Case Topology Vocabulary / System Case vs Work Case Boundary
Next delivery: A5 — API Envelope / SDK Call Context Propagation

## Purpose

Record the API projection stance for the A4 protocol contract owned by
`../yai/protocols`.

API does not own the A4 protocol meaning. API will later project the contract
into envelope and SDK call-context propagation during A5.

## Projection Summary

The canonical A4 protocol source of truth is in `yai`:

- `protocols/refs/*client*`
- `protocols/refs/system-call-ref.v1.schema.json`
- `protocols/refs/system-root-context-ref.v1.schema.json`
- `protocols/refs/work-case-ref.v1.schema.json`
- `protocols/schemas/system-call-record.v1.schema.json`
- `protocols/schemas/work-case-binding.v1.schema.json`
- `protocols/conformance/check_client_attachment_system_call_record.py`

API documentation now classifies the contract as a future projection input, not
an implemented API behavior.

## Files Changed

| File | Change type |
| ---- | ----------- |
| `Documentation/client/console-client-alignment.md` | update projection wording for A4 refs |
| `Documentation/operation-to-transport-mapping.md` | update transport boundary wording for system call records |
| `Documentation/waves/a-series-map.md` | mark A4 done and A5 next |
| `Documentation/waves/a4-protocol-contract-client-attachment-system-call-record.md` | add API projection wave report |
| `conformance/check_operation_transport_mapping.py` | align existing A-series map assertions with A4 done |

## Boundary Confirmation

- `client_subject_ref` is not a case.
- `client_connection_ref` is not a stable subject or session.
- `client_attachment_ref` is not work case ownership.
- `system_call_record` is not a work-case action record.
- `work_case_ref` is optional.
- Work-case binding does not merge system lineage and work-case lineage.
- Provider/model transport is not client-runtime transport.

## Non-Implementation Confirmation

No API behavior changed.
No OpenAPI route changed.
No runtime dispatch behavior changed.
No SDK behavior changed.
No Console behavior changed.
No API mirror schemas were created for A4 in this delivery.

## Validation Commands

```bash
python3 conformance/check_operation_transport_mapping.py
python3 conformance/check_transport_contract_index.py
git diff --check
```
