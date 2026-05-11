#!/usr/bin/env python3
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

PROJECTION_SCHEMAS = [
    "schemas/client-subject-ref.v1.schema.json",
    "schemas/client-connection-ref.v1.schema.json",
    "schemas/client-attachment-ref.v1.schema.json",
    "schemas/system-call-ref.v1.schema.json",
    "schemas/system-root-context-ref.v1.schema.json",
    "schemas/work-case-ref.v1.schema.json",
    "schemas/system-call-record.v1.schema.json",
    "schemas/work-case-binding.v1.schema.json",
]

ENVELOPE_SCHEMAS = [
    "schemas/request-envelope.v1.schema.json",
    "schemas/response-envelope.v1.schema.json",
    "schemas/readiness-envelope.v1.schema.json",
    "schemas/client-ref.v1.schema.json",
]

REQUEST_FIELDS = {
    "client_subject_ref",
    "client_connection_ref",
    "client_attachment_ref",
    "system_root_context_ref",
    "work_case_ref",
    "system_call_ref",
}

RESPONSE_FIELDS = REQUEST_FIELDS | {"control_admission_ref"}
READINESS_FIELDS = REQUEST_FIELDS


def fail(message: str) -> None:
    print(f"client-call-context-projection: FAIL: {message}")
    raise SystemExit(1)


def load_json(relpath: str) -> dict[str, Any]:
    path = ROOT / relpath
    if not path.exists():
        fail(f"missing required file: {relpath}")
    try:
        value = json.loads(path.read_text())
    except Exception as exc:
        fail(f"{relpath} is not valid JSON: {exc}")
    if not isinstance(value, dict):
        fail(f"{relpath} must contain a JSON object")
    return value


def require_projection_marker(schema: dict[str, Any], relpath: str) -> None:
    marker = schema.get("x-yai-projection")
    if not isinstance(marker, dict):
        fail(f"{relpath} must be marked as an API projection mirror")
    if marker.get("projection_role") != "api_schema_mirror":
        fail(f"{relpath} projection marker must use api_schema_mirror role")
    source = marker.get("source_of_truth")
    if not isinstance(source, str) or not source.startswith("../yai/protocols/"):
        fail(f"{relpath} projection marker must point at ../yai/protocols")


def require_fields(
    schema: dict[str, Any],
    fields: set[str],
    relpath: str,
    required_must_not_include: set[str],
) -> None:
    props = schema.get("properties", {})
    if not isinstance(props, dict):
        fail(f"{relpath} must define properties")
    required = set(schema.get("required", []))
    for field in fields:
        if field not in props:
            fail(f"{relpath} missing A5 call context field {field}")
        if field in required_must_not_include and field in required:
            fail(f"{relpath} must keep {field} optional")


def main() -> None:
    for relpath in PROJECTION_SCHEMAS:
        schema = load_json(relpath)
        require_projection_marker(schema, relpath)

    request = load_json("schemas/request-envelope.v1.schema.json")
    response = load_json("schemas/response-envelope.v1.schema.json")
    readiness = load_json("schemas/readiness-envelope.v1.schema.json")
    client_ref = load_json("schemas/client-ref.v1.schema.json")

    require_fields(request, REQUEST_FIELDS, "schemas/request-envelope.v1.schema.json", REQUEST_FIELDS)
    require_fields(response, RESPONSE_FIELDS, "schemas/response-envelope.v1.schema.json", RESPONSE_FIELDS)
    require_fields(readiness, READINESS_FIELDS, "schemas/readiness-envelope.v1.schema.json", READINESS_FIELDS)
    require_fields(
        client_ref,
        {"client_subject_ref", "client_connection_ref", "client_attachment_ref"},
        "schemas/client-ref.v1.schema.json",
        {"client_subject_ref", "client_connection_ref", "client_attachment_ref"},
    )

    system_root = request["properties"]["system_root_context_ref"]
    if system_root.get("default") != "root-context://system/default":
        fail("request-envelope system_root_context_ref must default to root-context://system/default")

    client_subject_schema = load_json("schemas/client-subject-ref.v1.schema.json")
    pattern = client_subject_schema.get("pattern")
    if not isinstance(pattern, str):
        fail("client-subject-ref schema must define a pattern")
    compiled = re.compile(pattern)
    for forbidden in (
        "case://root",
        "case://acme-inc/customer-onboarding",
        "principal://local-dev/operator",
        "session://legacy/default",
    ):
        if compiled.fullmatch(forbidden):
            fail(f"client_subject_ref accepts forbidden ref form: {forbidden}")

    request_required = set(request.get("required", []))
    if "work_case_ref" in request_required:
        fail("work_case_ref must not be required on every request")
    if "system_call_ref" in request_required:
        fail("system_call_ref must not be required before runtime admission/materialization")

    # system.status is the canonical no-work-case example for A5 projection.
    if "work_case_ref" in request_required:
        fail("system.status would incorrectly require work_case_ref")

    docs = {
        "Documentation/client/console-client-alignment.md": (ROOT / "Documentation/client/console-client-alignment.md").read_text(),
        "Documentation/operation-to-transport-mapping.md": (ROOT / "Documentation/operation-to-transport-mapping.md").read_text(),
        "Documentation/waves/a5-api-envelope-sdk-call-context-propagation.md": (
            ROOT / "Documentation/waves/a5-api-envelope-sdk-call-context-propagation.md"
        ).read_text(),
    }
    for relpath, text in docs.items():
        for fragment in (
            "A5 adds call-context projection fields to API envelopes.",
            "A5 does not implement runtime admission/materialization.",
        ):
            if fragment not in text:
                fail(f"{relpath} missing required A5 boundary fragment: {fragment}")

    console_doc = docs["Documentation/client/console-client-alignment.md"]
    if "YAI Console is the canonical terminal client." not in console_doc:
        fail("Console canonical naming must be preserved")
    if "Legacy CLI/Loom surfaces are compatibility names or historical references." not in console_doc:
        fail("CLI/Loom compatibility naming must be preserved")

    print("client-call-context-projection: ok")


if __name__ == "__main__":
    main()
