# A new project is taking shape

This repository is being transformed into a new open-source interface
engineering platform for AI and agent runtimes.

The goal is ambitious and concrete:

> Define a runtime once. Ship every trustworthy way to operate it.

One canonical operational model will describe capabilities, operations, types,
errors, effects, authority, transports, streams, compatibility, and proof. A
compiler will turn that model into coherent developer and operator surfaces:

```text
                       Operational Interface Graph
                                    │
             ┌──────────────────────┼──────────────────────┐
             ▼                      ▼                      ▼
       SDKs · CLI · docs     HTTP · events · IPC     fixtures · replay
                             MCP · A2A bridges         conformance · traces
             └──────────────────────┼──────────────────────┘
                                    ▼
                         interactive workbench
```

The result is intended to be more than a schema format or API linter. It will
combine an interface compiler, generated clients, protocol bridges, runtime
adapters, executable conformance, compatibility analysis, and a browser
workbench for inspecting and operating real systems.

## Current status

| Axis | Current truth |
| --- | --- |
| Product name | Unselected. `interfaces` and `YAI Interfaces` will not be the new identity. |
| Engineering | Not started. The roadmap is under review. |
| Existing code | Private source material from the former YAI Interfaces repository. It is not the new product architecture. |
| Public release | Blocked until naming, source classification, licensing, clean-history, security, and standalone validation gates pass. |
| Active implementation milestone | None. |
| Next proposed milestone | `REBIRTH.IDENTITY.0`: select the product name and namespaces. |

The current directories contain useful experiments in operation registries,
schemas, transports, SDKs, fixtures, and conformance. They also contain
YAI-specific assumptions, stale cross-repository links, internal material, and
incomplete standalone checks. Do not treat them as a stable API, supported SDK,
or open-source release.

## Roadmap

The complete product thesis, extraction policy, architecture, maturity matrix,
milestone sequence, launch demonstration, release gates, and current non-claims
live in [ROADMAP.md](ROADMAP.md).

The roadmap establishes two separate repositories in the future:

```text
this private repository          future public repository
complete source archive          new name and clean history
old branches and assumptions     reviewed, licensed artifacts only
```

This protects the original work while allowing the new project to begin with a
clear identity and a reviewable open-source boundary.

## Intended first proof

The first credible release must define one compact agent-runtime lifecycle and
generate enough real surfaces to prove the architecture:

- TypeScript and Python clients;
- a generated command-line client;
- HTTP, local IPC, and typed event behavior;
- MCP and A2A projection reports;
- positive, negative, and compatibility conformance;
- replayable traces and receipts;
- an interactive browser workbench;
- the same semantics exercised through two independent runtime adapters.

Unsupported or lossy projections must be reported explicitly. A generated file,
mock, or successful demo does not by itself establish runtime conformance or
production readiness.

## Licensing

No open-source license is currently granted by this repository. Licensing is a
required gate in the clean public extraction described by the roadmap. The
future public project will adopt an OSI-approved license only after authorship,
reuse, and third-party notice review are complete.
