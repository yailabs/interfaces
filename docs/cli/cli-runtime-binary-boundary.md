# CLI / Runtime Binary Boundary

## Status

* Delivery: V10.6
* Status: active local install policy
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Purpose

Define which binary owns the user-facing `yai` command.

## Decision

Product direction:

```text
The CLI owns the user-facing `yai` command.
The runtime carrier must not shadow the CLI command.
```

Current local decision:

```text
B - temporary PATH precedence required; tracked residual.
```

Residual:

```text
/usr/local/bin/yai still shadows the CLI unless ~/.cargo/bin is first in PATH.
Future packaging must resolve this by making CLI own `yai`.
```

## Binary Ownership

| Binary/path | Owner | Role | User-facing |
| ----------- | ----- | ---- | ----------- |
| `yai` from PATH | CLI | user command surface | yes |
| `/usr/local/libexec/yai/runtime` | runtime | service executable | no |
| `/usr/local/bin/yai` | current local residual | currently shadows CLI in plain PATH; must not remain runtime carrier long-term | no/preferred no |
| `~/.cargo/bin/yai` | CLI dev install | local development CLI | yes |

## Canonical Validation

Expected CLI validation command shape:

```bash
export PATH="$HOME/.cargo/bin:$PATH"
which yai
yai --help
yai auth status
yai case status
```

Expected behavior:

```text
which yai -> ~/.cargo/bin/yai
yai --help -> CLI help with auth/case commands
```

Current plain shell residual:

```text
which yai -> /usr/local/bin/yai
```

That plain-path binary is the runtime carrier in this workspace and does not
show the CLI auth/case command surface.

## Boundary Rules

```text
CLI command `yai` != runtime carrier
runtime carrier should be invoked by service manager or CLI internals, not by users
canonical smoke must use installed `yai`
cargo run is debug-only
YAI_CONFIG_HOME is test isolation only
YAI_ACCOUNT_USERNAME is debug override only
```
