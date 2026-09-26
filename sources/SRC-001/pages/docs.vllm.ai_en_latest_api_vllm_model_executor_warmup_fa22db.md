source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/warmup/
lastmod: 2026-09-24

#

`vllm.model_executor.warmup`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup)

Modules:

-
–[b12x_warmup](https://docs.vllm.ai/b12x_warmup/#vllm.model_executor.warmup.b12x_warmup)Warm b12x JIT kernels used by a loaded model.

-
–[cutedsl_warmup](https://docs.vllm.ai/cutedsl_warmup/#vllm.model_executor.warmup.cutedsl_warmup)Deprecated compatibility registry for legacy CuTeDSL warmups.

-
–[deep_gemm_warmup](https://docs.vllm.ai/deep_gemm_warmup/#vllm.model_executor.warmup.deep_gemm_warmup)Warmup deep_gemm kernels.

-
–[flashinfer_autotune_cache](https://docs.vllm.ai/flashinfer_autotune_cache/#vllm.model_executor.warmup.flashinfer_autotune_cache)FlashInfer autotune cache helpers.

-
–[flashinfer_sparse_mla_warmup](https://docs.vllm.ai/flashinfer_sparse_mla_warmup/#vllm.model_executor.warmup.flashinfer_sparse_mla_warmup)Warmup and autotune helpers for FlashInfer sparse MLA backends.

-
–[jit_warmup](https://docs.vllm.ai/jit_warmup/#vllm.model_executor.warmup.jit_warmup)Shared interfaces and tracing helpers for explicit JIT warmup keys.

-
–[jit_warmup_cutedsl_helper](https://docs.vllm.ai/jit_warmup_cutedsl_helper/#vllm.model_executor.warmup.jit_warmup_cutedsl_helper) -
–[jit_warmup_tilelang_helper](https://docs.vllm.ai/jit_warmup_tilelang_helper/#vllm.model_executor.warmup.jit_warmup_tilelang_helper)Compile-only helpers for TileLang JIT warmup.

-
–[jit_warmup_triton_helper](https://docs.vllm.ai/jit_warmup_triton_helper/#vllm.model_executor.warmup.jit_warmup_triton_helper) -
–[kernel_warmup](https://docs.vllm.ai/kernel_warmup/#vllm.model_executor.warmup.kernel_warmup)Warmup kernels used during model execution.

-
–[kimi_k3_triton_warmup](https://docs.vllm.ai/kimi_k3_triton_warmup/#vllm.model_executor.warmup.kimi_k3_triton_warmup)Warm up Kimi-K3 Triton kernels.

-
–[mamba_triton_warmup](https://docs.vllm.ai/mamba_triton_warmup/#vllm.model_executor.warmup.mamba_triton_warmup)Warm Mamba-style Triton kernels shared across GDN / Mamba / KDA models.

-
–[qwen4_exp_qsa_warmup](https://docs.vllm.ai/qwen4_exp_qsa_warmup/#vllm.model_executor.warmup.qwen4_exp_qsa_warmup)Connect loaded Qwen4Exp QSA modules to their kernel-owned warmup.

-
–[qwen_triton_warmup](https://docs.vllm.ai/qwen_triton_warmup/#vllm.model_executor.warmup.qwen_triton_warmup)Warm up Qwen Triton kernels from the loaded model's compile keys.

-
–[qwen_vl_triton_warmup](https://docs.vllm.ai/qwen_vl_triton_warmup/#vllm.model_executor.warmup.qwen_vl_triton_warmup)Warm Qwen3-VL ViT kernels and M-RoPE for SupportsMRoPE models.

-
–[watermark_sample_warmup](https://docs.vllm.ai/watermark_sample_warmup/#vllm.model_executor.warmup.watermark_sample_warmup)Warm up the watermarked sampler's Triton kernel.