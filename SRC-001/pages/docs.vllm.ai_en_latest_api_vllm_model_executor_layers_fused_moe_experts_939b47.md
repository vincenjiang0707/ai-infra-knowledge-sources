source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_moe.experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts)

Modules:

-
–[aiter_mxfp4_w4a16_moe](https://docs.vllm.ai/aiter_mxfp4_w4a16_moe/#vllm.model_executor.layers.fused_moe.experts.aiter_mxfp4_w4a16_moe) -
–[aiter_mxfp4_w4a8_moe](https://docs.vllm.ai/aiter_mxfp4_w4a8_moe/#vllm.model_executor.layers.fused_moe.experts.aiter_mxfp4_w4a8_moe) -
–[aiter_mxfp8_moe](https://docs.vllm.ai/aiter_mxfp8_moe/#vllm.model_executor.layers.fused_moe.experts.aiter_mxfp8_moe)MXFP8 (1x32 block, E8M0) MoE via AITER's FlyDSL two-stage grouped GEMM

-
–[batched_deep_gemm_moe](https://docs.vllm.ai/batched_deep_gemm_moe/#vllm.model_executor.layers.fused_moe.experts.batched_deep_gemm_moe) -
–[cpu_int4_moe](https://docs.vllm.ai/cpu_int4_moe/#vllm.model_executor.layers.fused_moe.experts.cpu_int4_moe)CPU INT4 W4A8 dynamic quantized fused MoE experts.

-
–[cpu_moe](https://docs.vllm.ai/cpu_moe/#vllm.model_executor.layers.fused_moe.experts.cpu_moe)CPU fused MoE experts.

-
–[cutlass_moe](https://docs.vllm.ai/cutlass_moe/#vllm.model_executor.layers.fused_moe.experts.cutlass_moe)CUTLASS based Fused MoE kernels.

-
–[deep_gemm_moe](https://docs.vllm.ai/deep_gemm_moe/#vllm.model_executor.layers.fused_moe.experts.deep_gemm_moe) -
–[fallback](https://docs.vllm.ai/fallback/#vllm.model_executor.layers.fused_moe.experts.fallback) -
–[flashinfer_b12x_moe](https://docs.vllm.ai/flashinfer_b12x_moe/#vllm.model_executor.layers.fused_moe.experts.flashinfer_b12x_moe) -
–[flashinfer_cutedsl_batched_moe](https://docs.vllm.ai/flashinfer_cutedsl_batched_moe/#vllm.model_executor.layers.fused_moe.experts.flashinfer_cutedsl_batched_moe) -
–[flashinfer_cutedsl_moe](https://docs.vllm.ai/flashinfer_cutedsl_moe/#vllm.model_executor.layers.fused_moe.experts.flashinfer_cutedsl_moe) -
–[flashinfer_cutlass_moe](https://docs.vllm.ai/flashinfer_cutlass_moe/#vllm.model_executor.layers.fused_moe.experts.flashinfer_cutlass_moe) -
–[fused_batched_moe](https://docs.vllm.ai/fused_batched_moe/#vllm.model_executor.layers.fused_moe.experts.fused_batched_moe)Fused batched MoE kernel.

-
–[fused_humming_moe](https://docs.vllm.ai/fused_humming_moe/#vllm.model_executor.layers.fused_moe.experts.fused_humming_moe)Fused MoE utilities for Humming.

-
–[gpt_oss_triton_kernels_moe](https://docs.vllm.ai/gpt_oss_triton_kernels_moe/#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe) -
–[int4_emulation_moe](https://docs.vllm.ai/int4_emulation_moe/#vllm.model_executor.layers.fused_moe.experts.int4_emulation_moe)Int4 weight-only quantization emulation for MoE.

-
–[lora_context](https://docs.vllm.ai/lora_context/#vllm.model_executor.layers.fused_moe.experts.lora_context) -
–[lora_experts_mixin](https://docs.vllm.ai/lora_experts_mixin/#vllm.model_executor.layers.fused_moe.experts.lora_experts_mixin) -
–[marlin_moe](https://docs.vllm.ai/marlin_moe/#vllm.model_executor.layers.fused_moe.experts.marlin_moe)Fused MoE utilities for GPTQ.

-
–[moonep_experts](https://docs.vllm.ai/moonep_experts/#vllm.model_executor.layers.fused_moe.experts.moonep_experts)MoonEP experts: grouped GEMM over MoonEP's expert-grouped activations.

-
–[mxfp8_emulation_moe](https://docs.vllm.ai/mxfp8_emulation_moe/#vllm.model_executor.layers.fused_moe.experts.mxfp8_emulation_moe)MXFP8 (1x32 block, E8M0 scale) MoE experts on Triton.

-
–[mxfp8_native_moe](https://docs.vllm.ai/mxfp8_native_moe/#vllm.model_executor.layers.fused_moe.experts.mxfp8_native_moe)Native MXFP8 (1x32 block, E8M0 scale) MoE for AMD CDNA4 (gfx950) via Triton

-
–[nvfp4_emulation_moe](https://docs.vllm.ai/nvfp4_emulation_moe/#vllm.model_executor.layers.fused_moe.experts.nvfp4_emulation_moe)NVFP4 quantization emulation for MoE.

-
–[ocp_mx_emulation_moe](https://docs.vllm.ai/ocp_mx_emulation_moe/#vllm.model_executor.layers.fused_moe.experts.ocp_mx_emulation_moe)OCP MX quantization emulation for MoE.

-
–[rdna3_moe](https://docs.vllm.ai/rdna3_moe/#vllm.model_executor.layers.fused_moe.experts.rdna3_moe)Fused MoE W4A16 experts on the RDNA3 (gfx1100) HIP kernel.

-
–[rocm_aiter_moe](https://docs.vllm.ai/rocm_aiter_moe/#vllm.model_executor.layers.fused_moe.experts.rocm_aiter_moe) -
–[triton_cutlass_moe](https://docs.vllm.ai/triton_cutlass_moe/#vllm.model_executor.layers.fused_moe.experts.triton_cutlass_moe) -
–[triton_deep_gemm_moe](https://docs.vllm.ai/triton_deep_gemm_moe/#vllm.model_executor.layers.fused_moe.experts.triton_deep_gemm_moe) -
–[triton_moe](https://docs.vllm.ai/triton_moe/#vllm.model_executor.layers.fused_moe.experts.triton_moe)Triton-based MoE expert implementations.

-
–[trtllm_bf16_moe](https://docs.vllm.ai/trtllm_bf16_moe/#vllm.model_executor.layers.fused_moe.experts.trtllm_bf16_moe) -
–[trtllm_fp8_moe](https://docs.vllm.ai/trtllm_fp8_moe/#vllm.model_executor.layers.fused_moe.experts.trtllm_fp8_moe) -
–[trtllm_lora_moe](https://docs.vllm.ai/trtllm_lora_moe/#vllm.model_executor.layers.fused_moe.experts.trtllm_lora_moe)LoRA-aware FlashInfer TRT-LLM MoE experts (BF16).

-
–[trtllm_mxfp4_moe](https://docs.vllm.ai/trtllm_mxfp4_moe/#vllm.model_executor.layers.fused_moe.experts.trtllm_mxfp4_moe) -
–[trtllm_mxint4_moe](https://docs.vllm.ai/trtllm_mxint4_moe/#vllm.model_executor.layers.fused_moe.experts.trtllm_mxint4_moe) -
–[trtllm_nvfp4_moe](https://docs.vllm.ai/trtllm_nvfp4_moe/#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe) -
–[xpu_moe](https://docs.vllm.ai/xpu_moe/#vllm.model_executor.layers.fused_moe.experts.xpu_moe)