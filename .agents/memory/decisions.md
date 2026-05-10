# Decisions

## 2026-05-10 - `.agents` must track repo truth
- Decision: `.agents` is living control-plane documentation and must be updated in the same delivery when repo truth changes.
- Reason: Prevent stale layout, fake modules, fake commands, and fake ownership.
- Affected paths: `.agents/**`
