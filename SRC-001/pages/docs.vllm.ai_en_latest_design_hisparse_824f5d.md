source: https://docs.vllm.ai/en/latest/design/hisparse/
lastmod: 2026-09-23

# HiSparse local KV offload architecture[¶](https://docs.vllm.ai#hisparse-local-kv-offload-architecture)

Status: experimental

## The short version[¶](https://docs.vllm.ai#the-short-version)

There are three different jobs:

- The normal KV cache system manages GPU block pools and tables.
manages logical host blocks, source-prefix identity, and host/GPU residency transitions.`HiSparseCoordinator`

carries residency work between scheduler and worker;`HiSparseConnector`

`HiSparseWorker`

coordinates transfers, while per-cacheobjects own host/hot views and GPU replacement state.`HiSparseRuntime`


Neither worker-side object allocates or frees logical blocks. HMA provides the GPU allocation shared by the resident and hot groups; it does not manage CPU memory or KV identity.

request ────► HiSparseCoordinator ── source blocks + residency policy
│
├──► KV cache manager ── resident/hot GPU leases (HMA)
│
└──► HiSparseConnector ── host bytes + copies + GPU LRU


This is a local KV connector. When P/D or another offload connector is also configured, [ MultiConnector](https://docs.vllm.ai/api/vllm/distributed/kv_transfer/kv_connector/v1/multi_connector/#vllm.distributed.kv_transfer.kv_connector.v1.multi_connector.MultiConnector) composes it with

[.](https://docs.vllm.ai/api/vllm/distributed/kv_transfer/kv_connector/v1/hisparse/connector/#vllm.distributed.kv_transfer.kv_connector.v1.hisparse.connector.HiSparseConnector)

`HiSparseConnector`

`host_pool_gib`

is configured on [ HiSparseConnector](https://docs.vllm.ai/api/vllm/distributed/kv_transfer/kv_connector/v1/hisparse/connector/#vllm.distributed.kv_transfer.kv_connector.v1.hisparse.connector.HiSparseConnector) and is the usable host-cache capacity per data-parallel replica, not a node-wide memory budget. Tensor-parallel ranks hold replicated views of that logical cache. Those views may use private per-rank backing or one shared physical allocation without changing the configured capacity. Physical host memory consumption is therefore topology- and implementation-dependent. The realized capacity may be slightly smaller because the budget is rounded down to complete host blocks.

## Ownership[¶](https://docs.vllm.ai#ownership)

| Thing | Owner | What “owner” means |
|---|---|---|
| HiSparse source and prefix identity |
`HiSparseCoordinator` |

`HiSparseCoordinator`

`HiSparseCoordinator`

`HiSparseWorker`

`HiSparseRuntime`

`HiSparseRuntime`

`HiSparseCacheHandle`

The key distinction is logical allocation versus contents. [ HiSparseCoordinator](https://docs.vllm.ai/api/vllm/v1/hisparse/coordinator/#vllm.v1.hisparse.coordinator.HiSparseCoordinator) owns host block IDs and their request/prefix associations.

`HiSparseWorker`

and its per-cache runtimes own the corresponding bytes. The normal cache manager sees only device pools. The source group has `block_pool_id=None`

; device-pool consumers must narrow it before indexing, so host ownership cannot masquerade as a numeric GPU pool.For single-node MP tensor parallelism, every TP worker maps the same pinned host pool and uses the same block and layer offsets. MLA source KV is replicated across TP ranks, so this stores one physical copy instead of one copy per rank. TP rank 0 writes the shared host pool; peers wait on its IPC events before reading it. Other executor and parallel layouts retain private per-rank pools.

The shared layout backs the per-replica logical capacity with one physical pool; the private layout allocates one physical pool per rank. Physical pool size includes block-stride alignment.

## Code boundary[¶](https://docs.vllm.ai#code-boundary)

scheduler process worker process
HiSparseConnector HiSparseConnector
└─ HiSparseCoordinator └─ HiSparseWorker
│ │
│ connector metadata ├─ host bytes
│ - page transfers ├─ copy scheduling
│ - block-table replacements └─ per-layer hot state
└───────────────────────────────────────────────►│
◄──────── connector worker metadata ─────────────┘
enqueued and completed transfer IDs


The command travels in `kv_connector_metadata`

; transfer updates return in `KVConnectorOutput.kv_connector_worker_meta`

. The model runner does not interpret page transfers. Enqueue acknowledgements let the scheduler release source leases in stream order; completion acknowledgements publish the copied host pages.

## Resident device pages[¶](https://docs.vllm.ai#resident-device-pages)

Resident pages are intentionally outside [ HiSparseRuntime](https://docs.vllm.ai/api/vllm/v1/hisparse/runtime/#vllm.v1.hisparse.runtime.HiSparseRuntime).

KV-cache initialization binds cache-manager allocations to the attention-facing [ HiSparseCacheHandle](https://docs.vllm.ai/api/vllm/v1/hisparse/runtime/#vllm.v1.hisparse.runtime.HiSparseCacheHandle) before constructing

`HiSparseWorker`

. That same handle's runtime retains the resident source index needed by a transfer plan. There is no second resident object or registration wrapper.KV cache setup
│
├─ bind resident allocation ──► HiSparseCacheHandle
│ cache + block table + slot mapping
│
├─ bind host/hot allocation ──► HiSparseRuntime
│ host + hot + GPU LRU
│
└─ register cache handles ────► HiSparseWorker
step-level transfers
HiSparseWorker registers the same HiSparseCacheHandle objects directly


Attention construction links each layer to the most recent layer that actually owns an indexer. This releases a follower's duplicate LRU tensors before GPU memory profiling. Cache binding only attaches storage; it does not infer semantic groups from the physical packed-tensor order. The construction cursor is discarded with the worker's pinned state.

Every HiSparse decode batch uses the same fused resolver. It checks resident pages first, then hot rows, then pinned host memory. A resident hit exits inside the kernel before hot-LRU lookup or host copying; there is no framework-level residency route or separate CUDA graph. No CPU decision is added to the decode path. The resolver consumes the existing graph-stable request mapping from attention metadata; neither the worker nor individual cache handles keep a duplicate mapping.

Speculative decoding resolves and consumes each verification step in order. Each step receives distinct replayable plan rows while sharing the request's hot-cache state, so a later step cannot reuse a hot row before an earlier step has consumed it.

## P/D import target[¶](https://docs.vllm.ai#pd-import-target)

The decoder chooses the landing target once per request from the normal cache admission calculation. If the complete imported prefix fits the device pools, NIXL transfers it directly into resident GPU pages. Otherwise, if the fixed host-backed GPU footprint and host source blocks fit, the request imports into the host tier. There is no context-length threshold or other heuristic, and a request waiting for capacity retains its choice across admission retries.

A host import reads through a bounded decoder-GPU staging pool before copying into registered host memory. Pages needed immediately are mirrored into their resident destinations during that copy. Both landing targets then use the same fused decode resolver described above.

## Indexer KV offloading[¶](https://docs.vllm.ai#indexer-kv-offloading)

HiSparse does not keep a private CPU copy of indexer KV. The indexer remains a normal prefix-cacheable GPU cache group. If `OffloadingConnector`

is configured with HiSparse, it stores and restores that group through the generic KV offloading path; HiSparse continues to own only the sparse MLA host tier.

The two prefix sources can have different hit lengths. When the HiSparse host prefix extends beyond the GPU-resident indexer prefix, the scheduler asks `OffloadingConnector`

to restore only the missing indexer suffix, capped at the host prefix boundary. If that suffix is unavailable, all groups fall back to the shorter prefix they share. NIXL P/D transfers continue to place indexer KV directly in its GPU group.

## Spill transaction[¶](https://docs.vllm.ai#spill-transaction)

A resident block cannot be reused until its contents have been handed to the worker.

HiSparseCoordinator HiSparseWorker
│ │
│ pin source and destination leases │
│── SparseKVPageTransfer ─────────────►│
│ │ enqueue GPU-to-host copy
│◄── enqueued transfer ID ────────────│
│ replace resident table entry │
│ release resident lease to HMA │
│ │ copy reaches its event
│◄── completed transfer ID ───────────│
│ mark host page valid │
│ release destination host lease │


“Enqueued” means the copy has entered the worker stream. Stream ordering makes it safe to reuse the resident GPU block for later work, but the host page is not yet published. “Completed” means the worker has observed the copy's event; only then does the coordinator publish the host page for prefix reuse and release its destination lease. A host-write event separately protects direct CPU readers from writes already queued on the accelerator.

The worker transfer contains only its transfer ID and physical copy coordinates. Request identity and logical page state remain in the scheduler.

## Hot lookup and LRU[¶](https://docs.vllm.ai#hot-lookup-and-lru)

The NVIDIA CUDA path keeps replacement entirely on the accelerator:

top-K logical positions
│
▼
resident page? ── yes ──► resident physical row
│ no
▼
hot row? ──────── yes ──► existing hot physical row + update GPU LRU
│ no
▼
choose GPU LRU victim ──► copy pinned host row ──► hot physical row


ROCm is not currently supported because the fused HiSparse cache operations are implemented only by CUDA kernels. A future platform-specific worker may provide the same command, output, and cache-resolution boundaries.

## Main classes[¶](https://docs.vllm.ai#main-classes)

| Class | Inherits / implements | Responsibility |
|---|---|---|
`HiSparseCoordinator` |

`HiSparseConnector`

[,](https://docs.vllm.ai/api/vllm/distributed/kv_transfer/kv_connector/v1/base/#vllm.distributed.kv_transfer.kv_connector.v1.base.KVConnectorBase_V1)`KVConnectorBase_V1`

`SupportsHMA`

`HiSparseResidentManager`

`SingleTypeKVCacheManager`

`PagedCacheView`

`HiSparseWorker`

`HiSparseRuntime`

`HiSparseCacheHandle`

`SparseKVOffloadCommand`

## Performance invariants[¶](https://docs.vllm.ai#performance-invariants)

- Resident hits bypass hot-LRU lookup and host copies inside the fused resolver.
- Hot lookup, victim selection, and LRU updates stay on the GPU.
- A hot miss still copies directly from registered pinned host memory.
- Top-K resolution stays inside the attention invocation and remains graph capturable.
- Compatible layers still share one miss plan.
- Index-sharing followers release their private LRU state before memory sizing.
- Indexer KV is untouched by HiSparse unless a generic KV offloader is configured.
- Resident and hot leases can still share one packed HMA allocation.
- No device scalar readback or CPU/device metadata round trip is added.
- The abstraction wraps the fused kernel; it does not add another kernel launch.
- When HiSparse is disabled, the scheduler does not construct an offload command or empty update table.

## What remains platform-specific[¶](https://docs.vllm.ai#what-remains-platform-specific)

The command/result and attention-layer boundaries can be shared. The host allocator, copy implementation, hot layout, and replacement policy should stay platform-specific. NVIDIA uses the current accelerator LRU and fused host/hot kernel. ROCm is not currently supported; AMD or other accelerator backends can implement their own worker without forcing NVIDIA's policy into the shared boundary.