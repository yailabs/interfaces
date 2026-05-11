# Truth Maintenance

Purpose:

- Keep `.agents/` synchronized with the current repository.
- Prevent fake paths, fake modules, fake commands, fake ownership, and stale validation.

Rules:

- Update `.agents` whenever structure, boundaries, ownership, commands, or current state change.
- Never write repo facts from memory alone.
- No fake path rule: every path must be `observed`, `legacy-observed`, `canonical`, `planned-not-created`, `external`, or `unknown`.
- No fake module rule: do not claim a module exists unless it was observed.
- No fake command rule: do not document a command unless it was observed or is standard for an observed tool file.
- No stale validation rule: if validation tooling changes, update validation docs in the same delivery.
- No stale ownership rule: if boundaries change, update ownership and boundary files in the same delivery.

Required path status vocabulary:

- `observed`
- `legacy-observed`
- `canonical`
- `canonical-target`
- `planned-not-created`
- `external`
- `unknown`

Required update matrix:

```text
Change type -> Required `.agents` update

New directory or moved directory
-> system/repository-layout.md
-> system/canonical-paths.md
-> memory/current-state.md
-> memory/handoff.md

Deleted directory or removed module
-> system/repository-layout.md
-> system/canonical-paths.md
-> memory/current-state.md
-> memory/decisions.md if it reflects a durable decision
-> memory/handoff.md

Ownership/boundary change
-> system/repo-profile.md
-> system/ownership-map.md
-> system/cross-repo-boundary.md
-> policies/edit-policy.md
-> memory/decisions.md
-> memory/handoff.md

Validation/build/test command change
-> validation/commands.md
-> validation/quality-gates.md
-> validation/repo-local-checklist.md
-> workflows/validation.md
-> memory/handoff.md

New forbidden state or safety rule
-> policies/safety-security.md
-> policies/no-fake-state.md
-> validation/forbidden-scans.md
-> validation/quality-gates.md

Workflow change
-> workflows/*.md
-> AGENTS.md if read order or top-level rule changes
-> manifest.yaml

Repo role change
-> README.md
-> AGENTS.md
-> manifest.yaml
-> system/repo-profile.md
-> system/ownership-map.md
-> system/cross-repo-boundary.md
-> memory/decisions.md

Skill/template change
-> skills/*/SKILL.md
-> templates/*.md
-> manifest.yaml
```
