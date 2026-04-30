# API Family Extraction Map (Wave 13)

Legend:
- classification: `extraction-ready`, `needs envelope normalization`, `needs session/account boundary cleanup`, `implementation-coupled`, `deferred`
- lifecycle state: `stable`, `scaffolded`, `transitional`, `deferred`

| Family | Classification | Extracted Contract Docs | Implementation Copied | Lifecycle State | Extraction Blockers | Wave 14 SDK Eligibility |
|---|---|---|---|---|---|---|
| runtime | needs envelope normalization | yes | no (reference-only) | scaffolded | status/envelope consistency | partial after normalization |
| session | needs session/account boundary cleanup | yes | no (reference-only) | transitional | attach-user + active-case compatibility semantics | not yet |
| case | extraction-ready | yes | no (reference-only) | stable | minor envelope pass | yes |
| inspect | extraction-ready | yes | no (reference-only) | stable | minor consistency pass | yes |
| flow | needs envelope normalization | yes | no (reference-only) | scaffolded | binding/readiness envelope consistency | partial after normalization |
| govern | implementation-coupled | yes | no (reference-only) | scaffolded | runtime-coupled outputs | deferred until thinning |
| supervisor | deferred | scaffold only | no | deferred | no dedicated first-class family surface | not yet |
| knowledge | implementation-coupled | yes | no (reference-only) | scaffolded | broad surface + internal coupling | deferred/sliced |
| skills | extraction-ready | yes | no (reference-only) | stable | minor consistency pass | yes |
| analytics | needs envelope normalization | yes | no (reference-only) | scaffolded | response normalization | partial after normalization |
| provider | implementation-coupled | yes | no (reference-only) | scaffolded | provider/runtime lifecycle coupling | deferred |
| models | deferred | scaffold only | no | deferred | missing dedicated family contracts | not yet |
| agent | implementation-coupled | yes (surface notes) | no (reference-only) | scaffolded | orchestration entry coupling, execution deferred | partial (proposal-entry only) |
| ai | implementation-coupled | yes | no (reference-only) | transitional | mixed CLI/runtime/provider/session semantics | deferred |


## Wave 13B Mirror Note

- Canonical contract repository: `../api`.
- In-repo `yai/api` remains a compatibility mirror while build/runtime consumers still compile against `api/contracts` and `api/families`.
- `implementation copied` in this table remains `no` or `reference-only`; runtime implementation is not moved in 13B.


## 13C Contract Ownership Note

Family contract classification in this map is canonical in `api`.
Runtime adapter implementation remains in `yai/api` until split/migration.
