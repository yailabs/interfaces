# Command Projection Model

Command-like UX (CLI/TUI/GUI) is a projection over canonical API operations.

Projection ownership:
- API: operation grammar and composition metadata
- SDK: typed clients generated later
- CLI/Loom: presentation/rendering and interaction
- runtime: operation handler implementation only
