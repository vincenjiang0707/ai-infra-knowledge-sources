source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/integrations/kv-cache-integrations/lm-cache
lastmod: 2026-09-23T23:30:39.914Z

# LMCache

Integrate LMCache with Dynamo’s vLLM backend for prefill-once, reuse-everywhere KV cache across requests.

## Introduction

LMCache is a high-performance KV cache layer that supercharges LLM serving by enabling **prefill-once, reuse-everywhere** semantics. As described in the [official documentation](https://docs.lmcache.ai/index.html), LMCache lets LLMs prefill each text only once by storing the KV caches of all reusable texts, allowing reuse of KV caches for any reused text (not necessarily prefix) across any serving engine instance.

This document describes how LMCache is integrated into Dynamo’s vLLM backend to provide enhanced performance and memory efficiency.

## Installation Notes

Dynamo’s vLLM runtime expects LMCache to be present in the same Python environment. On supported environments (x86_64, Python 3.10-3.13, PyTorch built against CUDA 12.x), the published wheel installs directly:

LMCache only publishes x86_64 manylinux wheels linked against CUDA 12. For aarch64 hosts, or hosts running PyTorch built against a different CUDA major version, build LMCache from source against your matching torch + CUDA stack — see the official [LMCache installation guide](https://docs.lmcache.ai/getting_started/installation.html).


Compatibility note

`LMCacheMPConnector`

needs the fix from[LMCache#3282], which is on LMCache`main`

but not yet released. Without it, the MP path fails on vLLM ≥ 0.20.0 (including the`vllm==0.21.0`

Dynamo currently pins) with`RuntimeError: Unsupported GPUKVFormat: 7`

— vLLM 0.20+ uses GPU KV formats 6 / 7 that the MP path doesn’t yet handle.Until the next LMCache release, build LMCache from source against that PR.


## Aggregated Serving

### Configuration

LMCache runs the cache engine as an out-of-process sidecar (`lmcache server`

); the Dynamo worker connects to it via the `LMCacheMPConnector`

. Start the sidecar, then launch the worker:

### Customization

The LMCache MP server is configured via CLI arguments. See the [Configuration Reference](https://docs.lmcache.ai/mp/configuration.html) for the full list of `lmcache server`

flags.

LMCache MP uses a two-tier storage architecture: an in-memory L1 cache (sized with `--l1-size-gb`

) plus optional persistent L2 adapters configured with `--l2-adapter`

. The supported [L2 storage backends](https://docs.lmcache.ai/mp/l2_storage.html) are:

**POSIX**: Standard POSIX file I/O on any file system**GDS**/**GDS_MT**: NVIDIA GPU Direct Storage (single- and multi-threaded), bypassing the CPU for NVMe SSDs that support GDS**HF3FS**: Distributed / shared file-system backend**OBJ**: Object store backend**AZURE_BLOB**: Azure Blob Storage

### Deployment

Use the provided launch script for quick setup:

This will:

- Start the LMCache MP server
- Start the Dynamo frontend
- Launch a single vLLM worker with
`LMCacheMPConnector`

connected to the sidecar

### Architecture for Aggregated Mode

In aggregated mode, the system uses:

**KV Connector**:`LMCacheMPConnector`

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

#### Aggregated Mode

#### Prefill Worker (Disaggregated Mode)

#### Decode Worker (Disaggregated Mode)

#### Fallback (No LMCache)

### Integration Points

-
**Argument Parsing**(`args.py`

):- Configures appropriate KV transfer settings
- Sets up connector configurations based on worker type

-
**Engine Setup**(`main.py`

):- Creates vLLM engine with proper KV transfer config
- Handles both aggregated and disaggregated modes

-
**Sidecar Lifecycle**(launch script):- Starts the
`lmcache server`

process before the Dynamo worker - Tears it down on exit via the script’s cleanup trap

- Starts the

### Best Practices

-
**Chunk Size Tuning**: Pass`--chunk-size`

to`lmcache server`

based on your use case:- Smaller chunks (128-256): Better reuse granularity for varied content
- Larger chunks (512-1024): More efficient for repetitive content patterns

-
**Memory Allocation**: Set`--l1-size-gb`

on`lmcache server`

conservatively:- Leave sufficient RAM for other system processes
- Monitor memory usage during peak loads

-
**Workload Optimization**: LMCache performs best with:- Repeated prompt patterns (RAG, multi-turn conversations)
- Shared context across sessions
- Long-running services with warm caches


## Metrics and Monitoring

The LMCache MP server records metrics through the OpenTelemetry SDK and exposes them on its own HTTP admin port (default `:8080/metrics`

), prefixed `lmcache_mp_`

:

vLLM and Dynamo metrics remain on Dynamo’s `:8081/metrics`

(set `DYN_SYSTEM_PORT=8081`

on the worker to enable that endpoint).

For detailed information on LMCache metrics, including the complete list of available metrics and how to access them, see the ** LMCache Metrics section** in the vLLM Prometheus Metrics Guide.

## Troubleshooting

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

[LMCache Documentation](https://docs.lmcache.ai/index.html)- Comprehensive guide and API reference[Configuration Reference](https://docs.lmcache.ai/mp/configuration.html)-`lmcache server`

CLI arguments[LMCache Observability Guide](https://docs.lmcache.ai/mp/observability.html)- Metrics and monitoring details