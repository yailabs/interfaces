# YAI SDK

Industrial multi-language SDK workspace for YAI client consumption.

## Package Map
- `packages/rust`: Rust SDK surface for YAI Console (`yai-console`) and other native Rust clients.
- `packages/typescript`: typed plane clients for web/product clients.
- `packages/python`: integration and automation SDK surface.
- `packages/c`: native SDK surface for Console compatibility and native consumers.

## Dependency Chain
clients -> SDK packages -> API contracts/operation registry -> YAI runtime

- API contracts source: `../api`
- runtime implementation source: `../yai`
- SDK does not own runtime internals
- SDK does not own runtime truth
- SDK does not implement account backend behavior
- generated artifacts are not source and must remain ignored

Current posture:
- transport is SDK-owned and explicitly configured on the client side
- unconfigured transport remains truthful unavailable
- no fake execution claims
- canonical public SDK surfaces follow the API registry in `../api`
- legacy SDK aliases remain compatibility-only and do not define canonical grammar
- SDK clients are `sdk-embedded` transport clients
- SDK clients do not own auth, case, operator context, session, or runtime lifecycle
- SDK does not own runtime server/listener implementation
- SDK does not own provider/model transport
- SDK client identity is a client subject/client attachment concern, not a case
  identity concern

API.01 transport freeze:
- Rust/native local clients target `local_ipc_rpc` as the primary native local
  transport class
- browser/dashboard clients target `local_http_loopback` plus
  `local_event_stream`
- current package implementations may still expose HTTP-based transports during
  migration, but that does not make HTTP the only canonical transport class

API.02 mapping rule:
- SDK consumes `../api/mappings/operation-transport-map.v1.json`
- SDK does not invent operation-to-transport grammar
- migration-era compatibility helpers do not promote extra canonical API
  operation ids

API.03 envelope/error/frame rule:
- SDK will encode and decode API request envelopes, response envelopes, and
  stream event frames according to `../api/envelopes`, `../api/errors`, and
  `../api/schemas`
- SDK does not define envelope grammar independently
- current simplified SDK envelope types remain migration-era implementation
  until later SDK alignment waves

A5 call-context rule:
- SDK propagates call context.
- SDK does not materialize system call records.
- SDK does not perform control-plane admission.
- `system_call_ref` is optional and normally runtime-created later.
- `work_case_ref` is optional and separate from client attachment.
- SDK call context distinguishes `client_ref` and `client_subject_ref` from
  `principal_ref`, and distinguishes client connection/attachment from work
  case binding.

API.09 alignment:
- API transport freeze closure now lives in
  `../api/transports/transport-contract-index.v1.md`
- SDK implementation readiness now lives in
  `../api/transports/implementation-readiness-matrix.v1.md`
- SDK handoff sequencing now lives in
  `../api/transports/implementation-handoff.v1.md`
- immediate SDK sequence is `SDK.01`, then `SDK.02`, then `SDK.03`

## Client connection boundary

V12 defines SDK clients as library-managed connection surfaces.

They may carry or observe transport, endpoint, and client metadata, but they do
not become domain owners.

## Shell UX boundary

V13/A1 defines shell as a Console UX plane, with legacy CLI/Loom surfaces kept as
compatibility names, not as SDK-owned domain surfaces.

SDK packages may support clients that participate in shell UX later, but the
SDK does not own shell attach/detach semantics, auth login, active case
selection, or runtime lifecycle through shell vocabulary.

SDK transport clients are not work cases. A client attachment may later bind to
an active work case, but that does not make the client itself the owner of
`case://root` or `case://<account-username>`.

## Sealed posture boundary

V14 treats operational authorization as separate from runtime liveness/health.

SDK/runtime health signals must not be interpreted as automatic authorization,
and neither session nor shell/client connection posture may unseal governed
operations by themselves.

## Runtime readiness projection boundary

V15 aligns CLI/runtime status output to canonical readiness projection language:
`operationalReadiness`, `sealReason`, `authPosture`, `casePosture`,
`operatorContextPosture`, `clientPosture`, and `sessionPosture`.

`runtime_transport_unavailable` is transport posture, not auth success or
failure. SDK clients should keep lifecycle/health/readiness distinct from local
operational authorization.

## Runtime control plan boundary

V19 defines `controlPlan` as a declarative runtime-control projection, not as
proof that start/stop/restart executed.

SDK surfaces may expose control-plan methods or unavailable envelopes, but they
must not claim:

- runtime start succeeded
- runtime stop succeeded
- runtime restart succeeded
- service manager exists

unless the underlying transport and validation actually prove it.

## SDK runtime surface alignment

V20 aligns TypeScript and Rust SDK runtime surfaces to the canonical posture
model:

- `lifecycle`
- `health`
- `readiness`
- `operationalReadiness`
- `sealReason`
- `authPosture`
- `casePosture`
- `operatorContextPosture`
- `clientPosture`
- `sessionPosture`
- `controlPlan`

Where a runtime transport is unavailable, SDK surfaces must stay
`unavailable`/error-truthful rather than inventing ready, healthy, running, or
control-executed state.

## Auth command boundary

`yai auth login`, `yai auth status`, and `yai auth logout` are legacy-compatible
command surfaces. SDK auth clients are not implemented in V3. SDK docs must
not teach `client.session()` as login, account identity, runtime health, active
case selection or shell/client attachment.

V4 adds CLI-only local development auth through `yai auth login --local-dev`.
This writes a local marker for a `local-dev:<value>` principal. It is not SDK
account auth, does not create account or entitlement refs, and does not create
the canonical work root by itself. `case://user` remains placeholder-only; the
operational root is `case://<account-username>`.

## Session containment

Session is a legacy compatibility surface.
It is not the canonical YAI domain model.

Use:
  yai auth ...
  yai case ...
  yai shell ... / yai client ...

Session must not be used to model login, account, active case, work ownership,
permissions or the root harness.

## Wave CLI-2A Rust Surface Expansion

Rust SDK now exposes typed transport-backed surfaces for Console-compatible command paths:

- `client.system().status()` -> `system.status`
- `client.session().status()` -> `session.status` legacy compatibility
- `client.case().current()` -> `case.current`
- `client.providers().list()` -> `providers.list`
- `client.models().list()` -> `models.list`

Compatibility aliases remain available for downstream consumers:
- `client.runtime().status_inspect()` -> canonical `system.status`
- `client.provider().list_inspect()` -> canonical `providers.list`
- `client.case().current_inspect()` -> canonical `case.current`
- `client.models().list_inspect()` -> canonical `models.list`
- `client.session().status_inspect()` -> legacy compatibility `session.status`

These methods use the SDK transport abstraction and preserve existing envelope/error behavior.
