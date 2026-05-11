# Package Release Model

SDK package releases are independent language package releases. They do not
replace protocol version.

Each package release should record:

- package version;
- supported protocol version;
- supported generated surface version when generated outputs are included;
- supported conformance profile version;
- repository release or source commit;
- compatibility aliases or deprecations.

Package release notes must state whether the package contains protocol-aligned
changes, language-only ergonomics, generated output refreshes, or compatibility
cleanup.
