# WSV-8.4 Composition Debt Disposition (SDK/CLI Consumer Layer)

Date: 2026-03-10

This note records the WSV-8.4 audited disposition for workspace families that were still partially composition-backed.

## Decision matrix

| Family | Current backing | WSV-8.4 disposition | Canonical path | Secondary fallback |
|---|---|---|---|---|
| `ws graph` | direct runtime ids (`yai.workspace.graph.*`) | **direct-backed (kept)** | `ws graph ...` | `ws query graph*` for low-level cases only |
| `ws data` | canonical grammar over query substrate | **partially promoted (kept composition)** | `ws data ...` | `ws query <family>` |
| `ws db` | mixed direct (`status/tail`) + inspect/query composition | **partially promoted (kept composition)** | `ws db ...` | `ws query workspace/events` |
| `ws knowledge` | status via inspect + query families (`transient/memory/providers/context`) | **partially promoted (kept composition)** | `ws knowledge ...` | `ws query transient/memory/providers/context` |
| `ws recovery` | canonical grammar mapped to status/lifecycle/open | **partially promoted (kept composition)** | `ws recovery ...` | low-level lifecycle ids |
| `ws policy` | direct runtime ids (`policy_*`) | **direct-backed (kept)** | `ws policy ...` | n/a |
| `ws domain` | direct runtime ids (`domain_get/domain_set`) | **direct-backed (kept)** | `ws domain ...` | n/a |
| `ws debug` | direct runtime id (`debug_resolution`) | **direct-backed (kept)** | `ws debug resolution` | n/a |

## Why composition remains in selected families

1. Runtime already exposes canonical behavior, but some subcommands still aggregate status/inspect/query slices rather than dedicated ids.
2. CLI and SDK now expose canonical grammar/helpers first; composition is internal implementation detail for those subcommands.
3. Keeping these composed paths avoids breaking operator/consumer flows while preserving canonical first-path UX.

## Canonical-first rule

Use canonical families first:

- `ws db ...`
- `ws knowledge ...`
- `ws recovery ...`

Use query fallback only when needed for raw/substrate exploration:

- `ws query <family>`

## Follow-up scope (post-WSV-8.4)

1. Promote `db classes/count` and selected `knowledge`/`recovery` calls to dedicated runtime ids when runtime roadmap lands.
2. Keep fallback paths compatibility-only in examples and avoid promoting them in quickstarts.
