#!/usr/bin/env python3
from pathlib import Path


root = Path(__file__).resolve().parents[1]
in_process_root = root / "transports/in-process-test"
subprocess_root = root / "transports/subprocess-stdio-compat"

in_process_required = [
    root / "transports/in-process-test.v1.md",
    in_process_root / "README.md",
    in_process_root / "purpose.v1.md",
    in_process_root / "harness-boundary.v1.md",
    in_process_root / "conformance-usage.v1.md",
    in_process_root / "security-limitations.v1.md",
    in_process_root / "non-product-boundary.v1.md",
    in_process_root / "errors.v1.md",
    in_process_root / "conformance-profile.v1.md",
]
subprocess_required = [
    root / "transports/subprocess-stdio-compat.v1.md",
    subprocess_root / "README.md",
    subprocess_root / "purpose.v1.md",
    subprocess_root / "stdout-stderr-contract.v1.md",
    subprocess_root / "exit-status-model.v1.md",
    subprocess_root / "env-boundary.v1.md",
    subprocess_root / "security-limitations.v1.md",
    subprocess_root / "deprecation-policy.v1.md",
    subprocess_root / "errors.v1.md",
    subprocess_root / "conformance-profile.v1.md",
]
doc_required = [
    root / "Documentation/in-process-subprocess-compat-boundary.md",
]

errors = []
for path in in_process_required + subprocess_required + doc_required:
    if not path.exists():
        errors.append(f"missing required API.08 file: {path.relative_to(root)}")

in_process_text = "\n".join(path.read_text() for path in in_process_required if path.exists())
subprocess_text = "\n".join(path.read_text() for path in subprocess_required if path.exists())
doc_text = "\n".join(path.read_text() for path in doc_required if path.exists())
all_text = "\n".join((in_process_text, subprocess_text, doc_text))

in_process_needles = {
    "test-only": "in_process_test docs must say test-only",
    "non-product": "in_process_test docs must say non-product",
    "harness": "in_process_test docs must mention harness context",
    "guard": "in_process_test docs must require guards even in harness",
    "provider": "in_process_test docs must keep provider boundary separate",
}
for needle, message in in_process_needles.items():
    if needle not in in_process_text and needle not in doc_text:
        errors.append(message)

subprocess_needles = {
    "compat-only": "subprocess docs must say compat-only",
    "stdout": "subprocess docs must mention structured stdout",
    "stderr": "subprocess docs must mention stderr diagnostics",
    "exit status": "subprocess docs must mention exit-status separation",
    "environment": "subprocess docs must mention environment boundary",
    "not canonical": "subprocess docs must say not canonical",
    "Local IPC RPC": "subprocess docs must keep Local IPC RPC separate",
}
for needle, message in subprocess_needles.items():
    if needle not in subprocess_text and needle not in doc_text:
        errors.append(message)

for forbidden in (
    "in-process bridge implemented",
    "subprocess runner implemented",
    "stdout parser implemented",
    "SDK implements subprocess_stdio_compat",
    "SDK implements in_process_test",
    "subprocess is canonical",
    "in_process_test is product transport",
):
    if forbidden in all_text:
        errors.append(f"docs must not claim implementation or product posture: {forbidden}")

if errors:
    print("test-compat-transport-boundary: FAIL")
    for error in errors:
        print("-", error)
    raise SystemExit(1)

print("test-compat-transport-boundary: ok")
