# Validation Commands

Required AGENTS.1 commands:

```sh
pwd
git branch --show-current
git status --short
find .agents -maxdepth 5 -type f | sort
find . -maxdepth 3 -type d -not -path './.git*' -not -path './node_modules*' -not -path './target*' -not -path './dist*' -not -path './build*' | sort
git diff --check
test ! -d .agents/codex
test ! -d .agents/claude
test ! -d .agents/cursor
test ! -d .agents/copilot
```

Observed repo-local validation command:

```sh
python3 -m json.tool extraction/source-manifest.json >/dev/null
```
