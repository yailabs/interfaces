# A-Series Delivery Map

## Status

* Track: A - Console canonicalization and transport drift reconciliation
* Branch: `refoundation/phase-01`

## Deliveries

| Delivery | Name | Status | Purpose |
| -------- | ---- | ------ | ------- |
| A1 | Console Canonicalization | current | Make Console the canonical terminal client; retain CLI/Loom only as legacy, compatibility, or historical names. |
| A2 | Operation Transport Mapping Drift Reconciliation | next | Reconcile operation-to-transport mapping drift after client naming canonicalization. |

## Rule

Console is the canonical terminal client. CLI and Loom are not separate
canonical active clients after A1.

## Remote History Note

The pulled remote already contains
`Documentation/waves/a1-operation-transport-mapping-drift-reconciliation.md`.
That accepted report is left intact as historical remote state. The A-series
planning map above records the current delivery direction: A1 Console
canonicalization, A2 operation transport mapping reconciliation.
