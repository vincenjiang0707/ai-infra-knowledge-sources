source: https://docs.nvidia.com/dynamo/knowledge-base/modular-components/kvbm/kvbm-guide
lastmod: 2026-09-24T19:58:16.636Z

# KVBM Guide

Enable KV offloading using KV Block Manager (KVBM) for Dynamo deployments

The Dynamo KV Block Manager (KVBM) is a scalable runtime component designed to handle memory allocation, management, and remote sharing of Key-Value (KV) blocks for inference tasks across heterogeneous and distributed environments. It acts as a unified memory layer and write-through cache for frameworks like vLLM and TensorRT-LLM.

KVBM is modular and can be used standalone via `pip install kvbm`

or as the memory management component in the full Dynamo stack. This guide covers installation, configuration, and deployment of the Dynamo KV Block Manager (KVBM) and other KV cache management systems.

## Quick start with the pre-built NGC container

The fastest path is the published Dynamo container, which includes KVBM:

For installation from source or custom builds, see [Local Installation](https://docs.nvidia.com/dynamo/cli/installation/install-dynamo) and [Release Artifacts](https://docs.nvidia.com/dynamo/reference/general/release-artifacts.mdx).

## Run KVBM Standalone

KVBM can be used independently without using the rest of the Dynamo stack:

See the [compatibility page](https://docs.nvidia.com/dynamo/reference/general/compatibility.mdx) for version compatibility.

### Build from Source

To build KVBM from source, see the detailed instructions in the [KVBM bindings README](https://github.com/ai-dynamo/dynamo/tree/v1.4.2/lib/bindings/kvbm/README.md#build-from-source).

## Run KVBM in Dynamo with vLLM

### Docker Setup

Pick one of the following to get a Dynamo vLLM container with KVBM built in. The subsequent serving commands are the same either way.

**Option A: Pre-built NGC container (recommended for quick start)**

See the [Local Installation Guide](https://docs.nvidia.com/dynamo/cli/installation/install-dynamo) for full setup instructions and [Release Artifacts](https://docs.nvidia.com/dynamo/reference/general/release-artifacts.mdx) for available versions.

**Option B: Build from source**

### Aggregated Serving

#### Verify Deployment

#### Alternative: Using Direct vllm serve

You can also use `vllm serve`

directly with KVBM:

## Run KVBM in Dynamo with TensorRT-LLM

**Prerequisites:**

- Ensure
`etcd`

and`nats`

are running before starting - KVBM only supports TensorRT-LLM’s PyTorch backend
- Disable partial reuse (
`enable_partial_reuse: false`

) to increase offloading cache hits - KVBM requires TensorRT-LLM v1.2.0rc2 or newer

### Docker Setup

Pick one of the following to get a Dynamo TensorRT-LLM container with KVBM built in. The subsequent serving commands are the same either way.

**Option A: Pre-built NGC container (recommended for quick start)**

See the [Local Installation Guide](https://docs.nvidia.com/dynamo/cli/installation/install-dynamo) for full setup instructions and [Release Artifacts](https://docs.nvidia.com/dynamo/reference/general/release-artifacts.mdx) for available versions.

**Option B: Build from source**

### Aggregated Serving

#### Verify Deployment

#### Alternative: Using trtllm-serve

## Run Dynamo with SGLang HiCache

SGLang’s Hierarchical Cache (HiCache) extends KV cache storage beyond GPU memory to include host CPU memory. When using NIXL as the storage backend, HiCache integrates with Dynamo’s memory infrastructure.

### Quick Start


Learn more:See the[SGLang HiCache Integration Guide]for detailed configuration, deployment examples, and troubleshooting.

## Disaggregated Serving with KVBM

KVBM supports disaggregated serving where prefill and decode operations run on separate workers. KVBM is enabled on the prefill worker to offload KV cache.

### Disaggregated Serving with vLLM

### Disaggregated Serving with TRT-LLM

## Configuration

### Cache Tier Configuration

Configure KVBM cache tiers using environment variables:

You can also specify exact block counts instead of GB:

`DYN_KVBM_CPU_CACHE_OVERRIDE_NUM_BLOCKS`

`DYN_KVBM_DISK_CACHE_OVERRIDE_NUM_BLOCKS`


[!NOTE] KVBM is a write-through cache and it is possible to misconfigure. Each of the capacities should increase as you enable more tiers. As an example, if you configure your GPU device to have 100GB of memory dedicated for KV cache storage, then configure

`DYN_KVBM_CPU_CACHE_GB >= 100`

. The same goes for configuring the disk cache;`DYN_KVBM_DISK_CACHE_GB >= DYN_KVBM_CPU_CACHE_GB`

. If the cpu cache is configured to be less than the device cache, thenthere will be no benefit from KVBM. In many cases you will see performance degradation as KVBM will churn by offloading blocks from the GPU to CPU after every forward pass. To know what your minimum value for`DYN_KVBM_CPU_CACHE_GB`

should be for your setup, consult your llm engine’s kv cache configuration.

### SSD Lifespan Protection

When disk offloading is enabled, disk offload filtering is enabled by default to extend SSD lifespan. The current policy only offloads KV blocks from CPU to disk if the blocks have frequency ≥ 2. Frequency doubles on cache hit (initialized at 1) and decrements by 1 on each time decay step.

To disable disk offload filtering:

### NCCL Replicated Mode for MLA Models

For MLA (Multi-Layer Attention) models such as DeepSeek, KVBM can use **NCCL replicated mode** so that only rank 0 loads KV blocks from G2/G3 storage and then broadcasts them to all GPUs via NCCL. This avoids redundant loads and can improve performance when multiple GPUs share the same replicated KV cache.

**Enable NCCL MLA mode:**

**Requirements:**

- MPI must be initialized (e.g., when launching with
`mpirun`

or equivalent) so that rank and world size are available for NCCL. - For optimal broadcast-based replication, build KVBM with the NCCL feature:
`cargo build -p kvbm --features nccl`

. Without it, the connector falls back to worker-level replication (each GPU loads independently).

When disabled (default), each GPU loads KV blocks independently. Set `DYN_KVBM_NCCL_MLA_MODE=true`

when running MLA models with KVBM to use the NCCL broadcast optimization.

## Enable and View KVBM Metrics

### Setup Monitoring Stack

### Enable Metrics for vLLM

### Enable Metrics for TensorRT-LLM

### Firewall Configuration (Optional)

### View Metrics

Access Grafana at [http://localhost:3000](http://localhost:3000/) (default login: `dynamo`

/`dynamo`

) and look for the **KVBM Dashboard**.

### Available Metrics

## Benchmarking KVBM

Use [LMBenchmark](https://github.com/LMCache/LMBenchmark) to evaluate KVBM performance.

### Setup

### Run Benchmark

Average TTFT and other performance numbers will be in the output.


TIP:If metrics are enabled, observe KV offloading and onboarding in the Grafana dashboard.

### Baseline Comparison

#### vLLM Baseline (without KVBM)

#### TensorRT-LLM Baseline (without KVBM)

## Troubleshooting

### No TTFT Performance Gain

**Symptom:** Enabling KVBM does not show TTFT improvement or causes performance degradation.

**Cause:** Not enough prefix cache hits on KVBM to reuse offloaded KV blocks.

**Solution:** Enable KVBM metrics and check the Grafana dashboard for `Onboard Blocks - Host to Device`

and `Onboard Blocks - Disk to Device`

. Large numbers of onboarded KV blocks indicate good cache reuse:


### KVBM Worker Initialization Timeout

**Symptom:** KVBM fails to start when allocating large memory or disk storage.

**Solution:** Increase the leader-worker initialization timeout (default: 1800 seconds):

### Disk Offload Fails to Start

**Symptom:** KVBM fails to start when disk offloading is enabled.

**Cause:** `fallocate()`

is not supported on the filesystem (e.g., Lustre, certain network filesystems),
or the storage backend requires a different method for setting `O_DIRECT`

.

**Solution:**

- If
`fallocate()`

is not supported, enable the zerofill fallback:

- If your filesystem ignores
`fcntl(F_SETFL, O_DIRECT)`

(e.g., IBM Storage Scale), set the disk allocator type to pass`O_DIRECT`

at file open time instead:

Supported values for `DYN_KVBM_DISK_ALLOCATOR_TYPE`

:

`default`

: Apply`O_DIRECT`

via`fcntl`

after file creation. Works on most POSIX filesystems (ext4, XFS, Lustre, etc.).`open-direct`

: Pass`O_DIRECT`

to`mkostemp`

at file open time. Required on filesystems where`fcntl(F_SETFL, O_DIRECT)`

is ignored (e.g., IBM Storage Scale).

- If you encounter “write all error” or EINVAL (errno 22), or need to debug without
`O_DIRECT`

:

### Disk to Device Onboarding Hangs with cuFile/GDS Errors

**Symptom:** KV cache onboarding from disk to device hangs indefinitely and requests become blocked. KVBM logs show errors similar to:

And `cufile.log`

contains errors like:

**Cause:** NVIDIA GPUDirect Storage (GDS) fails to register the disk-cache file handle and falls back to its POSIX-compatible mode, but the fallback also fails. This typically happens in containerized environments (including Kubernetes) when cuFile cannot resolve the backing block device for the disk-cache path.

See [ai-dynamo/dynamo#6032](https://github.com/ai-dynamo/dynamo/issues/6032) for the original report and discussion.

**Solution:** Point the disk cache at a path backed by a real block device and, in Kubernetes, expose `/run/udev`

so cuFile can query volume attributes.

For a Kubernetes pod spec (e.g., on the prefill worker where `DYN_KVBM_DISK_CACHE_GB > 0`

):

Key points:

`/run/udev`

must be mounted as a`hostPath`

volume. Without it, cuFile cannot read volume attributes and file registration fails.`DYN_KVBM_DISK_CACHE_DIR`

must point to a volume backed by a real block device (e.g., an`emptyDir`

volume, a`hostPath`

mount to a block-backed directory, or any other GDS-supported filesystem). The default`/tmp`

is usually overlayfs inside a container, which cuFile cannot handle.

After applying these changes, cuFile should log that it is running in compatible mode and disk-to-device onboarding should proceed.

## Developing Locally

Inside the Dynamo container, after changing KVBM-related code (Rust and/or Python):

To use [Nsight Systems](https://developer.nvidia.com/nsight-systems) for perf analysis, please follow below steps (using vLLM as example). KVBM has NVTX annotation on top level KV Connector APIs (search for `@nvtx_annotate`

). If more is needed, please add then rebuild.

## See Also

[KVBM Overview](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/kvbm/overview)for a quick overview of KV Caching, KVBM and its architecture[KVBM Configuration Reference](https://docs.nvidia.com/dynamo/reference/components/kvbm-configuration)for the full`DYN_KVBM_*`

and`KVBM_*`

configuration field reference[KVBM Design](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/kvbm/kvbm-design)for a deep dive into KVBM architecture[KV Cache Offloading](https://docs.nvidia.com/dynamo/cli/kv-cache-offloading/overview)[SGLang HiCache](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/sg-lang/hi-cache)