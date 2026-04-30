# Session Family (Transitional Compatibility)

`api/families/session` currently carries transitional compatibility semantics.

Compatibility commands that remain operational:
- `session attach`
- `session detach`
- `session current`
- `session active-case`
- `attach --user`

Canonical future split direction:
- identity/auth status
- runtime instance status
- client connection attach/detach
- operator context current/set-case
- case current/inspect/watch

Wave 12G does not break existing behavior; it marks this family as boundary-cleanup required for Wave 13.
