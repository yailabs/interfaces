# Python SDK Package

Enterprise package for Python consumers of YAI SDK contracts.

This package lives in `interfaces/packages/python`. It preserves distribution
name `yailabs-yai-sdk` and import name `yai_sdk`. It is an official SDK package
projection over YAI Interfaces protocol truth; it does not define protocol
truth.

INTF.4 validation: compile passed. `pytest` found 0 tests and exited 5, which
is classified as no-tests-discovered rather than a package failure.

Validation:
```sh
python3 -m py_compile src/yai_sdk/*.py src/yai_sdk/families/*.py
```
