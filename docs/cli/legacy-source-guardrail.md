# Legacy Source Guardrail

## Status

* Delivery: V21.6
* Status: active partial guardrail
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Purpose

Prevent deleted legacy source areas from returning and prevent new dependencies
from Rust CLI into quarantined `cli/source/`.

## Current State

| Area | Status |
| ---- | ------ |
| `cli/source/out` | deleted in V21.5; must not return |
| `cli/source/shared` | deleted in V21.5; must not return |
| remaining `cli/source/*` | quarantined residual |
| Rust `src/` dependency on `source/` | forbidden |
| Cargo dependency on `source/` | forbidden |
| Rust tests dependency on `source/` | forbidden |

## Guardrail Rule

```text
No new dependency from Cargo, Rust src, or Rust tests may point to cli/source/.
Deleted subtrees cli/source/out and cli/source/shared must not be recreated.
```

## Not Yet Full Absence

```text
This is not the final absence guardrail.
Full source absence can only be enforced after remaining source residuals are
deleted.
```

## Remaining Residuals

| Residual | Reason retained | Future wave |
| -------- | --------------- | ----------- |
| `source/main.c` | legacy entrypoint/build sentinel | V21.7/V21.8 |
| `source/cmd/flow` | heavy semantic area | V21.7 |
| `source/cmd/knowledge` | heavy semantic area | V21.7 |
| `source/cmd/case` | heavy semantic area | V21.7 |
| `source/cmd/session` | legacy non-canonical removal candidate | V21.7/V21.8 |
| `source/assets/shell` | legacy shell UX assets | V21.7/V21.8 |

## Final Direction

```text
cli/source/ must be removed completely.
```
