source: https://docs.nvidia.com/dynamo/zh-CN/kubernetes/kv-cache-offloading/overview
lastmod: 2026-09-24T19:58:16.636Z

# Set up KV Cache Offloading

KV cache offloading lets a worker keep more KV cache than fits in GPU memory by spilling blocks to host (CPU) memory or local disk. This serves longer contexts and reuses cached prefixes across requests. This page shows how to turn it on **inside a DynamoGraphDeployment (DGD)** — the engine-internals and local-CLI details live in the per-backend pages linked at the end.

This is a [how-to](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/deploy-with-dgd) for an existing deployment. If you have not authored a DGD yet, start with the [DGD Guide](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/deploy-with-dgd).

## The pattern

Offloading is configured **on the worker**, not the Frontend. For vLLM workers, you pass a `--kv-transfer-config`

JSON argument that names a connector, then size the offload tiers with environment variables. The shape is always the same:

### Choose a connector

Each offloading backend uses the same `--kv-transfer-config`

hook with a different `kv_connector`

. Pick one — they are alternatives, not layers.

SGLang HiCache does not use the `--kv-transfer-config`

connector mechanism. On an SGLang worker, set `--enable-hierarchical-cache`

in `args`

and `DYN_SHARED_CACHE_TYPE`

in the container `env`

. See [Using HiCache](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/sg-lang/hi-cache).

### Worked example: KVBM on a vLLM worker

This aggregated Qwen3-32B worker offloads KV blocks to 100 GB of host memory. It is the worker section of the [agg-kvbm recipe](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/recipes/qwen3-32b/vllm/agg-kvbm/deploy.yaml):

Two things to size together:

`DYN_KVBM_CPU_CACHE_GB`

(and optionally`DYN_KVBM_DISK_CACHE_GB`

) set the offload tier sizes.`resources.limits.memory`

must be large enough to hold the CPU cache tier plus the engine’s normal footprint. The recipe requests 150–200 GB for a 100 GB CPU cache.

To add a disk tier, set `DYN_KVBM_DISK_CACHE_GB`

and mount a volume for it. To export offloading metrics to Prometheus, set `DYN_KVBM_METRICS=true`

.

### Verify

After the worker is `Running`

, send repeated requests that share a long prefix and confirm the second request has lower TTFT. With `DYN_KVBM_METRICS=true`

, check the offload hit-rate metrics — see [Metrics](https://docs.nvidia.com/dynamo/kubernetes/operations/observability).

## Related pages

These cover engine internals, the local-CLI workflow, and tuning for each backend:

[KVBM Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/kvbm/kvbm-guide)— KV Block Manager architecture and the full env-var reference.[Local KV Cache Offloading](https://docs.nvidia.com/dynamo/cli/kv-cache-offloading/overview)— compare the available backends and run their local examples.[Using HiCache](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/sg-lang/hi-cache)— SGLang hierarchical cache.[Publish KV Events](https://docs.nvidia.com/dynamo/advanced-customizations/writing-custom-backends/publish-kv-events)— publish KV events from a custom engine.