# [Issue #425] sm121a: `paged_mqa_logits` varlen path produces illegal memory access; uniform path does not scale past batch 1 at long context

source: https://github.com/deepseek-ai/DeepGEMM/issues/425
state: open | updated: 2026-09-16T08:56:36Z
labels: 

## 正文

DeepGEMM 2.6.1 (as bundled in a vLLM main snapshot), GB10 / sm_121a (DGX Spark), 2-GPU TP via vLLM. Consumer of these kernels: vLLM's DeepSeek-Sparse-Attention indexer, model GLM-5.3-Flash (DSA geometry: kv_lora 512, index_topk 2048).

- The SM120 kernel family added for #317 (`sm120_fp8_paged_mqa_logits.cuh` + `sm120_paged_mqa_logits.cuh` scheduler) **works single-sequence** on sm_121a, verified up to 128K context with exact needle recall.
- With `kIsVarlen` engaged (2 sequences in the decode batch, ~50K tokens each) we get `cudaErrorIllegalAddress`. Same fault with batch shapes produced by a multimodal encoder even at batch 1. Faults reproduce 100% within seconds of the shape appearing.
- With the **uniform** path (batch 2, identical lengths, `next_n=2`) there is no fault, but throughput drops ~10x vs batch 1 (2.2 tok/s aggregate vs 23.4 single) - the kernel appears to serialise or oversubscribe on the 48-SM part at long context.

GB10 has 48 SMs and ~101 KB smem/SM, which several kernels in this family assume larger (cf. the `persistent_topk` 128 KB issue). vLLM-side, vllm-project/vllm#49896 documents a NaN-logits -> garbage-indices -> illegal-access chain in this kernel family on SM120 prefill; our decode/varlen faults may share that root. If useful I can run instrumented builds or provide the exact tensor shapes from vLLM's dump on crash.


## 评论 (3)

### ima-helikoptaaa · 2026-09-01

Tested on RTX PRO 6000 (sm120, arch_major=12) with deep_gemm 0.1.5.post3.

Calling `get_paged_mqa_logits_metadata` with any non-None `indices` value hits a hard assertion at dispatch before any kernel launches:

```
attention.hpp:226: arch_major == 10 and next_n == 1 and (block_kv == 64 or block_kv == 32)
```

The compiled `_C.so` only dispatches `kIsVarlen=true` for arch_major=10 (SM100/GB200). On sm12x (both sm120 and sm121a report arch_major=12) the assertion fires before any GPU memory is accessed. The IMA on GB10 you saw was likely from a build that let sm121a reach the kernel without a matching implementation.

The uniform path (indices=None) works cleanly at batch=1,2,4,8 and runs at about 0.013ms for batch=4, seq_len=8192 on sm120 (188 SMs). The SM-serialization slowdown you described for the uniform path on GB10 was not reproduced here at those sizes.

The short version: the varlen dispatch path is entirely absent for sm12x in 0.1.5.post3. The `sm120_fp4_paged_mqa_logits.cuh` scheduler exists in the headers but the dispatch table does not extend `kIsVarlen=true` support to arch_major=12.

### ima-helikoptaaa · 2026-09-01

Looking further, `nv_dev` already has this wired. In that branch `get_paged_mqa_logits_metadata` extends the varlen gate to `arch_major == 10 or arch_major == 12`, adds an sm120 metadata dispatch branch, and `fp8_fp4_paged_mqa_logits` gets a corresponding `arch_major == 12` dispatch that calls `sm120_paged_mqa_logits(...)` with `is_varlen` passed through.

So no external PR needed here. The fix exists, just hasn't landed on `main` yet.

### lucifer1004 · 2026-09-16

Both halves re-verified on a GB10 (sm_121a, 48 SMs, driver 580.159.03, CUDA 13.0) against #447:

**Varlen illegal access — fixed.** The rewritten paged-MQA stack (metadata scheduler + kernel) has explicit bounds guards for the varlen pairing paths. Repro of the failing classes: 2×~50K-token varlen decode batches (next_n=1, pages 64/128/256, heads 32/64, multiple seeds, eager + CUDA graph capture/replay with weight mutation) and batch-1 irregular context lengths (1, 3, 65537, 131072) — 23/23 pass, numerically exact vs an eager fp8-dequant reference, and the full-scale 2×50K varlen case is compute-sanitizer memcheck clean (0 errors). One contract note: varlen+indices with next_n=2 is now a host-side assertion (`next_n == 1`); next_n=2 exists on the uniform path only.

**Uniform-path batch scaling — the cliff is gone.** Kernel time (next_n=2, heads=64, page 64, CUDA events):

| context | b=1 | b=2 | b=4 | b2/b1 |
|---|---|---|---|---|
| 50K | 17.3 µs | 24.1 µs | 93.1 µs | 1.39x |
| 128K | 30.1 µs | 152.7 µs | 296.1 µs | 5.08x |

batch 2→4 is linear (1.94x @128K) with ~450 GB/s per call at batch≥2 (DRAM-saturated); batch 1 partially fits L2, which explains the residual superlinearity. The launch is num_sms-adaptive (persistent CTAs sized from device props), with no 48-SM assumptions.

