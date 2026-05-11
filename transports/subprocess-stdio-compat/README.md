# Subprocess Stdio Compat Contract

`api/transports/subprocess-stdio-compat/` holds the verticalized API.08
contract for the `subprocess_stdio_compat` transport class.

Purpose:
- define legacy, debug, and migration compatibility posture for process
  invocation over structured stdout and stderr
- keep subprocess invocation explicit and bounded
- prevent subprocess compatibility from becoming a canonical SDK transport

Boundary:
- `subprocess_stdio_compat` is compat-only
- `subprocess_stdio_compat` is not canonical
- `subprocess_stdio_compat` is not default CLI or Loom transport
- `subprocess_stdio_compat` is not browser or dashboard transport
- `subprocess_stdio_compat` is not provider/model transport

Out of scope:
- no subprocess runner implementation
- no stdout parser implementation
- no SDK transport implementation
