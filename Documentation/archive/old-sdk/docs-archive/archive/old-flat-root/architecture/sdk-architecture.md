# yai-sdk Architecture

`yai-sdk` is a contract-bound client bridge over `yai-api`.

Boundary:
- Contract source: `../api`
- Runtime execution: `../yai`
- SDK surface: language packages under `packages/`

This wave provides scaffolded SDK shape only.

Wave 15 addition: SDK can target agent orchestration proposal entry contracts; execution remains deferred.


SDK authority:
- SDK is the official client consumption layer for applications.
- Runtime adapter internals in `yai` are not canonical client dependencies.
- Direct adapter use is transitional and limited to debug/conformance/bootstrap.
- SDK does not implement account backend behavior.

## Wave CLI-2A Surface Additions

Rust SDK family surfaces now include `runtime`, `session`, `case`, `provider`, and `models`.
Each family method dispatches through `YaiTransport::invoke` with canonical operation IDs and typed envelope data models.
