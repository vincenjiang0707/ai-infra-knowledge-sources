source: https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/overview
lastmod: 2026-09-24T19:58:16.636Z

# Router

KV cache-aware router that picks workers by combined prefill and decode cost to maximize throughput and minimize latency.

The Dynamo KV Router intelligently routes requests by evaluating their computational costs across different workers. It considers both decoding costs (from active blocks) and prefill costs (from newly computed blocks), using KV cache overlap to minimize redundant computation. Optimizing the KV Router is critical for achieving maximum throughput and minimum latency in distributed inference setups.

## Quick Start

To launch the Dynamo frontend with the KV Router:

The [Frontend Configuration Reference](https://docs.nvidia.com/dynamo/reference/components/frontend-configuration#router) is the
canonical reference for embedded-router flags, environment variables, defaults, and
boolean forms. See [Configuration and Tuning](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/configuration-and-tuning) for behavioral
guidance.

`--router-mode kv`

(or `DYN_ROUTER_MODE=kv`

) enables KV routing on the
frontend, but it does not enable KV event publishing on backend workers. With
the default `--router-kv-events`

setting, missing publishers leave the router
in event-driven mode without real cache state; the router does not
automatically switch to approximate prediction. Configure the backend-specific
publishing flags in [Router Operations](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-operations#additional-notes).
If workers will not publish events, use `--no-router-kv-events`

for approximate
cache prediction or `--load-aware`

for load-only routing.

For Kubernetes, set `DYN_ROUTER_MODE=kv`

on the Frontend service.

### Standalone Router

You can also run the KV router as a standalone service (without the Dynamo frontend). See the [Standalone Router component](https://github.com/ai-dynamo/dynamo/tree/v1.4.2/components/src/dynamo/router/) for more details.

For deployment modes and quick start steps, see the [Router Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-guide). For tuning guidelines, see [Configuration and Tuning](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/configuration-and-tuning). For A/B benchmarking, see the [KV Router A/B Benchmarking Guide](https://docs.nvidia.com/dynamo/recipes/benchmarks/kv-router-ab-testing).

## Prerequisites and Limitations

**Requirements:**

**Dynamic endpoints only**: KV router requires`register_model()`

with`model_input=ModelInput.Tokens`

. Your backend handler receives pre-tokenized requests with`token_ids`

instead of raw text.- Backend workers must call
`register_model()`

with`model_input=ModelInput.Tokens`

(see[Backend Guide](https://docs.nvidia.com/dynamo/advanced-customizations/writing-custom-backends/writing-python-workers)) - Use dynamic discovery with KV routing so the router can track worker instances and KV cache state

**Multimodal Support:**

**Image routing via multimodal hashes**: Supported in the documented SGLang, TRT-LLM, and vLLM router paths. SGLang needs the hash-forwarding patch that Dynamo’s own image ships; a custom build without it serves the request but routes on the text prefix alone.**Other backend or modality combinations**: Check the backend-specific multimodal docs before relying on multimodal hash routing.

**Limitations:**

- Static endpoints are not supported with KV routing; use dynamic discovery so the router can track worker instances and KV cache state
- With
`DYN_LORA_ENABLED`

, only KV, random, and round-robin routing are LoRA-aware. Direct, power-of-two, least-loaded, and device-aware-weighted modes fail startup. Session affinity is supported with LoRA only in KV mode; LoRA plus random or round-robin affinity is rejected.

For basic model registration without KV routing, use `--router-mode round-robin`

, `--router-mode random`

, `--router-mode power-of-two`

, `--router-mode least-loaded`

, or `--router-mode device-aware-weighted`

with both static and dynamic endpoints.

## Next Steps

: Deployment modes, quick start, and page map[Router Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-guide): Cost model and worker-selection behavior[Routing Concepts](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/routing-concepts): Candidate eligibility, DP-rank filtering, and busy-threshold overload handling[Router Filtering](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-filtering): Canonical embedded-router flags and environment variables[Frontend Configuration Reference](https://docs.nvidia.com/dynamo/reference/components/frontend-configuration#router): Router behavior, transport modes, and tuning guidance[Configuration and Tuning](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/configuration-and-tuning): Weighted policy-class arbitration, cursor movement, and bulk virtual rounds[Deficit Round Robin Queue Scheduling](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/deficit-round-robin): Router queue, backend engine, and cache priority behavior[Priority Scheduling](https://docs.nvidia.com/dynamo/agents/priority-scheduling): Prefill and decode routing setups[Disaggregated Serving](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/disaggregated-serving): Replicas, persistence, and recovery[Router Operations](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-operations): Python API usage, K8s examples, and custom routing patterns[Router Examples](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-examples): Test layers from Rust unit tests to fixture-backed replay and full process E2E[Router Testing](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-testing): Cross-datacenter KV routing and the DC Relay (experimental)[Multi-DC KV Routing](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/multi-dc-kv-routing): Run the KV indexer as a separate service for independent scaling[Standalone Indexer](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/standalone-indexer): Expose KV-aware selection and reservation accounting over HTTP[Standalone Selection Service](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/standalone-selection): Run active-request load accounting as a separate HTTP service[Standalone Slot Tracker](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/standalone-slot-tracker): Architecture details, algorithms, and event transport modes[Router Design](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-design)