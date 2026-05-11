#!/usr/bin/env python3
from pathlib import Path


root = Path(__file__).resolve().parents[1]
lan_root = root / "transports/lan-secure"
remote_root = root / "transports/remote-https"
provider_doc = root.parent / "yai/providers/transport/README.md"

lan_required = [
    root / "transports/lan-secure.v1.md",
    lan_root / "README.md",
    lan_root / "pairing.v1.md",
    lan_root / "discovery.v1.md",
    lan_root / "endpoint-binding.v1.md",
    lan_root / "security.v1.md",
    lan_root / "device-allowlist.v1.md",
    lan_root / "revocation.v1.md",
    lan_root / "operation-exposure.v1.md",
    lan_root / "errors.v1.md",
    lan_root / "conformance-profile.v1.md",
]
remote_required = [
    root / "transports/remote-https.v1.md",
    remote_root / "README.md",
    remote_root / "platform-boundary.v1.md",
    remote_root / "account-auth-boundary.v1.md",
    remote_root / "machine-license-boundary.v1.md",
    remote_root / "release-update-boundary.v1.md",
    remote_root / "future-hosted-capability-boundary.v1.md",
    remote_root / "security.v1.md",
    remote_root / "errors.v1.md",
    remote_root / "conformance-profile.v1.md",
]
doc_required = [
    root / "Documentation/lan-secure-remote-https-boundary.md",
]

errors = []
for path in lan_required + remote_required + doc_required:
    if not path.exists():
        errors.append(f"missing required boundary file: {path.relative_to(root)}")

lan_text = "\n".join(path.read_text() for path in lan_required if path.exists())
remote_text = "\n".join(path.read_text() for path in remote_required if path.exists())
doc_text = "\n".join(path.read_text() for path in doc_required if path.exists())
provider_text = provider_doc.read_text() if provider_doc.exists() else ""
all_text = "\n".join((lan_text, remote_text, doc_text, provider_text))

lan_needles = {
    "disabled by default": "LAN docs must say disabled by default",
    "0.0.0.0": "LAN docs must prohibit automatic 0.0.0.0",
    "pairing": "LAN docs must require pairing",
    "allowlist": "LAN docs must require device allowlist",
    "revocation": "LAN docs must require revocation",
    "TLS": "LAN docs must mention TLS or equivalent secure channel",
    "Local HTTP Loopback": "LAN docs must say Local HTTP Loopback is not LAN",
}
for needle, message in lan_needles.items():
    if needle not in lan_text and needle not in doc_text:
        errors.append(message)

remote_needles = {
    "platform": "Remote HTTPS docs must state platform boundary",
    "account": "Remote HTTPS docs must state account boundary",
    "update": "Remote HTTPS docs must state update boundary",
    "future capability": "Remote HTTPS docs must state future capability boundary",
    "not default local runtime execution": "Remote HTTPS docs must say it is not default local runtime execution",
    "not provider/model transport": "Remote HTTPS docs must say it is not provider/model transport",
}
for needle, message in remote_needles.items():
    if needle not in remote_text and needle not in doc_text:
        errors.append(message)

if "provider HTTP APIs are provider/model transport, not YAI Remote HTTPS" not in provider_text:
    errors.append("provider transport docs must state provider HTTP APIs are not YAI Remote HTTPS")

for forbidden in (
    "LAN listener implemented",
    "pairing implemented",
    "Remote HTTPS client implemented",
    "hosted compute implemented",
    "LAN enabled by default",
):
    if forbidden in all_text:
        errors.append(f"docs must not claim implementation or unsafe posture: {forbidden}")

if errors:
    print("lan-remote-boundary: FAIL")
    for error in errors:
        print("-", error)
    raise SystemExit(1)

print("lan-remote-boundary: ok")
