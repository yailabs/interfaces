# SDK Consumption Boundary

SDK packages are typed consumption/projection surfaces for the canonical
developer interface.

SDK packages must not define protocol truth. They must not invent operation
identifiers, redefine envelope grammar, redefine transport grammar, create new
runtime dispatch semantics, or promote compatibility-only vocabulary into
protocol authority.

SDK packages may provide:

- typed clients;
- package-level transport bindings;
- language-native status and error wrappers;
- generated or hand-maintained constants that are traceable to protocol inputs;
- examples for consuming the canonical interface.

SDK package operation constants and envelope types are package projections
pending INTF.6 validation hardening.
