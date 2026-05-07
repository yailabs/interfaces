#!/usr/bin/env python3
import json
from pathlib import Path


def load_json(path: Path):
    return json.loads(path.read_text())


root = Path(__file__).resolve().parents[1]

schema_paths = {
    "envelope": root / "schemas/envelope.v1.schema.json",
    "request": root / "schemas/request-envelope.v1.schema.json",
    "response": root / "schemas/response-envelope.v1.schema.json",
    "error": root / "schemas/error.v1.schema.json",
    "operation_result": root / "schemas/operation-result.v1.schema.json",
    "readiness": root / "schemas/readiness-envelope.v1.schema.json",
    "watch_event": root / "schemas/watch-event.v1.schema.json",
}
registry_paths = {
    "api_envelopes": root / "registry/api-envelopes.v1.json",
    "api_errors": root / "registry/api-errors.v1.json",
    "api_operations": root / "registry/api-operations.v1.json",
    "transport_map": root / "mappings/operation-transport-map.v1.json",
}
error_paths = {
    "error_code_registry": root / "errors/error-code-registry.v1.json",
    "error_http_status_map": root / "errors/error-http-status-map.v1.json",
}

schemas = {name: load_json(path) for name, path in schema_paths.items()}
registries = {name: load_json(path) for name, path in registry_paths.items()}
error_docs = {name: load_json(path) for name, path in error_paths.items()}

errors = []

request_required = set(schemas["request"].get("required", []))
for field in ("operation_id", "request_id"):
    if field not in request_required:
        errors.append(f"request-envelope schema must require {field}")

response_required = set(schemas["response"].get("required", []))
if "status" not in response_required:
    errors.append("response-envelope schema must require status")
response_props = schemas["response"].get("properties", {})
if "result" not in response_props:
    errors.append("response-envelope schema must define result")
if "error" not in response_props:
    errors.append("response-envelope schema must define error")
if not schemas["response"].get("oneOf"):
    errors.append("response-envelope schema must encode terminal result/error exclusivity")
if registries["api_envelopes"].get("response", {}).get("terminal_payload_rule") != "exactly_one_of_result_or_error":
    errors.append("api-envelopes registry must record the terminal result/error rule")

watch_required = set(schemas["watch_event"].get("required", []))
for field in (
    "stream_id",
    "event_id",
    "operation_id",
    "request_id",
    "sequence",
    "event_type",
    "created_at",
):
    if field not in watch_required:
        errors.append(f"watch-event schema must require {field}")

required_event_types = {
    "stream.open",
    "stream.heartbeat",
    "stream.data",
    "stream.warning",
    "stream.error",
    "stream.cancelled",
    "stream.closed",
}
event_type_enum = set(
    schemas["watch_event"].get("properties", {}).get("event_type", {}).get("enum", [])
)
if event_type_enum != required_event_types:
    errors.append("watch-event schema must expose the canonical stream event type set")

error_required = set(schemas["error"].get("required", []))
if not {"code", "message", "category"}.issubset(error_required):
    errors.append("error schema must require code, message, and category")

error_registry = error_docs["error_code_registry"]
api_error_registry = registries["api_errors"]
error_http_map = error_docs["error_http_status_map"]

if error_registry.get("kind") != "yai.api.error_code_registry":
    errors.append("error-code registry kind must be yai.api.error_code_registry")
if api_error_registry.get("kind") != "yai.api.error_registry":
    errors.append("api-errors registry kind must be yai.api.error_registry")
if error_http_map.get("kind") != "yai.api.error_http_status_map":
    errors.append("error-http-status map kind must be yai.api.error_http_status_map")

schema_error_codes = set(schemas["error"].get("properties", {}).get("code", {}).get("enum", []))
schema_categories = set(schemas["error"].get("properties", {}).get("category", {}).get("enum", []))
registry_error_codes = set(api_error_registry.get("errors", []))
registry_categories = set(api_error_registry.get("categories", []))
doc_error_codes = {entry["code"] for entry in error_registry.get("errors", [])}
doc_categories = set(error_registry.get("categories", []))
http_codes = {entry["code"] for entry in error_http_map.get("mapping", [])}

if schema_error_codes != registry_error_codes:
    errors.append("error schema codes must align with registry/api-errors.v1.json")
if schema_error_codes != doc_error_codes:
    errors.append("error schema codes must align with errors/error-code-registry.v1.json")
if schema_error_codes != http_codes:
    errors.append("error-http-status map must cover the full API error code set")
if schema_categories != registry_categories:
    errors.append("error schema categories must align with registry/api-errors.v1.json")
if schema_categories != doc_categories:
    errors.append("error schema categories must align with errors/error-code-registry.v1.json")

base_transport_enum = set(
    schemas["envelope"]
    .get("properties", {})
    .get("transport", {})
    .get("properties", {})
    .get("transport_class", {})
    .get("enum", [])
)
request_transport_enum = set(
    schemas["request"]
    .get("properties", {})
    .get("transport", {})
    .get("properties", {})
    .get("transport_class", {})
    .get("enum", [])
)
response_transport_enum = set(
    schemas["response"]
    .get("properties", {})
    .get("transport", {})
    .get("properties", {})
    .get("transport_class", {})
    .get("enum", [])
)
stream_ref_enum = set(
    schemas["response"]
    .get("properties", {})
    .get("stream_ref", {})
    .get("properties", {})
    .get("event_transport", {})
    .get("enum", [])
)

for enum_name, values in (
    ("base envelope transport", base_transport_enum),
    ("request envelope transport", request_transport_enum),
    ("response envelope transport", response_transport_enum),
    ("response stream_ref transport", stream_ref_enum),
):
    if "provider_transport_boundary" in values:
        errors.append(f"{enum_name} must not include provider_transport_boundary")

if "local_event_stream" in request_transport_enum or "local_event_stream" in response_transport_enum:
    errors.append("request/response envelope transports must not treat local_event_stream as a generic envelope carrier")
if "local_event_stream" not in stream_ref_enum:
    errors.append("response stream_ref transport enum must include local_event_stream")

transport_map = registries["transport_map"]
registry_ops = {
    op["operation_id"]: op for op in registries["api_operations"].get("operations", [])
}
for entry in transport_map.get("entries", []):
    opid = entry.get("operation_id")
    allowed = entry.get("allowed_transports", [])
    default_transport = entry.get("default_transport")
    streamable = bool(entry.get("streamable"))

    if "provider_transport_boundary" in allowed or default_transport == "provider_transport_boundary":
        errors.append(f"{opid}: provider_transport_boundary must never be used as an API envelope transport")

    if "local_event_stream" in allowed or default_transport == "local_event_stream":
        op = registry_ops.get(opid)
        if not streamable:
            errors.append(f"{opid}: local_event_stream mapping requires streamable true")
        if not op:
            errors.append(f"{opid}: missing registry operation for stream mapping validation")
            continue
        if not op.get("watchable"):
            errors.append(f"{opid}: local_event_stream mapping requires registry watchable true")
        if op.get("output_schema") != "schemas/watch-event.v1.schema.json":
            errors.append(f"{opid}: local_event_stream mapping requires watch-event output schema")
    elif streamable:
        errors.append(f"{opid}: streamable operations must carry local_event_stream in API.03")

for path in schema_paths.values():
    raw = path.read_text()
    for forbidden in (
        "runtime/boundary/api",
        "API implements",
        "listener",
        "server implementation",
    ):
        if forbidden in raw:
            errors.append(f"{path.name}: schema must not claim runtime implementation ownership ({forbidden})")

if errors:
    print("api-envelope-error-stream: FAIL")
    for error in errors:
        print("-", error)
    raise SystemExit(1)

print("api-envelope-error-stream: ok")
