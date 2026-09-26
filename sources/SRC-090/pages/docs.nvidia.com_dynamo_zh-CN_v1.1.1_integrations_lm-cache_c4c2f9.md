source: https://docs.nvidia.com/dynamo/zh-CN/v1.1.1/integrations/lm-cache
lastmod: 2026-09-23T23:30:39.914Z

# LMCache

## Introduction

LMCache is a high-performance KV cache layer that supercharges LLM serving by enabling **prefill-once, reuse-everywhere** semantics. As described in the [official documentation](https://docs.lmcache.ai/index.html), LMCache lets LLMs prefill each text only once by storing the KV caches of all reusable texts, allowing reuse of KV caches for any reused text (not necessarily prefix) across any serving engine instance.

This document describes how LMCache is integrated into Dynamo’s vLLM backend to provide enhanced performance and memory efficiency.

## Aggregated Serving

### Configuration

LMCache is enabled using the `--kv-transfer-config`

flag:

### Customization

LMCache configuration can be customized via environment variables listed [here](https://docs.lmcache.ai/api_reference/configurations.html).

For advanced configurations, LMCache supports multiple [storage backends](https://docs.lmcache.ai/index.html):

**CPU RAM**: Fast local memory offloading**Local Storage**: Disk-based persistence**Redis**: Distributed cache sharing**GDS Backend**: GPU Direct Storage for high throughput**InfiniStore/Mooncake**: Cloud-native storage solutions

### Deployment

Use the provided launch script for quick setup:

This will:

- Start the Dynamo frontend
- Launch a single vLLM worker with LMCache enabled

### Architecture for Aggregated Mode

In aggregated mode, the system uses:

**KV Connector**:`LMCacheConnectorV1`

**KV Role**:`kv_both`

(handles both reading and writing)

## Disaggregated Serving

Disaggregated serving separates prefill and decode operations into dedicated workers. This provides better resource utilization and scalability for production deployments.

### Deployment

Use the provided disaggregated launch script (requires at least 2 GPUs):

This will:

- Start the Dynamo frontend
- Launch a decode worker on GPU 0
- Wait for initialization
- Launch a prefill worker on GPU 1 with LMCache enabled

### Worker Roles

#### Decode Worker

**Purpose**: Handles token generation (decode phase)**GPU Assignment**: CUDA_VISIBLE_DEVICES=0**LMCache Config**: Uses`NixlConnector`

only for KV transfer between prefill and decode workers

#### Prefill Worker

**Purpose**: Handles prompt processing (prefill phase)**GPU Assignment**: CUDA_VISIBLE_DEVICES=1**LMCache Config**: Uses`MultiConnector`

with both LMCache and NIXL connectors. This enables prefill worker to use LMCache for KV offloading and use NIXL for KV transfer between prefill and decode workers.**Flag**:`--disaggregation-mode prefill`


## Architecture

### KV Transfer Configuration

The system automatically configures KV transfer based on the deployment mode and worker type:

#### Prefill Worker (Disaggregated Mode)

#### Decode Worker or Aggregated Mode

#### Fallback (No LMCache)

### Integration Points

-
**Argument Parsing**(`args.py`

):- Configures appropriate KV transfer settings
- Sets up connector configurations based on worker type

-
**Engine Setup**(`main.py`

):- Initializes LMCache environment variables
- Creates vLLM engine with proper KV transfer config
- Handles both aggregated and disaggregated modes


### Best Practices

-
**Chunk Size Tuning**: Adjust`LMCACHE_CHUNK_SIZE`

based on your use case:- Smaller chunks (128-256): Better reuse granularity for varied content
- Larger chunks (512-1024): More efficient for repetitive content patterns

-
**Memory Allocation**: Set`LMCACHE_MAX_LOCAL_CPU_SIZE`

conservatively:- Leave sufficient RAM for other system processes
- Monitor memory usage during peak loads

-
**Workload Optimization**: LMCache performs best with:- Repeated prompt patterns (RAG, multi-turn conversations)
- Shared context across sessions
- Long-running services with warm caches


## Metrics and Monitoring

When LMCache is enabled with `--kv-transfer-config '{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_both"}'`

and `DYN_SYSTEM_PORT`

is set, LMCache metrics are automatically exposed via Dynamo’s `/metrics`

endpoint alongside vLLM and Dynamo metrics.

**Requirements to access LMCache metrics:**

`--kv-transfer-config '{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_both"}'`

- Enables LMCache`DYN_SYSTEM_PORT=8081`

- Enables metrics HTTP endpoint`PROMETHEUS_MULTIPROC_DIR`

(optional) - If not set, Dynamo manages it internally

For detailed information on LMCache metrics, including the complete list of available metrics and how to access them, see the ** LMCache Metrics section** in the vLLM Prometheus Metrics Guide.

## Troubleshooting

### LMCache log: `PrometheusLogger instance already created with different metadata`


You may see an error like:

**Version note**: We reproduced this behavior with **vLLM v0.12.0**. We have not reproduced it with **vLLM v0.11.0**, so it may be specific to (or introduced in) v0.12.0.

This is emitted by LMCache when the LMCache connector is initialized more than once in the same process (for example, once for a `WORKER`

role and later for a `SCHEDULER`

role). LMCache uses a process-global singleton for its Prometheus logger, so the second initialization can log this warning if its metadata differs.

**Impact**: This is a log-only error; in our testing it does not prevent vLLM/Dynamo from serving requests. If you care about LMCache metric labels, be aware the logger singleton uses the first-seen metadata.**Repro without Dynamo**(vLLM v0.12.0):

**Mitigation (silence)**: set`LMCACHE_LOG_LEVEL=CRITICAL`

.**Upstream issue**:[vLLM issue #30996](https://github.com/vllm-project/vllm/issues/30996).

### vLLM log: `Found PROMETHEUS_MULTIPROC_DIR was set by user`


vLLM v1 uses `prometheus_client.multiprocess`

and stores intermediate metric values in `PROMETHEUS_MULTIPROC_DIR`

.

- If you
**set**, vLLM warns that the directory must be wiped between runs to avoid stale/incorrect metrics.`PROMETHEUS_MULTIPROC_DIR`

yourself - When running via Dynamo, the vLLM wrapper may set
`PROMETHEUS_MULTIPROC_DIR`

internally to a temporary directory to avoid vLLM cleanup issues. If you still see the warning, confirm you are not exporting`PROMETHEUS_MULTIPROC_DIR`

in your shell or container environment.

## References and Additional Resources

[LMCache Documentation](https://docs.lmcache.ai/index.html)- Comprehensive guide and API reference[Configuration Reference](https://docs.lmcache.ai/api_reference/configurations.html)- Detailed configuration options[LMCache Observability Guide](https://docs.lmcache.ai/production/observability/vllm_endpoint.html)- Metrics and monitoring details