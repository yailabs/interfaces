# A-Series Delivery Map

## Status

* Track: A - Console canonicalization and transport drift reconciliation
* Branch: `refoundation/phase-01`

## Deliveries

| Delivery | Name | Status | Purpose |
| -------- | ---- | ------ | ------- |
| A1 | Console Canonicalization / Legacy CLI-Loom Drain | done | Make Console the canonical terminal client; retain CLI/Loom only as legacy, compatibility, or historical names. |
| A2 | Operation Transport Mapping Drift Reconciliation | done | Reconcile operation-to-transport mapping drift after RT.04 and A1 Console naming canonicalization. |
| A3 | Case Topology Vocabulary / System Case vs Work Case Boundary | done | Establish the case topology vocabulary boundary without widening transport or runtime behavior. |
| A4 | Protocol Contract for Client Attachment + System Call Record | next | Define protocol-facing client attachment and system call record contracts after A3 vocabulary freeze. |

## Rule

Console is the canonical terminal client. CLI and Loom are not separate
canonical active clients after A1.

## Remote History Note

The pulled remote already contains
`Documentation/waves/a1-operation-transport-mapping-drift-reconciliation.md`.
That accepted report is left intact as historical remote state. The A-series
map above records the accepted sequence now reflected in the tree: A1 Console
canonicalization, A2 operation transport mapping reconciliation, A3 case
topology vocabulary boundary, A4 client-attachment and system-call protocol
contract next.
