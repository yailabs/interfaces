# Command Projection Model

Command-like UX (Console, legacy CLI/TUI, GUI) is a projection over canonical API operations.

Projection ownership:
- API: operation grammar and composition metadata
- SDK: typed clients generated later
- Console: canonical terminal presentation/rendering and interaction
- legacy CLI/Loom: compatibility presentation names, not separate canonical clients
- runtime: operation handler implementation only
