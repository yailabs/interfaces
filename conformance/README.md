# Conformance

Run:
- `python3 conformance/check_operation_registry.py`
- `python3 conformance/check_api_contracts.py`
- `python3 conformance/check_operation_transport_mapping.py`
- `python3 conformance/check_api_envelope_error_stream.py`
- `python3 conformance/check_local_ipc_rpc_contract.py`
- `python3 conformance/check_local_http_loopback_contract.py`
- `python3 conformance/check_local_event_stream_contract.py`
- `python3 conformance/check_lan_remote_boundary.py`
- `python3 conformance/check_test_compat_transport_boundary.py`
- `python3 conformance/check_transport_contract_index.py`
- `python3 conformance/check_logout_seal_policy.py`
- `python3 conformance/check_case_evidence_binding.py`

Coverage:
- registry grammar integrity
- schema reference integrity
- operation-to-transport mapping integrity
- envelope/error/stream frame contract integrity
- Local IPC RPC contract integrity
- Local HTTP Loopback contract integrity
- Local Event Stream contract integrity
- LAN Secure and Remote HTTPS boundary split integrity
- In-process Test and Subprocess Stdio compatibility boundary integrity
- transport contract index and implementation readiness integrity
- OpenAPI parse + operationId/family-tag consistency
- forbidden lifecycle/policy/supervisor checks
- API mirror alignment with canonical protocol artifacts in `../yai/protocols`

Boundary:
- `check_api_contracts.py` and `check_operation_registry.py` are API-owned checks.
- `check_operation_transport_mapping.py` is an API-owned mapping conformance
  check for API.02 dispatch and transport policy.
  It also enforces the explicit A2 RT.04 Local IPC RPC coverage markers for
  the audited supported, deferred, and blocked operation subset.
- `check_api_envelope_error_stream.py` is an API-owned contract conformance
  check for API.03 envelope, error, and stream-frame alignment.
- `check_local_ipc_rpc_contract.py` is an API-owned contract conformance check
  for API.04 Local IPC RPC discovery, handshake, frame, stream, and security
  alignment.
- `check_local_http_loopback_contract.py` is an API-owned contract conformance
  check for API.05 Local HTTP Loopback discovery, route, header, origin, token,
  and security alignment.
- `check_local_event_stream_contract.py` is an API-owned contract conformance
  check for API.06 Local Event Stream binding, frame, subscription, heartbeat,
  backpressure, redaction, and terminal-event alignment.
- `check_lan_remote_boundary.py` is an API-owned contract conformance check
  for API.07 LAN Secure and Remote HTTPS boundary split, separation from
  loopback and provider transport, and disabled-by-default LAN posture.
- `check_test_compat_transport_boundary.py` is an API-owned contract
  conformance check for API.08 In-process Test and Subprocess Stdio
  compatibility boundary split and non-product posture.
- `check_transport_contract_index.py` is an API-owned contract conformance
  check for API.09 transport indexing, implementation readiness classification,
  and runtime or SDK handoff sequencing.
- `check_logout_seal_policy.py` and `check_case_evidence_binding.py` are API-side
  mirror checks that consume canonical protocol artifacts from `yai/protocols`.
- protocol mirror checks validate projection compatibility; they do not make API
  the owner of protocol meaning.
