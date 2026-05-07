#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
registry_file = root / "registry/api-operations.v1.json"
mapping_file = root / "mappings/operation-transport-map.v1.json"
schema_file = root / "mappings/operation-transport-map.v1.schema.json"

registry = json.loads(registry_file.read_text())
mapping = json.loads(mapping_file.read_text())
json.loads(schema_file.read_text())

expected_transports = [
    "local_ipc_rpc",
    "local_http_loopback",
    "local_event_stream",
    "lan_secure",
    "remote_https",
    "in_process_test",
    "subprocess_stdio_compat",
]
allowed_default_transports = {
    "local_ipc_rpc",
    "local_http_loopback",
    "local_event_stream",
    "remote_https",
    "none",
}
allowed_lan_exposure = {
    "blocked_by_default",
    "allowed_with_pairing",
    "not_applicable",
}
allowed_remote_exposure = {
    "local_only",
    "platform_boundary",
    "future_remote_capability",
    "not_applicable",
}
allowed_provider_boundary = {
    "excluded",
    "runtime_provider_only",
    "not_applicable",
}
allowed_dispatch_targets = {
    "runtime_boundary_api",
    "platform_remote_api",
    "sdk_local_only",
    "test_only",
    "compat_only",
    "not_implemented",
}
allowed_runtime_readiness = {
    "implemented",
    "partial",
    "planned",
    "not_implemented",
}
required_fields = {
    "operation_id",
    "family",
    "default_transport",
    "allowed_transports",
    "disallowed_transports",
    "streamable",
    "local_native_recommended",
    "browser_recommended",
    "lan_exposure",
    "remote_exposure",
    "provider_transport_boundary",
    "dispatch_target",
    "runtime_handler_readiness",
    "sdk_projection",
    "cli_projection",
    "tui_projection",
    "notes",
}

errors = []

if mapping.get("kind") != "yai.api.operation_transport_map":
    errors.append("mapping kind must be yai.api.operation_transport_map")
if mapping.get("version") != "v1":
    errors.append("mapping version must be v1")
if mapping.get("source_registry") != "registry/api-operations.v1.json":
    errors.append("mapping source_registry must point to registry/api-operations.v1.json")
if mapping.get("transport_classes") != expected_transports:
    errors.append("transport_classes must match the canonical API.01 transport list and order")

registry_ops = registry.get("operations", [])
registry_by_id = {op["operation_id"]: op for op in registry_ops}
entries = mapping.get("entries", [])
entry_by_id = {}
for entry in entries:
    opid = entry.get("operation_id")
    if opid in entry_by_id:
        errors.append(f"duplicate mapping entry for {opid}")
    else:
        entry_by_id[opid] = entry

if len(entries) != len(registry_ops):
    errors.append(f"mapping entry count {len(entries)} does not match registry operation count {len(registry_ops)}")

missing = sorted(set(registry_by_id) - set(entry_by_id))
extra = sorted(set(entry_by_id) - set(registry_by_id))
for opid in missing:
    errors.append(f"missing mapping entry for registry operation {opid}")
for opid in extra:
    errors.append(f"mapping entry has unknown operation_id {opid}")

for opid, op in registry_by_id.items():
    entry = entry_by_id.get(opid)
    if not entry:
        continue

    missing_fields = sorted(required_fields - set(entry))
    if missing_fields:
        errors.append(f"{opid}: missing fields {', '.join(missing_fields)}")
        continue

    if set(entry) != required_fields:
        extra_fields = sorted(set(entry) - required_fields)
        if extra_fields:
            errors.append(f"{opid}: unexpected fields {', '.join(extra_fields)}")

    if entry["family"] != op["family"]:
        errors.append(f"{opid}: family mismatch ({entry['family']} != {op['family']})")
    if entry["runtime_handler_readiness"] != op["runtime_handler_readiness"]:
        errors.append(f"{opid}: runtime_handler_readiness mismatch")
    if entry["sdk_projection"] != op["sdk_projection"]:
        errors.append(f"{opid}: sdk_projection mismatch")
    if entry["cli_projection"] != op["cli_projection"]:
        errors.append(f"{opid}: cli_projection mismatch")
    if entry["tui_projection"] != op["tui_projection"]:
        errors.append(f"{opid}: tui_projection mismatch")

    allowed = entry["allowed_transports"]
    disallowed = entry["disallowed_transports"]

    if entry["default_transport"] not in allowed_default_transports:
        errors.append(f"{opid}: invalid default_transport {entry['default_transport']}")
    if entry["lan_exposure"] not in allowed_lan_exposure:
        errors.append(f"{opid}: invalid lan_exposure {entry['lan_exposure']}")
    if entry["remote_exposure"] not in allowed_remote_exposure:
        errors.append(f"{opid}: invalid remote_exposure {entry['remote_exposure']}")
    if entry["provider_transport_boundary"] not in allowed_provider_boundary:
        errors.append(f"{opid}: invalid provider_transport_boundary {entry['provider_transport_boundary']}")
    if entry["dispatch_target"] not in allowed_dispatch_targets:
        errors.append(f"{opid}: invalid dispatch_target {entry['dispatch_target']}")
    if entry["runtime_handler_readiness"] not in allowed_runtime_readiness:
        errors.append(f"{opid}: invalid runtime_handler_readiness {entry['runtime_handler_readiness']}")

    if len(allowed) != len(set(allowed)):
        errors.append(f"{opid}: duplicate allowed_transports")
    if len(disallowed) != len(set(disallowed)):
        errors.append(f"{opid}: duplicate disallowed_transports")

    for transport in allowed + disallowed:
        if transport not in expected_transports:
            errors.append(f"{opid}: unknown transport {transport}")

    if "provider_transport_boundary" in allowed:
        errors.append(f"{opid}: provider_transport_boundary must never appear in allowed_transports")

    if entry["default_transport"] != "none" and entry["default_transport"] not in allowed:
        errors.append(f"{opid}: default transport {entry['default_transport']} not included in allowed_transports")

    expected_disallowed = sorted(set(expected_transports) - set(allowed))
    if sorted(disallowed) != expected_disallowed:
        errors.append(f"{opid}: disallowed_transports must be the complement of allowed_transports")

    if entry["provider_transport_boundary"] == "runtime_provider_only" and entry["dispatch_target"] != "runtime_boundary_api":
        errors.append(f"{opid}: runtime_provider_only is only valid for runtime_boundary_api dispatch")

    if entry["lan_exposure"] == "allowed_with_pairing" and "lan_secure" not in allowed:
        errors.append(f"{opid}: allowed_with_pairing requires lan_secure in allowed_transports")
    if entry["lan_exposure"] != "allowed_with_pairing" and "lan_secure" in allowed:
        errors.append(f"{opid}: lan_secure may only appear when lan_exposure is allowed_with_pairing")

    watchable = bool(op.get("watchable"))
    if bool(entry["streamable"]) != watchable:
        errors.append(f"{opid}: streamable must match registry watchable flag")
    if watchable:
        if entry["default_transport"] != "local_event_stream":
            errors.append(f"{opid}: watchable operations must default to local_event_stream")
        if "local_event_stream" not in allowed:
            errors.append(f"{opid}: watchable operations must allow local_event_stream")
        if "local_ipc_rpc" in allowed or "local_http_loopback" in allowed:
            errors.append(f"{opid}: watchable operations must not reuse generic request/response transports as canonical mapping")
    else:
        if "local_event_stream" in allowed:
            errors.append(f"{opid}: non-streamable operations must not allow local_event_stream")

    if op.get("projection_kind") == "high_level_composition":
        if entry["dispatch_target"] != "sdk_local_only":
            errors.append(f"{opid}: high-level composition operations must dispatch as sdk_local_only")
        if entry["default_transport"] != "none":
            errors.append(f"{opid}: high-level composition operations must default to none")
        if allowed:
            errors.append(f"{opid}: high-level composition operations must not declare direct client-runtime transports in API.02")

    if op["family"] in {"auth", "identity"}:
        if entry["dispatch_target"] != "platform_remote_api":
            errors.append(f"{opid}: auth/identity operations must dispatch to platform_remote_api")
        if entry["default_transport"] != "remote_https":
            errors.append(f"{opid}: auth/identity operations must default to remote_https")
        if "remote_https" not in allowed:
            errors.append(f"{opid}: auth/identity operations must allow remote_https")
        if entry["remote_exposure"] != "platform_boundary":
            errors.append(f"{opid}: auth/identity operations must be marked platform_boundary")
    elif "remote_https" in allowed or entry["default_transport"] == "remote_https":
        errors.append(f"{opid}: remote_https is reserved for platform boundary operations in the current registry")

    if op["family"] == "session":
        if entry["dispatch_target"] != "compat_only":
            errors.append(f"{opid}: session operations must remain compat_only in API.02")
        if entry["remote_exposure"] != "local_only":
            errors.append(f"{opid}: session compatibility operations must remain local_only")

if errors:
    print("operation-transport-map: FAIL")
    for error in errors:
        print("-", error)
    raise SystemExit(1)

print("operation-transport-map: ok")
