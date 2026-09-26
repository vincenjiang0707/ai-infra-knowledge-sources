# [Issue #3132] Streaming Subgraph Prefetching - Overlap Disk I/O with Computation

source: https://github.com/vllm-project/llm-compressor/issues/3132
state: open | updated: 2026-09-23T02:29:33Z
labels: enhancement

## 正文

## Objective

Overlap disk I/O for the next subgraph with computation on the current subgraph to reduce overall runtime for large model processing.

## Current Behavior

Processing currently follows a strictly serial pattern:

```text
read weights
transfer weights
compute
read next weights
transfer next weights
compute
...
```

For sufficiently large models, disk reads can contribute significantly to total runtime.

## Proposed Improvement

Since the identity of the next subgraph is already known, its parameters should be prefetched into CPU memory while the current subgraph is being processed on the GPU:

```text
GPU:   [ compute layer N       ][ compute layer N+1     ]
CPU:           [ transfer N+1 ]       [ transfer N+2 ]
Disk:  [ read N+1           ][ read N+2           ]
```

## Proposed Implementation

```python
prefetcher = Prefetcher(...)

prefetcher.submit(subgraphs[0])

for i, subgraph in enumerate(subgraphs):
    prefetched = prefetcher.wait(subgraph)

    if i + 1 < len(subgraphs):
        prefetcher.submit(subgraphs[i + 1])

    move_to_device(prefetched, main_device)
    subgraph(batch)
```

## Key Considerations

- Prefetching should materialize parameters on **CPU** rather than triggering their normal onload path to the GPU
- Prefetching should be bounded to avoid excessive CPU memory usage
  - Initially: current on GPU, next on CPU, rest on disk
- Should not regress performance on systems where storage bandwidth is not the bottleneck
- Requires a mechanism to explicitly materialize offloaded parameters onto CPU while keeping them associated with modules

## Expected Benefits

- Hide disk-read latency behind GPU computation
- Reduced total processing time for very large models
- Improved utilization of system resources by enabling concurrent operations across GPU, CPU, and disk

## 评论 (9)

### aayush7511 · 2026-09-08

@kylesayrs Hi, can I work on this? 

### aayush7511 · 2026-09-09

Wanted to follow up on this

### ishrith-gowda · 2026-09-17

Before anyone builds the prefetcher, there is a detail in the current load path that changes what it has to do.

`DiskCache.onload` ends with:

```python
onloaded = file.get_tensor(weight_info["weight_name"])
onloaded = to_tensor(onloaded, offloaded)
onloaded = onloaded.to(getattr(torch, weight_info["dtype"]))
```

`safe_open(...).get_tensor(...)` returns a lazily mapped tensor rather than an eager copy, and `.to(dtype)` is a no-op when the dtype already matches. So whether onload actually reads from disk depends on whether that cast is real. Measured on a 134 MB offloaded tensor, cold:

```
  dtype matches (cast is a no-op)   onload   55.42 ms | first touch 3838.39 ms
  dtype differs (cast materializes) onload 3821.04 ms | first touch    3.03 ms
```

When the dtype matches, the disk read is deferred to whenever the weights are first touched, which is inside the forward pass. The serial picture in the issue description

```
read weights
transfer weights
compute
```

is then not what happens: the read is already interleaved with compute at page-fault granularity.

Two consequences for the design:

1. A prefetcher that just calls `onload` early on a background thread will prefetch the header and the mapping, not the data. In the dtype-matching case it would do close to nothing. To actually prefetch it has to force materialization, for example by touching the pages explicitly.
2. How much there is to win depends on which of the two regimes a given run is in. Worth measuring on a real model before sizing the work, because in the lazy regime the OS is already overlapping some of this for free, and the gain is the difference between page-fault-driven overlap and explicit prefetch, not the full read time.

I have not started an implementation and am not claiming this issue. @aayush7511 mentioned interest on Sep 8. Posting because it seemed better to surface before someone builds against the serial model.

Related: this came out of measuring the read path for #3133, where the same laziness is why per-open header parsing dominates grouped reads.


### ishrith-gowda · 2026-09-17

Following up on my own comment to make it definite rather than conditional: the lazy regime is the normal one, not a coin flip.

Both paths that populate `DiskCache.index` carry the stored dtype through unchanged:

- `DiskCache.offload` records `"dtype": str(tensor.dtype)` for the same tensor it then passes to `save_file`, so the recorded dtype and the file's dtype are identical by construction (`offload/cache/disk.py:112`).
- `create_checkpoint_symlink` copies `weight_info["dtype"]` straight from the source index, and logs a warning if it disagrees with the offloaded meta tensor (`offload/cache/disk.py:178-195`).

So `.to(getattr(torch, weight_info["dtype"]))` in `onload` is a no-op in the ordinary case, and the code treats a mismatch as a condition worth warning about rather than a normal path.

That means the measurement I posted above is the default behaviour: onload maps, and the read happens when the weights are first touched during the forward pass. A prefetcher built against the serial model would need to force materialization to move any I/O at all.


### xesdiny · 2026-09-22

### Prototype: Phase 4b Async Subgraph Prefetch (Dense + MoE)

We've implemented and benchmarked a prototype of the streaming subgraph prefetch described in this issue, extended to MoE models. This is the first of three comments — covering architecture and implementation details. The second covers methodology and related PRs; the third covers results.

Hardware: single NVIDIA L20 (48 GB), GPTQ W4A16, offload to NFS. Each configuration repeated 3×.


---

#### What We Built (Phase 4b)

The original `SequentialPipeline` (Phase 1) executes serially per subgraph:

```
disk → [blocking read] → CPU → [blocking H2D] → GPU compute → [evict back to disk]
```

Phase 4b replaces this with a meta-device workflow. The base architecture (`device_map="meta"` startup, `CheckpointMap`, `stage_modules`, `SubgraphPrefetcher`, `commit_staged`, `release_modules → meta`) was introduced by [PR #3111](https://github.com/vllm-project/llm-compressor/pull/3111) (@Isotr0py, `StreamingPipeline`). Phase 4b adds one layer on top:

1. **Instant model load** — `from_pretrained(device_map="meta")` + `load_quantizable_moe()` ([PR #3208](https://github.com/vllm-project/llm-compressor/pull/3208), @Roderick-Wu): model structure initialized in ~0.2s (MoE: ~15–26s), all params on `meta`, no data read. For MoE, `load_quantizable_moe()` linearizes 2D-format expert weights at load time so no separate linearization step is needed in the pipeline loop.
2. **CheckpointMap** — lightweight safetensors header scan, builds `{param_fqn → (shard, offset)}` index without reading any weights (PR #3111 design).
3. **MetaSubgraphPrefetcher** — background thread reads next subgraph's weights NFS→CPU during current subgraph's GPU compute (extended from PR #3111's `SubgraphPrefetcher`).
4. **`commit_staged_async`** — H2D transfer queued on a dedicated CUDA stream (non-blocking). **This is the sole addition over PR #3111**, which uses blocking `commit_staged`.
5. **`release_modules → meta`** — after compute, GPU params replaced with fresh meta tensors in <1ms; no disk write (same as PR #3111).

The three-layer pipeline this produces:

```
Disk bg:    [read sg_N+1 ──────────]
H2D stream:                   [DMA sg_N+1 ──]
GPU:        [compute sg_N          ]  [wait ≈0ms]  [compute sg_N+1 ────]
```

**Correctness**: On Qwen3-0.6B (476/476 disk tensors), all weights injected correctly; calibration result bit-identical to Phase 1 baseline. MoE expert quantization on 30B confirmed post-run: 18,432 modules (`hasattr(mod, "weight_scale")`) = 128 experts × 3 projections × 48 MoE layers.

---

#### Re: @ishrith-gowda's Comments on Lazy mmap

The observation is correct. `safe_open(...).get_tensor(...)` returns a lazy mmap-backed tensor — no physical I/O until page faults occur. We confirmed the same in our implementation:

```
get_tensor() for 311 MB tensor:  0.08ms  (maps the file only)
.clone() after get_tensor():    1243ms  (actual NFS read)
```

Our original `stage_modules` called only `get_tensor()`, deferring actual disk reads to the CUDA DMA path during `commit_staged_async`. We've since added an explicit `.clone()` in the background thread:

```python
tensor = f.get_tensor(key)
tensor = tensor.clone()  # forces page faults in bg thread → genuine 3-layer overlap
```

With this fix, disk→CPU reads happen entirely in the background thread; `commit_staged_async` then runs pinned-memory DMA with no page-fault stalls.

#### Re: Grouped Reads and PR #883

`CheckpointMap` + `stage_modules` already groups reads by shard: each shard file is opened once and all its tensors are read in one pass. For MoE, a single subgraph may reference up to 128 × 3 = 384 tensors from the same shard — grouping is especially important here.

This is functionally equivalent to what `disk_load_context()` in [CT PR #883](https://github.com/vllm-project/compressed-tensors/pull/883) (@ishrith-gowda) does for the DiskCache path. One difference: PR #883's benefit applies to **original checkpoint shards** (multiple tensors per file); CT-written OffloadCache files are one-tensor-per-file, so Phase 1's hot path sees no improvement from PR #883. Phase 4b reads directly from original checkpoint shards and naturally groups those reads.


### xesdiny · 2026-09-22

#### Metric Alignment: How to Compare P1 and P4b

P1 and P4b report different fields. The correct comparison:

| Dimension | Phase 1 | Phase 4b |
|-----------|---------|---------|
| **Total time** | `load_s + wall_s` | `load_s + wall_s` |
| Model load | `load_s` (DiskCache write: MoE ~430–3200s) | `load_s` (meta init: MoE ~0.2–26s) |
| Pipeline | `wall_s = disk_wait_s + evict_s + compute≈` | `wall_s ≈ compute_s` |
| Async wait | — | `inject_wait_s` (target ≈ 0ms) |
| I/O efficiency | — | `compute_s / wall_s` (target ≥ 92%) |

> **Important for MoE**: `wall_s` alone is not the right comparison. Phase 1 MoE builds a DiskCache at load time (30B: ~430–670s; 235B: ~2400–3200s). Phase 4b avoids this entirely. Always compare `load_s + wall_s` (total).

**Memory constraints (bench setup)**: P1 uses `max_memory={0:"6GB", cpu:"8GB"}` to force DiskCache offload, simulating single-GPU deployment of a model that doesn't fit in VRAM. P4b uses no memory constraints — `device_map="meta"` means no VRAM is consumed at load; only the active subgraph's weights and Hessian reside on GPU during the pipeline.

---

#### Implementation Notes

**Scope**: ~500 lines in 2 new files (`meta_checkpoint_map.py`, bench harness). No changes to core `SequentialPipeline`. Compatible with `LifecycleCallbacks`, GPTQ modifier, and `trace_subgraphs`.

**Dependency on PR #3208**: MoE support in this prototype relies on `load_quantizable_moe()` and the linearize framework from [PR #3208](https://github.com/vllm-project/llm-compressor/pull/3208) (@Roderick-Wu). The P4b files implement the meta-device pipeline; `load_quantizable_moe()` handles MoE expert linearization at load time. These are complementary and would need to be integrated together in any upstreaming effort.

---

#### Related PRs

- **[PR #3111](https://github.com/vllm-project/llm-compressor/pull/3111)** (@Isotr0py) — StreamingPipeline: the original meta-device streaming pipeline. Introduced `device_map="meta"` startup, `CheckpointMap`, `stage_modules`, `SubgraphPrefetcher`, `commit_staged` (blocking H2D), and `release_modules → meta` (2-layer overlap: disk ∥ compute). Phase 4b builds on this architecture and adds async H2D via CUDA stream (`commit_staged_async`) for 3-layer overlap.
- **[PR #3208](https://github.com/vllm-project/llm-compressor/pull/3208)** (@Roderick-Wu) — Sequential Offloading, Linearization + Repacking: provides `load_quantizable_moe()`, `linearize_moe_subgraph()`, `repack_moe_subgraph()`, and `offloading.py`. This prototype's MoE support depends on PR #3208's linearize framework.
- **[PR #3209](https://github.com/vllm-project/llm-compressor/pull/3209)** (@Roderick-Wu) — Sequential Pipeline Prefetching Threads: parallel work on DiskCache-path async prefetching (complements this meta-device approach for the existing DiskCache pipeline).
- **[PR #2995](https://github.com/vllm-project/llm-compressor/pull/2995)** (@kylesayrs) — "Add layerwise decompression and compression to sequential pipeline": llm-compressor-side implementation of per-subgraph quantization state control (`layerwise_decompression`, `layerwise_compression` flags). Companion [CT PR #811](https://github.com/vllm-project/compressed-tensors/pull/811) provides the underlying `allowed_modules` and `leave_decompressed=False` primitives. Not yet integrated in this prototype.
- **[CT PR #883](https://github.com/vllm-project/compressed-tensors/pull/883)** (@ishrith-gowda) — `disk_load_context()`: grouped shard reads for DiskCache path. Functionally equivalent to what `CheckpointMap` + `stage_modules` does for the meta-device path; would be the clean integration point if this approach is upstreamed into the DiskCache pipeline.


### xesdiny · 2026-09-22

#### Dense Models: Phase 1 vs Phase 4b

Hardware: single L20. P1: `max_memory={0:"6GB", cpu:"8GB"}` to force DiskCache offload (simulates memory-constrained deployment). P4b: no memory constraint — `device_map="meta"` at load (≈0 VRAM); only the active subgraph's weights and Hessian reside on GPU during the pipeline. Each row is mean of 3 runs.

**27B (Qwen3.8-27B, ~52 GB bf16)**

| Config | P1 wall | P1 I/O (dw+evict) | P4b wall | P4b compute/wall | Speedup |
|--------|---------|--------------------|---------|-----------------|---------|
| N=16, sl=256 | 292s | 52+109=161s (55%) | 223s | 97.4% | **1.31×** |
| N=128, sl=256 | 523s | 73+117=190s (36%) | 409s | 98.5% | **1.28×** |
| N=16, sl=2048 | 385s | 66+108=174s (45%) | 925s | 98.3% | 0.42× |
| N=128, sl=2048 | 1214s | 84+126=210s (17%) | 1176s | 98.8% | **1.03×** |

**72B (Qwen2.5-72B, ~136 GB bf16)**

| Config | P1 wall | P1 I/O (dw+evict) | P4b wall | P4b compute/wall | Speedup |
|--------|---------|--------------------|---------|-----------------|---------|
| N=16, sl=256 | 985s | 197+276=473s (48%) | 1983s | 98.8% | 0.50× |
| N=128, sl=256 | 1507s | 228+293=521s (35%) | 2422s | 99.0% | 0.62× |
| N=16, sl=2048 | 1398s* | 252+331=583s (42%) | 1987s | 98.9% | 0.70× |
| N=128, sl=2048 | 4002s | 334+332=666s (17%) | 2640s | 99.4% | **1.52×** |

*72B N=16 sl=2048: one NFS-congested run excluded (disk_wait=962s); average of remaining 2 runs.

`inject_wait_s` ≈ 0ms across all dense configurations (0.005–0.029s total across all subgraphs). P4b wins when N ≥ 128 or calibration compute dominates. At N=16, per-subgraph weight size (~330 MB for 72B) creates PCIe contention that outweighs I/O savings. At N=128 sl=2048, P4b's compute actually runs faster than P1's (72B: 2624s vs 3337s), suggesting removal of CPU-GPU synchronization overhead improves GPU utilization.

---

#### MoE 30B: Phase 1 vs Phase 4b

Model: Qwen3-30B-A3B (128 experts, 48 MoE layers, ~57 GB bf16). 49 GPTQ subgraphs. For MoE, `load_s` must be included — Phase 1 writes the full model to DiskCache before quantization begins.

| Config | P1 load | P1 wall | P1 total | P4b load | P4b wall | P4b total | Speedup (total) |
|--------|---------|---------|---------|---------|---------|---------|----------------|
| N=16, sl=256 | 567s | 276s | **843s** | 0.2s | 56s | **56s** | **15.1×** |
| N=128, sl=256 | 430s | 566s | **996s** | 0.2s | 298s | **298s** | **3.3×** |
| N=16, sl=2048 | 573s | 253s | **826s** | 21.5s | 696s | **718s** | **1.15×** |
| N=128, sl=2048 | 673s | 617s | **1290s** | 18.1s | 925s | **943s** | **1.37×** |
| N=256, sl=256 | 411s | 861s | **1271s** | 13s | 8697s | **8709s** | **6.9× slower** ❌ |
| N=256, sl=2048 | 393s | 892s | **1285s** | 11.2s | 8707s | **8719s** | **6.8× slower** ❌ |


P4b `compute/wall` for N=16/128: 32–95% (N=16 sl=2048 staging exceeds compute window; N=128 fully hidden). N=256: 99.3–99.4% (I/O fully hidden, but compute itself is the problem — see limitation below).

**Why P4b wins for N=16/128**: Phase 1 `load_s` (430–673s) is writing ~57 GB of expert weights to NFS DiskCache. Phase 4b avoids this entirely. Even at N=16 sl=2048 where P4b's pipeline is 2.75× slower (NFS staging exceeds compute window), the load_s saving (~552s) more than covers the pipeline penalty (~443s). Phase 1's `evict_s` (99–118s, 19–45% of wall) is also eliminated by `release → meta`.

Additionally, Phase 1 requires a separate `linearize_moe_model()` pass: in production runs without the artificial memory cap, this costs 1720–1869s (>99% of Phase 1's `disk_wait_s`). Phase 4b linearizes at load time via `load_quantizable_moe()`. Real end-to-end result: Phase 1 ~9472s (r1/r2 avg) → Phase 4b ~7069s, **~1.34×** — with 18,432 expert modules confirmed quantized.

---

#### MoE 235B: Phase 1 vs Phase 4b

Model: Qwen3-235B-A22B (~447 GB bf16). Phase 1 DiskCache: ~2400–3200s load. Phase 4b meta init: ~26s. 3 runs each.

| Config | P1 load | P1 wall | P1 total | P4b load | P4b wall | P4b total | Speedup |
|--------|---------|---------|---------|---------|---------|---------|---------|
| N=16, sl=256 | 3189s | 2116s | **5305s** | 36.9s | 3060s | **3097s** | **1.71×** |
| N=16, sl=2048 | 2836s | 2048s | **4884s** | 24.4s | 2784s | **2808s** | **1.74×** |
| N=128, sl=256 | 2430s | 2539s | **4968s** | 24.2s | 3624s | **3648s** | **1.36×** |
| N=128, sl=2048 | 2565s† | 2932s† | **5497s†** | 23.3s | 4423s | **4447s** | **1.24×†** |
| N=256, sl=256 | 3682s‡ | 3622s | **7303s‡** | 23.9s | 6037s | **6061s** | **1.21×‡** |
| N=256, sl=2048 | 4211s | 4286s | **8497s** | 22.2s | 7803s | **7825s** | **1.09×** |

†N=128 sl=2048 r3: NFS congestion during concurrent runs; stable reference (r1+r2 avg): P1 5289s → P4b 4447s, **1.19×**.  
‡N=256 sl=256: NFS bandwidth contention from concurrent DiskCache writes. Single-run reference (r1): P1 6323s → P4b 6061s, **1.04×**.

`inject_wait_s` (total across all subgraphs): 0.010–0.011s — effectively zero. `compute/wall`: N=16: 37–44% (NFS staging exceeds compute window per subgraph); N=128: 92–94% ✅; N=256: 95–96% ✅.

---

#### Summary

**`inject_wait_s` ≈ 0ms is consistent across all 48 configurations tested** (dense 27B/72B × 4 configs × P4b; MoE 30B × 6 configs; MoE 235B × 6 configs). The async H2D mechanism works as designed.

**Dense models**

| Scenario | P4b outcome | Dominant factor |
|----------|-------------|-----------------|
| Small N (N=16), any model | Mixed — P4b slower for 72B | I/O savings < compute overhead |
| Large N (N≥128), sl=2048 | **P4b wins** (72B: 1.52×) | GPTQ compute dominates; sync overhead amortized |

**MoE models**

| Model | Best speedup | Worst case | Key driver |
|-------|-------------|------------|-----------|
| 30B-A3B (N=16–128) | **15.1×** (N=16 sl=256) | **1.15×** (N=16 sl=2048) | `load_s` elimination (430–670s → 0.2s) |
| 235B-A22B | **1.74×** (N=16 sl=2048) | **1.09×** (N=256 sl=2048) | `load_s` elimination (2400–3200s → 26s) |

For MoE (N=16 to N=128), P4b wins in all tested configurations. The `load_s` saving (430–3200s) guarantees a positive outcome even when the pipeline-level comparison is unfavorable.

**Notably, this approach brings vLLM's deployment-time weight loading pattern to calibration**: model structure initialized on `meta` device, weights streamed to GPU subgraph-by-subgraph on demand, nothing retained after each step. The result is that a 235B model (~447 GB bf16) can be fully GPTQ-calibrated end-to-end on a single L20 (48 GB GPU) — no model sharding, no multi-GPU coordination.

---

#### Limitations

**MoE Limitation 1: 3D Checkpoint Format (Qwen3.5-35B-A3B)**

The Phase 4b approach does not work for **Qwen3.5-35B-A3B** (`qwen3_5_moe` architecture). Its experts are stored as stacked 3D tensors. `load_quantizable_moe()` is a no-op for this architecture (`has_linearize_load_mappings=False` — not in `ARCH_TO_2D_MAPPINGS`), so linearization is deferred to pipeline execution after GPTQ hooks have already registered. Measured impact: `linearize_s = 12276s` (94% of total wall in a 2-layer probe). Fix: add `"qwen3_5_moe": "qwen2_moe"` to `ARCH_TO_2D_MAPPINGS` (1-line fix) or move `linearize_moe_model()` before `calibration_start()`.

**MoE Limitation 2: N=256 GPTQ Compute Explosion (30B)**

At N=256, P4b's pipeline efficiency remains excellent (`inject_wait_s ≈ 0ms`, `compute/wall ≈ 99%`), but the GPTQ compute itself explodes: per-weight-matrix time increases from ~0.016s at N=128 to ~0.47s at N=256 (gate≈0.64s, up≈0.64s, down≈0.23s, per-expert≈1.5s — 30× increase), causing P4b wall ~8700s vs P1 wall ~861s. Including `load_s`, P4b total is ~6.8–6.9× **slower** than P1 at N=256. This is not an I/O or GPU-contention issue — verified by clean re-runs on an isolated GPU. Root cause: `LinearExperts2D` GPTQ hits a non-linear computation regime at N=256 Hessian size; P1 is unaffected because its expert parameters are stored as scalars with a different solve path. N=256 is not a production-relevant calibration size for most use cases; N=16–128 results are unaffected.

---

#### Planned Next Steps

The current implementation delivers the prefetch + async H2D layer (#3132). The full per-subgraph pipeline vision has two remaining pieces:

- **Layerwise quantization apply/compress ([PR #2995](https://github.com/vllm-project/llm-compressor/pull/2995), @kylesayrs)**: Adds `layerwise_decompression` and `layerwise_compression` flags to `SequentialPipeline`, enabling per-subgraph quantization state control. Companion [CT PR #811](https://github.com/vllm-project/compressed-tensors/pull/811) provides the underlying primitives: `allowed_modules` (restrict `apply_quantization_config` to the current subgraph) and `leave_decompressed=False` (clear all quantization state after `decompress_module`, so the module can be safely released to `meta`). With these in place, the full per-subgraph loop becomes: `prefetch → apply(subgraph) → calibrate → compress → decompress(clear) → release → meta`.

- **Streaming model saving ([#3131](https://github.com/vllm-project/llm-compressor/issues/3131))**: Once PR #2995 is integrated, the remaining gap is `stream_write` — incremental safetensors shard writing that flushes each subgraph's compressed weights to disk immediately after the compress step, before `decompress(clear)` and `release → meta`. This eliminates the need to hold the full quantized model in memory before the final `save_pretrained()` call.

- **`disk_load_context()` integration ([CT PR #883](https://github.com/vllm-project/compressed-tensors/pull/883), @ishrith-gowda)**: Once CT PR #883 lands, `stage_modules`' background-thread read pass can use `disk_load_context()` as the integration point for the DiskCache path, keeping both paths consistent.

---

*Hardware: single NVIDIA L20 (48 GB), NFS offload*  
*Dense: Qwen3.8-27B and Qwen2.5-72B, GPTQ W4A16, 3 rounds × 4 (N, sl) configs each*  
*MoE: Qwen3-30B-A3B (128 experts, 2D ckpt, 3 rounds × 6 configs); Qwen3-235B-A22B (3 rounds × 6 configs)*  

### xesdiny · 2026-09-22

#### Follow-up: Discussion Draft PR

Based on the benchmark results above, we've opened a discussion Draft PR:

**[PR #3216: [Discussion] StreamingPipeline: meta-device async subgraph prefetch for dense + MoE](https://github.com/vllm-project/llm-compressor/pull/3216)**

The PR contains:
- `checkpoint.py`: `CheckpointMap`, `stage_modules`, `commit_staged_async`, `release_modules`, `MetaSubgraphPrefetcher` — the core streaming utilities benchmarked above
- `pipeline.py`: `StreamingPipeline(CalibrationPipeline)` skeleton (placeholder, `NotImplementedError`)
- `__init__.py`: public exports

`pipeline.py` is intentionally left unimplemented — the goal is to discuss the `checkpoint.py` design and the async H2D approach before writing the full `__call__` loop. Three open questions are listed in the PR description.


### Roderick-Wu · 2026-09-22

Hi @xesdiny 

I believe the current plan is to augment the sequential pipeline to include the option for streaming prefetching instead of creating a new pipeline from scratch. I think it might be good to wait until we land the linearization, offloading, and layerwise decompression+comrpession changes before building on top. That being said, is there an existing branch to take a look at?
