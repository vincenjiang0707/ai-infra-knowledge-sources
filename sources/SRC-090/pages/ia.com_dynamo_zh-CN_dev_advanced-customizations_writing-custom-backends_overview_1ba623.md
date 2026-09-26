source: https://docs.nvidia.com/dynamo/zh-CN/dev/advanced-customizations/writing-custom-backends/overview
lastmod: 2026-09-23T23:30:39.914Z

# Custom Backend Overview

Choose the right path for bringing your own engine to Dynamo

Dynamo supports custom backends through one preferred unified contract, a lower-level worker path, and a packaging path:

The unified backend path is the preferred starting point for new custom engines. It gives Python and Rust backends the same lifecycle shape: parse arguments, start the engine, stream generated chunks, handle cancellation, drain, and clean up. The Dynamo framework owns runtime registration, signal handling, model registration, and graceful shutdown.

Use the lower-level Python worker path when your backend must own model registration, endpoint serving, request handling, or lifecycle behavior.

If your custom engine uses KV-aware routing, [publish KV events](https://docs.nvidia.com/dynamo/dev/advanced-customizations/writing-custom-backends/publish-kv-events)
so the Dynamo router can track which workers hold each prefix.