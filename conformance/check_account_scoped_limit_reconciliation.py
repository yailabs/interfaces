#!/usr/bin/env python3
"""Dependency-free conformance checks for V45 account limit reconciliation."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "account-scoped-limit-reconciliation.v1.schema.json"
FIXTURE_DIR = ROOT / "fixtures" / "account-scoped-limit-reconciliation"

EXPECTED_FIXTURES = {
    "account-limit-shared.json",
    "local-cache-stale.json",
    "multi-machine-limit-pressure.json",
    "conflict-requires-refresh.json",
    "offline-posture-limited.json",
    "safe-reconciliation-projection.json",
}

REQUIRED_STRING_FIELDS = (
    "account_limit_reconciliation_ref",
    "account_ref",
    "limit_key",
    "scope",
)

NUMERIC_FIELDS = {
    "account_global_usage",
    "local_observed_usage",
    "remote_observed_usage",
    "remaining",
    "max_allowed",
}

FORBIDDEN_KEYS = {
    "billing_customer",
    "stripe_customer",
    "subscription",
    "invoice",
    "price",
    "plan_object",
    "supabase_user",
    "provider_user",
    "raw_usage_ledger",
}

SECRET_KEYS = {
    "api_key",
    "token",
    "secret",
    "password",
    "private_key",
}

SAFE_PROJECTION_KEYS = {
    "account_ref",
    "limit_key",
    "scope",
    "reconciliation_status",
    "staleness_posture",
    "offline_posture",
    "cache_posture",
    "decision",
    "warning_codes",
    "expires_at",
}


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def schema_enums(schema: dict) -> dict[str, set[str]]:
    defs = schema["$defs"]
    return {
        "scope": set(defs["scope"]["enum"]),
        "limit_key": set(defs["limitKey"]["enum"]),
        "reconciliation_status": set(defs["reconciliationStatus"]["enum"]),
        "conflict_status": set(defs["conflictStatus"]["enum"]),
        "staleness_posture": set(defs["stalenessPosture"]["enum"]),
        "offline_posture": set(defs["offlinePosture"]["enum"]),
        "cache_posture": set(defs["cachePosture"]["enum"]),
        "decision": set(defs["decision"]["enum"]),
        "blocked_reason": set(defs["blockedReason"]["enum"]),
        "warning_codes": set(defs["warningCode"]["enum"]),
    }


def walk_keys(node: object, errors: list[str], path: str = "$") -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            if key in FORBIDDEN_KEYS:
                errors.append(f"{path}.{key}: forbidden billing/private/provider field")
            if key in SECRET_KEYS:
                errors.append(f"{path}.{key}: forbidden secret-like key")
            walk_keys(value, errors, f"{path}.{key}")
    elif isinstance(node, list):
        for index, value in enumerate(node):
            walk_keys(value, errors, f"{path}[{index}]")


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def validate_safe_projection(name: str, projection: object, enums: dict[str, set[str]], errors: list[str]) -> None:
    require(
        isinstance(projection, dict),
        f"{name}: safe_reconciliation_projection must be an object",
        errors,
    )
    if not isinstance(projection, dict):
        return

    extra = set(projection.keys()) - SAFE_PROJECTION_KEYS
    require(not extra, f"{name}: safe_reconciliation_projection has unsafe keys {sorted(extra)}", errors)

    value = projection.get("account_ref")
    require(
        isinstance(value, str) and value.strip(),
        f"{name}: safe_reconciliation_projection.account_ref must be non-empty",
        errors,
    )

    for field in (
        "limit_key",
        "scope",
        "reconciliation_status",
        "staleness_posture",
        "offline_posture",
        "cache_posture",
        "decision",
    ):
        value = projection.get(field)
        require(value in enums[field], f"{name}: unknown safe_reconciliation_projection {field} {value!r}", errors)

    if "warning_codes" in projection:
        require(
            isinstance(projection["warning_codes"], list),
            f"{name}: safe_reconciliation_projection.warning_codes must be a list",
            errors,
        )
        if isinstance(projection["warning_codes"], list):
            for code in projection["warning_codes"]:
                require(
                    code in enums["warning_codes"],
                    f"{name}: unknown safe_reconciliation_projection warning code {code!r}",
                    errors,
                )


def validate_fixture(name: str, payload: object, enums: dict[str, set[str]], errors: list[str]) -> None:
    require(isinstance(payload, dict), f"{name}: top-level JSON must be an object", errors)
    if not isinstance(payload, dict):
        return

    require(
        "account_limit_reconciliation" in payload,
        f"{name}: missing account_limit_reconciliation",
        errors,
    )
    reconciliation = payload.get("account_limit_reconciliation")
    require(
        isinstance(reconciliation, dict),
        f"{name}: account_limit_reconciliation must be an object",
        errors,
    )
    if not isinstance(reconciliation, dict):
        return

    for field in REQUIRED_STRING_FIELDS:
        value = reconciliation.get(field)
        require(isinstance(value, str) and value.strip(), f"{name}: {field} must be a non-empty string", errors)

    for field in (
        "limit_key",
        "scope",
        "reconciliation_status",
        "conflict_status",
        "staleness_posture",
        "offline_posture",
        "cache_posture",
        "decision",
    ):
        value = reconciliation.get(field)
        require(value in enums[field], f"{name}: unknown {field} {value!r}", errors)

    for field in NUMERIC_FIELDS:
        if field in reconciliation:
            value = reconciliation[field]
            require(
                not isinstance(value, bool) and isinstance(value, (int, float)),
                f"{name}: {field} must be numeric",
                errors,
            )

    if "blocked_reason" in reconciliation:
        value = reconciliation["blocked_reason"]
        require(value in enums["blocked_reason"], f"{name}: unknown blocked_reason {value!r}", errors)

    if "warning_codes" in reconciliation:
        require(isinstance(reconciliation["warning_codes"], list), f"{name}: warning_codes must be a list", errors)
        if isinstance(reconciliation["warning_codes"], list):
            for code in reconciliation["warning_codes"]:
                require(code in enums["warning_codes"], f"{name}: unknown warning code {code!r}", errors)

    if "safe_reconciliation_projection" in reconciliation:
        validate_safe_projection(name, reconciliation["safe_reconciliation_projection"], enums, errors)

    if reconciliation.get("decision") == "blocked":
        require("blocked_reason" in reconciliation, f"{name}: blocked decisions require blocked_reason", errors)

    if reconciliation.get("decision") == "warning":
        warning_codes = reconciliation.get("warning_codes")
        require(
            isinstance(warning_codes, list) and len(warning_codes) > 0,
            f"{name}: warning decisions require warning_codes",
            errors,
        )

    if name == "account-limit-shared.json":
        require(
            reconciliation.get("scope") == "account_global",
            f"{name}: shared account fixture must use scope account_global",
            errors,
        )

    walk_keys(payload, errors)


def main() -> int:
    errors: list[str] = []

    schema = load_json(SCHEMA_PATH)
    require(isinstance(schema, dict), "schema: must be a JSON object", errors)
    if not isinstance(schema, dict):
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    enums = schema_enums(schema)

    fixture_paths = sorted(FIXTURE_DIR.glob("*.json"))
    names = {path.name for path in fixture_paths}
    require(names == EXPECTED_FIXTURES, f"fixtures: expected {sorted(EXPECTED_FIXTURES)}, found {sorted(names)}", errors)

    for path in fixture_paths:
        payload = load_json(path)
        validate_fixture(path.name, payload, enums, errors)

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("account-scoped-limit-reconciliation: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
