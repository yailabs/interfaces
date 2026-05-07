#!/usr/bin/env python3
import json
from pathlib import Path


root = Path(__file__).resolve().parents[1]

required_files = [
    root / "transports/transport-contract-index.v1.md",
    root / "transports/implementation-readiness-matrix.v1.json",
    root / "transports/implementation-readiness-matrix.v1.md",
    root / "transports/implementation-handoff.v1.md",
    root / "docs/transport-contract-index-implementation-readiness.md",
]

expected_transports = {
    "local_ipc_rpc": {
        "contract_status": "frozen",
        "implementation_priority": "primary_now",
        "runtime_readiness": "ready_for_implementation",
        "sdk_readiness": "ready_for_client_implementation",
        "client_default": "cli_loom_native",
    },
    "local_http_loopback": {
        "contract_status": "frozen",
        "implementation_priority": "primary_now",
        "runtime_readiness": "ready_for_implementation",
        "sdk_readiness": "ready_for_client_implementation",
        "client_default": "dashboard_web",
    },
    "local_event_stream": {
        "contract_status": "frozen",
        "implementation_priority": "primary_now",
        "runtime_readiness": "ready_for_implementation",
        "sdk_readiness": "ready_for_client_implementation",
        "client_default": "realtime",
    },
    "lan_secure": {
        "contract_status": "frozen",
        "implementation_priority": "controlled_future",
        "runtime_readiness": "future_only",
        "sdk_readiness": "future_only",
        "client_default": "none",
    },
    "remote_https": {
        "contract_status": "frozen",
        "implementation_priority": "controlled_future",
        "runtime_readiness": "future_only",
        "sdk_readiness": "future_only",
        "client_default": "none",
    },
    "provider_transport_boundary": {
        "contract_status": "frozen",
        "implementation_priority": "separate_boundary",
        "runtime_readiness": "separate_provider_boundary",
        "sdk_readiness": "separate_provider_boundary",
        "client_default": "none",
    },
    "in_process_test": {
        "contract_status": "frozen",
        "implementation_priority": "test_only",
        "runtime_readiness": "not_product",
        "sdk_readiness": "test_only",
        "client_default": "none",
    },
    "subprocess_stdio_compat": {
        "contract_status": "frozen",
        "implementation_priority": "compat_only",
        "runtime_readiness": "not_product",
        "sdk_readiness": "compat_only",
        "client_default": "none",
    },
}

allowed_contract_status = {"frozen", "partial", "deferred"}
allowed_priority = {
    "primary_now",
    "secondary_later",
    "controlled_future",
    "test_only",
    "compat_only",
    "separate_boundary",
}
allowed_runtime = {
    "ready_for_skeleton",
    "ready_for_implementation",
    "future_only",
    "not_product",
    "separate_provider_boundary",
}
allowed_sdk = {
    "ready_for_client_contract",
    "ready_for_client_implementation",
    "future_only",
    "test_only",
    "compat_only",
    "separate_provider_boundary",
}
allowed_client_default = {"cli_loom_native", "dashboard_web", "realtime", "none"}

errors = []

for path in required_files:
    if not path.exists():
        errors.append(f"missing required API.09 file: {path.relative_to(root)}")

matrix = {}
matrix_path = root / "transports/implementation-readiness-matrix.v1.json"
if matrix_path.exists():
    matrix = json.loads(matrix_path.read_text())

entries = {
    entry.get("transport"): entry
    for entry in matrix.get("transports", [])
    if isinstance(entry, dict) and entry.get("transport")
}

index_text = (root / "transports/transport-contract-index.v1.md").read_text() if (root / "transports/transport-contract-index.v1.md").exists() else ""
matrix_md_text = (root / "transports/implementation-readiness-matrix.v1.md").read_text() if (root / "transports/implementation-readiness-matrix.v1.md").exists() else ""
handoff_text = (root / "transports/implementation-handoff.v1.md").read_text() if (root / "transports/implementation-handoff.v1.md").exists() else ""
summary_text = (root / "docs/transport-contract-index-implementation-readiness.md").read_text() if (root / "docs/transport-contract-index-implementation-readiness.md").exists() else ""

for transport in expected_transports:
    if transport not in index_text:
        errors.append(f"transport-contract-index must index {transport}")
    if transport not in entries:
        errors.append(f"implementation-readiness matrix missing {transport}")

required_fields = {
    "contract_status",
    "implementation_priority",
    "runtime_readiness",
    "sdk_readiness",
    "client_default",
}
for transport, expected in expected_transports.items():
    entry = entries.get(transport)
    if not entry:
        continue
    missing = sorted(required_fields - set(entry))
    for field in missing:
        errors.append(f"{transport}: missing required field {field}")
    if entry.get("contract_status") not in allowed_contract_status:
        errors.append(f"{transport}: invalid contract_status {entry.get('contract_status')}")
    if entry.get("implementation_priority") not in allowed_priority:
        errors.append(f"{transport}: invalid implementation_priority {entry.get('implementation_priority')}")
    if entry.get("runtime_readiness") not in allowed_runtime:
        errors.append(f"{transport}: invalid runtime_readiness {entry.get('runtime_readiness')}")
    if entry.get("sdk_readiness") not in allowed_sdk:
        errors.append(f"{transport}: invalid sdk_readiness {entry.get('sdk_readiness')}")
    if entry.get("client_default") not in allowed_client_default:
        errors.append(f"{transport}: invalid client_default {entry.get('client_default')}")
    for field, value in expected.items():
        if entry.get(field) != value:
            errors.append(f"{transport}: expected {field}={value}, found {entry.get(field)}")

expected_handoff_markers = [
    "RT.01 — Runtime Transport Boundary Skeleton",
    "RT.02 — Local IPC RPC Runtime Listener",
    "SDK.01 — Rust Local IPC RPC Client Transport",
    "CLI.01 — CLI Local IPC RPC Default",
    "LOOM.01 — Loom Local IPC RPC Default",
    "RT.03 — Local HTTP Loopback Runtime Server",
    "SDK.02 — TypeScript Local HTTP Loopback Client",
    "WEB.01 — Dashboard Local Runtime Binding",
    "RT.04 — Local Event Stream Runtime Serving",
    "SDK.03 — Stream Clients TS/Rust",
]
for marker in expected_handoff_markers:
    if marker not in handoff_text:
        errors.append(f"implementation handoff must include {marker}")

combined_text = "\n".join((index_text, matrix_md_text, handoff_text, summary_text))
for forbidden in (
    "transport implementation complete",
    "runtime listener implemented",
    "SDK transport implemented",
    "CLI already uses local_ipc_rpc",
    "Loom already uses local_ipc_rpc",
    "dashboard already uses local_http_loopback",
    "LAN ready for default",
    "Remote HTTPS is default runtime",
    "subprocess is canonical product transport",
    "in_process_test is product transport",
):
    if forbidden in combined_text:
        errors.append(f"API.09 docs must not claim completed implementation: {forbidden}")

if errors:
    print("transport-contract-index: FAIL")
    for error in errors:
        print("-", error)
    raise SystemExit(1)

print("transport-contract-index: ok")
