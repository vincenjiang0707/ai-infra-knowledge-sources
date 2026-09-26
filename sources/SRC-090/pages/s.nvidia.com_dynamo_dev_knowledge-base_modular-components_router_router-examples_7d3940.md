source: https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/router-examples
lastmod: 2026-09-24T19:58:16.636Z

# Router Examples

For quick start instructions, see the [Router README](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/overview). This document provides further examples for using the Dynamo Router, including Python API usage, Kubernetes deployments, and custom routing patterns.

## Using KvRouter Python API

Instead of launching the KV Router via command line, you can create a `KvRouter`

object directly in Python. This allows per-request routing configuration overrides.

**Multiple Routers from the Same Runtime**: Do not create multiple independently managed `KvRouter`

instances from the same `DistributedRuntime`

. Routers created from endpoints owned by the same runtime share that runtime’s primary cancellation token, so dropping one router can cancel background work used by the others. For one in-process frontend, use a single `KvRouter`

; for independent router lifetimes, use separate frontend processes or create each router from a separate `DistributedRuntime`

.

With the event loop available as `loop`

, independent in-process router lifetimes require separate runtimes:

### Methods

The `KvRouter`

provides the following methods:

-
: Route and execute a request, returning an async stream of responses. Automatically handles worker selection, state tracking, and lifecycle management.`generate(token_ids, model, ...)`

-
: Query which worker would be selected for given tokens. Returns`best_worker(token_ids, router_config_override=None, request_id=None, update_indexer=False)`

`(worker_id, dp_rank, overlap_blocks)`

.- Without
`request_id`

: Query-only, doesn’t update router state - With
`request_id`

: Updates router lifecycle state to track the request.**Note**: If used with`request_id`

, you must call`mark_prefill_complete()`

and`free()`

at the appropriate lifecycle points to maintain accurate load tracking - With
`update_indexer=True`

: Records the selected worker in the approximate indexer for future overlap predictions. This is only meaningful when`use_kv_events=False`


- Without
-
: Get detailed load information for all workers, including potential prefill tokens, potential decode blocks, and active requests. Returns a list of load dictionaries.`get_potential_loads(token_ids)`

-
: Get per-worker KV overlap by storage tier, including shared-cache overlap when configured.`get_overlap_scores(token_ids, ...)`

-
: Signal that a request has completed its prefill phase. Only used for`mark_prefill_complete(request_id)`

[manual lifecycle management](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/router-examples#2-manual-state-management-advanced)when using`best_worker()`

for manual routing instead of`generate()`

. -
: Signal that a request has completed and its resources should be released. Only used for`free(request_id)`

[manual lifecycle management](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/router-examples#2-manual-state-management-advanced)when using`best_worker()`

for manual routing instead of`generate()`

. -
: Dump all KV cache events from the router’s indexer as a JSON string. Useful for debugging and analysis.`dump_events()`


### Setup

First, launch at least two backend engines so the router has a meaningful selection to make. Each worker needs a unique system port and KV event endpoint:

### Example Script

## K8s Examples

For basic Kubernetes deployment with the KV Router, see [Dynamo Frontend Routing](https://docs.nvidia.com/dynamo/dev/kubernetes/kv-aware-routing/using-the-dynamo-frontend).

### Complete K8s Examples

[TRT-LLM aggregated router example](https://github.com/ai-dynamo/dynamo/blob/main/examples/backends/trtllm/deploy/agg_router.yaml)[vLLM aggregated router example](https://github.com/ai-dynamo/dynamo/blob/main/examples/backends/vllm/deploy/agg_router.yaml)[SGLang aggregated router example](https://github.com/ai-dynamo/dynamo/blob/main/examples/backends/sglang/deploy/agg_router.yaml)[Kubernetes deployment guide](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart)

**For A/B Testing and Advanced K8s Setup:**
See the comprehensive [KV Router A/B Benchmarking Guide](https://docs.nvidia.com/dynamo/dev/recipes/benchmarks/kv-router-ab-testing) for step-by-step instructions on deploying, configuring, and benchmarking the KV router in Kubernetes.

### Example with Advanced Configuration

### Alternative: Using Command Args in K8s

You can also pass CLI arguments directly in the container command:

**Recommendation:** Use environment variables for easier configuration management and consistency with Dynamo’s K8s patterns.

## Routing Patterns

The `KvRouter`

supports multiple usage patterns depending on your control requirements:

### 1. Automatic Routing (Recommended)

Call `generate()`

directly and let the router handle everything:

**Best for**: Most use cases**Router automatically**: Selects best worker, updates state, routes request, tracks lifecycle

### 2. Manual State Management (Advanced)

Use `best_worker(request_id=...)`

to select and track, then manage the request yourself:

**Best for**: Custom request handling with router state tracking**Requires**: Calling`mark_prefill_complete()`

and`free()`

at correct lifecycle points**Approximate mode**: Pass`update_indexer=True`

to`best_worker()`

when`use_kv_events=False`

so the router learns from manual worker selections**Direct dispatch**:`Client.direct()`

targets the returned worker instance; include the returned DP rank in the preprocessed request’s`routing`

field**Caution**: Incorrect lifecycle management degrades load balancing accuracy

### 3. Hierarchical Router Probing

Query without state updates, then route through a chosen router:

**Best for**: Multi-tier deployments (e.g., Envoy Gateway routing to multiple router groups)**Advantage**: Query multiple routers before committing to one

### 4. Custom Load-Based Routing

Use `get_potential_loads()`

to implement custom routing logic:

**Best for**: Custom optimization strategies beyond the built-in cost function**Advantage**: Full control over worker selection logic**See also**: Detailed example below in “Custom Routing Example: Minimizing TTFT”

All patterns support `router_config_override`

to adjust routing behavior per-request without recreating the router.

## Custom Routing Example: Minimizing TTFT

Here’s an example of using `get_potential_loads()`

to implement custom routing that minimizes Time To First Token (TTFT) by selecting the worker with the least prefill work:

This approach gives you complete control over routing decisions, allowing you to optimize for different metrics based on your specific requirements. As some examples:

**Minimize TTFT**: Select worker with lowest`potential_prefill_tokens`

**Maximize cache reuse**: Use`best_worker()`

which considers both prefill and decode loads**Balance load**: Consider both`potential_prefill_tokens`

and`potential_decode_blocks`

together**Balance active batches**: Include`active_requests`

when decode step latency depends materially on request count

See [Router Design](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/router-design) for architecture details and the cost function algorithm.

## KV Event Publishing for Custom Engines

For full documentation on implementing KV event publishing for custom inference engines, see the dedicated [KV Event Publishing for Custom Engines](https://docs.nvidia.com/dynamo/dev/advanced-customizations/writing-custom-backends/publish-kv-events) guide. It covers:

**Direct publishing**: Call`publish_stored()`

/`publish_removed()`

to push events over the Dynamo event plane**ZMQ relay**: For engines that emit raw KV events over ZMQ (like SGLang and vLLM), the same`KvEventPublisher`

subscribes to the ZMQ socket and relays events automatically- API reference, event structure, ZMQ wire format, and best practices

## Global Router (Hierarchical Routing)

For deployments with multiple worker pools, the **Global Router** enables hierarchical routing by sitting between the frontend and local routers. It selects the appropriate pool for each request based on configurable policies, supporting disaggregated topologies where pools are tuned for different workload characteristics.

**Component details**:`components/src/dynamo/global_router/`

**Example**:`examples/global_planner/`


## See Also

: Quick start guide for the KV Router[Router README](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/overview): Router flags and production setup[Configuration and Tuning](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/configuration-and-tuning): Give premium traffic a larger service share while regular traffic continues to progress[Prioritize Premium Requests with Policy Classes](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/deficit-round-robin#prioritize-premium-requests-with-policy-classes): Architecture details and event transport modes[Router Design](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/router-design)