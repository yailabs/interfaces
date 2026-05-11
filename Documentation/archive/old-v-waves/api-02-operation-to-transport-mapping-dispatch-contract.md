# API.02 — Operation-to-Transport Mapping / Dispatch Contract

## Status

Delivery: API.02
Status: done
Track: API / Transport / SDK / Runtime alignment
Repo branch: `refoundation/phase-01`
Repo change type: mapping contract + dispatch boundary documentation
Previous delivery: API.01 — Transport Boundary / Operation Surface Vocabulary Freeze
Next delivery: API.03 — API Envelope / Error / Stream Frame Alignment

## Purpose

API.02 maps canonical API operations to allowed transport classes and defines
the dispatch flow from SDK transport entrypoints into
`yai/runtime/boundary/api` before any new transport implementation is added.

## Files Changed

| Repo | File/path | Change type | Reason |
| ---- | --------- | ----------- | ------ |
| `api` | `mappings/README.md` | modified | define `api/mappings` as the canonical operation-to-transport contract root |
| `api` | `mappings/operation-transport-map.v1.schema.json` | added | define the canonical mapping entry shape and enums |
| `api` | `mappings/operation-transport-map.v1.json` | added | record the first canonical operation-to-transport map from the live registry |
| `api` | `mappings/operation-dispatch-contract.v1.md` | added | define normalized envelope dispatch flow into `runtime/boundary/api` |
| `api` | `mappings/transport-selection-policy.v1.md` | added | define default client transport selection rules |
| `api` | `mappings/streamable-operation-policy.v1.md` | added | limit `local_event_stream` to streamable/watch/tail surfaces |
| `api` | `mappings/lan-exposure-policy.v1.md` | added | freeze LAN as blocked by default with pairing-only allowance |
| `api` | `mappings/provider-transport-exclusion-policy.v1.md` | added | keep provider/model transport out of client-runtime mapping |
| `api` | `Documentation/operation-to-transport-mapping.md` | added | document the API.02 mapping model and dispatch interpretation |
| `api` | `conformance/check_operation_transport_mapping.py` | added | validate mapping structure and policy invariants against the live registry |
| `api` | `conformance/README.md` | modified | register the new API.02 conformance checker |
| `api` | `Documentation/waves/api-02-operation-to-transport-mapping-dispatch-contract.md` | added | record delivery scope, audit, validation, and outcome |
| `yai` | `runtime/boundary/api/README.md` | modified | align runtime dispatch ownership to normalized operation envelopes |
| `yai` | `runtime/boundary/transport/README.md` | modified | state runtime transport consumes API contracts and does not define operation grammar |
| `yai` | `runtime/boundary/service/README.md` | modified | align local HTTP loopback ownership to future service exposure only |
| `yai` | `runtime/connections/README.md` | modified | keep connection/session observation separate from grammar and provider transport |
| `yai` | `providers/transport/README.md` | modified | state provider transport is excluded from client-runtime mapping |
| `sdk` | `README.md` | modified | state SDK consumes API mapping and does not invent transport grammar |
| `sdk` | `generated/README.md` | modified | state generated outputs consume API mapping rather than define transport truth |
| `sdk` | `packages/rust/README.md` | modified | align Rust transport ownership and compatibility wording |
| `sdk` | `packages/typescript/README.md` | modified | align TypeScript transport ownership and mapping consumption wording |

## Registry Audit Result

| Operation source | Result | Notes |
| ---------------- | ------ | ----- |
| `api/registry/api-operations.v1.json` | audited | 112 operation ids audited across 27 families/projection families; this registry remained the only canonical source for API.02 mapping entries |
| SDK TS operations | audited | `YAI_OPERATIONS` constants align to registry-backed operation ids; `YAI_COMPAT_OPERATIONS` still exposes migration-era ids outside the registry such as `runtime.status.inspect`, `runtime.service.*`, `case.watch.snapshot`, `records.projection.list`, and `agent.orchestration.entry.propose` |
| SDK Rust operations | audited | `YAI_OPERATIONS` constants align to registry-backed ids; `YAI_COMPAT_OPERATIONS.runtime_service_control_plan` remains migration-era and outside the registry |
| compatibility operations | classified / deferred | registry `session.*` remains `compat_only`; SDK compatibility constants remain non-canonical and were not promoted into the API registry or operation transport map |

Minimum inspected operation groups recorded in this wave:

- `system.*`
- `case.*`
- `conversation.*`
- `providers.*`
- `models.*`
- `control.*`
- `governance.*`
- `state.*`
- `workflow.*`
- `agents.*`
- `knowledge.*`
- `skills.*`
- `analytics.*`
- `auth.*`
- `identity.*`
- `session.*`
- high-level composition families `act.*`, `chat.*`, `gate.*`, `guide.*`, `plan.*`, `proof.*`, `recall.*`

## Operation Mapping Result

| Operation group | Local IPC RPC | Local HTTP Loopback | Local Event Stream | LAN Secure | Remote HTTPS | Notes |
| --------------- | ------------- | ------------------- | ------------------ | ---------- | ------------ | ----- |
| `system.*` | yes, default | yes | no | selected read-only ops allowed with pairing | local only | `system.status` and inspection surfaces also keep explicit subprocess compatibility for migration/debug |
| `case.*` | yes, default except `case.records.tail` | yes, non-stream ops | `case.records.tail` only | selected read-only ops allowed with pairing | local only | case tail remains the stream boundary |
| `conversation.*` | yes, default | yes | no | selected read-only ops allowed with pairing | local only | send/propose operations stay local runtime dispatch surfaces |
| `providers.*` | yes, default | yes | no | read-only inspection ops allowed with pairing; mutating/provider-routing ops blocked | local only | provider transport remains separate after runtime dispatch |
| `models.*` | yes, default | yes | no | read-only inspection ops allowed with pairing; evaluation/use blocked | local only | provider/model routing stays runtime-side only |
| `control.*` | yes, default | yes | no | selected inspection ops allowed with pairing; mutating/guard-sensitive ops blocked | local only | guard-sensitive surfaces remain local-first |
| `governance.*` | yes, default | yes | no | selected read-oriented ops allowed with pairing | local only | governance write posture stays off LAN by default |
| `state.*` | yes, default except `state.records.tail` | yes, non-stream ops | `state.records.tail` only | selected read-only ops allowed with pairing | local only | tail/read split is explicit |
| `workflow.*` | yes, default except `workflow.runs.watch` | yes, non-stream ops | `workflow.runs.watch` only | selected read-only ops allowed with pairing | local only | start/mutate surfaces remain off LAN by default |
| `agents.*` | yes, default | yes | no | read-oriented ops may pair; plan/run stay blocked | local only | execution-oriented agent ops may trigger provider work only after runtime dispatch |
| `knowledge.*` | yes, default | yes | no | selected read-oriented ops allowed with pairing | local only | `knowledge.query` may trigger provider/model routing only after runtime dispatch |
| `skills.*` | yes, default | yes | no | read-oriented ops may pair; `skills.run` stays blocked | local only | skill execution remains runtime-side and may later route to providers |
| `analytics.*` | yes, default | yes | no | selected read-oriented ops allowed with pairing | local only | analytics remains local runtime dispatch |
| `auth.*` | no | no | no | not applicable | yes, default | platform/account boundary only; not default local runtime execution |
| `identity.*` | no | no | no | not applicable | yes, default | machine/entitlement/principal boundary only |
| `session.*` | yes, default | yes | no | blocked by default | local only | compatibility-only family; not restored as canonical domain truth |
| `client.*` | yes, default | yes | no | selected read-oriented ops allowed with pairing | local only | client observation stays local-first |
| `prompting.*` | yes, default | yes | no | blocked by default | local only | render/preview surfaces may route to providers only after runtime dispatch |
| `output.*` | yes, default | yes | no | selected read-oriented ops allowed with pairing | local only | export/render remain off LAN by default |
| `orchestrator.*` | yes, default | yes | no | blocked by default | local only | orchestration planning stays runtime-bound |
| `act.*`, `chat.*`, `gate.*`, `guide.*`, `plan.*`, `proof.*`, `recall.*` | deferred | deferred | deferred | not applicable | not applicable | high-level composition registry surfaces are `sdk_local_only` in API.02 and do not declare direct client-runtime transports yet |

## Dispatch Contract Result

Recorded dispatch path:

```text
SDK transport
-> transport entrypoint
-> normalized API operation envelope
-> runtime/boundary/api
-> guards / handler binding
-> runtime handler
-> normalized response envelope
```

API.02 records that transport entrypoints normalize requests into canonical API
operation envelopes before runtime dispatch, and that physical listeners belong
to `runtime/boundary/transport` or `runtime/boundary/service` rather than
`api/`.

## Provider Transport Exclusion

Provider transport is runtime -> provider/model only.
It is excluded from client-runtime operation mapping.

## Compatibility Findings

- SDK TypeScript still exposes migration-era compatibility ids outside the API
  registry: `runtime.status.inspect`, `runtime.service.lifecycle.inspect`,
  `runtime.service.health.inspect`, `runtime.service.control.plan`,
  `case.watch.snapshot`, `case.memory.projection.inspect`,
  `records.projection.list`, `flow.binding.readiness.inspect`,
  `governance.readiness.inspect`, `control.readiness.inspect`, and
  `agent.orchestration.entry.propose`.
- SDK Rust still exposes the migration-era compatibility id
  `runtime.service.control.plan`.
- API registry high-level composition surfaces `act.run`, `chat.send`,
  `chat.start`, `gate.approve`, `guide.create`, `plan.create`, `proof.bundle`,
  and `recall.query` were mapped as deferred `sdk_local_only` surfaces instead
  of being silently treated as direct runtime transports.
- API registry operations not yet projected by the current SDK remain registry
  truth but were not promoted into new SDK behavior in this wave.
- No behavior changed.

## Security Baseline

- LAN blocked by default.
- HTTP loopback only.
- IPC same-machine only.
- stream payloads projection-safe.
- subprocess compat only.

## Validation Commands

| Repo | Command | Result | Notes |
| ---- | ------- | ------ | ----- |
| `api` | `test -f transports/README.md` | pass | required existence check |
| `api` | `test -f mappings/operation-transport-map.v1.schema.json` | pass | required existence check |
| `api` | `test -f mappings/operation-transport-map.v1.json` | pass | required existence check |
| `api` | `test -f mappings/operation-dispatch-contract.v1.md` | pass | required existence check |
| `api` | `test -f mappings/transport-selection-policy.v1.md` | pass | required existence check |
| `api` | `test -f mappings/streamable-operation-policy.v1.md` | pass | required existence check |
| `api` | `test -f mappings/lan-exposure-policy.v1.md` | pass | required existence check |
| `api` | `test -f mappings/provider-transport-exclusion-policy.v1.md` | pass | required existence check |
| `api` | `test -f Documentation/operation-to-transport-mapping.md` | pass | required existence check |
| `api` | `test -f Documentation/waves/api-02-operation-to-transport-mapping-dispatch-contract.md` | pass | required existence check |
| `api` | `python3 conformance/check_api_contracts.py` | pass | output: `api-contracts: ok` |
| `api` | `python3 conformance/check_operation_registry.py` | pass | output: `conformance: ok` |
| `api` | `python3 conformance/check_operation_transport_mapping.py` | pass | output: `operation-transport-map: ok` |
| `api` | `python3 -m json.tool mappings/operation-transport-map.v1.json >/dev/null` | pass | JSON parses |
| `api` | `python3 -m json.tool mappings/operation-transport-map.v1.schema.json >/dev/null` | pass | JSON parses |
| `api` | `git diff --check` | pass | no whitespace or patch-format errors |
| `yai` | `test -f runtime/boundary/api/README.md` | pass | required existence check |
| `yai` | `test -f runtime/boundary/transport/README.md` | pass | required existence check |
| `yai` | `test -f runtime/boundary/service/README.md` | pass | required existence check |
| `yai` | `test -f runtime/connections/README.md` | pass | required existence check |
| `yai` | `test -f include/ipc/README.md` | pass | existing boundary surface |
| `yai` | `test -f providers/transport/README.md` | pass | required existence check |
| `yai` | `git diff --check` | pass | no whitespace or patch-format errors |
| `cli` | `test ! -e source` | pass | source absence guard held |
| `cli` | `scripts/check-no-source-dependency.sh` | pass | source dependency guard held |
| `cli` | `git diff --check` | pass | clean diff formatting |
| `sdk` | `git diff --check` | pass | docs touched only; no whitespace or patch-format errors |
| `loom` | `git diff --check` | pass | no whitespace or patch-format errors |
| `all` | `rg -n "HTTP is the only canonical transport|IPC RPC is deprecated|LAN enabled by default|provider transport is client runtime transport|SDK defines operation transport grammar|CLI defines operation transport grammar|Loom defines operation transport grammar|runtime owns API source of truth|API implements runtime dispatch|API implements listener|subprocess is canonical" ../api ../yai ../sdk ../cli ../loom 2>/dev/null || true` | pass/classified | matches appeared only inside wave-report command text in `api/Documentation/waves/api-02-...` and `api/Documentation/waves/api-01-...`; no positive ownership claims were found |

## Non-Implementation Confirmation

- no runtime listener implemented
- no SDK transport implemented
- no CLI/Loom behavior changed
- no OpenAPI semantic expansion
- no provider/model behavior changed
