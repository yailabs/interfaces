# External Client Authoring

External clients consume YAI through the canonical interface layer:

```text
external client or Console or future Studio
  -> interfaces SDK/API
  -> yai runtime/system effect
```

Client authors should start from protocol docs, select a supported transport,
use an official SDK package when available, and check package compatibility and
conformance status before relying on generated or package-specific helpers.
