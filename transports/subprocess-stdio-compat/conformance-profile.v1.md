# Subprocess Stdio Compat Conformance Profile v1

## Purpose

Define the minimum contract claims that a future `subprocess_stdio_compat`
implementation must satisfy.

## Required Contract Areas

- compat-only posture
- structured stdout required
- stderr diagnostics only
- exit status separated from operation result
- explicit environment boundary
- deprecation posture
- non-canonical boundary

## Out of Scope for API.08

- no subprocess runner implementation
- no stdout parser implementation
- no SDK transport implementation
