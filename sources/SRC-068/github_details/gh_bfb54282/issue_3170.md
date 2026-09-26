# [Issue #3170] DGX Spark (SM121) Current Support Audit

source: https://github.com/flashinfer-ai/flashinfer/issues/3170
state: open | updated: 2026-09-21T15:20:53Z
labels: good first issue, wip, op: gemm, op: misc, arch: sm12x, op: linear attention

## 正文

# FlashInfer — DGX Spark (SM121) Current Support Audit

**Date:** 2026-04-24
**Scope:** Audit of SM121 (compute capability 12.1, DGX Spark) support across FlashInfer ops, APIs, backends, and testing.
**Goal:** Improve Spark usability on FlashInfer by identifying existing gaps.

**Note: skip to "15. Consolidated Action Items" for TLDR.**

---

## Architecture Context

| Gencode | Target | CUDA Requirement |
|---------|--------|------------------|
| `compute_120a` / `sm_120a` | RTX 5090 (SM120) | CUDA 12.8 |
| `compute_120f` / `sm_120f` | SM12x family (120 + 121) | CUDA 12.9 |
| `compute_121a` / `sm_121a` | DGX Spark (SM121) | CUDA 12.9 |

### SM120 vs SM121: Implications for FlashInfer

Per the [CUDA 13.2 Programming Guide — Compute Capabilities](https://docs.nvidia.com/cuda/archive/13.2.0/cuda-programming-guide/05-appendices/compute-capabilities.html) (Tables 29–33), SM120 and SM121 share a single "12.x" spec column: identical shared memory (99 KB/block, 100 KB/SM), warps (48/SM), registers (64K/SM), tensor core data types (TF32, BF16, FP16, FP8, FP6, FP4, INT8), TMA, and cluster support. [Table 28](https://docs.nvidia.com/cuda/archive/13.2.0/cuda-programming-guide/05-appendices/compute-capabilities.html#compute-capabilities-family-specific-compatibility) confirms `compute_120f` is compatible with **both** CC 12.0 and 12.1. The chip-level differences (SM121 = aarch64 host, unified LPDDR5x, 84 SMs vs SM120's x86_64, discrete GDDR7, up to 170 SMs) do not affect kernel correctness — only SM-count-based heuristics and host toolchain.

### `f` vs `a` compilation targets: performance implications

Per the [PTX ISA 9.3](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html) (§9.7.15.5.14 for dense `mma`, §9.7.15.6.3 for sparse `mma.sp`), `120f` (family) is a subset of `120a`/`121a` (arch-specific). Most SM12x features — including **dense** NVFP4/MXFP4 block-scaled MMA — are family-specific and available via `120f` from PTX ISA 8.8. The arch-specific restriction (requiring `sm_120a`/`sm_121a`) applies **only to sparse MMA** (`mma.sp`) with `.kind::mxf4nvf4`/`.kind::mxf4`:

| PTX Feature | `compute_120` (baseline) | `compute_120f` (family) | `compute_120a` / `compute_121a` (arch) |
|-------------|--------------------------|------------------------|----------------------------------------|
| FP4/FP6/FP8 conversions (`cvt`) | No | Yes | Yes |
| FP4/FP6 MMA, block-scaled MMA (`.kind::mxf8f6f4`) | No | Yes | Yes |
| **Dense** NVFP4 MMA (`.kind::mxf4nvf4`) | No | **Yes** (PTX ISA ≥ 8.8) | **Yes** |
| **Dense** MXFP4 MMA (`.kind::mxf4`) | No | **Yes** (PTX ISA ≥ 8.8) | **Yes** |
| **Sparse** NVFP4 MMA (`mma.sp` `.kind::mxf4nvf4`) | No | **No** | **Yes** |
| **Sparse** MXFP4 MMA (`mma.sp` `.kind::mxf4`) | No | **No** | **Yes** |

FlashInfer's b12x GEMM kernel (`dense_blockscaled_gemm_sm120_b12x.py`) uses `cute.nvgpu.warp.MmaMXF4NVF4Op` — a **dense** block-scaled MMA atom. This means `sm_120f` wheels already emit native NVFP4/MXFP4 dense MMA instructions. Only **sparse** NVFP4/MXFP4 MMA (not currently used in FlashInfer) requires `sm_120a`/`sm_121a`.

> **Correction (2026-06-12):** An earlier version of this table stated that ALL `.kind::mxf4nvf4`/`.kind::mxf4` MMA was arch-specific-only. Per [Harry-Chen's feedback](https://github.com/flashinfer-ai/flashinfer/issues/3170#issuecomment-4677810517) and PTX ISA §9.7.15.5.14 vs §9.7.15.6.3, the restriction is limited to the sparse (`mma.sp`) variant.

### Wheel build arch targets

The release wheel CI (`.github/workflows/release.yml`) builds the following SM12x targets:

| CUDA Version | SM12x target in `FLASHINFER_CUDA_ARCH_LIST` |
|---|---|
| < 12.9 | `12.0a` (SM120 arch-specific; no SM121 support) |
| >= 12.9, < 13.0 | `12.0f` (family; covers SM120 + SM121; includes dense NVFP4/MXFP4 MMA) |
| >= 13.0 | `12.0f` (same) |

**No `121a` target is included in any wheel build.** However, since FlashInfer's FP4 kernels use **dense** block-scaled MMA (`MmaMXF4NVF4Op`, not sparse), the `120f` wheels already emit native NVFP4/MXFP4 MMA instructions. The `121a` target would only be needed for future sparse MMA kernels. JIT compilation on SM121 still produces `121a` cubins for forward-compatibility.

### What this means for FlashInfer

- **Any kernel that runs on SM120 is architecturally compatible with SM121.** Hardcoded `sm_version == "sm_120"` or `minor == 0` checks in backend dispatch are over-restricting without justification.
- **Separate cubins matter for JIT but not for wheels.** `CompilationContext` correctly emits `sm_121a` for JIT on SM121. Since FlashInfer uses only dense block-scaled MMA (available on `120f`), the wheels do not lose FP4 GEMM performance. The `121a` JIT path provides forward-compatibility for future sparse MMA use.
- **SMEM capacity maps, tile configs, and MMA atoms are identical.** Code using `get_smem_capacity_in_bytes("sm_120")` returns the correct value for SM121 too — the only risk is `KeyError` if a map expects an `"sm_121"` key and doesn't have one.

### Key utility functions

| Function (`utils.py`) | Behavior for SM121 |
|------------------------|--------------------|
| `is_sm12x_supported` | True (CUDA ≥ 12.9) |
| `is_sm121a_supported` | True (CUDA ≥ 12.9) |
| `is_sm120a_supported` | **False** (12.0 only) |
| `device_support_pdl` | True (`major >= 9`) |
| `determine_attention_backend` | Returns `fa2` (fa3 is SM90-only) |
| `determine_gemm_backend` | Returns `sm80` (no SM12x branch) |

---

## 1. Attention

### 1.1 Decode (batch paged KV)

| Backend | CC Gate | SM121 Status | Notes |
|---------|---------|--------------|-------|
| **fa2** | Generic | **Supported** | Default via `determine_attention_backend` for non-FP8 tensor-core decode |
| **fa3** | SM90 only | **Not available** | `determine_attention_backend` returns fa3 only on SM90 |
| **xqa** | `major in {9, 10, 12}` | **Supported** | `trtllm_batch_decode` auto → xqa when `major != 10` |
| **trtllm-gen** | `major == 10` only | **Not available** | Auto selects this only for SM100 |
| **cudnn** | Runtime-dependent | **Unknown** | No explicit CC exclusion; depends on cuDNN + driver |
| **MLA tensor path** | `device_arch == 80` | **Not available** | SM80-only legacy path; use XQA MLA instead |

**Dispatch:** `decode.py:~2429` (trtllm batch), `~1057` (tensor-core), `~1934` (MLA legacy).

### 1.2 Prefill (batch paged KV)

| Backend | CC Gate | SM121 Status | Notes |
|---------|---------|--------------|-------|
| **fa2** | Generic | **Supported** | Default auto path |
| **fa3** | SM90 only | **Not available** | |
| **cudnn** | Runtime-dependent | **Unknown** | No explicit CC block |
| **cutlass FMHA** | `is_sm100a_supported \|\| is_sm110a_supported` | **Not available** | Explicitly excluded for SM12x (no tcgen05); error message names RTX 5090 / DGX Spark |
| **FMHAv2 (TRT-LLM)** | `is_sm12x_supported` | **Supported** | Intended Blackwell 12x path; FP8 FMHAv2 explicitly blocked |
| **cute-dsl** | SM100+ code paths | **Uncertain** | Kernels use SM100-oriented helpers (`get_smem_capacity_in_bytes("sm_100")`); needs on-device validation |

**Dispatch:** `prefill.py:~132–163` (CUTLASS FMHA gate), `~1973` (auto), `~4416` (FMHAv2).

### 1.3 MLA (Multi-Latent Attention)

| Backend | CC Gate | SM121 Status | Notes |
|---------|---------|--------------|-------|
| **xqa** | `major == 12` | **Supported** | Auto for decode MLA on SM12x |
| **xqa (FP8/NVFP4)** | `major in {12}` | **Supported** | Docstring says "SM120" but gate is `major == 12` (includes 121) |
| **trtllm-gen** | `major == 10` | **Not available** | |
| **cute-dsl** | `cc[0] >= 10` | **Supported (gate)** | SM121 passes the check; SM100-oriented internals need validation |
| **fa2** | Generic | **Supported** | Fallback path |

**Dispatch:** `mla/_core.py:~677` (trtllm MLA decode), `~686` (XQA MLA).

### 1.4 XQA

| Backend | CC Gate | SM121 Status | Notes |
|---------|---------|--------------|-------|
| **xqa** | `major in {9, 10, 12}` | **Supported** | |
| **xqa_mla** | `major in {12}` | **Supported** | JIT `gen_xqa_module_mla` uses `supported_major_versions=[12]` |
| **xqa NVFP4** | `major in {12}` | **Supported** | Error message says "SM120 GPUs" — misleading for SM121 |

**Dispatch:** `xqa.py:~316` (general), `~536` (MLA). **JIT:** `jit/xqa.py:~97` (xqa), `~172` (xqa_mla).

### 1.5 POD / Cascade / Sparse / Attention Sink

| API | SM121 Status | Notes |
|-----|--------------|-------|
| **POD** | Inherits prefill + decode | Same as §1.1 / §1.2 |
| **Cascade** (`merge_state`) | **Supported** | No arch filter |
| **Sparse** | **Supported (fa2)** | Auto → fa2 on SM121 |
| **Attention sink** | **Supported (fa2)** | Auto → fa2 on SM121 |

### 1.6 cuDNN Attention

No explicit CC exclusion in `cudnn/prefill.py` or `cudnn/decode.py`. **Runtime-dependent** on cuDNN version and driver support for Spark hardware.

---

## 2. GEMM

### 2.1 `mm_fp4` / FP4 Dense GEMM

| Backend | CC Gate | SM121 Status | Notes |
|---------|---------|--------------|-------|
| **cutlass** | `[100, 103, 110, 120, 121]` | **Supported** | `get_gemm_sm120_module_cutlass_fp4()` for `sm_major == 12` |
| **cudnn** | `[100, 103, 110, 120, 121]` | **Supported** | MXFP4 on 12x needs cuDNN ≥ 9.14.0 |
| **b12x** | `[120, 121]` (decorator) | **Supported (gate) but excluded from auto** | Heuristic checks `major == 12 and minor == 0` — **SM121 never gets b12x in auto** |
| **trtllm** | `[100, 103]` | **Not available** | |
| **cute-dsl** | `[100, 103]` | **Not available** | Uses SM100-style kernel; not enabled for SM12x |

**Key issue:** `_heuristic_func_mm_fp4` (`gemm_base.py:5065–5071`) sets `is_sm120 = major == 12 and minor == 0`; only then prepends b12x. **SM121 falls through to cutlass/cudnn only.** A prior internal FP4 audit also identified this as the likely root cause of DGX Spark NVFP4 performance complaints, along with related issues: AOT building `fp4_quantization_121` while runtime redirects to `120f`, the `sm120a` FP4 quant module being dead code, and an upstream `nvidia-cutlass-dsl` blocker (missing `"sm_121"` in `SMEM_CAPACITY_MAP`, pending cutlass-dsl 4.5).

### 2.2 `mm_bf16` / `bmm_bf16`

| Backend | CC Gate | SM121 Status | Notes |
|---------|---------|--------------|-------|
| **cudnn** | `[80, 86, 89, 90, 100, 103]` | **Not available** | 121 not in list |
| **cutlass** | `[100, 103]` | **Not available** | |
| **tgv** | `[100, 103]` | **Not available** | |

**SM121 has no BF16 mm/bmm backend through the standard `bf16_gemm_sm100` path.** Falls back to generic segment GEMM or PyTorch.

### 2.3 `mm_mxfp8` / `bmm_mxfp8`

| Backend | CC Gate | SM121 Status | Notes |
|---------|---------|--------------|-------|
| **cutlass** | `[120, 121]` for mm; `[120, 121]` for bmm | **Supported** | Enforces 1D swizzled scales, 128×4 block, K/N multiples of 32 on SM12x |
| **cute-dsl** | `[100, 103]` | **Not available** | |
| **trtllm** | `[100, 103]` | **Not available** | |
| **cudnn** (bmm) | `[100, 103]` | **Not available** | |

**Dispatch:** `gemm_base.py:~3984+` (mm_mxfp8), `~7503+` (bmm_mxfp8).

### 2.4 `bmm_fp8`

| Backend | CC Gate | SM121 Status | Notes |
|---------|---------|--------------|-------|
| **cutlass_sm12x** | `_match_sm_version(["120", "121"])` | **Supported** | Uses `get_gemm_sm120_module_cutlass_fp8` |
| **cudnn** | CC-dependent | **Unknown** | |
| **cublas** | Generic | **Supported** | |

### 2.5 Groupwise / Blockscaled GEMM

| API | CC Gate | SM121 Status | Notes |
|-----|---------|--------------|-------|
| `gemm_fp8_nt_groupwise` | `[100, 103, 120, 121]` | **Supported** | Uses `get_gemm_sm120_module()` on SM12x |
| `gemm_fp8_nt_blockscaled` | `[100, 103, 120, 121]` | **Supported** | |
| `group_gemm_fp8_nt_groupwise` | `[100, 103, 120, 121]` | **Supported** | **Correctness issues for `num_groups > 1` on SM120/121** (documented) |
| `group_gemm_mxfp4_nt_groupwise` | `[120, 121]` | **Supported** | |
| `group_gemm_nvfp4_nt_groupwise` | `[120, 121]` | **Supported** | |

### 2.6 DeepGEMM

| API | CC Gate | SM121 Status |
|-----|---------|--------------|
| `group_deepgemm_fp8_nt_groupwise` | `[100, 103]` | **Not available** |
| `batch_deepgemm_fp8_nt_groupwise` | `[100, 103]` | **Not available** |

### 2.7 Other GEMM

| API | SM121 Status | Notes |
|-----|--------------|-------|
| `SegmentGEMMWrapper` | **Not SM12x-optimized** | Uses `determine_gemm_backend → "sm80"`; no SM12x branch |
| `routergemm` (`tinygemm_bf16`, etc.) | **Not available** | `[100, 103]` only |
| `tgv_gemm_sm100` | **Not available** | SM10x stack |
| `mm_fp8` (TRT-LLM low-latency) | **Unknown** | No explicit CC gate in Python |

### 2.8 GEMM JIT

All `gen_gemm_sm120_*` generators use `get_nvcc_flags_list(supported_major_versions=[12])` — `CompilationContext` supplies `sm_121a` when device is SM121. CUTLASS kernel generation (`generate_kernels.py:1049`) explicitly checks `has_arch(120) or has_arch(121)`.

---

## 3. MoE (Mixture of Experts)

### 3.1 `cutlass_fused_moe` (FP8)

| Backend | CC Gate | SM121 Status | Notes |
|---------|---------|--------------|-------|
| **cutlass SM120** | `major*10+minor` → "120"/"121" both → `gen_cutlass_fused_moe_sm120_module` | **Supported** | JIT uses `supported_major_versions=[12]`; FP8 MoE may fall back to SM89 tactics when native occupancy is zero |
| **trtllm MoE** | `arch[0] >= 10` | **Supported** | No 120/121 split |

### 3.2 `b12x_fused_moe` (NVFP4 MoE)

| Backend | CC Gate | SM121 Status | Notes |
|---------|---------|--------------|-------|
| **b12x** | `@supported_compute_capability([120, 121])` | **Supported (gate)** | Docstrings say SM120/SM121; uses `dense_blockscaled_gemm_sm120` internals |

### 3.3 `cute_dsl_fused_moe_nvfp4`

| Backend | CC Gate | SM121 Status |
|---------|---------|--------------|
| **cute-dsl** | `[100, 103]` | **Not available** |

---

## 4. Norm

### 4.1 RMSNorm / LayerNorm / Gemma Norm

| API | Backend | SM121 Status | Notes |
|-----|---------|--------------|-------|
| `rmsnorm` | CUDA JIT or CuTe DSL | **Supported** | No CC gate; PDL enabled (`__CUDA_ARCH__ >= 900`) |
| `fused_add_rmsnorm` | CUDA JIT or CuTe DSL | **Supported** | |
| `gemma_rmsnorm` | CUDA JIT or CuTe DSL | **Supported** | |
| `gemma_fused_add_rmsnorm` | CUDA JIT or CuTe DSL | **Supported** | |
| `layernorm` | CUDA JIT or CuTe DSL | **Supported** | |
| `fused_add_layernorm` | CUDA JIT or CuTe DSL | **Supported** | |
| All `*_quant` variants | CUDA JIT or CuTe DSL | **Supported** | |

### 4.2 `fused_rmsnorm_silu`

| Dtype | CC Gate | SM121 Status | Notes |
|-------|---------|--------------|-------|
| BF16/FP16 | `sm_version >= 80` | **Supported** | |
| FP8 output | `sm_version >= 89` | **Supported** | |
| NVFP4 output | `sm_version >= 100` | **Supported** | SM121 = 121 ≥ 100; uses SM100+ sweep LUT |

### 4.3 `rmsnorm_fp4quant` / `add_rmsnorm_fp4quant`

CuTe DSL only (requires `nvidia-cutlass-dsl`). Uses `get_sm_version` = `major*10+minor` → 121. No explicit SM121 exclusion. **Supported** assuming CuTe DSL + CUDA support FP4 PTX on SM121.

---

## 5. RoPE

| API | Backend | SM121 Status | Notes |
|-----|---------|--------------|-------|
| `apply_rope` / `*_inplace` | CUDA JIT | **Supported** | No CC gate |
| `apply_rope_pos_ids` / `*_inplace` | CUDA JIT | **Supported** | |
| `apply_llama31_rope` / `*_inplace` | CUDA JIT | **Supported** | |
| `apply_rope_with_cos_sin_cache` / `*_inplace` | CUDA JIT | **Supported** | |
| `rope_quantize_fp8` | CUDA JIT | **Supported** | |
| `mla_rope_quantize_fp8` | CUDA JIT | **Supported** | |

All RoPE kernels use PDL via `__CUDA_ARCH__ >= 900` (SM121 qualifies). No Triton RoPE in-tree.

---

## 6. Activation

| API | Backend | SM121 Status | Notes |
|-----|---------|--------------|-------|
| `silu_and_mul` | CUDA JIT | **Supported** | PDL enabled on SM121 |
| `gelu_and_mul` | CUDA JIT | **Supported** | |
| `gelu_tanh_and_mul` | CUDA JIT | **Supported** | |
| `silu_and_mul_scaled_nvfp4_experts_quantize` | TRT-LLM FP4 JIT | **Supported** | Uses `get_fp4_quantization_module("121")` → remaps to `"120f"` on CUDA ≥ 12.9 |

Triton `silu_and_mul` also available with no SM-specific guards.

---

## 7. Sampling

| API | Backend | SM121 Status | Notes |
|-----|---------|--------------|-------|
| `sampling_from_logits` / `*_probs` | CUDA JIT | **Supported** | Arch-agnostic |
| `top_k_*` / `top_p_*` / `min_p_*` | CUDA JIT | **Supported** | |
| `chain_speculative_sampling` | CUDA JIT | **Supported** | |
| `top_k` (clusters path) | CUDA JIT | **Not available** | `can_use_clusters_topk` requires `cap[0] == 10` (SM100 only) |

---

## 8. Quantization

| API | Backend | SM121 Status | Notes |
|-----|---------|--------------|-------|
| `fp4_quantize` (TRT-LLM style) | CUDA JIT (120f) | **Supported** | Runtime remaps "121" → "120f" on CUDA ≥ 12.9 |
| `nvfp4_*` / `mxfp4_*` | CUDA JIT | **Supported** | `@supported_compute_capability` includes 121 |
| Generic `quantization` module | CUDA JIT | **Supported** | No per-SM override |
| `mxfp8_quantization` | CUDA JIT | **Supported** | `gen_mxfp8_quantization_sm100_module` uses all arches from context |

---

## 9. Mamba

| API | Backend | SM121 Status | Notes |
|-----|---------|--------------|-------|
| `selective_state_update` | CUDA JIT (SM100 generator) | **Supported** | `major >= 10` → uses `gen_selective_state_update_sm100_module`; **not in AOT list** — JIT on first use |
| `SSDCombined` | CuTe DSL | **Supported** | `major >= 10` |

**AOT gap:** `gen_selective_state_update_sm100_module` is not in the default AOT build list. SM121 users with `FLASHINFER_DISABLE_JIT` will hit a missing-module error.

---

## 10. Communication

| API | Backend | SM121 Status | Notes |
|-----|---------|--------------|-------|
| `alltoall` | CUDA JIT (generic) | **Supported** | All arches from compilation context |
| `vllm_comm` | CUDA JIT (generic) | **Supported** | |
| `trtllm_allreduce` | CUDA JIT | **Not available** | `supported_major_versions=[9, 10]` — **SM12 excluded** |
| `trtllm_mnnvl` | AOT only | **Not available** | Only built when `has_sm100` |
| `moe_alltoall` | AOT only | **Not available** | Only built when `has_sm100` |

---

## 11. GDN (Gated Delta Net)

| API | Backend | SM121 Status | Notes |
|-----|---------|--------------|-------|
| `gdn_prefill` | CUDA JIT (SM90 path) | **Broken** | Blackwell CuTe path requires `is_sm100a_supported` — not SM121. Falls through to SM90 path, but that JIT module is compiled with `sm90a_nvcc_flags` (`compute_90a,code=sm_90a`), producing SM90-only SASS with no PTX fallback. **Will fail to load on SM121.** |
| `gdn_decode` | CUDA JIT (SM90 path) | **Broken (same issue)** | Also compiled with `sm90a` flags; incompatible with SM121 |

---

## 12. Page (KV Cache Ops)

KV cache append/management via generic CUDA JIT. **No CC gates. Supported.**

---

## Cross-Cutting Issues Summary

| # | Severity | Area | Issue |
|---|----------|------|-------|
| 1 | **HIGH** | GEMM | `b12x` FP4 backend excluded from auto on SM121 (heuristic checks `minor == 0`) |
| 2 | **HIGH** | GEMM | `mm_bf16` / `bmm_bf16` have **no backend available** for SM121 |
| 3 | **MEDIUM** | Quantization | AOT builds `fp4_quantization_121` module but runtime always uses `120f` — wasted artifact + JIT penalty if `120f` not prebuilt |
| 4 | **MEDIUM** | Mamba | `gen_selective_state_update_sm100_module` missing from AOT — JIT penalty on first SSU call; breaks `FLASHINFER_DISABLE_JIT` |
| 5 | **MEDIUM** | Comm | `trtllm_allreduce` JIT limited to SM 9/10 — no fused allreduce on SM121 |
| 6 | **HIGH** | GDN | GDN prefill falls through to SM90 path on SM121, but the JIT module is compiled with `sm90a_nvcc_flags` (`compute_90a,code=sm_90a`) — **incompatible with SM121**; would fail to load at runtime |
| 7 | **LOW** | Sampling | Clusters top-k optimization SM100-only; SM121 uses slower fallback |
| 8 | **LOW** | GEMM | `SegmentGEMMWrapper` not SM12x-optimized (uses `sm80` backend) |
| 9 | **INFO** | Quantization | `sm120a` FP4 quant module is dead code (always remapped to 120f on CUDA ≥ 12.9) |
| 10 | **INFO** | GEMM | SM100 FP4 CUTLASS compiles for SM12x needlessly (`supported_major_versions=[10, 11, 12]`) |

Test-related and documentation issues are covered in §13.5 and §14.3 respectively.

---

## Key Files Reference

| File | Relevance |
|------|-----------|
| `flashinfer/compilation_context.py` | Arch normalization (120a vs 120f vs 121a) |
| `flashinfer/utils.py` | `is_sm12x_supported`, `is_sm121a_supported`, `determine_attention_backend`, `determine_gemm_backend` |
| `flashinfer/jit/core.py` | NVCC flag definitions (`sm120f_nvcc_flags`, `sm121a_nvcc_flags`) |
| `flashinfer/gemm/gemm_base.py` | All GEMM backend dispatch, b12x runner, heuristics |
| `flashinfer/fused_moe/core.py` | MoE dispatch |
| `flashinfer/fused_moe/cute_dsl/b12x_moe.py` | b12x MoE API + CC gate |
| `flashinfer/quantization/fp4_quantization.py` | FP4 quant module selection + 121→120f redirect |
| `flashinfer/aot.py` | AOT build module list + `detect_sm_capabilities()` |
| `flashinfer/prefill.py` | Prefill backend dispatch incl. CUTLASS FMHA exclusion |
| `flashinfer/decode.py` | Decode backend dispatch |
| `flashinfer/mla/_core.py` | MLA backend dispatch |
| `flashinfer/xqa.py` | XQA CC gates |
| `flashinfer/mamba/selective_state_update.py` | Mamba SSU dispatch |
| `flashinfer/jit/comm.py` | Comm module JIT (trtllm_allreduce SM9/10 only) |
| `flashinfer/gdn_prefill.py` | GDN prefill SM100a vs SM90 branching |

---

# Part 2: Test Coverage & Arch-Check Audit

## 13. Unit Test SM121 Skip / xfail / Waiver Inventory

### 13.1 Attention Tests

| Test File | Condition | SM121 Impact | Justified? |
|-----------|-----------|--------------|------------|
| `test_batch_attention.py:207–249` | `xfail` when `cap[0] == 12` | **xfail on SM121** (and SM120) — tile size/stages | Yes — known limitation for SM12x family |
| `test_fmha_v2_prefill.py:486–489` | `is_sm90a_supported or is_sm120a_supported` | **SM121 SKIPPED** — uses `is_sm120a` (12.0-only) not `is_sm12x` | **Gap** — message says "SM12x" but condition excludes SM121 |
| `test_fmha_v2_prefill.py:492–506` | `is_sm120_plus = is_sm120a_supported(...)` | **SM121 excluded** from FP8/sliding/SQV sub-tests | **Gap** — should use `is_sm12x_supported` if FMHAv2 is intended for SM12x |
| `test_xqa.py:123–126` | `cap[0] not in [9, 10, 12]` | **SM121 included** | OK |
| `test_xqa.py:468–471` | `cap[0] not in [12]` | **SM121 included** | OK |
| `test_xqa_batch_decode.py:393–396` | `cap[0] not in [9, 10, 12]` | **SM121 included** | OK |
| `test_xqa_batch_decode.py:582–585` | `cap[0] not in [12]` | **SM121 included** but reason says "SM120 GPUs" only | Minor doc gap |
| `test_xqa_mla_batch_decode.py:25–27` | `cap[0] != 12` | **SM121 included** | OK |
| `test_trtllm_gen_mla.py:276–279` | `cap[0] != 12` for xqa backend | **SM121 included** | OK |

### 13.2 GEMM Tests

| Test File | Condition | SM121 Impact | Justified? |
|-----------|-----------|--------------|------------|
| `test_mm_fp4.py:40–45` | `cap[0] != 12 or cap[1] != 0` | **SM121 SKIPPED** for b12x backend — reason: "b12x only supports SM120" | Aligned with current heuristic; **gap if b12x should work on SM121** |
| `test_mm_fp4.py:105–106` | cuDNN xfail for FP4/MXFP4 | SM120-specific cuDNN quirk | OK |
| `test_bmm_mxfp8.py:23–24` | `cap[0] in [11, 12]` → skip | **SM121 SKIPPED** — "Not tested on SM110/SM120/SM121" | **Gap** — MXFP8 BMM cutlass lists [120, 121] in `supported_compute_capability` but test skips both |
| `test_bmm_fp8.py:20–23` | `cap[0] not in [10, 11, 12]` for cutlass | **SM121 included** | OK |
| `test_group_gemm_fp4.py:118–121` | `cap[0] not in [12]` | **SM121 included** | OK |
| `test_groupwise_scaled_gemm_fp8.py:202–212` | `group_size > 1 and cap[0] in [12]` → skip | **SM121 SKIPPED** (same as SM120) — known correctness issue | Justified — documented bug |
| `test_groupwise_scaled_gemm_mxfp4.py:257–335` | `cap[0] not in [10, 12]` | **SM121 included** | OK |
| `test_mm_mxfp8.py:88–518` | `cap[0] == 12` for swizzled scales | **SM121 included** | OK |
| `test_mm_mxfp8_sm120.py:12–24` | `cc[0] == 12` | **SM121 included** (despite "SM120" naming) | OK |

### 13.3 MoE Tests

| Test File | Condition | SM121 Impact | Justified? |
|-----------|-----------|--------------|------------|
| `test_b12x_fused_moe.py:88–90` | `@not_sm121` (`_is_sm121()`) | **SM121 SKIPPED for ALL b12x MoE tests** — 10+ test methods | **Major gap** — API decorator lists [120, 121] but tests say "not supported on SM121" |
| `test_trtllm_cutlass_fused_moe.py:486–488` | `cap[0] not in [10, 11, 12]` | **SM121 included** for NVFP4 MoE | OK |
| `test_trtllm_cutlass_fused_moe.py:1826–1828` | `not is_sm100a_supported` | **SM121 skipped** for unswizzled_input_sf | Questionable — only checks SM100a |
| `test_trtllm_cutlass_fused_moe.py:1981–1984` | `not is_sm100a and not is_sm12x` | **SM121 included** | OK |

### 13.4 Utils / Other Tests

| Test File | Condition | SM121 Impact | Justified? |
|-----------|-----------|--------------|------------|
| `test_jit_example.py:169–171` | `xfail` when `cap == (12, 1)` | **SM121 xfail** — "Numerical accuracy issue on SM 121 (Spark)" | Justified if reproducible; **should verify if still needed** |
| `test_fp4_quantize.py` / `test_fp4_quantize_padding.py` | `is_sm12x_supported` | **SM121 included** | OK |
| `test_gen_module_symlink_race_condition.py` | `is_sm100a or is_sm12x` | **SM121 included** | OK |

### 13.5 Test Gap Summary

| # | Severity | Test File | Issue |
|---|----------|-----------|-------|
| T1 | **HIGH** | `test_fmha_v2_prefill.py` | Uses `is_sm120a_supported` instead of `is_sm12x_supported` — SM121 skips all FMHAv2 prefill tests |
| T2 | **HIGH** | `test_b12x_fused_moe.py` | All b12x MoE tests have `@not_sm121` — contradicts API decorator `[120, 121]` |
| T3 | **MEDIUM** | `test_bmm_mxfp8.py` | Skips SM12x entirely despite MXFP8 BMM cutlass supporting [120, 121] |
| T4 | **LOW** | `test_jit_example.py` | SM121-specific xfail for numerical accuracy — needs re-verification |
| T5 | **LOW** | `test_xqa_batch_decode.py` | NVFP4 XQA reason string says "SM120" but condition includes SM121 |
| T6 | **LOW** | `test_trtllm_cutlass_fused_moe.py` | `unswizzled_input_sf` test only checks `is_sm100a` — SM12x not considered |

---

## 14. Arch-Check Over-Restriction Audit

Audit of all `sm120`/`sm121`/`sm120a`/`sm121a`/`sm120f` checks in non-test source code for cases where logic is more restrictive than necessary.

### 14.1 Confirmed Over-Restrictions

| # | File | Lines | Pattern | Issue | Suggested Fix |
|---|------|-------|---------|-------|---------------|
| A1 | `utils.py` | 574–576 | `is_sm120f_supported`: requires `minor == 0` | Name implies SM12x family on CUDA 12.9, but implementation excludes SM121 | Change to `major == 12` (or rename to clarify SM120-only intent). Currently **unused** in the codebase. |
| A2 | `gemm/gemm_base.py` | 5065–5070 | `is_sm120 = major == 12 and minor == 0` in `_heuristic_func_mm_fp4` | b12x backend never selected in auto for SM121 | Change to `major == 12` if b12x is validated on SM121 |
| A3 | `gemm/kernels/dense_blockscaled_gemm_sm120.py` | 1591–1594 | `if sm_version != "sm_120": raise ValueError(...)` | Rejects any SM version string other than `"sm_120"` | Allow `"sm_121"` (or any `sm_12*`); architecturally compatible (same MMA atom, same smem) |
| A4 | `cute_dsl/attention/compat.py` | 29–36 | `_TMEM_MAX_ALLOC_COLUMNS_MAP` has `"sm_120": 512` but no `"sm_121"` | Would raise `KeyError` if `"sm_121"` ever passed to fallback path | Add `"sm_121": 512` |

### 14.2 Confirmed Intentional (Not Over-Restricting)

| # | File | Lines | Pattern | Why Intentional |
|---|------|-------|---------|-----------------|
| B1 | `compilation_context.py` | 47–54 | SM120 → `0f`, SM121 → `1a` (separate gencodes) | Required for correct cubins — SM120 SASS can cause illegal instructions on SM121 |
| B2 | `quantization/fp4_quantization.py` | 157–165 | `"120"` / `"121"` both → `"120f"` on CUDA ≥ 12.9 | Correct family-level consolidation |
| B3 | `jit/attention/fmha_v2/fmha_library.py` | Various | `kspec.sm == 120` as Blackwell bucket | Design choice: `120` = logical SM12x FMHA label; NVCC gets actual arch from `CompilationContext` |
| B4 | `jit/gemm/cutlass/generate_kernels.py` | 1049 | `has_arch(120) or has_arch(121)` | Explicitly includes both |
| B5 | `fused_moe/core.py` | 206–207 | `backend in ("120", "121")` → shared module | Both mapped to same JIT module |
| B6 | `aot.py` | 380–540 | Separate `has_sm120`, `has_sm121`, `has_sm120f` | AOT needs per-variant control; not over-restricting |
| B7 | All `@supported_compute_capability` decorators | Various | Lists include both `120` and `121` | Consistently inclusive across all audited APIs |

### 14.3 Cosmetic / Documentation Issues

| # | File | Lines | Issue |
|---|------|-------|-------|
| C1 | `prefill.py` | ~4423, 4464 | Docstrings say "SM120 (Blackwell)" without mentioning SM121 |
| C2 | `decode.py` | ~2338 | Mentions `sm_120`/`sm_121` but some messages say just "SM120" |
| C3 | `xqa.py` | ~310 | NVFP4 error message says "SM120 GPUs" but gate is `major == 12` |
| C4 | `fused_moe/cute_dsl/blackwell_sm12x/` | Various | Function names `launch_sm120_*`, `allocate_sm120_*` — naming suggests SM120-only but used for SM12x family |
| C5 | `gemm/kernels/dense_blockscaled_gemm_sm120.py` | Various | File and function names say SM120; architecturally covers SM12x |

---

## 15. Consolidated Action Items

### Must Fix (blocking SM121 correctness or coverage)

- [x] **1.** Change `is_sm120a_supported` → `is_sm12x_supported` in `test_fmha_v2_prefill.py` eligibility checks — `tests/attention/test_fmha_v2_prefill.py:486–492` (T1) — PR: https://github.com/flashinfer-ai/flashinfer/pull/3182 
- [ ] **2.** Validate b12x MoE on SM121 hardware; if passing, remove `@not_sm121` from tests — `tests/moe/test_b12x_fused_moe.py` (T2) — PR:
- [ ] **3.** Validate b12x FP4 GEMM on SM121; if passing, change heuristic to `major == 12` — `flashinfer/gemm/gemm_base.py:5065–5070` (A2) — PR:
- [x] **4.** Allow `"sm_121"` in `dense_blockscaled_gemm_sm120.py` version check — `flashinfer/gemm/kernels/dense_blockscaled_gemm_sm120.py:1591` (A3) — PR: https://github.com/flashinfer-ai/flashinfer/pull/3180
- [ ] **5.** Fix GDN prefill/decode for SM121 — compiled with `sm90a_nvcc_flags`, SM90-only SASS crashes on SM121; add SM12x gencode or SM12x-specific codepath — `flashinfer/jit/gdn.py`, `flashinfer/gdn_prefill.py` (§11, cross-cutting 6) — PR: https://github.com/flashinfer-ai/flashinfer/pull/3960, https://github.com/flashinfer-ai/flashinfer/pull/3731 
- [ ] **6.** Add graceful error or SM12x support for `mm_fp8` — only backend is `trtllm_low_latency` compiled with `sm100a`; crashes on SM121 at module load — `flashinfer/jit/gemm/core.py:868`, `flashinfer/trtllm_low_latency_gemm.py` (§2.7) — PR:
- [ ] **7.** Add `gen_selective_state_update_sm100_module` to AOT when `has_sm120 or has_sm121` — missing; breaks `FLASHINFER_DISABLE_JIT` for Mamba SSU — `flashinfer/aot.py` (§9, cross-cutting 4) — PR:

### Should Fix (improve robustness)

- [x] **8.** Fix `is_sm120f_supported` to use `major == 12` (or rename/remove) — `flashinfer/utils.py:574–576` (A1) — PR: https://github.com/flashinfer-ai/flashinfer/pull/3175
- [x] **9.** Add `"sm_121": 512` to TMEM fallback map — `flashinfer/cute_dsl/attention/compat.py:29–36` (A4) — PR: https://github.com/flashinfer-ai/flashinfer/pull/3173
- [x] **10.** Enable `test_bmm_mxfp8.py` for SM12x (remove skip for `cap[0] in [11, 12]`) — `tests/gemm/test_bmm_mxfp8.py:23–24` (T3) — PR: https://github.com/flashinfer-ai/flashinfer/pull/3183
- [x] **11.** Re-verify SM121 numerical accuracy xfail in `test_jit_example.py` — `tests/utils/test_jit_example.py:169–171` (T4) — PR: https://github.com/flashinfer-ai/flashinfer/pull/3890
- [ x] **12.** Add `120a` and `121a` to wheel build arch targets alongside `120f` — wheels lack NVFP4/MXFP4 MMA without JIT — `.github/workflows/release.yml:185`, `nightly-release.yml:156` (§Wheel) — PR: https://github.com/flashinfer-ai/flashinfer/pull/3907
- [x] **13.** Investigate adding SM12x (120, 121) to `mm_bf16` / `bmm_bf16` cuDNN CC gate — cuDNN likely supports BF16 on SM121 — `flashinfer/gemm/gemm_base.py:219, :446` (§2.2, cross-cutting 2) — PR:
- [x] **14.** Extend `trtllm_allreduce` JIT to support SM12x — currently `[9, 10]` only; no fused allreduce on Spark — `flashinfer/jit/comm.py` (§10, cross-cutting 5) — PR: https://github.com/flashinfer-ai/flashinfer/pull/3903
- [x] **15.** Fix FP4 quant AOT/runtime mismatch — stop redirecting `"121"` → `"120f"`; let `121a` module be used directly on SM121 (consistent with GEMM/MoE); `120f` remains as wheel fallback — `flashinfer/quantization/fp4_quantization.py:157–165`, `flashinfer/aot.py:530–541` (§8, cross-cutting 3) — PR: https://github.com/flashinfer-ai/flashinfer/pull/3906 

### Nice to Have (documentation / cosmetic)

- [x] **16.** Update docstrings/error messages to say "SM12x" or "SM120/SM121" instead of just "SM120" — Various (C1–C5) — PR: https://github.com/flashinfer-ai/flashinfer/pull/3174/changes 
- [ ] **17.** Fix NVFP4 XQA test reason string to say "SM120/SM121" — `tests/attention/test_xqa_batch_decode.py:582–585` (T5) — PR:



## 评论 (25)

### leonardHONG · 2026-04-25

Thanks for the audit — clear roadmap.

Can take Items 4, 5, 6, and 9–10 if they’re free. Also have an RTX Pro 6000 here for sm_120 regression on Items 1 and 7.


### kahyunnam · 2026-05-04

@leonardHONG thanks for taking on these tasks - the PRs look clean, I will help get them merged. I renumbered the list but added checked boxes for your contributions. 

### leonardHONG · 2026-05-05

Thanks @kahyunnam, happy to help with more items if useful.

### eelbaz · 2026-05-10

For anyone running DGX Spark (SM121) — we've been working through these exact gaps in production. A few things from our experience:

- Items 4/5/6/9-10 in the audit map closely to what we've hit. The SM121 smem constraint (99 KiB) is the root cause for most CUTLASS-related failures.
- We built a custom CUTLASS from main to get the StageCountAutoCarveout fix — it's necessary for FP4 MoE kernels.
- For Triton-based paths, pinning the container and clearing ~/.triton/cache between major torch bumps is essential.
- Our working stack: vLLM 0.12.x+ with VLLM_USE_FLASHINFER_MOE_FP4=1, built from the latest nightly, on CUDA 13.0 with the ptxas symlink.

Happy to collaborate on the SM121 support patches if useful — we have real production telemetry from 8× DGX Spark.

### kahyunnam · 2026-05-13

Hi @eelbaz any contributions are welcome here -- we are slightly short staffed for Spark work right now 🙂

### Harry-Chen · 2026-06-11

> Per the [PTX ISA (CUDA 13.2)](https://docs.nvidia.com/cuda/archive/13.2.0/parallel-thread-execution/index.html), `120f` (family) is a subset of `120a`/`121a` (arch-specific). Most SM12x features are family-specific and available via `120f`, but the **NVFP4/MXFP4 block-scaled MMA instructions** (`.kind::mxf4nvf4`, `.kind::mxf4`) are **arch-specific only** — they require `sm_120a` or `sm_121a` and are **not** available via `sm_120f`:

@kahyunnam I think this is only for sparse MMA (`mma.sp`)? Dense `mma` instructions have no type exceptions, and are supported by `sm120f` since PTX ISA 8.8 (per PTX ISA 9.3, §9.7.15.5.14):

> .e3m2, .e2m3 and .e2m1 alternate floating point type mma operation requires sm_120a and is supported on sm_120f from PTX ISA version 8.8.
> Support for .kind, .block_scale, .scale_vec_size qualifier requires sm_120a and are supported on sm_120f or higher in the same family from PTX ISA version 8.8.

vs §9.7.15.6.3 (mma.sp):

> Support for .kind, .block_scale, .scale_vec_size qualifier requires sm_120a and are supported on sm_120f and later generation 
> targets in the same family from PTX ISA version 8.8 except for .kind::mxf4nvf4/.kind::mxf4.
> Qualifiers .kind::mxf4nvf4 and .kind::mxf4 are supported on following architectures:
> sm_120a
> sm_121a

### kahyunnam · 2026-06-12

@Harry-Chen thanks for the catch! I've updated the audit (see "Correction (2026-06-12)") with your correction

### leonardHONG · 2026-06-14

Happy to take Items 6  if they’re still free.

I’ll add the graceful non-SM100 guard for `mm_fp8` and validate the reject path on my 5090..


### kahyunnam · 2026-06-15

@leonardHONG thanks for volunteering -- any unchecked items are still free, other than item 14 which @yichengj0 seems to be working on. You are more than welcome to help out with item 6 🙂

### Sujimoshi · 2026-06-25

@kahyunnam №5 is done

Hi! Wanted to let you know I took item **5** from the action list and it's done — PR is up: https://github.com/flashinfer-ai/flashinfer/pull/3731

This is actually my first open source contribution, so fingers crossed 🙂

Tested on a real DGX Spark (GB10, SM121, CUDA 13.0) — the kernel was crashing at module load before the fix, and works correctly after. The PR covers the CuteDSL path (`gdn_kernels/delta_rule_dsl/`); the older `jit/gdn.py` path is a separate issue as noted in the PR description.

### flashinfer-bot · 2026-06-25

This issue is already assigned. If you'd like to take over, ask a maintainer to use `!assign @Sujimoshi`.

### kahyunnam · 2026-06-26

@Sujimoshi ignore the flashinfer-bot, it seems confused. Thanks for the contribution! I will take a look to review.

### yichengj0 · 2026-07-09

hi @kahyunnam , i opened pr #3890 for fixing item 11, #3903 for item 14, #3906 for item 15, and #3907 for item 12 :)

regarding item 3: i benchmarked the b12x backend vs cutlass and cudnn when working on pr #3560 , and b12x is slightly slower than both. so i did not make b12x the auto-selected backend. this is recorded as a comment in `_heuristic_func_mm_fp4`. 

it seems item 2 and 17 have been fixed, and item 5-7 are already claimed with open prs. so i believe all open items in the list have been addressed at this point.

### ormandj · 2026-07-14

SM120 TP2 serving evidence is now available for item 14's PR #3903. The complete tested stack—#3903, a vLLM SM12x selector, and an initialization-only CUDA-runtime resolver—initialized the TensorRT-LLM workspace, passed semantic correctness, and changed sustained MTP:0 decode by +2.15% to +5.18% across C1-C32 versus an otherwise fixed PyNCCL control. This is joint-stack evidence, not isolated attribution to #3903. #3903's technical review threads are resolved; it still needs authorized CI and maintainer review. A vLLM selector companion is not ready until a FlashInfer release containing #3903 can be pinned.


### Suppressor72 · 2026-08-03

## vLLM impact: TRTLLM FMHA decode + FULL CUDA graphs on consumer Blackwell (SM120)

Adding a concrete downstream impact for the `trtllm-gen` / `trtllm_allreduce` SM12x gap from a vLLM serving perspective.

### Setup
- **GPU:** Dual RTX 5090 (SM120, 32GB each), PCIe Gen4, no NVLink
- **Model:** Qwen3.6-27B-FP8 (block-wise FP8, hybrid linear/full attention + GDN)
- **vLLM:** nightly `0.26.1rc1.dev251`, TP=2, 256k context, MTP=3 (speculative decoding)
- **FlashInfer:** 0.6.15.post1

### What happens

vLLM's `supports_trtllm_attention()` returns `False` for SM120 because the underlying `family(100)` gate matches only major==10. Even if that gate were widened, the kernel infrastructure isn't there:

1. **TRTLLM FMHA decode (`trtllm-gen`):** `isSMCompatible()` in `fmhaKernels.cuh` only handles `kSM_100`/`kSM_103`/`kSM_100f`. No SM120 kernel metadata entries exist in `sTllmGenFmhaKernelMetaInfos`. The pre-compiled cubin path (`cuModuleLoadData`) has nothing to load.

2. **Fused allreduce:** `trtllm_allreduce.cuh` kernels are guarded by `__CUDA_ARCH__ >= 900 && __CUDA_ARCH__ < 1200` — 13 sites, all excluding SM1200.

### Downstream consequence

vLLM's FlashInfer backend reports `AttentionCGSupport.UNIFORM_SINGLE_TOKEN_DECODE` on SM120 instead of `UNIFORM_BATCH`. With speculative decoding (MTP), this forces:

```
CUDAGraphMode.FULL_AND_PIECEWISE is not supported with spec-decode
for attention backend FlashInferBackend → setting cudagraph_mode=PIECEWISE
```

This means every FP8 + MTP serving configuration on consumer Blackwell is stuck on **PIECEWISE** CUDA graphs instead of **FULL**, leaving decode throughput on the table.

### The kernel source appears portable

The FMHA kernel headers (`fmhaKernels.cuh`, `kernelUtils.h`, `fmhaRunner.cuh`) use:
- Thread block clusters ✅ (SM120 supports)
- TMA (`cp.async.bulk`) ✅ (SM120 supports)
- Standard tensor core MMA ✅ (SM120 supports)
- `__CUDA_ARCH__ >= 1000` guards ✅ (naturally include 1200)

**No `tcgen05`/TMEM instructions** were found in the FMHA kernel code — unlike the CUTLASS FMHA and CuteDSL paths which are correctly excluded for SM12x due to tcgen05 dependency.

### Ask

Is there a roadmap for compiling and publishing SM120 (sm_120a) cubins for the TRTLLM FMHA decode path? The kernel source looks architecturally compatible — it appears to be a build/publish pipeline gap rather than a fundamental instruction-set limitation.

Happy to help test if SM120 cubins become available.

### ekinnee · 2026-08-16

SM121 / DGX Spark validation datapoint (not claiming broader coverage):

- Hardware: NVIDIA GB10 / DGX Spark, aarch64, sm121
- Driver: 580.173.02
- Container CUDA runtime: 13.0.2
- vLLM: 0.27.2rc1.dev110+gacb0f1dcd
- FlashInfer: 0.6.16.post3
- Target: RadixArk/Qwen3.8-27B-NVFP4
- KV cache: FP8 E4M3
- Speculation: Qwen DSpark, K=5

On startup, vLLM selected FlashInfer with:
`prefill=torch.bfloat16, decode=torch.bfloat16,
decode_backend=xqa, kv_cache_dtype=torch.float8_e4m3fn,
arch=sm121`

FlashInfer also created/used a `121a` autotune cache. The service started successfully and has served functional direct-code and tool-use requests without an `invalid resource handle` failure.

This is not a reproduction of every SM121 issue: Qwen3.8’s geometry differs from the Qwen3.6 head_dim=256 case, and it should not be read as a claim that all FlashInfer SM121 paths are fixed. It does confirm that this current XQA + FP8-KV path is working on GB10.

### bkryu · 2026-08-17

Hi @Suppressor72, thanks for reaching out about this

> Is there a roadmap for compiling and publishing SM120 (sm_120a) cubins for the TRTLLM FMHA decode path? The kernel source looks architecturally compatible — it appears to be a build/publish pipeline gap rather than a fundamental instruction-set limitation.

Short answer is no, we do not have plans to generate SM120 TRTLLM FMHA cubins. The reason here is SM100/103 and SM120/121 have different SM and tensor core architectures, which means a nearly full kernel rewrite is needed.

However, as pointed out by @ekinnee above, XQA is a strong decode option. It is based on the XQA kernels from TRTLLM, which has recently been expanded in  #4137  to cover attention sinks, spec-dec, and etc. without losing CUDA graph support. We expect fairly good performance on RTX PRO 6000 and DGX Spark.

The following recent vLLM PRs should have wired the XQA kernels
* https://github.com/vllm-project/vllm/pull/52148
* https://github.com/vllm-project/vllm/pull/49718

### jahnclawdmonet · 2026-08-26

SM121 / DGX Spark datapoint, bare-metal (no container), with a release-vs-nightly gate comparison for the XQA decode path.

Hardware: NVIDIA GB10 (cc 12.1, 48 SMs by torch multi_processor_count, 121.7 GiB unified), driver 580.159.03, CUDA 13.0 host toolkit, aarch64, Ubuntu 24.04.4.

**Bare-metal install path (uv, no container):** `uv venv --python 3.12` then `uv pip install vllm --torch-backend=auto` resolved and installed vLLM 0.27.1 + FlashInfer 0.6.16.post3 + torch 2.13.0+cu130 from plain PyPI in about 32 seconds. Two landmines worth documenting for bare-metal Spark users:
- FlashInfer JIT invokes `ninja` from PATH; running the venv python by absolute path without activating leaves it off PATH (`FileNotFoundError: 'ninja'`).
- NVFP4 GEMM goes through `FlashInferCutlassNvFp4LinearKernel` and JIT-builds the sm12x CUTLASS FP4 module on first start (no prebuilt sm_121 artifact); cold start to `/health` was 425 s, warm 255 s (weights 98-115 s, torch.compile 8.5 s cached, autotune 21 s, graph capture 13-20 s).

**Serving (vLLM 0.27.1 release, unsloth/Qwen3.6-27B-NVFP4, kv fp8, 65,536 ctx, TP=1):** starts and serves correctly. Backend resolution on sm_121: `decode_backend=flashinfer-native, prefill=torch.bfloat16, decode=torch.bfloat16, kv_cache_dtype=float8_e4m3fn, arch=sm121`; default cudagraph mode FULL_AND_PIECEWISE; KV cache 83.65-86.23 GiB available (about 2.5M tokens). Long-range recall on the release is clean across a 4-config matrix (default, +use_trtllm_attention with FULL requested, +enforce-eager, +PIECEWISE): every config resolves to flashinfer-native decode and needle retrieval passes 16/16 at 2.5K/10K/16K/49K depth, temperature 0, `chat_template_kwargs: {"enable_thinking": false}` so the codeword is measurable within a small max_tokens.

**XQA decode gate, release vs nightly:**
- 0.27.1 (release): `supports_trtllm_attention` allows SM90 (XQA) or `is_device_capability_family(100)` only. On GB10, `--attention-config.use_trtllm_attention true` logs `TRTLLM attention is not supported on this platform for prefill, but --attention-config.use_trtllm_attention is set to 1` and decode stays `flashinfer-native`. Requesting pure `FULL` cudagraphs is also demoted: `CUDAGraphMode.FULL is not supported with FlashInferBackend backend (support: AttentionCGSupport.UNIFORM_SINGLE_TOKEN_DECODE); setting cudagraph_mode=FULL_AND_PIECEWISE`. So the XQA-under-captured-graph regime is not constructible on the current release at all.
- Nightly (0.26.1rc1.dev1214+gf6130145c, FlashInfer 0.6.17; the nightly wheel's version string is numerically lower than the 0.27.1 release but the dev1214 build is newer): the gate now reads `if is_device_capability(90) or is_device_capability_family(120): return not is_prefill`, and `_get_flashinfer_trtllm_api_decode_kernel()` returns `FlashInferDecodeKernel.XQA` for family 12x, consistent with the earlier sm121 datapoint in this thread. `has_nvidia_artifactory()` is True from this host (edge.urm.nvidia.com reachable, HTTP 200 in 0.2 s), so XQA cubins can actually be fetched.

A follow-up with the nightly-side runs (XQA decode actually engaged, the cubins it fetches, and a needle-recall cross-check of vllm-project/vllm#49010's captured-graph corruption on sm_121) is in progress on the same box and will be posted when complete.

Environment probe used for the cell identification: blackwell-doctor (reports arch sm_121, unified 121.7 GiB, and the stack versions above).

### nickchan0412 · 2026-09-18

Precise datapoint for the audit, from vLLM nightly (`v0.3.1.dev3+g0bfc7a15d`, flashinfer 0.6.18.post1) on DGX Spark GB10 (capability 12.1, sm_121a):

**JIT compilation of the B12X CuTe-DSL MoE kernel for SM121 works.** With `--kernel-config '{"moe_backend":"flashinfer_b12x"}'` (vLLM's explicit opt-in path), the kernel compiles and persists cleanly:

```
flashinfer.jit: Compiling CuTe-DSL kernel b12x_moe_sm121a_cute_dsl/dynamic_e512_k2560_n640_t10_b58b2b30e71f146c
flashinfer.jit: Persisted CuTe-DSL kernel to /root/.cache/flashinfer/0.6.18.post1/121a/cached_ops/b12x_moe_sm121a_cute_dsl/...
```

(that is E=512 experts, K=2560 hidden, N=640 intermediate, top-k=10 — Qwen3.8-Flash-Next NVFP4's main experts.)

**The first run then dies with an illegal memory access** (delayed report surfaces on the next Triton `load_binary`):

```
RuntimeError: Triton Error [CUDA]: an illegal memory access was encountered
```

So on 0.6.18.post1 the SM121 story for `b12x_fused_moe` is: compile ✅ / run ❌ (dynamic kernel, modelopt source format, activation_precision=fp4). This matches vLLM's comment excluding FLASHINFER_B12X from auto-selection "until the upstream CUTLASS SM121 MMA op guard is resolved" (vllm `fused_moe/oracle/nvfp4.py`).

Two integration notes for anyone reproducing via vLLM:
1. `moe_backend=flashinfer_b12x` is global; mixed-quant checkpoints with FP8 MoE layers (e.g. the MTP draft experts) hit `map_fp8_backend: moe_backend='flashinfer_b12x' is not supported for FP8 MoE` — an FP8 fallback (we patch it to TRITON locally) is needed.
2. Suspect worth checking first: N=640 is not divisible by 256 (it is by 128) — if any tile/predication path assumes N % 256 == 0 that would produce exactly this kind of OOB on our shape.

Environment: aarch64, CUDA 13 line, `CUTE_DSL_ARCH=sm_121a`, kernel cache shows `121a/` path taken. Happy to run instrumented repros if useful.

Assisted-by: AI agent (ZCode); measurements made and confirmed on hardware by the submitter.

### jahnclawdmonet · 2026-09-18

Your instinct that a 256 alignment path could do this is not wrong in general. There are two such paths in 0.6.18.post1, and it is worth naming them so they can be ruled out rather than left hanging:

- `moe_direct_micro_kernel.py:993` carries the comment "A last 256-wide chunk overhanging a non-256-aligned n reads the uninitialized intermediate tail", which is the shape of failure you are describing.
- `moe_w4a16_kernel.py:5373,5406` overrides to `tile_n=256` behind `int(fc1_cols) % 256 == 0` and `int(hidden_size) % 256 == 0`.

Neither is reachable from where you are. The direct-micro path is gated on `n <= _DIRECT_MICRO_MAX_N` with `_DIRECT_MICRO_MAX_N = 512` (`moe_dispatch.py:83,1519`), so N=640 cannot enter it. The w4a16 override is a different quant mode: `_level_tile_n` raises "internal routing error: quant_mode='w4a16' reached the NVFP4 tile selector" if the two ever cross.

On the NVFP4 dynamic path you are actually on, the tile is `_LEVEL_TILE_N = 128` and the requirement is a multiple of 128, which 640 satisfies. Non-128-aligned N is padded rather than rejected (`moe_dispatch.py:3208`), with the `ValueError` at :549 as a backstop for pre-built weight views. `_STATIC_RETAINED_GROUP_N`, the one constant that does group N into 256, is absent from 0.6.18.post1 entirely and appears only on main, where it is confined to the static schedule and applied as padding: "retained2 always consumes two adjacent N128 slices ... dynamic keeps its native N128 geometry" (main `moe_dispatch.py:3534-3538`).

Two things that are specific to your shape and might be more useful.

First, 640 is above `_GATED_OPTIMIZED_MAX_INTERMEDIATE_SIZE`, which is `_GATED_OPTIMIZED_RETAINED_SLICES * 128 = 512` (`moe_dynamic_kernel.py:18-19,44-47`), so you fall to the generic dynamic kernel rather than the gated one. That is a real branch difference at your exact N.

Second, coverage. 640 is five N128 slices, an odd count, and no NVFP4 test in your version executes one. In `tests/moe/test_b12x_fused_moe.py` at that tag, 640 appears three times: two dispatch-decision parametrize entries and one assertion about the static cutover constant, none of them an executed shape. main added the missing case later as `test_intermediate_padding_matches_selected_backend`, parametrized `intermediate_size=[640, 704]`, docstring "Odd N128 counts stay correct across static and dynamic dispatch".

If you do run instrumented repros, two things would narrow it a lot. Record the `num_tokens` at the failure: for a gated activation `_select_dynamic_tile_m` picks the M tile from routed rows against the expert count, first band at `15 * num_experts`, so with E=512 and top-k 10 anything under 768 tokens sits in the smallest tile_m. Its docstring states the invariant that would produce this class of fault if it were ever broken, though I have not traced an actual mismatch: "Workspace sizing and the kernel build must both derive the tile from this function, or the scratch is mis-sized for what the kernel indexes." And raising `FLASHINFER_B12X_STATIC_COMPACT_CUTOVER_PAIRS` to force the same shape through static would say whether this is dynamic-only.


### nickchan0412 · 2026-09-18

Follow-up that supersedes part of my earlier comment, after deeper isolation on the same box (flashinfer 0.6.18.post1, GB10 sm_121a, Qwen3.8-Flash-Next NVFP4: E=512, K=2560, N=640, top-k=10):

**1. The kernel itself is fine on our shape.** A standalone `b12x_fused_moe` repro (random fp4-packed weights, MMA-swizzled e4m3 SFs via the same `convert_sf_to_mma_layout` vLLM uses, m swept 8 → 4096, plus CUDA-graph capture+replay via `B12xMoEWrapper(use_cuda_graph=True)`, plus adversarial topk_ids: all-one-expert, -1 padding, out-of-range) **passes everywhere**, including the exact dynamic kernel variant that dies inside vLLM (`dynamic_e512_k2560_n640_t10_b58b2b30e71f146c`). The in-vLLM crash surfaces synchronously (CUDA_LAUNCH_BLOCKING=1) at `launch_sm120_dynamic_moe` → `compiled(*runtime_args)` with `CUDA Error Code: 700`, launch params: `num_tokens=4096 k=2560 n=640 top_k=10 ws.max_rows=73664 ws.tile_m=64 E=512`. So the IMA is integration/tensor-lifetime dependent (real checkpoint SF bytes, allocator state, or stream context) rather than a plain shape bug — pointer for whoever digs next.

**2. B12X is doubly unusable for large-E + large-batch serving shapes regardless:**
- dynamic path: the IMA above;
- static path: `FLASHINFER_B12X_STATIC_COMPACT_CUTOVER_PAIRS` raised to cover warmup (40,960 routed rows) fails `_check_memref_limit`: `static packed_input needs 26,843,545,600 elements, which exceeds the 2^31-1 runtime memref limit` — the static packed_input scales with E × rows, so 512-expert models can't raise the cutover far.

Net: on GB10 with 512-expert NVFP4 MoE at 4,096-token batches, vLLM's auto-selected FLASHINFER_CUTLASS remains the only working backend in 0.6.18.post1. If the dynamic-kernel IMA under vLLM gets fixed and the static packed_input memref layout gets an E-aware split, B12X would become attractive again (the SM121 compile chain itself is healthy).

Assisted-by: AI agent (ZCode); measurements made and confirmed on hardware by the submitter.

### jahnclawdmonet · 2026-09-18

Your launch params close the workspace lead I raised, so it can come off the list.

Both numbers you printed are exactly what the host formulas produce for your shape. `routed_rows = 4096 * 10 = 40960` sits under `96 * 512 = 49152`, which is the band that selects `tile_m = 64`, matching your `ws.tile_m=64`. And `_align_up(40960, 64) // 64 = 640` plus `min(512, 40960) - 1 = 511` gives 1151 tiles, so `1151 * 64 = 73664`, matching your `ws.max_rows=73664` to the row.

That only shows the host side is self consistent: the workspace was sized from the same `tile_m` the plan reports. It does not prove the kernel indexes within it. But the specific failure the `_select_dynamic_tile_m` docstring warns about, the sizing and the kernel build deriving the tile from different places, would show up as a mismatch in exactly these two numbers, and there isn't one. Combined with your standalone repro passing on the same compiled variant, that points where you are pointing, at what vLLM hands the kernel rather than at the plan.


### jschmied · 2026-09-21

Data for action item 2 (validate b12x MoE on SM121), plus a note that its stated blocker is stale.

**Box**: NVIDIA DGX Spark, GB10, `sm_121`, aarch64, flashinfer `0.6.18.post1`, torch `2.13.0+cu130`,
driver 580.x. Tests taken from the `v0.6.18.post1` tag.

`tests/moe/test_b12x_fused_moe.py` passes on SM121:

```
189 passed, 2 warnings in 151.63s   (cold, JIT compile)
189 passed, 2 warnings in  44.61s   (warm cache, second run)
```

This includes the numerical-accuracy tests, not only the structural ones — `test_relu2_micro_accuracy`,
`test_relu2_functional_accuracy`, `test_relu2_wrapper_accuracy`, and the W4A16 variants
`test_relu2_w4a16_direct_micro_accuracy` / `test_relu2_w4a16_functional_accuracy`.

**The `@not_sm121` decorator named in item 2 no longer exists.** It is absent from
`tests/moe/test_b12x_fused_moe.py` both at `v0.6.18.post1` and on `main`, and a repository code
search for `not_sm121` returns no hits. So the item's action ("remove `@not_sm121` from tests") looks
already done or renamed; the validation half is what this comment supplies.

**Scope, stated plainly**: 11 distinct test functions, 48 of the 189 from one activation class. This
says the b12x MoE path runs and is numerically correct on SM121 for what that file covers. It is not
a claim about b12x MoE coverage in general, and I have not run a performance comparison.

Item 3 (b12x FP4 GEMM) I could not run the same way: there is no `test_b12x_*` file under
`tests/gemm`, so if you can name the intended test target I will run it on this box.

_AI assistance (Claude Code) was used in preparing this comment; the runs are from the box described._


### jahnclawdmonet · 2026-09-21

There is no `test_b12x_*` under `tests/gemm` because the b12x dense GEMM kernel is not exposed as its own entry point. `flashinfer/gemm/kernels/dense_blockscaled_gemm_sm120_b12x.py` defines `Sm120B12xBlockScaledDenseGemmKernel`, and two GEMM paths reach it.

FP4, through svdquant. `tests/gemm/test_nvfp4_svdquant_gemm.py` imports that module by name in `test_sm120_svdquant_kernel_iket_flag_defaults_off` and `test_sm120_svdquant_can_implement_rejects_ragged_rank`. The file also carries `_skip_unless_sm120` and `_assert_sm120_accuracy` helpers. That is the closest thing to item 3 as written.

mxfp8, through `flashinfer/gemm/gemm_mm_mxfp8_cute_dsl.py`, which defines `_b12x_gemm_mxfp8_runner` around the same kernel class. `gemm_base.py` imports that runner and its requirement predicate at lines 66 and 67. The SM120 file there is `tests/gemm/test_mm_mxfp8_sm120.py`.

`tests/jit/test_cute_dsl_cache.py` also pulls from `gemm_svdquant`, but only the kernel-name codegen, so it runs nothing on the device.


### jschmied · 2026-09-21

Root cause for the b12x MoE fault on SM121, at instruction level. Same box as my action-item-2
comment above (GB10, `sm_121a`, flashinfer `0.6.18.post1`, Qwen3.8-Flash-Next NVFP4: E=512, K=2560,
N=640, top-k=10).

**The kernel indexes its expert histogram with a routed id that can be `-1`.**
`_moe_dynamic/generic.py:1053-1057`:

```python
# Phase 1: histogram routed rows per expert.
hist_idx = flat_tid
while hist_idx < total_pairs:
    expert_id = topk_ids[hist_idx].to(Int32)
    atomic_add_global_i32(get_ptr_as_int64(row_counts, expert_id), Int32(1))
    hist_idx += flat_stride
```

vLLM writes `-1` into `topk_ids` for cudagraph padding rows (`VLLM_MOE_SKIP_PADDING`, on by
default) to mean "not routed". With `expert_id = -1` this forms a pointer one `int32` **before**
`row_counts` and atomically adds to it, which is why the Xid reads `ACCESS_TYPE_VIRT_WRITE` rather
than a read fault:

```
NVRM: Xid (PCI:000f:01:00): 31, MMU Fault: ENGINE GRAPHICS GPC1, FAULT_PDE ACCESS_TYPE_VIRT_WRITE
```

Two things that fit the symptom exactly:

- **Only the generic dynamic path is affected.** `gated.py:3012-3019` accumulates into shared
  memory and flushes with `hist_bin` as a loop counter over `0..num_experts`, so its global write is
  bounded by construction. `_can_use_gated_optimized_kernel` is `False` for any
  `intermediate_size > 512`, so N=640 lands on the generic path — 512 returns `True`, 640/768/1024
  return `False`.
- **Calling the same shapes with valid ids is clean.** At 320 / 640 / 1280 / 2560 / 5120 / 10240 /
  20480 / 40960 routed rows there is no fault, static and dynamic alike. Flipping only the routing
  table to all `-1`, same process and shapes, faults. Masking the padded slots makes it clean again.

**A predicate on that one line is not sufficient.** `expert_id` reaches seven indexing sites across
two phases, and is cached into shared memory and read back:

| line | use |
| --- | --- |
| 1057 | `atomic_add(row_counts, expert_id)` |
| 1139 / 1340 | `atomic_add(expert_write_rows, expert_id)` |
| 1142 / 1343 | `expert_tile_base[expert_id]`, then `st_global_i32(token_map, phys_row)` at the derived row |
| 1159 | `_st_shared_i32(route_expert_ids_addr + ..., expert_id)` |
| 1361 | `input_global_scale[expert_id]` |

Sites 1139/1142 and 1340/1343 are worse than the histogram: they derive `phys_row` from
out-of-bounds state and then store to it. Guarding only some of these would turn a clean fault into
silent corruption, so a correct fix means excluding padded pairs from the cooperative pack and its
row accounting, not adding predicates.

I have a vLLM-side workaround in flight (vllm-project/vllm#57946) that masks the sentinel before the
call — padded slots to expert 0 with weight 0. It costs ~6.3 us per MoE call under cudagraphs (5.4%
of the b12x MoE call at M=1 on this box, under 1.5% from M=4), and it still computes expert 0 for
padded routes rather than skipping them, so handling `topk_id < 0` natively here would be strictly
better on both counts. Happy to test any patch on this hardware — I can reproduce it in a ~40-line
script with no vLLM involved.

*Prepared with AI assistance (Claude Code); all numbers are from real runs on the box named.*

