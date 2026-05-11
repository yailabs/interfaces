# C SDK Command Compatibility

The C SDK command-id vocabulary is compatibility vocabulary, not protocol
truth.

`YAI_SDK_CMD_WORKSPACE_*` identifiers must not define operation semantics. They
are compatibility vocabulary until explicitly mapped to current YAI Interfaces
operation ids.

Future mapping to interfaces operation ids is required before treating these as
current command architecture.

INTF.6 does not remove or rename C command vocabulary. Preserve ABI/include
compatibility until an explicit major-version policy authorizes a breaking
change.

Current posture:

- C command-id vocabulary remains package compatibility surface.
- Protocol truth remains in registry, schema, mapping, transport, envelope,
  error, and conformance artifacts.
- Manual review remains required before compatibility command ids can be
  promoted, renamed, removed, or mapped into release-ready current operation
  architecture.
