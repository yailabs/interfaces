# Subprocess Stdio Compat Stdout and Stderr Contract v1

## Purpose

Freeze stdout and stderr posture for `subprocess_stdio_compat`.

## Rules

- structured stdout is required if this transport is used
- stderr is diagnostics only
- stdout must carry structured API envelope output rather than inventing new
  operation grammar
- operation errors remain response-envelope errors
- process lifecycle errors remain transport errors
