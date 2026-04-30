# API Core Leakage Audit (Wave 12G)

This audit captures extraction blockers for Wave 13.

## Coupling classes

1. Core struct leakage risk
- API surfaces that format responses from runtime-native structures without explicit contract projection layer.

2. Runtime internals leakage
- API family outputs tied to runtime state file/internal lifecycle shape rather than stable contract vocabulary.

3. CLI semantic leakage
- API behavior/messages carrying CLI command text as canonical response semantics.

4. Session-as-user compatibility leakage
- `session attach --user`, `session active-case`, user-linked session defaults surfaced as canonical semantics.

## Observed hotspots

- `api/families/session/session_api.c`
  - compatibility commands and user/session/case blending.
  - transitional semantics required for backward compatibility.

- `api/families/ai/ai_api.c`
  - mixed conversational/CLI formatted outputs and runtime/provider/session couplings.

- `api/families/provider/provider_api.c`
  - provider lifecycle detail coupling to runtime internals.

- `api/families/knowledge/*`
  - broad scope, mixed projection levels across records/lineage/context/memory.

## 12G posture

- No behavior break introduced.
- Couplings are documented for extraction slicing in Wave 13.
- Session compatibility remains intentionally transitional.
