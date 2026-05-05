# Canonical CLI Invocation

## Status

* Delivery: V10.5
* Status: active local model
* Track: V - Core/runtime/API/SDK/CLI/identity/case
* Repo branch: `feature/topology-refactor-8`

## Purpose

Define the canonical installed CLI workflow.

## Canonical Command Form

```bash
yai auth login --local-dev
yai case root
yai case open projects/site-e0-cleanup
yai case enter projects/site-e0-cleanup
yai case status
```

## Non-Canonical Dev Invocation

These are debug/test-only:

```bash
cargo run --quiet --
YAI_CONFIG_HOME=/tmp/...
YAI_ACCOUNT_USERNAME=...
```

## Install

Install the Rust CLI with:

```bash
cd ~/Developer/YAI/cli
cargo install --path . --force
```

The installed CLI binary is:

```text
~/.cargo/bin/yai
```

The shell PATH must resolve that binary before older runtime carrier binaries:

```bash
export PATH="$HOME/.cargo/bin:$PATH"
which yai
yai --help
```

In the current workspace, plain PATH initially resolved:

```text
/usr/local/bin/yai
```

That binary is the runtime carrier, not the Rust CLI. The canonical CLI path
therefore requires `$HOME/.cargo/bin` to be first for CLI smoke validation.

V10.6 records this as a temporary local residual. Product direction remains:
the CLI owns the user-facing `yai` command, and runtime carrier execution is
service/internal under `/usr/local/libexec/yai/runtime` or equivalent packaging
paths.

## State

| Concern | Canonical |
| ------- | --------- |
| binary | installed `yai` from PATH |
| config/state | `~/.yai` |
| test isolation | optional `YAI_CONFIG_HOME=/tmp/...` |
| account username | from real account later; derived/local only until backend exists |
| production login | deferred |
| Supabase/database | deferred |

## Boundary Rules

```text
installed yai != cargo run
canonical smoke != env-injected test
local-dev auth is temporary until account backend exists
CLI command names are canonical now
real account/Supabase integration is deferred to E waves
```
