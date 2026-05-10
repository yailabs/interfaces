# Drift Checks

Purpose:

- Compare `.agents` claims against the current repo.
- Catch vendor-folder regression and non-`.agents` scope drift.

Baseline inspection commands:

```sh
pwd
git branch --show-current
git status --short
find .agents -maxdepth 5 -type f | sort
find . -maxdepth 3 -type d -not -path './.git*' -not -path './node_modules*' -not -path './target*' -not -path './dist*' -not -path './build*' | sort
git diff --check
```

Vendor regression check:

```sh
test ! -d .agents/codex
test ! -d .agents/claude
test ! -d .agents/cursor
test ! -d .agents/copilot
```

AGENTS.1 scope check:

```sh
git diff --name-only | grep -v '^.agents/' && echo "ERROR: non-.agents changes detected" || true
```

Fake-claim checks where possible:

```sh
rg -n 'observed|legacy-observed|canonical|planned-not-created|external|unknown' .agents
rg -n 'contracts/|schemas/|envelopes/|errors/|transports/|openapi/|projections/|mappings/|registry/|lifecycle/' .agents
```
