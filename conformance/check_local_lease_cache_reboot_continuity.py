#!/usr/bin/env python3
"""Dependency-free conformance checks for V44 local lease cache continuity."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "local-lease-cache-reboot-continuity.v1.schema.json"
FIXTURE_DIR = ROOT / "fixtures" / "local-lease-cache-reboot-continuity"

EXPECTED_FIXTURES = {
    "valid-cache-after-reboot.json",
    "stale-cache-requires-refresh.json",
    "expired-cache-blocked.json",
    "revoked-cache-invalidated.json",
    "terminal-close-continuity.json",
    "safe-cache-projection.json",
}

REQUIRED_STRING_FIELDS = (
    "local_lease_cache_ref",
    "license_lease_ref",
)

FORBIDDEN_KEYS = {
    "billing_customer",
    "stripe_customer",
    "subscription",
    "invoice",
    "price",
    "plan_object",
    "supabase_user",
    "provider_user",
}

SECRET_KEYS = {
    "api_key",
    "token",
    "secret",
    "password",
    "private_key",
}

SAFE_PROJECTION_KEYS = {
    "license_lease_ref",
    "cache_status",
    "continuity_status",
    "reboot_posture",
    "offline_grace_posture",
    "stale_posture",
    "refresh_required_posture",
    "expires_at",
    "warning_codes",
}


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def schema_enums(schema: dict) -> dict[str, set[str]]:
    defs = schema["$defs"]
    return {
        "cache_status": set(defs["cacheStatus"]["enum"]),
        "continuity_status": set(defs["continuityStatus"]["enum"]),
        "reboot_posture": set(defs["rebootPosture"]["enum"]),
        "terminal_close_posture": set(defs["terminalClosePosture"]["enum"]),
        "runtime_restart_posture": set(defs["runtimeRestartPosture"]["enum"]),
        "offline_grace_posture": set(defs["offlineGracePosture"]["enum"]),
        "stale_posture": set(defs["stalePosture"]["enum"]),
        "refresh_required_posture": set(defs["refreshRequiredPosture"]["enum"]),
        "invalidation_posture": set(defs["invalidationPosture"]["enum"]),
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
    require(isinstance(projection, dict), f"{name}: safe_cache_projection must be an object", errors)
    if not isinstance(projection, dict):
        return

    extra = set(projection.keys()) - SAFE_PROJECTION_KEYS
    require(not extra, f"{name}: safe_cache_projection has unsafe keys {sorted(extra)}", errors)

    value = projection.get("license_lease_ref")
    require(
        isinstance(value, str) and value.strip(),
        f"{name}: safe_cache_projection.license_lease_ref must be non-empty",
        errors,
    )

    for field in (
        "cache_status",
        "continuity_status",
        "reboot_posture",
        "offline_grace_posture",
        "stale_posture",
        "refresh_required_posture",
    ):
        value = projection.get(field)
        require(value in enums[field], f"{name}: unknown safe_cache_projection {field} {value!r}", errors)

    if "warning_codes" in projection:
        require(isinstance(projection["warning_codes"], list), f"{name}: safe_cache_projection.warning_codes must be a list", errors)
        if isinstance(projection["warning_codes"], list):
            for code in projection["warning_codes"]:
                require(code in enums["warning_codes"], f"{name}: unknown safe_cache_projection warning code {code!r}", errors)


def validate_fixture(name: str, payload: object, enums: dict[str, set[str]], errors: list[str]) -> None:
    require(isinstance(payload, dict), f"{name}: top-level JSON must be an object", errors)
    if not isinstance(payload, dict):
        return

    require("local_lease_cache" in payload, f"{name}: missing local_lease_cache", errors)
    cache = payload.get("local_lease_cache")
    require(isinstance(cache, dict), f"{name}: local_lease_cache must be an object", errors)
    if not isinstance(cache, dict):
        return

    for field in REQUIRED_STRING_FIELDS:
        value = cache.get(field)
        require(isinstance(value, str) and value.strip(), f"{name}: {field} must be a non-empty string", errors)

    for field in (
        "cache_status",
        "continuity_status",
        "reboot_posture",
        "terminal_close_posture",
        "runtime_restart_posture",
        "offline_grace_posture",
        "stale_posture",
        "refresh_required_posture",
        "invalidation_posture",
    ):
        value = cache.get(field)
        require(value in enums[field], f"{name}: unknown {field} {value!r}", errors)

    if "blocked_reason" in cache:
        value = cache["blocked_reason"]
        require(value in enums["blocked_reason"], f"{name}: unknown blocked_reason {value!r}", errors)

    if "warning_codes" in cache:
        require(isinstance(cache["warning_codes"], list), f"{name}: warning_codes must be a list", errors)
        if isinstance(cache["warning_codes"], list):
            for code in cache["warning_codes"]:
                require(code in enums["warning_codes"], f"{name}: unknown warning code {code!r}", errors)

    if "safe_cache_projection" in cache:
        validate_safe_projection(name, cache["safe_cache_projection"], enums, errors)

    walk_keys(payload, errors)

    invalidated = cache.get("invalidation_posture") != "not_invalidated"
    blocked = cache.get("continuity_status") == "continuity_blocked" or cache.get("cache_status") in {
        "cache_corrupt",
        "cache_expired",
        "cache_revoked",
        "cache_invalidated",
    }
    if blocked or invalidated:
        require("blocked_reason" in cache, f"{name}: blocked or invalidated posture requires blocked_reason", errors)


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

    print("local-lease-cache-reboot-continuity: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
