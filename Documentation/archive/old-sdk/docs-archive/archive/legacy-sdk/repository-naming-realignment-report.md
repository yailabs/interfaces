# Repository Naming Realignment Report (`sdk`)

Date: 2026-03-08

## Scope
Repository naming realignment only (post-rename wave already completed).
No API/runtime/architecture semantic change.

## Applied mapping
- `yai-labs/yai-sdk` -> `yai-labs/sdk`
- `yai-labs/yai-law` -> `yai-labs/law`
- `yai-labs/yai-cli` -> `yai-labs/cli`
- `yai-labs/yai-ops` -> `yai-labs/ops`
- `yai-labs/yai-infra` -> `yai-labs/infra`
- `yai-labs/yai-studio` -> `yai-labs/studio`

Text references used as repository identity were aligned (`yai-law` -> `law`, `yai-cli` -> `cli`, etc.).

## Internal path policy decision
Decision: adopt canonical dependency naming in active references.

Applied:
- `deps/yai-law` -> `deps/law`
- `deps/yai-law.ref` -> `deps/law.ref` (workflow/docs references)

Current state:
- no `deps/` folder is structurally required by sdk runtime code;
- compatibility lookup remains via `tools/sh/resolve_law.sh` and explicit env/path resolution.

## Main realigned areas
- README/docs/wrappers naming and cross-repo references
- CI/workflows and templates (`.github/**`)
- build/tool scripts (`Makefile`, `tools/sh/*`)
- law alignment wording across docs and governance templates

## Residual legacy intentionally kept
The following remain as product/tool/runtime identifiers, not repository identity:
- `yai-sdk` in product/tool labels (e.g. `Makefile` banner, Python wrapper docstring, pkg-config name)
- `yai-cli` request client identifier in `src/rpc/rpc_client.c`

## Follow-up
Optional: if product string harmonization is desired (`yai-sdk` labels), handle in a dedicated branding pass, not in repository naming realignment.
