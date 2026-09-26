source: https://docs.nvidia.com/dynamo/dev/cli/kv-aware-routing/overview
lastmod: 2026-09-24T19:58:16.636Z

KV-Aware Routing


KV-Aware Routing

KV-aware routing places multiple workers behind the frontend and routes each request to the worker most likely to already hold its KV cache, eliminating redundant prefill computation. It is the local equivalent of the routing you configure in the [Kubernetes KV Routing guide](https://docs.nvidia.com/dynamo/dev/kubernetes/kv-aware-routing/using-the-dynamo-frontend) — same router, driven by CLI flags instead of a DynamoGraphDeployment.

For how routing decisions are made, see [Routing Concepts](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/routing-concepts) and the [Router Guide](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/router-guide).

## How it works locally

A KV-routed deployment is still just a frontend plus workers (see the [Overview](https://docs.nvidia.com/dynamo/dev/cli/kv-aware-routing/overview)), with two differences:

- The
**frontend**runs in KV routing mode so it tracks cache state across workers. - Each
**worker**publishes KV cache events (over ZMQ by default) so the frontend knows what each worker holds.

Use **two or more workers** when you want to evaluate worker selection. The vLLM and SGLang `launch/agg_router.sh`

presets wire up two workers; the TensorRT-LLM preset is a one-worker router-path smoke setup.

## Aggregated serving with KV routing

The vLLM and SGLang presets start two workers and require 2 GPUs. The TensorRT-LLM preset starts one worker and requires 1 GPU; use it to verify the router path, then add workers when you need worker selection.

###### vLLM

###### SGLang

###### TensorRT-LLM

This launches the frontend in KV routing mode with two workers publishing KV events over ZMQ.

## Disaggregated serving with KV routing

The vLLM and SGLang presets start 2 prefill and 2 decode workers and require 4 GPUs. The TensorRT-LLM preset starts 1 prefill and 1 decode worker and requires 2 GPUs. The frontend runs in KV routing mode and activates its internal prefill router after discovering compatible typed prefill and decode services for the same model and namespace.

###### vLLM

###### SGLang

###### TensorRT-LLM

Once a routed deployment is running, try adding another worker — the frontend discovers it automatically and starts routing to it.

## Change the Worker-Selection Policy

By default the frontend ranks workers with Dynamo’s built-in cost model. Dynamo also ships built-in worker-selection policies with the frontend, so you can swap that ranking step without rebuilding.

Write the policy into a YAML file:

Then point the frontend at it:

To compare against the built-in selector, restart with
`DYN_ROUTER_WORKER_SELECTION_POLICY=default`

— no config change needed.

For the available policy types and per-stage prefill/decode selection, see
[Worker-Selection Policies](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/configuration-and-tuning#worker-selection-policies).

## Troubleshooting

**Router not routing correctly (vLLM).** Ensure `PYTHONHASHSEED=0`

is set for all vLLM processes when using KV-aware routing, so cache-block hashes are consistent across workers. See [Hashing Consistency](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/backends/v-llm/reference-guide#hashing-consistency-for-kv-events).

## See also

— deployment topologies and routing modes[Router Guide](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/router-guide)— split prefill and decode across workers[Disaggregated Serving](https://docs.nvidia.com/dynamo/dev/cli/disaggregated-serving/overview)— copyable commands for KV-routing launch scripts[vLLM local deployment examples](https://docs.nvidia.com/dynamo/dev/recipes/cli-templates/v-llm)