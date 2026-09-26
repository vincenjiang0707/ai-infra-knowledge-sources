source: https://docs.nvidia.com/dynamo/zh-CN/knowledge-base/modular-components/backends/v-llm/kv-cache-offloading
lastmod: 2026-09-23T23:30:39.914Z

# KV Cache Offloading

Dynamo supports multiple KV cache offloading backends for vLLM, allowing you to extend effective KV cache capacity beyond GPU memory using CPU RAM and disk storage. Each backend integrates through vLLM’s connector interface and works with both aggregated and disaggregated serving.

## KVBM

[KVBM](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/kvbm/overview) (KV Block Manager) is Dynamo’s built-in KV cache offloading system. It provides a three-layer architecture (LLM runtime, logical block management, NIXL transport) with support for CPU and disk cache tiers, and integrates natively with Dynamo’s KV-aware routing and disaggregated serving.

For configuration details, see the [KVBM Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/kvbm/kvbm-guide).

## LMCache

[LMCache](https://github.com/LMCache/LMCache) is an open-source KV cache engine that provides prefill-once, reuse-everywhere caching with multi-level storage backends (CPU RAM, local storage, Redis, GDS, InfiniStore/Mooncake).

For local setup, see [KV Cache Offloading](https://docs.nvidia.com/dynamo/cli/kv-cache-offloading/overview).

## FlexKV

[FlexKV](https://github.com/taco-project/FlexKV) is a scalable, distributed KV cache runtime developed by Tencent Cloud’s TACO team. It supports multi-level caching (GPU, CPU, SSD), distributed KV cache reuse across nodes, and high-performance I/O via io_uring and GPUDirect Storage.

For local setup, see [KV Cache Offloading](https://docs.nvidia.com/dynamo/cli/kv-cache-offloading/overview).

## See Also

: Architecture and design of Dynamo’s built-in KV cache offloading[KVBM Design](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/kvbm/kvbm-design): Routing requests based on KV cache state[Routing Concepts](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/routing-concepts): Prefill/decode separation architecture[Disaggregated Serving](https://docs.nvidia.com/dynamo/knowledge-base/concepts/system-architecture/disaggregated-serving)