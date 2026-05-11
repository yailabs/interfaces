# Local Runtime Connection

Local runtime connection examples must use the transport contracts documented in
YAI Interfaces. They may show SDK usage, but SDK examples remain package
projections over protocol truth.

The expected flow is:

```text
external client or Console or future Studio
  -> interfaces SDK/API
  -> yai runtime/system effect
```

Runtime listener implementation and lifecycle behavior remain outside this
repository.
