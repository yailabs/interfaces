#!/usr/bin/env python3
from pathlib import Path


root = Path(__file__).resolve().parents[1]
contract_root = root / "transports/local-http-loopback"

required_files = [
    root / "transports/local-http-loopback.v1.md",
    contract_root / "README.md",
    contract_root / "discovery.v1.md",
    contract_root / "route-model.v1.md",
    contract_root / "request-response.v1.md",
    contract_root / "headers.v1.md",
    contract_root / "origin-cors-policy.v1.md",
    contract_root / "local-client-token.v1.md",
    contract_root / "security.v1.md",
    contract_root / "errors.v1.md",
    contract_root / "platform-bindings.v1.md",
    contract_root / "conformance-profile.v1.md",
    root / "Documentation/local-http-loopback-contract.md",
]

errors = []
for path in required_files:
    if not path.exists():
        errors.append(f"missing required Local HTTP Loopback contract file: {path.relative_to(root)}")

doc_text = "\n".join(path.read_text() for path in required_files if path.suffix == ".md" and path.exists())

required_mentions = {
    "127.0.0.1": "docs must mention 127.0.0.1",
    "::1": "docs must mention ::1",
    "localhost": "docs must mention localhost",
    "loopback": "docs must define loopback posture",
    "no LAN": "docs must require no-LAN posture",
    "CORS": "docs must mention CORS posture",
    "origin": "docs must mention origin posture",
    "token": "docs must mention local token posture",
    "API.03": "docs must mention API.03 request/response envelope carriage",
    "transport": "docs must mention transport error posture",
    "operation": "docs must mention operation error posture",
}
for needle, message in required_mentions.items():
    if needle not in doc_text:
        errors.append(message)

required_phrases = (
    "no wildcard CORS",
    "application/json",
    "request envelopes",
    "response envelopes",
)
for phrase in required_phrases:
    if phrase not in doc_text:
        errors.append(f"docs must mention {phrase}")

forbidden_claims = (
    "HTTP server implemented",
    "router implemented",
    "CORS middleware implemented",
    "SDK implements local_http_loopback",
    "dashboard defaults switched",
    "provider transport is local_http_loopback",
)
for forbidden in forbidden_claims:
    if forbidden in doc_text:
        errors.append(f"docs must not claim implementation ownership: {forbidden}")

if errors:
    print("local-http-loopback-contract: FAIL")
    for error in errors:
        print("-", error)
    raise SystemExit(1)

print("local-http-loopback-contract: ok")
