---
name: repo-audit
description: Inspect repo layout, dirty state, ownership boundaries, and deprecated paths before editing.
---

Procedure:
1. Inspect the current tree.
2. Never infer layout from memory.
3. Mark absent future paths as `planned-not-created`.
