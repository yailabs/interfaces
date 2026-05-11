#!/usr/bin/env python3
import json
from pathlib import Path


root = Path(__file__).resolve().parents[1]
contract_root = root / "transports/local-event-stream"

required_files = [
    root / "transports/local-event-stream.v1.md",
    contract_root / "README.md",
    contract_root / "sse-binding.v1.md",
    contract_root / "rpc-stream-binding.v1.md",
    contract_root / "websocket-reservation.v1.md",
    contract_root / "event-frame.v1.schema.json",
    contract_root / "event-types.v1.json",
    contract_root / "subscription-model.v1.md",
    contract_root / "heartbeat-reconnect.v1.md",
    contract_root / "backpressure-resume.v1.md",
    contract_root / "security-redaction.v1.md",
    contract_root / "errors-terminal-events.v1.md",
    contract_root / "conformance-profile.v1.md",
    root / "Documentation/local-event-stream-contract.md",
]

errors = []
for path in required_files:
    if not path.exists():
        errors.append(f"missing required Local Event Stream contract file: {path.relative_to(root)}")

event_schema = {}
event_types = {}
if (contract_root / "event-frame.v1.schema.json").exists():
    event_schema = json.loads((contract_root / "event-frame.v1.schema.json").read_text())
if (contract_root / "event-types.v1.json").exists():
    event_types = json.loads((contract_root / "event-types.v1.json").read_text())

required_fields = {
    "schema",
    "stream_id",
    "event_id",
    "operation_id",
    "request_id",
    "sequence",
    "event_type",
    "created_at",
    "terminal",
    "heartbeat",
}
schema_required = set(event_schema.get("required", []))
schema_props = set(event_schema.get("properties", {}).keys())
for field in required_fields:
    if field not in schema_required or field not in schema_props:
        errors.append(f"event-frame schema must include required field {field}")

expected_event_types = {
    "stream.open",
    "stream.heartbeat",
    "stream.data",
    "stream.warning",
    "stream.error",
    "stream.cancelled",
    "stream.closed",
}
schema_event_types = set(
    event_schema.get("properties", {}).get("event_type", {}).get("enum", [])
)
registry_event_types = {entry.get("type") for entry in event_types.get("event_types", [])}
if schema_event_types != expected_event_types:
    errors.append("event-frame schema must expose the canonical Local Event Stream event types")
if registry_event_types != expected_event_types:
    errors.append("event-types registry must expose the canonical Local Event Stream event types")

doc_text = "\n".join(path.read_text() for path in required_files if path.suffix == ".md" and path.exists())
required_mentions = {
    "SSE": "docs must mention SSE binding",
    "WebSocket": "docs must mention WebSocket reservation",
    "local_ipc_rpc": "docs must mention RPC stream over local_ipc_rpc",
    "API.03": "docs must mention API.03 stream-frame alignment",
    "stream frames": "docs must mention stream frames",
    "response envelopes": "docs must distinguish stream frames from response envelopes",
    "heartbeat": "docs must mention heartbeat posture",
    "reconnect": "docs must mention reconnect posture",
    "resume": "docs must mention resume posture",
    "last_event_id": "docs must mention last_event_id posture where applicable",
    "backpressure": "docs must mention backpressure posture",
    "redaction": "docs must mention redaction posture",
    "raw payloads": "docs must forbid raw provider or model payload streaming",
    "provider credentials": "docs must forbid provider credential streaming",
    "case.records.tail": "docs must mention current watchable operations",
    "state.records.tail": "docs must mention current watchable operations",
    "workflow.runs.watch": "docs must mention current watchable operations",
}
for needle, message in required_mentions.items():
    if needle not in doc_text:
        errors.append(message)

forbidden_claims = (
    "SSE server implemented",
    "WebSocket server implemented",
    "RPC streaming implemented",
    "SDK stream client implemented",
    "provider transport is local_event_stream",
)
for forbidden in forbidden_claims:
    if forbidden in doc_text:
        errors.append(f"docs must not claim implementation ownership: {forbidden}")

if errors:
    print("local-event-stream-contract: FAIL")
    for error in errors:
        print("-", error)
    raise SystemExit(1)

print("local-event-stream-contract: ok")
