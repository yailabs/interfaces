# Forbidden Scans

```sh
rg -n '(BEGIN [A-Z0-9 ]*PRIVATE KEY|api[_-]?key|secret|token=)' .
find .agents -type d \( -name codex -o -name claude -o -name cursor -o -name copilot \) -print
git diff --check
git diff --name-only | grep -v '^.agents/' && echo "ERROR: non-.agents changes detected" || true
```
