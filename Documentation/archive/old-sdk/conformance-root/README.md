# SDK Conformance

Planned checks:
- status vocabulary aligns with `yai-api`
- envelope model aligns with `yai-api`
- no CLI shell-out
- no raw core/runtime struct usage
- no transport assumption (HTTP/IPC)
- deferred families reported honestly
- package-level type/build checks pass
- SDK.01 Rust Local IPC RPC coverage validates endpoint discovery, frame
  vocabulary, handshake model, non-default posture, and provider-transport
  separation
