source: https://docs.nvidia.com/dynamo/reference/components/kvbm-configuration
lastmod: 2026-09-24T19:58:16.636Z

# KVBM Configuration Reference

Field reference for the KV Block Manager environment variables and the layered KVBM_* / TOML configuration system.

The KV Block Manager (KVBM) is configured through two layers:

— the primary, user-facing controls for cache tier sizing, offload behavior, object storage, distributed (leader/worker) mode, and metrics. Set these in the worker container`DYN_KVBM_*`

runtime environment variables`env`

. This is what most deployments use.**The**— a lower-level, layered configuration for the KVBM runtime (Tokio/Rayon threads, messenger transport, NixL backends, offload policies, event publishing). Used for advanced tuning and for vLLM’s`KVBM_*`

/ TOML figment system`kv_connector_extra_config`

.

For the conceptual model and worked examples, see the [KVBM Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/kvbm/kvbm-guide). Names and defaults on this page come from [ environment_names.rs](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/lib/runtime/src/config/environment_names.rs) and the

[crate.](https://github.com/ai-dynamo/dynamo/tree/v1.4.2/lib/kvbm-config)

`kvbm-config`

## Cache tiers

KVBM offloads KV blocks GPU (G1) → host/CPU (G2) → disk (G3) → object storage (G4). Enable a tier by giving it a size; each tier accepts either a size in GB or an explicit block count (the block-count override wins).

Set the CPU cache larger than the engine’s GPU KV cache — a good rule of thumb is `DYN_KVBM_CPU_CACHE_GB >= 100`

and `DYN_KVBM_DISK_CACHE_GB >= DYN_KVBM_CPU_CACHE_GB`

. If the CPU cache is smaller than the device cache, KVBM churns (offloading blocks after every forward pass) and you may see performance *degradation*. Consult your engine’s KV-cache configuration for the minimum useful value.

Size of the host (G2, pinned CPU memory) cache in GB. Setting this enables CPU offload.

Host cache size as an explicit block count. Takes priority over `DYN_KVBM_CPU_CACHE_GB`

.

Size of the disk (G3) cache in GB. Setting this enables disk offload.

Disk cache size as an explicit block count. Takes priority over `DYN_KVBM_DISK_CACHE_GB`

.

Directory for disk cache files. When unset, a default path is used.

## Offload and transfer

Disable the disk offload filter, allowing all eligible blocks to offload to disk. The filter is not supported in disk-cache-only mode.

Minimum prefix priority a block must have to be offloaded to the host tier. Raises the bar for what gets offloaded.

Maximum number of blocks per transfer batch.

Upper bound on the transfer batch size.

Maximum number of block transfers in flight at once.

Disable write-combined memory for transfers.

## Disk backend

Disk allocator implementation. `open-direct`

uses `O_DIRECT`

I/O.

Disable `O_DIRECT`

on disk I/O. Use on filesystems that do not support it.

Fall back to zero-filling when preallocating disk cache files is not supported.

## Object storage (G4)

The G4 tier stores blocks in an S3-compatible object store. Enable it with `DYN_KVBM_OBJECT_ENABLED=1`

and supply the bucket and credentials.

Enable object storage. Set to `1`

to enable.

Bucket name for the object-storage cache. Supports a `{worker_id}`

template for per-worker buckets, for example `kv-cache-{worker_id}`

.

Endpoint URL for the object store. Set for S3-compatible services such as MinIO.

Region for the object store.

Access key for object-store authentication.

Secret key for object-store authentication.

Number of blocks to store in object storage.

## Distributed (leader/worker)

In multi-worker deployments, one KVBM leader coordinates the worker cache tiers over ZMQ.

Timeout in seconds for KVBM leader and worker initialization. Raise it for large multi-node deployments that take longer to come up.

ZMQ host for the KVBM leader.

ZMQ publish port for the KVBM leader. The TRT-LLM integration derives its port from this value.

ZMQ acknowledgment port for the KVBM leader.

## MLA and NCCL

Enable the NCCL broadcast optimization for Multi-head Latent Attention (MLA) models. When disabled, each GPU loads KV blocks independently. Set `true`

when running MLA models with KVBM.

Maximum number of CTAs (cooperative thread arrays) NCCL may use for KVBM broadcasts.

Enable NUMA-aware allocation for the host cache.

## NixL backends

Enable individual NixL transfer backends with the `DYN_KVBM_NIXL_BACKEND_<backend>`

pattern.

Enable or disable a specific NixL backend, for example `DYN_KVBM_NIXL_BACKEND_UCX=true`

or `DYN_KVBM_NIXL_BACKEND_GDS=true`

. Backend names are case-insensitive.

## Metrics and debugging

Enable the KVBM metrics endpoint.

Port for the KVBM metrics endpoint.

Enable KVBM event recording for debugging.

Interval in seconds between cache-statistics log lines.

Maximum number of requests to accumulate in cache statistics.

## Advanced: the `KVBM_*`

/ TOML system

Beyond the `DYN_KVBM_*`

variables above, the KVBM runtime (crate [ kvbm-config](https://github.com/ai-dynamo/dynamo/tree/v1.4.2/lib/kvbm-config)) has a layered configuration system for low-level runtime tuning. Most deployments do not need it.

### How it loads

Sources are merged in priority order (lowest to highest):

- Code defaults
- System file
`/opt/dynamo/etc/kvbm.toml`

- TOML file at the path in
`KVBM_CONFIG_PATH`

`KVBM_*`

environment variables- Programmatic JSON overrides (for example, vLLM’s
`kv_connector_extra_config`

)

Leader and worker roles can carry different values via figment profiles (`profile.leader.*`

, `profile.worker.*`

in TOML/JSON).

Path to a TOML config file merged above the system file and below `KVBM_*`

env vars.

### Environment-variable groups

Each config section maps to an env prefix. The suffix after the prefix is lowercased into the field name (for example, `KVBM_TOKIO_WORKER_THREADS`

→ `tokio.worker_threads`

).

Nested sections without an env prefix (offload policies, onboard mode, object storage) are set through the TOML file or JSON overrides:

**Offload policies**(`offload.g1_to_g2`

,`offload.g2_to_g3`

): a`policies`

list of`pass_all`

/`presence`

/`presence_lfu`

, evaluated with AND logic.`presence_lfu.min_lfu_count`

defaults to`8`

.**Onboard mode**(`onboard.mode`

):`inter`

(async, default) or`intra`

(synchronous layer-wise).**Object storage**(`object.client`

):`s3`

or`nixl`

client; S3 fields`bucket`

(`kvbm-blocks`

),`region`

(`us-east-1`

),`endpoint_url`

,`force_path_style`

,`max_concurrent_requests`

(16).