source: https://docs.nvidia.com/dynamo/zh-CN/v1.2.1/backends/custom-backend/custom-backend-overview
lastmod: 2026-09-23T23:30:39.914Z

# Custom Backend Overview

Dynamo supports custom backends through one preferred unified contract, a lower-level worker path, and a packaging path:

The unified backend path is the preferred starting point for new custom engines. It gives Python and Rust backends the same lifecycle shape: parse arguments, start the engine, stream generated chunks, handle cancellation, drain, and clean up. The Dynamo framework owns runtime registration, signal handling, model registration, and graceful shutdown.

Use the lower-level Python worker path when your backend needs features that are still outside the unified contract, such as multimodal, LoRA adapter management, logprobs, guided decoding, engine-specific routes, or custom request handling.

If your custom engine wants KV-cache-aware routing, also implement [KV Events for Custom Engines](https://docs.nvidia.com/dynamo/v1.2.1/integrations/kv-cache-integrations/kv-events-for-custom-engines) so the Dynamo router can track which workers hold each prefix.