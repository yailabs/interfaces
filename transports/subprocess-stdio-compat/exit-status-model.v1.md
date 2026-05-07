# Subprocess Stdio Compat Exit Status Model v1

## Purpose

Define process exit-status posture for `subprocess_stdio_compat`.

## Rules

- exit status must be mapped separately from operation result
- non-zero exit status does not automatically redefine API operation error
  semantics
- invalid stdout envelope remains a transport decode failure, not a successful
  operation result
