# [Issue #4644] [Feature]:  Add NVFP4 W4A4 MLA decode for SM100/SM103

source: https://github.com/flashinfer-ai/flashinfer/issues/4644
state: open | updated: 2026-09-25T02:15:41Z
labels: feature request, needs-triage

## 正文

### Before submitting

- [x] I have searched existing issues and this request has not been filed yet.

### Problem

MHA/GQA accepts an NVFP4 KV cache through the public `kv_cache_sf` argument (#2702). MLA does not: every trtllm-gen MLA invocation in `flashinfer/mla/_core.py` passes `None` for `key_block_scales` and `value_block_scales` (`_core.py:3291-3292`, `4167-4168` on `main`).

vLLM's guard is per-model, not per-layer — `nvfp4 KV cache is not supported with MLA (Multi-head Latent Attention) backends` — so a hybrid model keeps its whole cache at FP8. Kimi-K3-NVFP4 has 24 MLA layers out of 93.

The MLA latent is `kv_lora_rank=512` + `qk_rope_head_dim=64`. Per token per layer: 1152 B in BF16, 576 B in FP8, 324 B in NVFP4 (288 B data + 36 B block scales).

#4568 scopes MLA prefill/decode to BF16 I/O with an FP8 KV cache, so this is not tracked there.


### Requested outcome

MLA decode on SM100/SM103 with an NVFP4 paged KV cache and NVFP4 compute, matching the BF16 and FP8 MLA decode kernels in semantics.

- `kv_cache_sf` accepted on `trtllm_batch_decode_with_kv_cache_mla` and `BatchMLAPagedAttentionWrapper`, replacing the hard-coded `None` block scales.
- NVFP4 query, with FP4 global scales folded into `bmm1_scale` / `bmm2_scale`.
- Both variants of the trailing `qk_rope_head_dim` channels: `mla_use_nope=true` (Kimi-K3) and RoPE applied (DeepSeek-style).
- An NVFP4 cache write path, rather than materializing BF16/FP8 and requantizing.

Dense MLA only; sparse MLA and DSA top-k paths are out of scope.

### Target hardware

SM100 (B200, GB200), SM103 (B300, GB300)

### Inference engine

vLLM

### Affected model or model family

nvidia/Kimi-K3-NVFP4 — https://huggingface.co/nvidia/Kimi-K3-NVFP4

### Workload and configuration

- Data type and quantization: NVFP4 KV (packed `uint8` + FP8 E4M3 block scales, `sf_vec_size=16`,
  FP32 global scale) with NVFP4 query and compute. Baselines: existing BF16 and FP8 KV MLA decode.
- Sequence lengths: 32K, 128K, the 196,608 TP8 baseline in #4568, and the 1,048,576 architectural
  maximum. Speculative query lengths 1-8.
- Parallelism: TP-local query head counts 96, 48, 24, 12, 6; decode context parallelism.
- Relevant shapes: `kv_lora_rank=512`, `qk_nope_head_dim=128`, `qk_rope_head_dim=64`,
  `v_head_dim=128`, 96 global query heads over one latent KV head, `mla_use_nope=true`. Also
  DeepSeek-V3/R1-class MLA: same latent dims, 128 query heads, RoPE applied.


### Current workaround

FP8 KV cache. There is no per-layer opt-in — the vLLM guard rejects the whole model once an MLA
backend is selected.

### Impact

Memory capacity or bandwidth, Throughput

### Acceptance criteria

- Matches the BF16 MLA reference within the tolerance used by the FP8 MLA tests, across ragged
  and non-aligned lengths, permuted and prefix-shared block tables, query lengths 1-8, TP-local
  head counts 96/48/24/12/6, NoPE and RoPE, and CUDA-graph replay.
- End-task accuracy on `nvidia/Kimi-K3-NVFP4` reported against the FP8 KV baseline. The same
  latent feeds BMM1 as K and BMM2 as V, so one FP4 buffer bounds both logits and output.
- Complete-call benchmark against the FP8 MLA path, including query quantization and metadata
  preparation, reporting decode throughput and KV pool token capacity.
- CUDA-graph safe as page tables, lengths, and scale tensors change in place, with no KV gather, per-step allocation, host synchronization, or device-to-host metadata copy in steady state.

### Related work, dependencies, or suggested scope

- #4568 — Kimi-K3-NVFP4 tracker; its MLA item reads "BF16 I/O, FP8 KV cache". This is the NVFP4
  upgrade of that item.
- #4178 — packed low-head and variable-Q MLA decode. State which of packed low-head tiles,
  compact variable-Q, and decode context parallelism the NVFP4 path supports or rejects.
- #2702, #2363 — NVFP4 KV cache for SM100. Reuse the layout: packed `uint8` latent
  `[num_pages, page_size, (kv_lora_rank + qk_rope_head_dim) / 2]` plus a swizzled FP8 E4M3
  block-scale tensor.
- Fail fast on a packed `uint8` MLA cache with no scales; keep the 3D and 4D `kv_cache` shapes
  accepted today working.

### Timing or release need

_No response_

## 评论 (3)

### elwhyjay · 2026-08-21

!claim

### flashinfer-bot · 2026-08-21

Issue assigned to @elwhyjay.

### elwhyjay · 2026-08-21

Hi @mispa-ms, I would like to work on this if it is open to external contribution.

I checked the current kernel coverage first. The trtllm-gen artifacts in both FlashInfer and TensorRT-LLM currently have no MLA kernel with E2M1 KV at the MLA head dimensions (576/512), and the generator also does not currently support an E2M1 query dtype.

Two things I would like to confirm:
1. Is a trtllm-gen cubin refresh with NVFP4-KV MLA support already planned? If so, I can focus on the FlashInfer-side API/cache-write plumbing and tests.
2. Otherwise, would it be reasonable to first add FP4-KV MLA decode in CuTe-DSL, following the existing NVFP4 GQA KV semantics (#2702), while leaving NVFP4 query/compute as a follow-up?
