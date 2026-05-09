<!--
YAI — Governed Case-Native Runtime

Copyright (c) 2026 Francesco Maiomascio.
All rights reserved.

This file is part of the YAI Community Source Tree.
Use, copying, modification, distribution, and production operation
are governed by the repository licensing documents, including
LICENSE, LICENSING.md, COMMERCIAL.md, and COPYING.

Development and non-production use is permitted under the applicable
YAI license terms. Production, organizational, persistent,
collaborative, customer-affecting, or business-critical use requires
a commercial license.
-->

# AGENTS.md

This file defines the operating contract for coding agents, AI assistants, and
automated tooling working in this repository.

Read it before changing anything.

The rules are not decorative. They exist because automated agents fail in
specific ways: they invent topology, cite files that were never checked, preserve
drift, overfit to stale plans, and create compatibility layers that become
permanent garbage.

This contract is the countermeasure.

---

## Repository Identity

YAI is a governed, case-native runtime system.

It is not a loose prototype, not a random monorepo, and not a collection of
interchangeable helper scripts. Each repository may expose a different slice of
the system, but every slice must preserve the same architectural discipline:

- Control judges.
- Runtime executes.
- State remembers.
- Lineage connects.
- Knowledge proposes.
- Memory consolidates.
- Recall reactivates.
- Analytics observes.
- Projections read.
- Clients connect.

No repository may silently collapse these roles into a convenient local shortcut.

---

## Universal Agent Rules

These rules apply in every YAI repository.

### 1. The repository is the source of truth

Do not rely on memory, prior summaries, plausible paths, or old plans when the
repository can be queried.

Before referencing a file, locate it.

Before moving code, inspect it.

Before claiming behavior, verify it.

Use commands such as:

```sh
pwd
git branch --show-current
git status --short
find . -maxdepth 4 -type f | sort
find . -maxdepth 4 -type d | sort
rg -n "<pattern>" <paths>
sed -n '1,220p' <file>
```

### 2. Do not invent topology

Do not create new root directories, domain surfaces, APIs, or compatibility
layers because they seem plausible.

If the canonical location is unclear, stop and record the ambiguity.

If a target surface already exists in another form, reuse, move, or drain it
instead of recreating it.

### 3. Do not cite unverified files

Every file mentioned in a patch, delivery report, or recommendation must have
been discovered in the current checkout or created in the current patch.

Plausible paths are not evidence.

### 4. Do not silently preserve drift

If code, documentation, tests, specs, and repository topology disagree, name the
drift explicitly.

Then either fix it inside the scoped work or record it as deferred.

Do not make summaries sound cleaner than the tree actually is.

### 5. Follow the current tree over stale plans

If prior context says a file exists but the tree says it does not, the tree wins.

If the plan says a branch or path is current but `pwd`, `git branch`, or `find`
disagree, record the divergence and proceed from verified state.

---

## Topology Discipline

YAI repositories do not all have the same topology.

Do not paste a universal root layout into every repo and treat it as truth.

Instead:

1. Discover the current root layout.
2. Identify the canonical surfaces already present.
3. Read repo-local documentation if present.
4. Preserve the repo’s real role in the broader YAI system.
5. Create new topology only when explicitly scoped.

A repository may be an API contract surface, CLI client, SDK, runtime/core tree,
website, Loom client, or another bounded surface. The local `AGENTS.md` applies
to all of them, but topology must be verified per repo.

---

## Direct-cut Refactor Rule

For internal private source files, prefer direct canonicalization.

When moving private implementation files:

```text
move implementation to canonical location
delete old private source path
update build/source references
update tests
record the move
```

Do not leave internal `.c`, `.rs`, `.ts`, `.py`, or similar source wrappers
unless there is a verified compatibility boundary.

Compatibility wrappers are allowed for:

* public headers
* public APIs
* external CLI surfaces
* serialized formats
* package exports
* build systems that cannot be updated in the current scope
* explicitly staged migrations with removal criteria

Compatibility wrappers are not allowed as a lazy way to avoid finishing an
internal refactor.

If a wrapper is kept, the patch must state:

* why it is required
* what depends on it
* when it can be removed
* how the canonical path is validated

---

## Ownership Discipline

Do not move semantics across planes.

### Knowledge

Knowledge is the active cognitive workbench.

It may assemble context, activate recall, retrieve candidates, build worksets,
detect gaps, identify contradictions, and produce proposals.

Knowledge does not own:

* canonical State facts
* causal Lineage truth
* Control decisions
* Runtime execution
* long-term Memory consolidation
* DuckDB projection truth
* Ladybug inspection truth
* account, license, entitlement, or machine authorization gates

### State

State preserves durable facts and canonical records.

State is not a query convenience layer, not a UI, not a projection, and not
Memory.

### Lineage

Lineage owns causal relation semantics.

Graph backends may store graph structures, but graph storage is not Lineage by
itself.

### Control

Control decides whether action may become consequence.

A proposal, signal, retrieval hit, health check, projection, or model output is
not a Control decision.

### Runtime

Runtime executes governed work.

Runtime does not own authorization, commercial entitlement, canonical case truth,
or long-term memory.

### Projections

Projection layers, including DuckDB, are derived read surfaces.

A missing or stale projection is not proof that a fact is missing or stale.

### Memory and Recall

Memory consolidates experience.

Recall reactivates relevant material.

Knowledge may trigger recall or work with recall candidates, but it does not
become the long-term Memory Spine.

### Ladybug

Ladybug is an inspection, navigation, or visualization boundary candidate.

Ladybug does not own causal truth, State, graph substrate, projections, Control,
or Memory.

---

## Working Method

Every implementation session must follow this order.

### 1. Discovery

Find the real files and current behavior.

### 2. Scope

State the exact files that may change.

State what must not change.

### 3. Patch

Make narrow changes.

Prefer moving and deleting private legacy paths over adding compatibility layers.

### 4. Verification

Verify the patch with targeted commands.

At minimum:

```sh
git diff --check
git status --short
rg -n "<expected marker>" <changed paths>
```

If code moved, verify:

* old path removed or intentionally wrapped
* new path exists
* references updated
* tests or compile checks reflect canonical paths

### 5. Build / Test

Run the narrowest meaningful validation.

If full build is out of scope or blocked by known red baseline, say so
explicitly. Do not imply green status.

---

## Documentation Discipline

Documentation must describe the repository that exists, not the repository the
agent wishes existed.

When documentation and code diverge:

* update the documentation, or
* record the drift as deferred.

Do not use documentation as a substitute for implementation.

Do not create long audit trails while leaving the filesystem unchanged unless
the explicit scope is investigation.

---

## Output Discipline

Every implementation session must end with:

```text
## Session Summary

### Scope
<what was in scope>

### Files Modified
<every file changed>

### Patch Summary
<what changed and where>

### Verification
<commands and evidence>

### Build and Validation
<build/test/compile results, or explicit reason not run>

### Residual Drift or Deferred Items
<known remaining misalignment>
```

If a command failed, include it.

If validation was not run, say exactly why.

If the work leaves debt, name it.

---

## Prohibited Actions

Agents must not:

* invent paths or topology
* cite files not discovered
* create parallel systems for existing concepts
* preserve private source wrappers without a verified reason
* claim projections are canonical truth
* claim health/readiness is semantic truth
* claim retrieval output is evidence
* claim Knowledge output is authorization
* claim Runtime execution is permission
* claim graph backend is Lineage
* claim Ladybug is Lineage
* claim session owns case/auth/runtime state
* silently ignore red baselines
* hide compile failures
* broaden scope to fix unrelated issues without approval

---

## Cross-repo Rule

If this repository is part of a synchronized YAI branch set, respect the
cross-repo phase.

Do not assume another repo has already been updated.

When changing shared contracts, record what sibling repos may need to consume.

When copying this file into another repo, do not alter that repo’s topology
claims unless they are verified locally.

---

## Governance

`AGENTS.md` is a root governance document.

Agents may update it only when explicitly instructed.

Changes to this file must be treated with the same care as changes to
`CONTRIBUTING.md`, `GOVERNANCE.md`, or security/licensing documents.

---

## Final Rule

Reality beats plan.

When this file, prior instructions, generated summaries, or external assumptions
conflict with the current repository tree, realign to the repository and surface
the divergence explicitly.
