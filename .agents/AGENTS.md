# AGENTS

Repo role: API/platform boundary and service contract projection.

Mandatory read order:
1. `.agents/AGENTS.md`
2. `.agents/system/repo-profile.md`
3. `.agents/system/ownership-map.md`
4. `.agents/system/cross-repo-boundary.md`
5. `.agents/system/repository-layout.md`
6. `.agents/system/canonical-paths.md`
7. `.agents/policies/edit-policy.md`
8. `.agents/policies/truth-maintenance.md`
9. `.agents/policies/no-fake-state.md`
10. `.agents/workflows/delivery.md`
11. `.agents/validation/commands.md`
12. `.agents/validation/drift-checks.md`
13. `.agents/memory/current-state.md`

Allowed edit surface: AGENTS.1 is limited to `.agents/**`.
Forbidden edit surface: non-`.agents` files in this wave and vendor folders under `.agents/`.
Truth rule: if a delivery changes repo truth, update `.agents` in the same delivery.
Never invent: paths, modules, commands, ownership, validation, or implementation state.
