# [Issue #2949] [Feature] Zero-copy DDP weight sharing for memory-constrained large MoE quantization

source: https://github.com/vllm-project/llm-compressor/issues/2949
state: closed | updated: 2026-09-01T07:00:24Z
labels: 

## 正文

## Problem

When running GPTQ W4A16 quantization on large MoE models with limited system RAM, the current
`auto_offload` DDP approach is infeasible because each rank holds an independent copy of all
model weights in CPU memory.

**Concrete hardware constraint:**

- Model: `Qwen/Qwen3.5-122B-A10B` (≈244 GB in BF16)
- Hardware: 8× NVIDIA L20 (48 GB GPU each), system RAM < 743 GB
- `auto_offload` with 8 ranks: 8 × ~477 GB ≈ **3.8 TB CPU RAM required → not feasible**
  - The ~477 GB per rank accounts for both the raw model weights (≈244 GB) and the
    MoE expert linearization overhead: fused 3D expert tensors are expanded into
    per-expert `LinearExperts2D` modules during `from_experts_module`, temporarily
    holding both the original fused tensor and the linearized copy in memory.
- IPC sharing: ~477 GB total (rank 0 only) → **fits within 743 GB system RAM**

## Current behavior

`LinearExperts2D.from_experts_module` is called identically on every rank:

```python
# src/llmcompressor/modeling/moe/linear_experts.py
@classmethod
@torch.no_grad()
def from_experts_module(cls, experts, config):
    with skip_weights_initialize():
        self = cls(config)

    for index in range(self.num_experts):        # all ranks copy weights independently
        self[index].copy_from_experts_module(experts, index)

    offload_kwargs = get_cache_init_kwargs(experts)
    for module in self.modules():
        offload_module(module, **offload_kwargs)  # → DistributedCPUCache per rank

    return self
```

This results in N ranks × model size CPU RAM consumption, making large-scale DDP infeasible
on machines with limited system memory.

## Proposed solution

Add a `rank0_share` mode to `from_experts_module` that:

1. Only rank 0 copies expert weights from the fused experts tensor
2. Rank 0 shares weights with other ranks via OS file-system shared memory (zero physical copy)
3. Other ranks map the same physical pages using public PyTorch/Python APIs
4. The existing GPTQ DDP pipeline (`greedy_bin_packing` → `_reduce_hessian_to_target_rank` →
   `broadcast_qparams_and_cleanup`) continues to work unchanged — only weight loading changes

**Conceptual API change:**

```python
@classmethod
@torch.no_grad()
def from_experts_module(
    cls,
    experts: FusedExpertsProtocol,
    config: PreTrainedConfig,
    rank0_share: bool = False,   # new optional parameter, default=False for backward compat
):
    with skip_weights_initialize():
        self = cls(config)

    if not rank0_share or not is_distributed():
        # existing behavior: all ranks copy independently
        for index in range(self.num_experts):
            self[index].copy_from_experts_module(experts, index)
    else:
        # rank 0 copies weights, broadcasts shared memory handle to other ranks
        _rank0_ipc_copy_and_share(self, experts)

    offload_kwargs = get_cache_init_kwargs(experts)
    for module in self.modules():
        offload_module(module, **offload_kwargs)

    return self
```

The IPC sharing layer (`_rank0_ipc_copy_and_share`) can be implemented using
`torch.multiprocessing` with `file_system` sharing strategy and
`torch.UntypedStorage.from_file(filename, shared=True, size=...)` — public stable APIs only.

## Validated implementation

We have a working implementation of this approach validated on the full `Qwen3.5-122B-A10B`
quantization pipeline with 8× L20 GPUs:

- Expert weights are consolidated into a single flat buffer per MoE layer by rank 0
- Flat buffer is placed in `file_system` shared memory (creates a single temp file per layer,
  avoids POSIX `shm_open` segment limits — 48 layers = 48 files vs potential 36,000+ shm segments)
- Other ranks map the same physical pages via the shared file path broadcast over `gloo`
- GPTQ Hessian accumulation and parallel compression (`_reduce_hessian_to_target_rank`,
  `broadcast_qparams_and_cleanup`) work correctly on top of shared weights
- Quantization parameters (`weight_scale`, `weight_zero_point`, `weight_g_idx`) are
  per-rank CPUCache entries and are correctly synchronized via `broadcast_qparams_and_cleanup`

Hardware: 8× L20 (48 GB), system RAM 743 GB, `Qwen3.5-122B-A10B`, 4096 calibration samples,
`MAX_SEQUENCE_LENGTH=6144`.

## Additional context

- **Why not broadcast from rank 0?** Broadcasting ~244 GB of BF16 weights per rank via NCCL
  requires staging the weights on GPU, which exceeds VRAM limits. IPC sharing avoids any
  data movement — all ranks read from the same physical RAM pages.

- **Actual measured memory footprint:** The peak RAM consumption during `from_experts_module`
  is ~477 GB per rank under `auto_offload`, not just the raw BF16 weight size. The gap comes
  from the MoE linearization process: each rank temporarily holds both the original fused
  3D expert tensors and the unrolled per-expert `LinearExperts2D` representation in CPU memory
  simultaneously. With IPC sharing this overhead exists only on rank 0, reducing total peak
  RAM from `N × 477 GB` to `~477 GB`.

- **Interaction with `broadcast_qparams_and_cleanup`:** Since the IPC-shared weight tensor is
  visible to all ranks immediately when rank 0 writes quantized values (same physical page),
  the `weight` entry in `_GPTQ_Q_PARAMS` can be skipped in the broadcast loop for IPC-shared
  modules. New quantization parameters (`weight_scale` etc.) are still per-rank and require
  the existing broadcast.

- **Scope:** This feature primarily benefits MoE models with large expert counts on
  memory-constrained machines. Dense models are less affected since per-rank weight copies
  are proportionally smaller.

## Questions for maintainers

1. Is this use case in scope for llm-compressor? We are happy to implement the clean
   `rank0_share` API as described above.
2. Is `torch.multiprocessing` `file_system` strategy + `UntypedStorage.from_file` an
   acceptable dependency, or do you prefer a different IPC mechanism?
3. Should `rank0_share` be a parameter on `from_experts_module`, or integrated into the
   `load_context` / `init_dist` flow?

We are ready to submit a PR once there is agreement on the API shape.

---

*Related existing work:*
- PR #2333: `[GPTQ][ddp] enabling DDP for GPTQ` (existing Hessian reduce + parallel compression)
- PR #2785: `[Distributed] Module parallel calibration for QuantizationModifier`
- PR #2943: `fix DDP obs stat deletion`


## 评论 (17)

### brian-dellabetta · 2026-07-22

> each rank holds an independent copy of all model weights in CPU memory.

Hi @xesdiny , while each rank requires a copy of the onloaded tensors in GPU memory, those are offloaded to either disk or cpu in a non-redundant manner, i.e. for N GPUs, you may have the same tensor onloaded N times across the N GPUs, but once offloaded there is only 1 copy of that tensor on CPU/disk. You can see more information in the [compressed_tensors offload module README](https://github.com/vllm-project/compressed-tensors/tree/main/src/compressed_tensors/offload), be sure to check out DistributedDiskCache and DistributedCPUCache.

Or are you saying this is specifically an issue with linearized experts?

(aside -- note that we are looking to reduce the amount of data copying in DDP, which may resolve any issues specifically around memory allocation when mapping 3D experts to 2D):
* https://github.com/vllm-project/llm-compressor/pull/2941

### xesdiny · 2026-07-23

Thanks @brian-dellabetta for the clarification!

We do understand that `DistributedCPUCache` already achieves shared memory via `_share_filename_cpu_()` / `_new_shared_filename_cpu()` — essentially the same IPC mechanism we used. And yes, the **steady-state** after `offload_module` completes is correctly 1 copy. We apologize for not being precise enough in the issue description.

The issue is specifically about the **peak RAM during `from_experts_module` linearization**, not the steady-state. Here is the exact sequence:

```python
# from_experts_module (current code)
for index in range(self.num_experts):
    expert.copy_from_experts_module(experts, index)  # ← phase 1: ALL ranks copy independently

offload_kwargs = get_cache_init_kwargs(experts)
for module in self.modules():
    offload_module(module, **offload_kwargs)          # ← phase 2: shared memory established
```

In **phase 1**, every rank calls `copy_from_experts_module`, which does `.copy_()` into freshly allocated per-rank tensors. The source `experts` module is already in shared memory (its `DistributedCPUCache` was set up in a prior call), but the **destination** `LinearExperts2D.gate_proj.weight / up_proj.weight / down_proj.weight` are new allocations that are private to each rank. All `N` ranks simultaneously fill their own private copies of the full set of linearized expert weights before **phase 2** begins. Peak RAM = `N × (linearized expert weight size)`.

In **phase 2**, `DistributedCPUCache.offload()` is called for each `LinearExperts2D` sub-module: source process calls `.share_memory_()` + `_share_filename_cpu_()`, broadcasts the handle, and other ranks remap via `tensor.set_(UntypedStorage._new_shared_filename_cpu(...))`. The private copies on non-source ranks are released, leaving 1 shared copy. But the peak has already been hit.

---

**On our measured ~477 GB per-rank figure:**
The gap above the raw BF16 model size (~244 GB) comes from two concurrent allocations during linearization:
1. The original fused 3D expert tensors still referenced in memory
2. The new per-rank `LinearExperts2D` weight copies (`.copy_()` destination)

Both live simultaneously in phase 1 for each rank, hence ~477 GB × 8 ≈ 3.8 TB peak.

---

**Regarding PR #2941 (`no-copy-3d`):**
This PR looks very promising for our use case! If `from_experts_module` stores `LinearExperts2D` weights as **views** of the original 3D fused tensors (which are already in `DistributedCPUCache` shared memory), then:
- No new allocation happens in phase 1 — views point to the existing shared pages
- Peak RAM stays flat (no additional per-rank copies)
- The `offload_module` call in phase 2 would then be a no-op or view registration

Could you confirm whether this is the intended memory behavior of #2941? If so, it would likely resolve the peak RAM constraint on our hardware, and we can test it directly on `Qwen3.5-122B-A10B` with 8× L20 once the PR is ready.

We are happy to close this issue if #2941 addresses the root cause. Thank you for pointing us to it!

---

**Update (Jul 23) — validation results and #2941 analysis:**

We have now validated our IPC workaround on the full pipeline and also reviewed the #2941 implementation more carefully.

**Linearization validation:** After linearizing all 48 MoE layers with our IPC patch, `/dev/shm` usage reached ~446 GB (vs. 8 × 477 GB ≈ 3.8 TB without sharing), confirming that rank-0 IPC sharing reduces linearization peak RAM to ~1× model_size as described.

**#2941 covers the same ground:** After reading the #2941 diff, we can now self-answer our own question above. PR #2941 assigns `LinearExperts2D` weights as **views into `experts.gate_up_proj`**, which is already in `DistributedCPUCache` shared memory at the time `from_experts_module` is called. This means:
- The view assignment is zero-copy and zero-allocation — it references the same physical pages already shared across ranks
- The only transient allocation is the per-expert copy in `copy_from_experts_module` (which is immediately `del`-ed), not the full model simultaneously
- This effectively achieves the same 1× physical copy goal as our IPC flat-buffer approach

If #2941 (+ compressed-tensors#786) merges, our separate IPC flat-buffer workaround for linearization becomes unnecessary. **We are happy to wait for that path** rather than introduce a duplicate fix.

**Separate orthogonal issue — AWQ calibration memory:** We also discovered a second independent memory pressure that #2941 does not address: the AWQ `SequentialPipeline`'s `IntermediatesCache` holds activations for all subgraphs simultaneously across all ranks on the same machine. For a 49-block model with 256 calibration samples and `seq_len=2048`, this adds ~46 GB/rank × 8 ranks = ~368 GB on top of the ~446 GB already in `/dev/shm`, pushing total physical RAM to ~844 GB > 743 GB limit. This is resolved by reducing calibration samples (128 → ~660 GB total), not by IPC sharing — so it is out of scope for this issue.

### brian-dellabetta · 2026-07-23

Great, yeah #2941 should resolve but it's WIP and probably will have some wrinkles to iron out before merging.

Regarding AWQ: if you are using the basic pipeline, this will happen. But the SequentialPipeline operates on a per-subgraph basis, activations are cached and offloaded (if offload_device is set), and onloaded for the grid search, but then deleted before moving on to the next subgraph

### xesdiny · 2026-07-24

**[Update Jul 24] Correction on AWQ memory estimate + plan to close**

Thank you @brian-dellabetta for the clarification on AWQ!

We need to correct an error in our Jul 23 update. The "Separate orthogonal issue — AWQ calibration memory" section was wrong. We incorrectly assumed `SequentialPipeline` holds all subgraph activations simultaneously, leading to the estimate of ~46 GB/rank × 8 ranks = ~368 GB. As you clarified, `SequentialPipeline` operates on a per-subgraph basis — activations are cached, used for grid search, and **deleted before moving on to the next subgraph** (matching `AWQModifier.on_sequential_epoch_end` which calls `batch_intermediates.clear()` after each layer). AWQ activation memory is therefore negligible (~1 subgraph at a time), and is not an additional memory constraint.

**Revised memory picture (after #2941, 122B, 8× L20, 743 GB RAM):**

| Component | Size | Note |
|---|---|---|
| Linearization peak (rank 0 shared) | ~477 GB | Resolved by #2941 |
| GPTQ IntermediatesCache (SHM) | ~350–450 GB (256×4096 est.) | Starts after AWQ ends; not simultaneous with linearization peak |
| AWQ activations | ~negligible | Per-subgraph, deleted after grid search |

The two large peaks are not simultaneous, so 256×4096 should fit within 743 GB once #2941 merges.

**Plan:** We will close this issue once #2941 (+ compressed-tensors#786) merges, and will validate with 256×4096 on our hardware at that point. Our local IPC flat-buffer workaround covers immediate production needs in the meantime.

Apologies for the noisy estimate in the previous update.


### brian-dellabetta · 2026-07-24

Sounds good, thanks for the info. We plan to use #2941 next week for some big models expected to land, and will likely merge in after that work

### xesdiny · 2026-07-27

**[Update Jul 27] View-based zero-copy validated on 122B MoE — implementation notes for #2941**

Following up on the previous thread — while waiting for #2941 to land, we implemented and validated a view-based `from_experts_module` ourselves on the full `Qwen3.5-122B-A10B` (122B MoE, 48 layers, 256 experts/layer) on 8× L20 + 743 GB RAM.

---

### What we did

We patched `LinearExperts2D.from_experts_module` to use tensor views instead of `copy_()`, gated by `LINEARIZE_NO_COPY` env var (default=1). The three-phase flow:

```python
# Phase 1: skip weight copy_(); handle biases (if any) normally
# Phase 2: del weight parameters, call offload_module to set up cache structure
# Phase 3: inside disable_onloading(), assign views into _parameters["weight"]
with disable_onloading():
    expert.gate_proj._parameters["weight"] = experts.gate_up_proj[index, :intermediate_size]
    expert.up_proj._parameters["weight"]   = experts.gate_up_proj[index, intermediate_size:]
    expert.down_proj._parameters["weight"] = experts.down_proj[index]
```

`disable_onloading()` serves as a workaround for the `compressed-tensors#786` issue: it prevents the offload cache from triggering a copy operation when views are assigned, so the views are stored as-is (pointing into the original 3D tensor storage).

In our DDP context (IPC flat_buf already in shared memory), the views point directly into the original model's IPC SHM pages — **zero additional allocation, zero SHM growth**.

---

### Measured memory results (Rank 0, 256×2048 calibration)

| Metric | `copy_()` baseline | View (no-copy) | Saved |
|--------|:---:|:---:|:---:|
| **VmPeak** (historical peak) | 650 GB | **479 GB** | **−171 GB** |
| **RssAnon** (private heap) | 220 GB | **4.9 GB** | **−215 GB** |
| RssShmem (shared pages) | 12.9 GB | 228.9 GB | +216 GB (shared, not duplicated) |
| **PSS** (fair-share physical) | 228 GB | **80 GB** | **−148 GB** |
| Physical RAM (steady-state) | 510 GB | **445 GB** | **−65 GB** |

The `VmPeak` drop confirms the copy peak during Linearizing is eliminated. `RssAnon` drops from 220 GB to 4.9 GB — the per-rank weight heap that was causing OOM no longer materializes.

---

### Correctness validation

Full GPTQ W4A16 compression completed end-to-end. All 8 ranks SCALE_CHECK clean:

```
[w4a16-v2:r0] [SCALE_CHECK] ✅ CLEAN rank=0 total=37056 nan=0 inf=0 neg=0 huge(>1e10)=0
[w4a16-v2:r1] [SCALE_CHECK] ✅ CLEAN rank=1 total=37056 nan=0 inf=0 neg=0 huge(>1e10)=0
... (all 8 ranks identical)
```

37,056 weight_scale tensors, zero numerical anomalies.

---

### Issues we found and fixed (relevant to #2941)

The Gemini code review on #2941 flagged some items — we hit these in practice and can confirm they're real:

1. **`is_transposed=True` fallback is required**: Transposed expert weights (`experts.is_transposed`) need contiguous tensors for offload. We auto-detect and fall back to `copy_()` when `is_transposed=True`. Without this, offloading breaks silently.

2. **`has_bias` must be handled separately**: Biases are not part of the view-assignment path. We copy biases normally via `copy_from_experts_module`, then separately assign weight views. Skipping bias handling causes missing bias parameters in the offloaded modules.

3. **`disable_onloading()` as the ct#786 workaround**: Rather than waiting for `compressed-tensors#786` to support views natively, `disable_onloading()` already exists in the API and works as an opt-in bypass. This may be a simpler path for #2941 to land without being blocked.

---

### Remaining question / offer

We are happy to share the full diff or submit a PR once `compressed-tensors#786` or the `disable_onloading()` path is confirmed acceptable. The core change to `linear_experts.py` is ~70 lines.

The DDP-specific piece (views into IPC SHM, avoiding flat_buf entirely) would be an incremental optimization on top of #2941 and can be handled separately.


### brian-dellabetta · 2026-07-27

Hi @xesdiny , thanks for the details. we are validating #2941 this week, so we can revisit once that is hardened and merged

### xesdiny · 2026-08-12

**Update (2026-08-12): validated zero-copy IPC DDP approach on 122B; sharing findings**

We have been working around the memory constraints on our 8× L20 setup (743 GB system RAM, `Qwen3.5-122B-A10B`) and wanted to share what we found, in case it is relevant to PR #2941 or future work.

---

### Background: why standard `auto_offload` DDP is infeasible for large MoE

The bottleneck is not steady-state memory — it is the **peak RAM during `from_experts_module`**.

When `offload_module` is called under DDP, `OffloadCache.cls_from_device` returns `DistributedCPUCache`, which creates a POSIX shm segment for every offloaded tensor. For a 256-expert model with 48 layers × 3 projections per expert, this amounts to ~36,864 shm segments — well above the default kernel limit (`shmmni=4096`), causing the process to stall or crash before a single forward pass runs.

Beyond the shm limit, the standard path copies expert weights independently on every rank: with 8 ranks and ~477 GB peak per rank during linearization, the total RAM requirement is ~3.8 TB — not feasible on our hardware.

---

### IPC approach: view-based zero-copy weight sharing

The key observation: `load_context` already places the original fused 3D expert tensors in IPC-shared memory. All ranks are reading from the same physical pages at load time. So instead of each rank copying weights into freshly allocated storage, `from_experts_module` can simply assign `nn.Parameter` views into those shared pages:

```python
# instead of: self.gate_proj.weight.copy_(experts.gate_up_proj[index, :I])
self.gate_proj.weight = nn.Parameter(experts.gate_up_proj[index, :I], requires_grad=False)
```

This means:
- **Zero new allocations** — no flat buffer, no shm broadcast, no new shm segments
- **All ranks share the same physical RAM** — peak stays at ~477 GB total regardless of world size
- **`is_transposed=True` falls back gracefully** — non-contiguous slices cannot be stored as Parameter views, so we copy only in that case

We fall back to `CPUCache` (instead of `DistributedCPUCache`) for the `offload_module` step on `LinearExperts2D`, avoiding the shm segment explosion entirely. We also set `torch.multiprocessing.set_sharing_strategy("file_system")` to route any remaining shm through tmpfs files rather than POSIX segments.

---

### Validation results

Tested on `Qwen3.5-122B-A10B`, 8× L20 (48 GB each), 743 GB system RAM:

| | standard `auto_offload` DDP | IPC view approach |
|---|---|---|
| Peak CPU RAM | ~3.8 TB (infeasible) | ~477 GB |
| shm segments | ~36,864 (crashes) | 48 (one temp file per MoE layer, fallback path only) |
| Linearization RssAnon | ~220 GB/rank | ~5 GB total |
| GPTQ correctness | — | ✅ validated end-to-end |

Currently running at 24K calibration samples × 6144 seq_len. GPTQ quantization parameters (`weight_scale`, `weight_zero_point`, `weight_g_idx`) are correctly distributed and synchronized across ranks.

---

### Happy to go deeper if useful

While implementing this we encountered a couple of other issues in the DDP GPTQ path (related to how `CPUCache` interacts with async broadcasts, and how `weight_scale` gets written before `save_pretrained`). Happy to share those details if they are relevant to the direction you are taking with #2941, or to open a separate discussion.

We are also ready to contribute a clean upstream implementation (adding `no_copy: bool = False` to `from_experts_module`, with a corresponding `view_from_experts_module` method on each `ExpertMLP` subclass) if that would be welcome alongside or after #2941.

### brian-dellabetta · 2026-08-13

Hi @xesdiny , thanks for the report. Do you have a small diff or RFC you can create on this usage of IPC instead of shm tables? Is it compatible through torchrun and with our current dependency list? We've hit this issue of needing far more shm segments than the default limit, and would be interested in ways to make this more robust.

Aside -- we have hit similar issues with very large models as well. on top of #2941 , we are investing time on layer-wise compression and decompression, essentially to load up the model layer by layer rather than entirely with offloading
* #2995

### xesdiny · 2026-08-14

Hi @brian-dellabetta — to answer your questions directly:

**torchrun compatible?** Yes. `set_sharing_strategy("file_system")` uses temp files under `/dev/shm`, so it's unaffected by the kernel segment limit and works correctly with torchrun.

**New dependencies?** None — only `torch.multiprocessing` (already required).

Note that the view-assignment approach (zero-copy nn.Parameter views into the fused 3D tensor, similar to #2941) handles the per-rank weight copy overhead — we have a local validated implementation of this. 
 The two remaining gaps in our validated setup are: (1) `offload_module` should use `CPUCache` instead of `DistributedCPUCache` during MoE linearization — `DistributedCPUCache` creates one POSIX shm segment per tensor (~36,864 for 122B, crashing against the kernel's 4096 default); (2) `broadcast_qparams_and_cleanup` needs an explicit `update_offload_parameter` writeback for non-weight params (`weight_scale`, `weight_zero_point`, `weight_g_idx`) after broadcast.

Happy to open a draft PR if useful.

```
The two changes amount to roughly a dozen lines. Sketch:

# 1. linear_experts.py — from_experts_module (offload section)
- offload_module(module, **offload_kwargs)          # creates DistributedCPUCache → shm segments
+ _force_cpu_cache(module, execution_device)         # CPUCache, zero shm_open calls

# 2. utils/dist.py — broadcast_qparams_and_cleanup
- def broadcast_qparams_and_cleanup(module_list, module_to_rank, qparam_names, skip_cpu=True)
+ def broadcast_qparams_and_cleanup(module_list, module_to_rank, qparam_names, skip_cpu=True,
+                                    ipc_weight_shared=False)
  # when ipc_weight_shared=True: weight broadcast is kept but write-back is skipped
  # (rank-0 writes propagate via shared pages); weight_scale / weight_zero_point /
  # weight_g_idx still get explicit update_offload_parameter write-back after wait_for_comms.
```



### brian-dellabetta · 2026-08-14

Hi @xesdiny , I personally would like to see the draft PR to better understand the tradeoffs, ideally in a way where we can set a flag to switch between shm and IPC to confirm replicated behavior. 

Tagging @kylesayrs and @HDCharles , who have led the development of distributed offloading, in case they have feedback.

### xesdiny · 2026-08-15

Thanks for the feedback, @brian-dellabetta! We will prepare a draft PR within the next few days — including a flag to switch between shm and IPC modes as you suggested, along with basic validation to confirm behavior parity. Looking forward to @kylesayrs and @HDCharles's input as well.

### kylesayrs · 2026-08-18

My understand from reading this thread is that the proposed changes are essentially and fully covered by the changes proposed in https://github.com/vllm-project/llm-compressor/pull/2941.

Specifically, the key change is to add a pathway (enabled by a flag) by which MoE expert weights can be copied into `LinearExperts2D` as **views**, not deep copies. 

```python3
with disable_onloading():
    expert.gate_proj._parameters["weight"] = experts.gate_up_proj[index, :intermediate_size]
    expert.up_proj._parameters["weight"]   = experts.gate_up_proj[index, intermediate_size:]
    expert.down_proj._parameters["weight"] = experts.down_proj[index]
```

There are no changes to `broadcast_qparams_and_cleanup` required, as torch handles both reading and writing to shared memory tensors seamlessly.

### xesdiny · 2026-08-19

Thanks for the clarification! @kylesayrs  We're currently running a comparison test to validate this — specifically testing whether the original `broadcast_qparams_and_cleanup` (without our patch) produces identical quantization results on the no-copy views path.

We'll report back with concrete numbers (RAM usage, weight_scale correctness) once the comparison run completes.


### xesdiny · 2026-08-20

## Comparison results: `broadcast_qparams_and_cleanup` does require a fix

Thanks for the response @kylesayrs — we ran the controlled experiment and can now report concrete results.

### Setup

- Model: fine-tuned checkpoint based on `Qwen3.5-122B-A10B` architecture (`Qwen3_5MoeForConditionalGeneration`, 48 layers, 256 experts/layer, 8 active)
- Hardware: 8× NVIDIA L20, system RAM 743 GB
- Calibration: N=8192, seq=6144, PACK_DATA=1
- Both runs use the **no-copy views path** (same mechanism as #2941)
- Single variable: whether `broadcast_qparams_and_cleanup` is patched

| | Run A | Run B |
|---|---|---|
| broadcast mode | with writeback patch | upstream original (unmodified) |
| subgraphs | 49/49 ✅ | 49/49 ✅ |
| SCALE_CHECK rank 0 | ✅ CLEAN | ⚠️ CORRUPTED `nan=31924 neg=402 huge=18` |
| SCALE_CHECK rank 1 | ✅ CLEAN | ⚠️ CORRUPTED `nan=840 inf=1 neg=3139` |
| SCALE_CHECK rank 4 | ✅ CLEAN | ⚠️ CORRUPTED `nan=3829 neg=3` |
| SCALE_CHECK all 8 ranks | total=37056 all CLEAN | multiple ranks CORRUPTED |
| elapsed | 28918s | 28500s |

Run B corruption is concentrated in `weight_scale` / `weight_zero_point` of `layers.0.mlp.experts.*` — the first-quantized layer — on non-source ranks.

### Root cause

The no-copy views path assigns expert weights with `disable_onloading()`, so `weight` lives outside CPUCache. However, `weight_scale`, `weight_zero_point`, and `weight_g_idx` are set as ordinary module attributes after GPTQ runs — these **do** go through CPUCache's `__setattr__`.

When `broadcast_qparams_and_cleanup` calls `getattr(module, "weight_scale")`, CPUCache onloads a temporary GPU tensor. `dist.broadcast` modifies that temporary in-place, but the **underlying CPU storage is never written back** — leaving non-source ranks with stale/uninitialised values.

> "torch handles both reading and writing to shared memory tensors seamlessly" holds for `weight` (which bypasses CPUCache via `disable_onloading`), but not for `weight_scale` / `weight_zero_point` / `weight_g_idx` which are stored inside CPUCache.

### Fix

The fix is a targeted addition to `broadcast_qparams_and_cleanup` in `utils/dist.py`: after `_wait_for_comms`, call `update_offload_parameter` on non-source ranks to flush the broadcast result back to CPUCache storage. The change is ~16 lines.

We've opened a PR with the fix and 4 unit tests: #3066

This is independent of the no-copy views change in #2941 and can be reviewed/merged separately.

### xesdiny · 2026-08-25

Hi @kylesayrs, following up on the Aug 20 comparison results — wanted to add a code-level explanation of why `weight_scale` behaves differently from `weight`.

**Why `weight` is fine (your Aug 18 point holds)**

Under #2941's view-based path, `weight` is assigned inside `disable_onloading()`:

```python
with disable_onloading():
    expert._parameters["weight"] = experts.gate_up_proj[index, :]
```

`disable_onloading()` causes `OffloadCache.__setitem__` to write directly into `offloaded_values` (shared memory pages). So `dist.broadcast`'s in-place update is immediately visible to all ranks — no writeback needed. Your description is correct for `weight`.

**Why `weight_scale` / `weight_zero_point` / `weight_g_idx` are different**

These are set by GPTQ *after* quantization completes, via the ordinary path:

```python
# gptq/base.py:342-343
for attr, val in q_param_dict.items():
    update_offload_parameter(module, attr, val)   # first-time write → offload(value)
```

Since `weight_scale` did not exist before GPTQ ran, `OffloadCache.__setitem__` takes the else branch and offloads the value into CPU storage — *not* shared memory. When `broadcast_qparams_and_cleanup` later calls `getattr(module, "weight_scale")`, `CPUCache.onload()` returns a **temporary GPU copy**. `dist.broadcast` modifies that copy in-place; the copy is discarded when the function returns, leaving the underlying CPU storage stale on non-source ranks.

This is consistent with the Aug 20 experiment: corruption is concentrated in `weight_scale` / `weight_zero_point` of the first-quantized layer on non-source ranks, while `weight` (which uses the shared-memory path) is clean.

The fix in #3066 (~16 lines) calls `update_offload_parameter` after `_wait_for_comms` on non-source ranks to flush the broadcast result back to CPUCache. Happy to address any review feedback — tagging @HDCharles as well since this touches the offload internals.

### xesdiny · 2026-09-01

**Closing this issue.**

**Status of the original proposal:** The IPC zero-copy / `rank0_share` approach proposed here was contingent on PR #2941 not fully resolving the CPU RAM bottleneck. PR #2941 has been stalled since August 2026 with unresolved merge conflicts and CI failures, and no clear path to merge. The IPC feature is no longer being pursued at this time.

**What came out of this work:** While validating the no-copy views path on 8× L20 + Qwen3.5-122B-A10B, we discovered an unrelated but real bug in `broadcast_qparams_and_cleanup`: when quantization parameter tensors (`weight_scale`, `weight_zero_point`, `weight_g_idx`) are stored via `CPUCache`, `dist.broadcast` modifies a temporarily onloaded GPU tensor in-place without writing back to the underlying offload storage — silently leaving non-source ranks with stale or NaN values.

This bug is tracked and fixed independently:
- Bug report: (filed separately — link to be added)
- Fix: #3066
