# [Issue #3752] [Feature] L1/L2/L3 cache hit rate observability — Prometheus metrics, OTel spans & per-request JSONL trace

source: https://github.com/LMCache/LMCache/issues/3752
state: open | updated: 2026-09-27T01:56:48Z
labels: stale

## 正文

### Motivation

LMCache's current `PrometheusLogger` provides basic metrics (`time_to_retrieve`, `num_retrieve_requests`), but is missing:

1. **Per-tier cache hit rate** — no way to distinguish whether a hit came from L2 (CPU RAM), L3 (NVMe Disk), or a remote backend.
2. **TTFT decomposition** — `frontend_latency` (API server → engine core) and per-request `kv_lookup_time` / `kv_retrieve_time` are not surfaced.
3. **Per-request tracing** — no way to correlate cache-hit details to an individual request for debugging latency spikes.

These gaps make it hard to answer operational questions like: *"Why did TTFT spike — was it a slow disk read, CPU cache contention, or GPU prefix cache eviction?"*

---

### Design Goals

1. **Three-layer observability model**: throughput → latency → cache hit rate
2. **Minimally invasive**: extend existing `LMCStatsMonitor`, `PrometheusLogger`, and `cache_engine` — no breaking API changes
3. **TP-aware**: cross-process bridge via `/dev/shm` for Worker ↔ EngineCore per-request data relay when TP > 1
4. **Self-verifying**: every trace carries token identity equations for automated correctness validation

---

### Proposed Design

#### Layer 1 — Throughput: Token Source Decomposition

```
Tokens/s = local_compute + L1_hit + L2_hit + L3_hit + remote_hit
```

**Approach**: Extend `cache_engine.py`'s `retrieve()` / `retrieve_layer()` to classify hit tokens by storage backend. Add a `_BACKEND_NAME_TO_HIT_TIER` mapping:

| Backend | Tier |
|---------|------|
| `LocalCPUBackend` | L2 |
| `LocalDiskBackend` / `GdsBackend` | L3 |
| `RemoteBackend` | Remote |

**New Prometheus metrics** (6 total):

| Metric | Type |
|--------|------|
| `lmcache:l2_hit_tokens` / `lmcache:num_l2_hit_tokens` | Histogram + Counter |
| `lmcache:l3_hit_tokens` / `lmcache:num_l3_hit_tokens` | Histogram + Counter |
| `lmcache:remote_hit_tokens` / `lmcache:num_remote_hit_tokens` | Histogram + Counter |

#### Layer 2 — Latency: TTFT Decomposition

```
TTFT = frontend_latency + queue_time + prefill_time
prefill_time ⊃ kv_lookup_time + kv_retrieve_time
```

**Approach**: Add `LMCacheKVConnectorStats` (extending vLLM's `KVConnectorStats`) on the vLLM side, and expose per-request timing through `vllm_v1_adapter.py`'s `request_finished()` via `EngineCoreOutput.kv_transfer_params`.

**New Prometheus metrics** (9 bridge metrics + 1 framework metric):

| Metric | Type | Description |
|--------|------|-------------|
| `vllm:lmcache_kv_lookup_seconds` | Histogram | KV lookup latency |
| `vllm:lmcache_kv_retrieve_seconds` | Histogram | KV retrieve latency |
| `vllm:lmcache_retrieve_process_tokens_seconds` | Histogram | Retrieve: process_tokens phase |
| `vllm:lmcache_retrieve_to_gpu_seconds` | Histogram | Retrieve: CPU→GPU DMA phase |
| `vllm:lmcache_num_l2_hit_tokens` | Counter | vLLM-side L2 bridge |
| `vllm:lmcache_num_l3_hit_tokens` | Counter | vLLM-side L3 bridge |
| `vllm:lmcache_num_remote_hit_tokens` | Counter | vLLM-side remote bridge |
| `vllm:request_frontend_latency_seconds` | Histogram | API server → engine core latency |

#### Layer 3 — Cache Hit Rate & Per-Request Trace

One JSONL `[trace]` line emitted per request at completion:

```json
{
  "ts": 1782023561.679,
  "rid": "chatcmpl-xxx",
  "prompt_tokens": 3934,
  "output_tokens": 32,
  "TTFT_ms": 169.2,
  "queue_ms": 0.04,
  "prefill_ms": 130.1,
  "decode_ms": 144.6,
  "e2e_ms": 314.3,
  "frontend_ms": 39.0,
  "input_tokens_cache_hit": 3840,
  "L1_hit": 0,
  "external_kv_hit": 3840,
  "L2_hit": 0,
  "L3_hit": 3840,
  "remote_hit": 0,
  "input_tokens_no_cache_hit": 94,
  "kv_transfer_mode": "non_layerwise",
  "kv_lookup_ms": 1.2,
  "kv_retrieve_ms": 101.5
}
```

**Token identity equations** (verifiable by automated scripts at runtime):

```
prompt_tokens = input_tokens_cache_hit + input_tokens_no_cache_hit
input_tokens_cache_hit = L1_hit + external_kv_hit
external_kv_hit ≈ L2_hit + L3_hit + remote_hit   (≈ due to chunk_size=256 granularity)
```

#### Cross-Process Bridge (TP > 1)

When TP > 1, `retrieve()` runs on Worker_TP0 while `request_finished()` runs on the EngineCore/scheduler process. Per-request data is relayed via file-based bridge in `/dev/shm/lmcache_bridge/` (tmpfs, memory-backed):

- Per-tier counters: file + `fcntl.flock` for atomic cross-process updates
- Timing data: `write-tmp + os.replace` for atomic JSON
- Cleanup: throttled periodic sweep + retry limit (3) to prevent `/dev/shm` exhaustion

#### OTel Span Attributes

8 attributes on the `"llm_request"` span:

| Attribute | Description |
|-----------|-------------|
| `gen_ai.latency.time_in_frontend` | API → engine |
| `gen_ai.latency.time_in_kv_lookup` | KV lookup |
| `gen_ai.latency.time_in_kv_transfer` | KV retrieve |
| `gen_ai.usage.l1_hit_tokens` | L1 (GPU prefix cache) |
| `gen_ai.usage.l2_hit_tokens` | L2 (CPU RAM) |
| `gen_ai.usage.l3_hit_tokens` | L3 (NVMe/SSD) |
| `gen_ai.usage.remote_hit_tokens` | Remote backend |
| `gen_ai.latency.kv_transfer_mode` | layerwise / non_layerwise |

---

### Metrics Summary (16 new Prometheus metrics)

**LMCache side (6):**

| Metric | Type |
|--------|------|
| `lmcache:l2_hit_tokens` / `lmcache:num_l2_hit_tokens` | Histogram + Counter |
| `lmcache:l3_hit_tokens` / `lmcache:num_l3_hit_tokens` | Histogram + Counter |
| `lmcache:remote_hit_tokens` / `lmcache:num_remote_hit_tokens` | Histogram + Counter |

**vLLM bridge (9):**

| Metric | Type |
|--------|------|
| `vllm:lmcache_kv_lookup_seconds` | Histogram |
| `vllm:lmcache_kv_retrieve_seconds` | Histogram |
| `vllm:lmcache_retrieve_process_tokens_seconds` | Histogram |
| `vllm:lmcache_retrieve_to_gpu_seconds` | Histogram |
| `vllm:lmcache_num_l2_hit_tokens` | Counter |
| `vllm:lmcache_num_l3_hit_tokens` | Counter |
| `vllm:lmcache_num_remote_hit_tokens` | Counter |
| `vllm:lmcache_kv_transfer_mode` | Info |

**vLLM framework (1):**

| Metric | Type |
|--------|------|
| `vllm:request_frontend_latency_seconds` | Histogram |

---

### Verification

The design has been validated end-to-end on real hardware with the BEAM-10M benchmark across **3 cache configurations × ~15,000 requests**:

| Scenario | Cache Layers | Requests | TTFT p50/p95 | kv_retrieve p50 |
|----------|-------------|:---:|------:|------:|
| S1 | L1 + L3 (GDS NVMe) | 2000/2000 | 335ms / 10.8s | 210ms |
| S2 | L1 + L2 (CPU RAM) | 1927/1928 | 344ms / 10.6s | 22ms |
| S3 | L3 only (GDS NVMe) | 1400/1613 | 927ms / 38.4s | 400ms |

Token identity equations passed **0 violations across all ~15,000 requests**. An automated verification script (`verify_s3.py`) cross-checks bench client records against container-side traces with 100% RID alignment.

---

### Scope & Non-Goals

- **Scope**: vLLM v0.22.1+ (`KVConnectorBase_V1` infrastructure), LMCache v0.4.7+
- **Models**: uniform attention (MLA, Dense). Mixed attention (HMA) not yet supported
- **Changes**: ~1000 lines across 8 files, all additive extensions to existing infrastructure
- **Non-goals**: Dashboard/Grafana recipes (the metrics and traces produced are compatible with standard collectors)

---

### Key Design Decisions

1. **Counter vs Histogram name separation**: Counters use `lmcache:num_*`, Histograms use `lmcache:*_hit_tokens` — avoids `prometheus_client` stripping `_total` suffix from Counter names
2. **Non-destructive snapshot**: `get_stats_snapshot()` does not clear interval counters, avoiding conflict with the background `LMCacheStatsLogger` periodic clear cycle
3. **Per-request bridge deltas**: `request_finished()` maintains independent `_req_bridge_last_*` snapshots so periodic metric collection does not consume per-request delta data
4. **GDS memory allocator retry**: `get_blocking()` and `sync_disk_load()` use `allocate(busy_loop=True)` with configurable retries and `memcheck()` guard

---

### Would this be of interest to the LMCache project?

The design is verified end-to-end with production-grade benchmarking. We'd welcome community feedback before proceeding to implementation.

## 评论 (3)

### ajinkyajawale14499 · 2026-06-27

@grissomsh can I pick this?

### grissomsh · 2026-07-28

Great!

### github-actions[bot] · 2026-09-27

This issue has been automatically marked as stale because it has not had activity within 60 days. It will be automatically closed if no further activity occurs within 30 days.
