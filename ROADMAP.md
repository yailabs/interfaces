# Interfaces Rebirth — living project roadmap

Date: 2026-09-11  
Status: planning authority; implementation not authorized  
Current repository: `mothx9/interfaces` (private)  
Future public name: **UNSELECTED**  
Release horizon: first credible open-source release, version to be named after identity selection

This file is the sole planning authority for turning the former YAI Interfaces
repository into a genuinely new open-source project. It owns the product thesis,
source-recovery boundary, dependency order, maturity model, milestone gates,
release definition, non-claims, and naming process.

It does not authorize implementation. Code, history rewriting, remote renaming,
repository visibility changes, license publication, package registration, domain
registration, or release work require a later explicit selection. Until then,
the existing repository remains a private source archive.

The working title in this document is **the Project**. `interfaces`, `YAI
Interfaces`, and `RelaySpec` are not candidate product names.

## At a Glance / Current Snapshot

| Question | Current answer |
| --- | --- |
| Project target | An open interface engineering platform for AI and agent runtimes: define one truthful operational model, then compile it into SDKs, CLI surfaces, OpenAPI/AsyncAPI, MCP/A2A adapters, documentation, conformance suites, replayable fixtures, and an interactive control workbench. |
| Current selected engineering boundary | **NONE. ROADMAP REVIEW ONLY.** No implementation milestone is active. |
| Active Next | `REBIRTH.IDENTITY.0`, pending explicit authorization after roadmap review. |
| Existing raw material | Operation registries, JSON Schemas, envelopes, error vocabularies, transport contracts, fixtures, conformance checks, OpenAPI projection, SDK experiments in Rust/Python/TypeScript/C, and extensive architecture work. |
| Existing repository condition | Private, not archived, default branch `main`; `refoundation/phase-02` is 40 commits ahead of `main`; the two branches represent different repository shapes. |
| Existing public-readiness condition | Not ready. The repository has no self-contained open-source license, contains YAI-specific commercial/license assumptions, internal planning material, personal paths, stale cross-repository references, and failing standalone conformance checks. |
| New-project posture | A new product and a new identity, not a YAI extraction release, not a documentation cleanup, and not a generic schema linter. |
| Source-history posture | Preserve the complete old repository privately. Build the future public repository from a reviewed, provenance-recorded clean export with new public history. |
| First release proof | One runtime definition must generate and drive several real surfaces, pass independent conformance, expose live/replayed behavior in the workbench, and demonstrate the same semantics over at least two transports. |
| Primary risk | Producing a large catalog of attractive specifications without a narrow executable vertical that proves the system is useful. |
| Next decision point | Accept, revise, or reject the product thesis; then authorize only the identity and source-classification milestone. |

## Adopted direction

The Project will answer one hard question:

> How can a runtime expose every operator and developer surface without letting
> each SDK, CLI, protocol adapter, UI, and documentation site invent a different
> version of the truth?

The answer is a canonical **Operational Interface Graph**. It describes what a
runtime can do, what each operation consumes and returns, which errors are
stable, which transports can carry it, which capabilities and authority it
requires, what it may affect, how it streams, and how its behavior is proven.

That graph is compiled into usable surfaces:

```text
                         Operational Interface Graph
                                      │
              ┌───────────────────────┼────────────────────────┐
              │                       │                        │
              ▼                       ▼                        ▼
       developer surfaces      protocol surfaces       proof surfaces
       SDKs / CLI / docs        HTTP / events /         fixtures / replay /
       typed clients            MCP / A2A / IPC         conformance / traces
              │                       │                        │
              └───────────────────────┼────────────────────────┘
                                      ▼
                           interactive workbench
                    inspect · invoke · watch · compare · debug
```

The Project is not another agent framework. It does not own planning, memory,
tools, model execution, or application policy. It makes those runtime-owned
capabilities explicit, consumable, testable, and interoperable.

The long-term product class is closer to a compiler, protocol laboratory, and
developer workbench than to an API description file. A user should be able to
describe an unfamiliar runtime once and immediately obtain a coherent developer
and operator experience around it.

## Decisions already made

| ID | Decision | Consequence |
| --- | --- | --- |
| `DIRECTION.0` | This is a new project. | Existing names, package identities, assumptions, and release claims do not carry forward automatically. |
| `DIRECTION.1` | A contract-only linter is too small. | Validation is foundational, but compilation, runtime adapters, proof, and a workbench are first-class product programs. |
| `DIRECTION.2` | The existing code is raw material, not the target architecture. | Every artifact is classified before reuse; provenance never grants automatic admission. |
| `DIRECTION.3` | The old repository remains private during the rebirth. | Public visibility is blocked until source, history, licensing, secrets, names, paths, and claims pass a public-boundary audit. |
| `DIRECTION.4` | The future public repository starts with clean, reviewable history. | The old Git history is retained privately; accepted artifacts are exported with explicit provenance and license decisions. |
| `DIRECTION.5` | One semantic owner must drive every generated surface. | SDKs, CLI, OpenAPI, adapters, docs, and UI cannot become competing authorities. |
| `DIRECTION.6` | Executable proof outranks descriptive completeness. | No capability is promoted because a schema, generator, mock, or document exists. |
| `DIRECTION.7` | Interoperability means bridges with declared loss. | MCP, A2A, OpenAI-compatible APIs, local IPC, and other protocols are projections with explicit gaps, not replacements for the core model. |
| `DIRECTION.8` | The final name is a product decision. | Naming closes only after collision, namespace, meaning, pronunciation, domain, and visual-identity checks. |
| `DIRECTION.9` | This roadmap is the only authorized artifact in the current pass. | No source refactor, repository rename, push, publication, or visibility change is implied by this file. |

## Product promise

The eventual one-line promise should remain structurally equivalent to:

> Define a runtime once. Ship every trustworthy way to operate it.

A successful Project lets a maintainer:

1. describe operations, types, capabilities, authority, effects, errors,
   transports, streams, and compatibility in one source model;
2. compile deterministic client and protocol artifacts with exact provenance;
3. attach one or more real runtime adapters;
4. run contract, fixture, negative, transport, compatibility, and live
   conformance suites;
5. explore and invoke the runtime through a generated CLI and browser workbench;
6. compare two runtime versions and see semantic compatibility changes;
7. bridge supported operations into ecosystem protocols without pretending that
   unsupported semantics survived the projection;
8. publish a versioned interface package that other teams can consume without
   reading the runtime source.

## The launch demonstration

The first release is not credible unless one coherent demonstration proves the
whole idea.

The reference runtime will expose a compact but demanding agent lifecycle:

- inspect runtime and capability status;
- create and inspect a task/session;
- submit a bounded run request;
- stream typed progress and output events;
- cancel an active run;
- surface structured refusal and failure;
- retrieve an evidence/receipt record;
- expose the same accepted semantics over local IPC and HTTP.

From one Operational Interface Graph, the toolchain must produce:

- validated JSON Schema artifacts;
- an OpenAPI projection for the request/response subset;
- an AsyncAPI or equivalent event projection for the stream subset;
- TypeScript and Python clients;
- a generated command-line client;
- MCP and A2A bridge reports and at least one executable bridge;
- human-readable reference documentation;
- positive and negative conformance cases;
- a browser workbench that discovers, invokes, watches, and explains the same
  operations;
- a compatibility report between two intentionally different interface
  versions.

The demonstration must include deliberate failure: an invalid fixture, an
unsupported bridge operation, a capability refusal, and a breaking interface
change must all be detected and explained precisely.

## What can be recovered from the old repository

Recovery is based on semantics and evidence, not filenames or volume.

| Source family | Current value | Default disposition | Admission requirement |
| --- | --- | --- | --- |
| Operation registries | Strong conceptual seed; extensive operation metadata and projection thinking | Extract concepts and a very small neutral example set | New grammar, neutral vocabulary, consumer proof, no YAI IDs |
| Envelope and error models | Useful cross-transport boundary work | Re-design and selectively reimplement | Demonstrate request, response, stream, refusal, partial, and cancellation behavior |
| JSON Schemas | Mixed: reusable patterns plus deeply product-specific types | Classify individually | Valid schema, stable identity, neutral semantics, fixtures, compatibility rule |
| Transport contracts | Valuable separation of IPC, HTTP, events, subprocess, LAN, and remote concerns | Recover architecture and test ideas | At least two executable transports and explicit projection loss |
| Mappings and readiness matrices | Strong seed for compilation and truthfulness | Recast as compiler-owned projection plans | Machine-checked linkage to operations and generated artifacts |
| Fixtures | High potential as executable documentation | Keep only neutral, reviewed fixtures | Positive and negative oracle, schema binding, deterministic result |
| Conformance scripts | Useful intent, uneven standalone health | Rewrite around one runner and stable issue taxonomy | Self-contained execution, no sibling-repository assumptions, cross-platform CI |
| OpenAPI projection | Useful output example, not a canonical source | Replace with generated output | Deterministic regeneration and zero hand-edited semantic truth |
| TypeScript SDK | Best early client-language seed | Mine API ergonomics and tests | Generated core plus thin handwritten transport runtime |
| Python SDK | Minimal seed | Rebuild after the TypeScript vertical | Typed public surface, real tests, packaging, independent consumer |
| Rust SDK | Substantial transport and type experiments | Recover after core grammar stabilizes | No hardcoded competing registry; exact error and lifecycle semantics |
| C SDK | Large but tightly coupled to old law/runtime paths | Defer; mine ABI and resource-lifecycle lessons | Independent headers, portable build, memory ownership contract, real C consumer |
| Documentation | Valuable decisions buried in large internal/history trees | Extract durable principles only | Current, public, product-neutral, linked to executable owners |
| `.agents` control material | Useful maintenance ideas, obsolete repository identity | Recreate later for the new project | Must describe the new repository exactly; no copied fake state |
| Licensing/commercial gates | Not reusable as open-source project policy | Keep private with old archive | New license decision based on admitted authorship and dependencies |
| YAI-specific account, entitlement, lease, Case, Studio, and product semantics | Domain material, not generic core | Exclude from core; possible future example/extension only | Independent public value, explicit ownership, neutral core remains clean |
| Internal wave reports and personal filesystem paths | Historical private context | Private archive only | Never enter the public export |

## Public-source and licensing boundary

Changing the current GitHub repository from private to public is explicitly
blocked. The current history contains material that was written under a YAI
community/commercial posture, while `LICENSE-REFERENCE.md` merely points to
license files outside the repository. That is not a distributable open-source
license.

The safe topology is:

```text
mothx9/interfaces              future-name/future-name
private source archive         clean public repository
full old branches/history      admitted artifacts only
YAI names and internal docs    new identity and public license
no public release promise      independent release history
```

Before public creation, `REBIRTH.PUBLIC.BOUNDARY.0` must produce one reviewable
source manifest with four classes:

- `rewrite`: the concept is useful, but implementation/text is recreated;
- `adapt`: identifiable code is retained and modified under confirmed rights;
- `example-only`: domain material is converted into neutral demonstration data;
- `private-archive`: the artifact never enters the public repository.

The license gate must establish authorship and redistribution rights for every
adapted file, choose an OSI-approved project license, preserve required
third-party notices, and scan the complete public tree and history. A sole Git
author is useful evidence, but it is not by itself a license determination.

## Target system

### 1. Operational Interface Graph

The graph is the canonical semantic owner. It must model:

- interface package identity and compatibility version;
- operation identity, family, lifecycle, stability, and deprecation;
- input, output, error, event, and receipt types;
- query, command, stream, subscription, and long-running operation behavior;
- idempotency, retry, timeout, cancellation, and partial-result semantics;
- required capabilities, authority, scopes, and preconditions;
- side effects, danger, confirmation, review, and audit posture;
- transport eligibility and transport-specific bindings;
- client and protocol projection availability;
- examples, negative cases, and conformance obligations;
- implementation readiness and explicitly unsupported behavior;
- source and generator provenance for every derived artifact.

The graph describes runtime-owned truth. It does not decide business policy or
grant authority to callers.

### 2. Interface compiler

The compiler consumes the graph and produces a deterministic Interface Package.
It owns normalization, reference resolution, semantic checks, compatibility
analysis, projection planning, generation provenance, and stable diagnostics.

Compiler output must be content-addressed or otherwise reproducibly identified.
Running it twice against the same source and toolchain must produce byte-stable
artifacts except for fields explicitly declared volatile.

### 3. Generated developer surfaces

The initial surface order is deliberate:

1. JSON Schema and machine-readable normalized graph;
2. reference documentation and compatibility report;
3. TypeScript client and generated CLI;
4. OpenAPI request/response projection;
5. Python client;
6. event-stream projection;
7. Rust client;
8. C ABI only after the semantic surface has earned stability.

Generated cores may have small handwritten transport runtimes. Handwritten
convenience APIs cannot redefine operation IDs, types, errors, or compatibility.

### 4. Runtime adapter kit

Adapters bind abstract operations to real runtimes. The kit must support an
in-process reference adapter, local IPC, HTTP, and a typed event stream before
claiming generality. Each adapter publishes capability and loss information.

An adapter is responsible for framing, connection lifecycle, deadlines,
cancellation delivery, authentication handoff, stream ordering, and exact
transport errors. It does not reinterpret operation meaning.

### 5. Interoperability bridges

MCP, A2A, OpenAI-compatible APIs, and later ecosystems are projections. Every
bridge produces a machine-readable report with:

- operations mapped exactly;
- operations mapped with declared loss;
- operations unavailable in the target protocol;
- target-protocol features with no source equivalent;
- security/authority facts that must be supplied by the host;
- streaming, cancellation, error, and identity differences.

The Project wins trust by refusing false equivalence.

### 6. Conformance laboratory

Conformance is a product, not a directory of scripts. It must offer:

- bundle and graph validation;
- schema and example validation;
- generated-artifact drift checks;
- adapter contract suites;
- black-box runtime conformance;
- deterministic replay;
- negative and refusal testing;
- compatibility and breaking-change classification;
- transport parity checks;
- machine-readable evidence and a concise human report;
- extension profiles with explicit inheritance.

Passing conformance means passing a named profile at an exact Project version.
It never means the runtime is secure, correct in all behavior, or production
ready.

### 7. Interactive workbench

The workbench makes the system legible. It discovers an Interface Package and
renders:

- capability and operation explorer;
- schema-aware request builder;
- live response, event, and cancellation views;
- error/refusal explanations;
- trace and receipt timeline;
- fixture runner and replay controls;
- transport comparison;
- interface-version diff;
- generator and provenance inspection;
- exportable conformance report.

The workbench consumes the same public package and adapter protocols as any
other client. It may not read compiler internals or runtime-private state to
create a better-looking truth.

### 8. Ecosystem registry

A later registry may index public Interface Packages, generators, adapters,
bridge profiles, and conformance evidence. It is not required for the first
release and must not become a centralized permission service.

Local files, Git revisions, and content-addressed artifacts remain valid primary
distribution paths. A hosted registry is a discovery convenience, not semantic
authority.

## System maturity

Maturity describes the product property, independently of whether a milestone
is scheduled.

| State | Meaning |
| --- | --- |
| 🟢 ESTABLISHED | Implemented in the new project and qualified at the exact stated scope |
| 🟡 SEED | Useful evidence or code exists in the private source archive, but it is not admitted into the new project |
| 🔴 OPEN | Adopted for the first credible release and absent |
| ⚪ LATER | Valuable, deliberately outside the first release dependency horizon |

| ID | Property | Maturity | Current truth | Promotion condition |
| --- | --- | --- | --- | --- |
| `identity.name` | Distinct product identity | 🔴 OPEN | Old repository name is retired for the future product; no replacement is selected | Name, namespaces, collision review, meaning, domain and visual direction accepted |
| `source.private_archive` | Recoverable private source | 🟢 ESTABLISHED | `mothx9/interfaces` exists privately with branches and history | Preserve immutable recovery refs before any remote restructuring |
| `source.public_boundary` | Clean public source boundary | 🔴 OPEN | No classified export or clean public history exists | Manifest, license audit, secret/path/claim scan and independent review pass |
| `core.operation_model` | Operation semantic model | 🟡 SEED | Rich YAI-specific registries and schemas exist | Neutral graph supports the launch vertical and stable diagnostics |
| `core.type_system` | Cross-surface type model | 🟡 SEED | JSON Schemas and duplicated SDK types exist | One canonical type owner generates validated target types |
| `core.capability_model` | Capability and refusal truth | 🟡 SEED | Readiness, authorization and gate concepts exist in domain-specific forms | Runtime discovery and invocation share one neutral capability contract |
| `core.compatibility` | Semantic version diff | 🔴 OPEN | Versioning prose exists; executable classification does not | Real compatible, risky and breaking fixtures produce deterministic reports |
| `compiler.deterministic` | Interface compiler | 🔴 OPEN | Current projections are partially handwritten | Same inputs produce stable normalized graph and artifacts with provenance |
| `conformance.bundle` | Source and fixture validation | 🟡 SEED | Many checks exist; standalone main currently has failing cross-path assumptions | One runner passes from a clean checkout with stable issue codes |
| `conformance.runtime` | Black-box runtime qualification | 🔴 OPEN | No neutral runtime profile exists | Reference and independent adapter pass the same profile |
| `surface.typescript` | TypeScript client | 🟡 SEED | An old product-bound package exists | Generated client drives the reference runtime over two transports |
| `surface.python` | Python client | 🟡 SEED | Minimal old package exists | Independently packaged client passes shared conformance |
| `surface.rust` | Rust client | 🟡 SEED | Substantial old transport experiments exist | Generated types and handwritten transport core pass parity tests |
| `surface.c` | Stable C ABI | ⚪ LATER | Large coupled seed exists | Core semantics freeze and a real independent C consumer justifies the ABI |
| `surface.cli` | Generated operator CLI | 🔴 OPEN | No neutral generated CLI exists | Command discovery and invocation derive entirely from the graph |
| `projection.openapi` | OpenAPI projection | 🟡 SEED | Old YAI projection exists | Generated projection round-trips supported semantics and declares loss |
| `projection.events` | Event-stream projection | 🟡 SEED | Event contract ideas exist | Ordered stream, cancellation and terminal states execute end to end |
| `bridge.mcp` | MCP bridge | 🔴 OPEN | No admitted implementation | Executable bridge plus loss report passes the launch vertical subset |
| `bridge.a2a` | A2A bridge | 🔴 OPEN | No admitted implementation | Executable or independently verified bridge profile with exact gaps |
| `adapter.local` | Local IPC adapter | 🟡 SEED | Old local IPC designs and clients exist | Cross-platform or explicitly bounded native implementation passes lifecycle tests |
| `adapter.http` | HTTP adapter | 🟡 SEED | Old HTTP projection/client code exists | Real reference runtime and two generated clients pass black-box tests |
| `workbench.explorer` | Interactive browser workbench | 🔴 OPEN | No new-project UI exists | Discovery, invoke, stream, cancel, replay and diff use public interfaces only |
| `ecosystem.registry` | Decentralized package discovery | ⚪ LATER | No new-project registry exists | Multiple external packages create a discovery need |
| `quality.security` | Adversarial parser/adapter qualification | 🔴 OPEN | No neutral threat model or campaigns exist | Path, schema, payload, stream and transport campaigns pass on release targets |
| `quality.performance` | Scale and latency characterization | 🔴 OPEN | No accepted workloads exist | Large graph, generation and workbench workloads have bounded evidence |
| `release.public` | Credible open-source release | 🔴 OPEN | Repository remains private and product identity is absent | All first-release gates close together |

## Milestone control

Only one milestone may be `active`. A milestone becomes active only through an
explicit roadmap update after authorization. The states are:

| State | Meaning |
| --- | --- |
| `review` | Proposed here for decision; no implementation authorization |
| `blocked` | Required work whose named predecessor is incomplete |
| `selected` | Authorized next boundary, not yet started |
| `active` | The single boundary currently being implemented |
| `partial` | Useful work accepted, but its stated after-state is not closed |
| `complete` | After-state and validation gates are accepted |
| `superseded` | Retained trace of a boundary replaced before completion |

### Current execution sequence

| Order | Milestone | State | Owned after-state | Depends on |
| ---: | --- | --- | --- | --- |
| 0 | `REBIRTH.ROADMAP.0` | `review` | One accepted product thesis, recovery boundary, maturity model, sequence, release proof, and non-claims document | none |
| 1 | `REBIRTH.IDENTITY.0` | `blocked` | Final product name, one-line promise, naming rationale, repository/package/CLI namespaces, collision report, and initial visual territory | `REBIRTH.ROADMAP.0` |
| 2 | `REBIRTH.SOURCE.FREEZE.0` | `blocked` | Immutable refs for old `main` and `refoundation/phase-02`, full tree/history inventory, secret and personal-path audit, and recoverability proof | `REBIRTH.IDENTITY.0` |
| 3 | `REBIRTH.EXTRACTION.MAP.0` | `blocked` | Every source family classified as rewrite, adapt, example-only, or private-archive with ownership and rationale | `REBIRTH.SOURCE.FREEZE.0` |
| 4 | `REBIRTH.PUBLIC.BOUNDARY.0` | `blocked` | Clean local public-candidate repository, accepted OSI license, notices, contribution/security policy, and zero old-history reachability | `REBIRTH.EXTRACTION.MAP.0` |
| 5 | `V01.VERTICAL.CONTRACT.0` | `blocked` | Minimal Operational Interface Graph for the launch lifecycle, neutral type system, examples, negative cases, and compatibility fixtures | `REBIRTH.PUBLIC.BOUNDARY.0` |
| 6 | `V01.COMPILER.CORE.0` | `blocked` | Deterministic parser, normalization, semantic validation, projection plan, stable diagnostics, provenance and compatibility classification | `V01.VERTICAL.CONTRACT.0` |
| 7 | `V01.CONFORMANCE.BUNDLE.0` | `blocked` | One installable runner validates source, generated output, examples, negatives and drift from a clean checkout | `V01.COMPILER.CORE.0` |
| 8 | `V01.SURFACE.TYPESCRIPT.CLI.0` | `blocked` | Generated TypeScript client and generated CLI invoke the in-process reference adapter without handwritten semantic duplication | `V01.CONFORMANCE.BUNDLE.0` |
| 9 | `V01.ADAPTER.HTTP.EVENTS.0` | `blocked` | The same launch semantics execute over HTTP and typed events with cancellation, refusal and terminal-state parity | `V01.SURFACE.TYPESCRIPT.CLI.0` |
| 10 | `V01.SURFACE.PYTHON.0` | `blocked` | Independently packaged Python client passes the shared reference and negative suite | `V01.ADAPTER.HTTP.EVENTS.0` |
| 11 | `V01.BRIDGE.MCP.0` | `blocked` | MCP projection generates an exact mapping/loss report and executes its supported launch subset | `V01.ADAPTER.HTTP.EVENTS.0` |
| 12 | `V01.BRIDGE.A2A.0` | `blocked` | A2A projection is implemented or verified at its honest subset with identity, task, stream and cancellation gaps recorded | `V01.BRIDGE.MCP.0` |
| 13 | `V01.WORKBENCH.0` | `blocked` | Browser workbench discovers, invokes, watches, cancels, replays and diffs the launch runtime through public interfaces | `V01.SURFACE.PYTHON.0`, `V01.BRIDGE.MCP.0` |
| 14 | `V01.RUNTIME.CONFORMANCE.0` | `blocked` | Reference runtime plus one independently structured adapter pass a named black-box conformance profile | `V01.WORKBENCH.0`, `V01.BRIDGE.A2A.0` |
| 15 | `V01.HARDENING.0` | `blocked` | Parser, compiler, generators, adapters, streams and workbench pass security, fuzz/property, failure, resource and performance campaigns | `V01.RUNTIME.CONFORMANCE.0` |
| 16 | `V01.PUBLIC.RELEASE.0` | `blocked` | Public repository, packages, documentation, demonstration, evidence, compatibility policy, signed artifacts and release claims close together | `V01.HARDENING.0` |

Active Next: **NONE — `REBIRTH.ROADMAP.0` is awaiting review.**

## Milestone acceptance

### `REBIRTH.IDENTITY.0`

Naming is complete only when the selected name:

- does not retain `YAI`, `interfaces`, `API`, or `SDK` as the product identity;
- expresses creation, connection, translation, operation, or many surfaces from
  one truth without reducing the product to schemas;
- is easy to pronounce and spell after hearing it once;
- does not collide materially with active developer tools, AI protocols,
  package ecosystems, or infrastructure companies;
- has acceptable GitHub organization/repository, package, CLI, and domain
  options;
- supports a distinct visual language and does not imitate YAI branding;
- survives a trademark-risk screening appropriate to the intended release;
- has one accepted short name and no parallel codename in public surfaces.

The naming dossier should explore semantic territories before individual names:
fabric/weaving, nervous systems, cartography, translation, orchestration,
optics/facets, circuitry, and navigation. Candidate names are evidence, not a
vote; availability and product fit both matter.

### `REBIRTH.SOURCE.FREEZE.0`

The private source baseline must record exact commit IDs for both current lines,
all remote branches/tags, author identities, large blobs, generated payloads,
license references, secrets, credentials, internal URLs, personal paths, and
cross-repository assumptions. Recovery refs must be tested from a second clone.

No merge of the 40-commit phase-02 line into old `main` is required. The branch
is a source corpus, not a release candidate.

### `REBIRTH.PUBLIC.BOUNDARY.0`

The public candidate must pass from a fresh clone with:

- no YAI product identity or private repository dependency;
- no internal wave reports, commercial-license gates, account secrets, personal
  filesystem paths, or dead organizational links;
- no copied code without an explicit admission and license basis;
- one root license and complete third-party notices;
- clean package identities and no publication collision;
- secret scanning over the full public history;
- reproducible bootstrap and tests;
- a small, legible initial tree with no archival landfill.

### `V01.VERTICAL.CONTRACT.0`

The minimal graph must be small enough to review completely. It earns expansion
only after the launch operations model query, command, stream, cancellation,
refusal, evidence and two-transport eligibility without product-specific terms.

### `V01.COMPILER.CORE.0`

The compiler must reject ambiguity. Unknown fields, duplicate identities,
unresolved references, incompatible lifecycle declarations, missing projection
requirements, unsafe retries, contradictory capability gates, and unstable
generation inputs receive stable, located diagnostics.

### `V01.RUNTIME.CONFORMANCE.0`

The second adapter cannot share the reference adapter's dispatch implementation.
It exists to show that the specification and tests describe public behavior
rather than one implementation's internals.

### `V01.PUBLIC.RELEASE.0`

The release closes only when a new user can:

1. install the compiler and conformance runner;
2. run the launch example locally;
3. inspect it in the workbench;
4. call it from generated TypeScript and Python clients;
5. invoke the generated CLI;
6. observe HTTP and event behavior;
7. generate and inspect the MCP/A2A mapping reports;
8. introduce a breaking change and receive a correct compatibility diagnosis;
9. reproduce the published checks from documented commands;
10. understand exactly what the release does not claim.

## First-release gates

| Gate | Current state |
| --- | --- |
| Product thesis accepted | review |
| New name and namespaces | blocked |
| Private source frozen and recoverable | blocked |
| Public extraction and license boundary | blocked |
| Operational Interface Graph launch vertical | blocked |
| Deterministic compiler and compatibility engine | blocked |
| Bundle conformance runner | blocked |
| TypeScript client and generated CLI | blocked |
| Python client | blocked |
| Two real transports plus typed event stream | blocked |
| MCP bridge and loss report | blocked |
| A2A bridge/profile and loss report | blocked |
| Browser workbench | blocked |
| Independent runtime conformance | blocked |
| Security and robustness qualification | blocked |
| Public documentation and reproducible demonstration | blocked |
| Release artifacts and claims | blocked |

## Target repository shape

Names below describe responsibilities, not frozen filesystem paths. Physical
layout is selected during the public-boundary and compiler milestones.

```text
project root
├── core/             graph model, parser, normalization, compatibility
├── compiler/         projection plans, generators, provenance
├── conformance/      profiles, runner, fixtures, replay, reports
├── adapters/         in-process, local IPC, HTTP, events
├── bridges/          MCP, A2A, other ecosystem projections
├── clients/          generated cores and minimal transport runtimes
├── cli/              generated operator/developer surface
├── workbench/        public-package consumer and interface explorer
├── examples/         complete neutral runtime verticals
├── docs/             product, architecture, specification, guides, decisions
└── tools/            repository-only development and release tooling
```

No `archive/` directory is planned in the public repository. Git owns public
chronology; the old private repository owns private source history.

## Engineering doctrine

1. **One truth, many projections.** A generated artifact may add ergonomics but
   cannot add semantic facts absent from the graph.
2. **Capabilities are discovered, not assumed.** A client must distinguish
   unsupported, unavailable, forbidden, degraded, and failed.
3. **Every bridge declares loss.** Interoperability reports are part of the
   output and conformance model.
4. **Examples execute.** Documentation payloads are fixtures; fixtures bind to
   exact operations and schemas.
5. **Negative behavior is public behavior.** Refusal, timeout, cancellation,
   partial results, stream termination, and version mismatch are specified and
   tested.
6. **Generation records provenance.** Inputs, compiler version, profile,
   configuration, and output identity remain inspectable.
7. **The workbench is an ordinary client.** It receives no private shortcut to
   compiler or runtime truth.
8. **Compatibility is semantic.** A text diff does not decide whether an
   operation remains safe for existing consumers.
9. **Extensions cannot corrupt the core.** Vendor and domain packs use namespaced
   extension points and declare their conformance profile.
10. **No ceremonial scale.** New registries, schemas, generators, languages, and
    documents require a named consumer and executable acceptance.
11. **Clean checkout is the unit of truth.** No adjacent YAI repository, local
    absolute path, hidden tool installation, or operator memory may be required.
12. **Claims follow evidence.** A mock proves shape; a fixture proves an example;
    a live independent conformance run proves only its named profile and scope.

## Open-source and community model

The first release should be useful without a hosted account, proprietary
service, telemetry requirement, or closed generator. Core graph, compiler,
conformance runner, reference adapters, initial clients, bridges, workbench, and
launch example are intended to be open source.

Contribution boundaries should support:

- core grammar proposals through public decisions;
- external generators without core merge requirements;
- runtime adapters maintained by vendors or communities;
- conformance profiles for domain-specific contracts;
- reproducible compatibility fixtures;
- bridge mappings that can be reviewed independently of a runtime;
- public security reporting and coordinated fixes.

A hosted registry, collaboration service, or managed conformance system may be
considered later, but the local toolchain and package format remain complete on
their own.

## Quality strategy

Validation grows with the dependency graph:

| Layer | Required evidence |
| --- | --- |
| Graph | parser oracles, schema/property tests, invalid corpus, reference and identity checks |
| Compiler | deterministic snapshots, metamorphic tests, compatibility golden cases, provenance verification |
| Generators | compile/typecheck, independent sample consumers, regeneration drift, language-specific lifecycle tests |
| Adapters | connection/failure cleanup, deadlines, cancellation, stream order, malformed peer, capability mismatch |
| Bridges | exact mapping fixtures, loss classification, unsupported-operation refusal, upstream-version pins |
| Conformance | reference positive control, deliberately broken runtimes, report stability, profile inheritance tests |
| Workbench | browser interaction, accessibility, narrow/wide layouts, large graphs, stream pressure, public-interface-only guard |
| Release | clean-machine install, signed artifacts, dependency/SBOM scan, complete demo replay, documented non-claims |

Performance work begins with declared workloads: graph size, reference count,
generation volume, compatibility diff size, concurrent event streams, trace
length, and workbench rendering pressure. Thresholds are registered before
candidate results are examined.

## Risks and controls

| Risk | Why it matters | Control |
| --- | --- | --- |
| Scope explosion | The old repository already contains many domains, languages and transports | Freeze the launch vertical; additions require a consumer and gate |
| Specification theatre | A large grammar can appear mature without any runtime using it | Two independent adapters and black-box conformance before release |
| Generator drift | Handwritten clients silently become semantic authorities | Generated cores, drift checks and provenance-bound artifacts |
| Lowest-common-denominator design | Protocol bridges can flatten important semantics | Canonical graph remains richer; every projection declares loss |
| YAI leakage | Old names, private doctrine and commercial rules could reach the public tree | Clean export, no old-history publication, full path/name/license scan |
| Licensing ambiguity | The current repo references external terms that are absent | File-level admission manifest and new license gate before public creation |
| Premature naming | A weak or colliding name can cap the project's identity | Dedicated identity milestone with namespace and product-fit evidence |
| Too many languages | Four SDKs dilute the first vertical | TypeScript, then Python; Rust after parity; C later |
| UI as a second product | Workbench can diverge from the public interfaces | Workbench uses generated client and public adapter contracts only |
| Ecosystem churn | MCP, A2A and compatibility APIs evolve | Exact upstream versions, isolated bridges and compatibility fixtures |
| Unsafe remote invocation | A generic workbench could expose dangerous operations casually | Graph-level effects/authority/confirmation plus adapter enforcement tests |
| Centralized registry capture | Discovery service could become mandatory authority | Local/Git/content-addressed packages remain first-class |

## Current non-claims

The Project does not currently claim:

- a selected final name;
- an authorized implementation program;
- a public or open-source-ready repository;
- permission to publish the current history or relicence every old artifact;
- an accepted canonical graph or file format;
- working code generation;
- SDK, CLI, protocol, bridge, adapter, or workbench support;
- MCP or A2A equivalence;
- conformance of any external runtime;
- production security, stability, compatibility, or performance;
- replacement of YAI Interfaces inside YAI;
- compatibility with the old YAI operation registry or SDK packages;
- a hosted service, commercial plan, foundation, standard body, or ecosystem
  registry;
- a version number or release date.

## Promotion and roadmap discipline

This file changes only when accepted evidence changes macro truth or when the
product direction is deliberately revised. Implementation notes and daily logs
do not belong here. Git owns chronology; issues will own bounded selected work;
pull requests will own delivery evidence; decision records will own durable
architectural choices after the public repository exists.

Every milestone update must include:

- exact before and after repository identity;
- files and semantic owners changed;
- acceptance evidence and commands;
- failures, blocks and environmental limits;
- compatibility impact;
- security and licensing impact where applicable;
- explicit non-claims;
- the single next milestone, or `NONE`.

Completion of a milestone does not promote an entire maturity row unless its
stated promotion condition is met. A generated file is not implementation
proof. A reference adapter is not independent conformance. A successful demo is
not production readiness. Public visibility is not a release.

## Decision required after this roadmap

The next review should decide only these questions:

1. Is the Project an interface engineering platform for AI/agent runtimes, or
   should its target be narrower or broader?
2. Is the launch demonstration the right proof of value?
3. Is the private-archive plus clean-public-repository topology accepted?
4. If yes, may `REBIRTH.IDENTITY.0` become `selected`?

No later milestone should be selected during the same decision. The name and
source boundary deserve their own evidence before code begins.
