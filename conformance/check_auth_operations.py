#!/usr/bin/env python3
"""Dependency-free V53 conformance checks for canonical auth operations."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"
SCHEMA_PATH = ROOT / "schemas" / "auth-operation.v1.schema.json"
FIXTURE_DIR = ROOT / "fixtures" / "auth-operation"

EXPECTED_FIXTURES = {
    "auth-login-unavailable.json",
    "auth-login-local-dev.json",
    "auth-status-unauthenticated.json",
    "auth-status-local-dev.json",
    "auth-logout-clears-auth-only.json",
    "auth-context-inspect-safe.json",
    "auth-provider-status-not-configured.json",
    "auth-device-login-start-contract.json",
}

REQUIRED_AUTH_OPS = {
    "auth.login",
    "auth.login.local_dev",
    "auth.status",
    "auth.logout",
    "auth.context.inspect",
    "auth.provider.status",
    "auth.device_login.start",
    "auth.device_login.status",
    "auth.device_login.cancel",
}

ACTION_TO_OPERATION = {
    "auth.login": "auth.login",
    "auth.login.local_dev": "auth.login.local_dev",
    "auth.status": "auth.status",
    "auth.logout": "auth.logout",
    "auth.context.inspect": "auth.context.inspect",
    "auth.provider.status": "auth.provider.status",
    "auth.device_login.start": "auth.device_login.start",
    "auth.device_login.status": "auth.device_login.status",
    "auth.device_login.cancel": "auth.device_login.cancel",
}

REQUEST_KINDS = {
    "login",
    "login_local_dev",
    "status",
    "logout",
    "context_inspect",
    "provider_status",
    "device_login_start",
    "device_login_status",
    "device_login_cancel",
}

OPERATION_STATUSES = {
    "allowed",
    "blocked",
    "unavailable",
    "not_implemented",
    "legacy_alias",
    "forbidden",
}

AUTH_POSTURES = {
    "authenticated",
    "unauthenticated",
    "local_dev_authenticated",
    "expired",
    "revoked",
    "unavailable",
    "unknown",
}

PROVIDER_POSTURES = {
    "not_configured",
    "configured",
    "unavailable",
    "provider_session_present",
    "provider_session_absent",
    "unknown",
}

AUTH_CONTEXT_POSTURES = {
    "present",
    "missing",
    "expired",
    "revoked",
    "refresh_required",
    "not_issued",
    "unknown",
}

SAFE_PROJECTION_FIELDS = {
    "action_id",
    "operation_status",
    "auth_posture",
    "provider_posture",
    "auth_context_posture",
    "principal_ref",
    "account_ref",
    "auth_context_ref",
    "reason",
    "next_action",
}

FORBIDDEN_KEYS = {
    "session_ref",
    "session_id",
    "session_owner",
    "provider_user",
    "supabase_user",
    "authjs_session",
    "clerk_user",
    "oauth_token",
    "refresh_token",
    "access_token",
    "id_token",
    "provider_secret",
    "client_secret",
    "private_key",
    "api_key",
    "billing_customer",
    "subscription",
    "invoice",
    "price",
}

AUTH_SCHEMA = "schemas/auth-operation.v1.schema.json"


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def scan_forbidden_keys(name: str, node: object, errors: list[str]) -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            require(key not in FORBIDDEN_KEYS, f"{name}: forbidden key present: {key}", errors)
            scan_forbidden_keys(name, value, errors)
    elif isinstance(node, list):
        for value in node:
            scan_forbidden_keys(name, value, errors)


def validate_fixture(name: str, payload: object, errors: list[str]) -> None:
    require(isinstance(payload, dict), f"{name}: top-level JSON must be an object", errors)
    if not isinstance(payload, dict):
        return

    scan_forbidden_keys(name, payload, errors)

    require("auth_operation" in payload, f"{name}: missing auth_operation", errors)
    operation = payload.get("auth_operation")
    require(isinstance(operation, dict), f"{name}: auth_operation must be an object", errors)
    if not isinstance(operation, dict):
        return

    for field in (
        "operation_id",
        "action_id",
        "request_kind",
        "operation_status",
        "auth_posture",
        "provider_posture",
        "auth_context_posture",
        "safe_projection",
    ):
        require(field in operation, f"{name}: missing {field}", errors)

    opid = operation.get("operation_id")
    action_id = operation.get("action_id")
    request_kind = operation.get("request_kind")
    operation_status = operation.get("operation_status")
    auth_posture = operation.get("auth_posture")
    provider_posture = operation.get("provider_posture")
    auth_context_posture = operation.get("auth_context_posture")

    require(isinstance(opid, str) and opid.startswith("auth."), f"{name}: operation_id must start with auth.", errors)
    require(isinstance(action_id, str) and action_id.startswith("auth."), f"{name}: action_id must start with auth.", errors)
    require(request_kind in REQUEST_KINDS, f"{name}: unknown request_kind {request_kind!r}", errors)
    require(operation_status in OPERATION_STATUSES, f"{name}: unknown operation_status {operation_status!r}", errors)
    require(auth_posture in AUTH_POSTURES, f"{name}: unknown auth_posture {auth_posture!r}", errors)
    require(provider_posture in PROVIDER_POSTURES, f"{name}: unknown provider_posture {provider_posture!r}", errors)
    require(
        auth_context_posture in AUTH_CONTEXT_POSTURES,
        f"{name}: unknown auth_context_posture {auth_context_posture!r}",
        errors,
    )

    safe_projection = operation.get("safe_projection")
    require(isinstance(safe_projection, dict), f"{name}: safe_projection must be an object", errors)
    if isinstance(safe_projection, dict):
        extra = sorted(set(safe_projection) - SAFE_PROJECTION_FIELDS)
        require(not extra, f"{name}: safe_projection contains unsafe fields: {extra}", errors)
        for field in (
            "action_id",
            "operation_status",
            "auth_posture",
            "provider_posture",
            "auth_context_posture",
        ):
            require(field in safe_projection, f"{name}: safe_projection missing {field}", errors)
        if isinstance(action_id, str):
            require(
                safe_projection.get("action_id") == action_id,
                f"{name}: safe_projection.action_id must match action_id",
                errors,
            )
        if operation_status in OPERATION_STATUSES:
            require(
                safe_projection.get("operation_status") == operation_status,
                f"{name}: safe_projection.operation_status must match operation_status",
                errors,
            )
        if auth_posture in AUTH_POSTURES:
            require(
                safe_projection.get("auth_posture") == auth_posture,
                f"{name}: safe_projection.auth_posture must match auth_posture",
                errors,
            )
        if provider_posture in PROVIDER_POSTURES:
            require(
                safe_projection.get("provider_posture") == provider_posture,
                f"{name}: safe_projection.provider_posture must match provider_posture",
                errors,
            )
        if auth_context_posture in AUTH_CONTEXT_POSTURES:
            require(
                safe_projection.get("auth_context_posture") == auth_context_posture,
                f"{name}: safe_projection.auth_context_posture must match auth_context_posture",
                errors,
            )

    if name == "auth-login-local-dev.json":
        require(request_kind == "login_local_dev", f"{name}: local-dev fixture must use login_local_dev", errors)
        require(auth_posture == "local_dev_authenticated", f"{name}: local-dev fixture must be local_dev_authenticated", errors)
        value = operation.get("local_dev_principal_ref")
        require(isinstance(value, str) and value.strip(), f"{name}: local_dev_principal_ref must be non-empty", errors)

    if name == "auth-logout-clears-auth-only.json":
        text = json.dumps(operation, sort_keys=True)
        for forbidden_phrase in (
            "runtime.stop",
            "case.delete",
            "evidence.delete",
            "knowledge.delete",
            "records.delete",
            "license revoke",
            "lease revoke",
            "machine revoke",
        ):
            require(forbidden_phrase not in text, f"{name}: logout fixture must not imply {forbidden_phrase}", errors)


def main() -> int:
    errors: list[str] = []

    schema = load_json(SCHEMA_PATH)
    require(isinstance(schema, dict), "schema: top-level schema must be an object", errors)
    if isinstance(schema, dict):
        require(schema.get("$id") == "https://yai.dev/schemas/auth-operation.v1.schema.json", "schema: unexpected $id", errors)
        require("auth_operation" in schema.get("properties", {}), "schema: missing auth_operation property", errors)

    fixtures = {path.name for path in FIXTURE_DIR.glob("*.json")}
    require(fixtures == EXPECTED_FIXTURES, f"fixtures: expected {sorted(EXPECTED_FIXTURES)}, found {sorted(fixtures)}", errors)

    operations_doc = load_json(REGISTRY / "api-operations.v1.json")
    surfaces_doc = load_json(REGISTRY / "api-surfaces.v1.json")
    projections_doc = load_json(REGISTRY / "api-operation-projections.v1.json")
    actions_doc = load_json(REGISTRY / "yai-actions.v1.json")

    if isinstance(operations_doc, dict):
        operation_rows = {row["operation_id"]: row for row in operations_doc.get("operations", [])}
        for opid in REQUIRED_AUTH_OPS | {"auth.whoami"}:
            row = operation_rows.get(opid)
            require(row is not None, f"registry: missing auth operation {opid}", errors)
            if row is None:
                continue
            require(row.get("family") == "auth", f"registry: {opid} must stay in auth family", errors)
            require(row.get("output_schema") == AUTH_SCHEMA, f"registry: {opid} must use {AUTH_SCHEMA}", errors)
            require(row.get("governance_required") is False, f"registry: {opid} must not require governance", errors)
            require(row.get("records_emitted") is False, f"registry: {opid} must not emit records", errors)
            require(row.get("conversation_bound") is False, f"registry: {opid} must not be conversation-bound", errors)
        for opid in REQUIRED_AUTH_OPS:
            row = operation_rows.get(opid)
            if row is None:
                continue
            require(row.get("status") == "seed", f"registry: {opid} must stay seed in V53", errors)
        whoami_row = operation_rows.get("auth.whoami")
        if whoami_row is not None:
            require(whoami_row.get("status") in {"legacy", "deprecated"}, "registry: auth.whoami must be legacy/deprecated", errors)
        for opid, row in operation_rows.items():
            if row.get("family") == "session":
                text = json.dumps(row, sort_keys=True)
                for token in ("auth.login", "auth.logout", "auth.status", "auth.context", "device_login", "provider.status"):
                    require(token not in text, f"registry: session operation must not own auth semantics: {opid}", errors)

    if isinstance(surfaces_doc, dict):
        auth_surface = set(surfaces_doc.get("surfaces", {}).get("auth", []))
        for projection in (
            "login",
            "login.local_dev",
            "status",
            "logout",
            "context.inspect",
            "provider.status",
            "device_login.start",
            "device_login.status",
            "device_login.cancel",
        ):
            require(projection in auth_surface, f"surfaces: auth surface missing {projection}", errors)

    if isinstance(projections_doc, dict):
        aliases = {row.get("alias"): row for row in projections_doc.get("legacy_alias_mappings", [])}
        require("auth.whoami" in aliases, "projections: missing auth.whoami legacy alias", errors)
        if "auth.whoami" in aliases:
            require(
                aliases["auth.whoami"].get("canonical_operation_id") == "auth.context.inspect",
                "projections: auth.whoami must map to auth.context.inspect",
                errors,
            )

    if isinstance(actions_doc, dict):
        action_rows = {row["action_id"]: row for row in actions_doc.get("actions", [])}
        for action_id, opid in ACTION_TO_OPERATION.items():
            row = action_rows.get(action_id)
            require(row is not None, f"yai-actions: missing {action_id}", errors)
            if row is None:
                continue
            require(row.get("api_operation_candidate") == opid, f"yai-actions: {action_id} must map to {opid}", errors)

    for fixture_name in sorted(EXPECTED_FIXTURES):
        validate_fixture(fixture_name, load_json(FIXTURE_DIR / fixture_name), errors)

    if errors:
        print("auth-operations: FAIL")
        for error in errors:
            print("-", error)
        return 1

    print("auth-operations: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
