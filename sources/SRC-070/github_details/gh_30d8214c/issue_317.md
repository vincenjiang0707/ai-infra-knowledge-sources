# [Issue #317] DeepSeek-V4 on SM120: tf32_hc_prenorm_gemm and paged_mqa_logits kernels missing

source: https://github.com/deepseek-ai/DeepGEMM/issues/317
state: closed | updated: 2026-04-30T06:54:14Z
labels: 

## 正文

## Summary

Two DeepGEMM kernel families used by DeepSeek-V4 hit `Unsupported architecture` assertions on SM120 (Compute Capability 12.0):

1. `tf32_hc_prenorm_gemm` — used by Manifold-Constrained Hyper-Connections (mHC). Assertion at `csrc/apis/hyperconnection.hpp:56`.
2. `get_paged_mqa_logits_metadata` / `paged_mqa_logits` — used by the Lightning Indexer. Assertion at `csrc/apis/attention.hpp:211`.

This blocks DeepSeek-V4-Flash and DeepSeek-V4-Pro from running on RTX Pro 6000 Blackwell and RTX 5090 GPUs in frameworks that depend on DeepGEMM for these kernels.

Looking at `csrc/apis/hyperconnection.hpp` and the `impls/` directory, only `sm90_tf32_hc_prenorm_gemm.hpp` and `sm100_tf32_hc_prenorm_gemm.hpp` exist — there is no SM120 implementation. The same pattern applies to the paged MQA logits kernels (see existing Issue #236, which reports the missing `sm120_fp8_paged_mqa_logits.cuh`).

## Environment

- **GPU:** 2× NVIDIA RTX Pro 6000 Blackwell (96 GB GDDR7, SM120 / Compute Capability 12.0)
- **CPU:** AMD EPYC Turin (Gen 5), single-socket
- **Driver:** 595.45.04 (host)
- **CUDA Toolkit (host, max supported):** 13.2
- **CUDA Toolkit (container, used for build):** 13.0 (from image tag `cu130`)
- **Model:** `deepseek-ai/DeepSeek-V4-Flash` (released 2026-04-24)

Two frameworks were tested:
- **vLLM** `0.1.dev15830+g8d599d76a` (image `vllm/vllm-openai:deepseekv4-cu130`)
- **SGLang** (image `lmsysorg/sglang:deepseek-v4-blackwell`, container CUDA 12.9.1)

## Crash 1: HyperConnection kernel (vLLM)

Launching DeepSeek-V4-Flash with `tensor-parallel-size 2`, `--kv-cache-dtype fp8`, `--enforce-eager`. The model loads successfully (148.66 GiB across 46 shards, ~73.91 GiB per GPU). The crash occurs during `profile_run`, on the first forward pass through an HC layer.

```
File "vllm/model_executor/models/deepseek_v4.py", line 519, in forward
    x, post, comb = self.hc_pre(...)
File "vllm/model_executor/models/deepseek_v4.py", line 490, in hc_pre
    post_mix, res_mix, layer_input = torch.ops.vllm.mhc_pre(...)
File "vllm/model_executor/layers/mhc.py", line 263, in mhc_pre
    tf32_hc_prenorm_gemm(...)
File "vllm/utils/deep_gemm.py", line 479, in tf32_hc_prenorm_gemm
    return _tf32_hc_prenorm_gemm_impl(...)
RuntimeError: Assertion error (/workspace/.deps/deepgemm-src/csrc/apis/hyperconnection.hpp:56): Unsupported architecture
```

## Crash 2: Lightning Indexer kernel (SGLang)

With `SGLANG_DISABLE_DEEP_GEMM=1`, `--fp8-gemm-backend triton`, `--moe-runner-backend triton`, and `--disable-cuda-graph`, SGLang successfully:

- Loads the model (88.05 GiB per GPU)
- Initializes the memory pool (`DSv4 compressed attention: kv_cache_dtype=torch.float8_e4m3fn`)
- Starts the server and accepts the first HTTP request (`Prefill batch, #new-seq: 1, #new-token: 256`)

On the first forward pass, the crash occurs inside the attention backend's indexer metadata initialization:

```
File ".../sglang/srt/layers/attention/deepseek_v4_backend_radix.py", line 491,
    in init_forward_metadata_prefill
    self.init_forward_metadata_indexer(core_attn_metadata)
File ".../sglang/srt/layers/attention/deepseek_v4_backend_radix.py", line 410,
    in init_forward_metadata_indexer
    return PagedIndexerMetadata(...)
File ".../sglang/srt/layers/attention/compressed/metadata.py", line 142,
    in __post_init__
    self.deep_gemm_metadata = get_paged_mqa_logits_metadata(...)
RuntimeError: Assertion error (csrc/apis/attention.hpp:211): Unsupported architecture
```

Notably, SGLang's mHC path does **not** crash on SM120 — SGLang implements `mhc_pre` via TileLang (TVM-based JIT), visible in the stack trace at `sglang/srt/layers/mhc.py:514` calling `tilelang/jit/kernel.py`. TileLang generates SM120-compatible code at runtime. This demonstrates that at least for the HC kernel, an SM120-capable alternative implementation path exists.

SGLang's Lightning Indexer path, however, calls `get_paged_mqa_logits_metadata` directly from DeepGEMM with no alternative backend, so the `attention.hpp:211` assertion is a hard blocker.

## Root cause

Both assertions dispatch by compute capability and find only `sm90_*` and `sm100_*` implementations. `csrc/jit_kernels/impls/` contains no SM120 variants for either kernel family.

This extends the SM120 gap already tracked in:
- #185 — SM120 cannot use SM100 kernels (`tcgen05.fence` not available on SM120) or SM90 kernels (`wgmma` not available on SM120); SM120 needs its own implementations.
- #236 — Feature request for general SM120 support, reporting missing `sm120_fp8_paged_mqa_logits.cuh`.

## Impact

DeepSeek-V4 (both Flash and Pro) cannot complete a forward pass on any consumer/workstation Blackwell GPU (RTX 5090, RTX Pro 6000 Blackwell) in vLLM or SGLang until SM120 implementations of these kernels exist. V4-Flash fits on 2× RTX Pro 6000 from a memory perspective (~88 GiB per GPU for weights, within the 96 GiB per-GPU budget), so this is purely a kernel-availability issue.

## Request

Would the team consider adding SM120 implementations for:
1. `tf32_hc_prenorm_gemm` (and any related HC-API kernels)
2. `paged_mqa_logits` and `get_paged_mqa_logits_metadata`

Even slower reference implementations that simply unblock SM120 would be highly valuable to the community while tuned versions are developed.

If the team is unable to prioritize this, would a community contribution be welcome? Guidance on the expected approach (e.g., CUTLASS 4.x SM120 collective builder, hand-written kernels, or exposing a non-DeepGEMM fallback through the same API) would help others contribute.

Thank you for your work on DeepGEMM.

## 评论 (1)

### zheanxu · 2026-04-30

Thanks for the detailed report. Please see PR #318 for a reference implementation. We do not plan to maintain SM120 ourselves due to lack of hardware and manpower, but community contributions are very welcome.

