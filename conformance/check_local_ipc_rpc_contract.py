#!/usr/bin/env python3
import json
from pathlib import Path


root = Path(__file__).resolve().parents[1]
contract_root = root / "transports/local-ipc-rpc"

required_files = [
    root / "transports/local-ipc-rpc.v1.md",
    contract_root / "README.md",
    contract_root / "discovery.v1.md",
    contract_root / "handshake.v1.md",
    contract_root / "frame.v1.schema.json",
    contract_root / "frame-model.v1.md",
    contract_root / "message-types.v1.json",
    contract_root / "security.v1.md",
    contract_root / "streaming.v1.md",
    contract_root / "cancellation-timeout.v1.md",
    contract_root / "errors.v1.md",
    contract_root / "platform-bindings.v1.md",
    contract_root / "conformance-profile.v1.md",
    root / "Documentation/local-ipc-rpc-contract.md",
]

errors = []

for path in required_files:
    if not path.exists():
        errors.append(f"missing required Local IPC RPC contract file: {path.relative_to(root)}")

frame_schema = {}
message_types = {}
if (contract_root / "frame.v1.schema.json").exists():
    frame_schema = json.loads((contract_root / "frame.v1.schema.json").read_text())
if (contract_root / "message-types.v1.json").exists():
    message_types = json.loads((contract_root / "message-types.v1.json").read_text())

required_frame_fields = {
    "frame_schema",
    "frame_id",
    "frame_type",
    "frame_version",
    "payload_encoding",
    "payload",
    "payload_size",
}
schema_fields = set(frame_schema.get("properties", {}).keys())
required_schema = set(frame_schema.get("required", []))
for field in required_frame_fields:
    if field not in required_schema or field not in schema_fields:
        errors.append(f"frame schema must include required field {field}")

expected_frame_types = {
    "handshake.request",
    "handshake.response",
    "operation.request",
    "operation.response",
    "stream.open",
    "stream.frame",
    "stream.close",
    "cancel.request",
    "heartbeat",
    "error",
}
message_type_values = {entry.get("type") for entry in message_types.get("frame_types", [])}
missing_types = sorted(expected_frame_types - message_type_values)
for frame_type in missing_types:
    errors.append(f"message-types registry missing frame type {frame_type}")

doc_text = "\n".join(path.read_text() for path in required_files if path.suffix == ".md")

required_mentions = {
    "Unix domain socket": "docs must mention Unix domain socket",
    "named pipe": "docs must mention Windows named pipe",
    "same-machine": "docs must require same-machine posture",
    "no LAN": "docs must require no-LAN posture",
    "transport error": "docs must distinguish transport error",
    "operation error": "docs must distinguish operation error",
    "API.03": "docs must mention API.03 envelope or frame carriage",
}
for needle, message in required_mentions.items():
    if needle not in doc_text:
        errors.append(message)

positive_forbidden = (
    "IPC listener implemented",
    "Unix socket server implemented",
    "named pipe server implemented",
    "SDK implements local_ipc_rpc",
    "API implements IPC server",
    "API owns socket lifecycle",
    "provider transport is local_ipc_rpc",
)
for forbidden in positive_forbidden:
    if forbidden in doc_text:
        errors.append(f"docs must not claim implementation ownership: {forbidden}")

if errors:
    print("local-ipc-rpc-contract: FAIL")
    for error in errors:
        print("-", error)
    raise SystemExit(1)

print("local-ipc-rpc-contract: ok")
