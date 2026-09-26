source: https://docs.vllm.ai/en/latest/api/vllm/config/kernel/
lastmod: 2026-09-24

#

`vllm.config.kernel`

[¶](https://docs.vllm.ai#vllm.config.kernel)

Classes:

-
–[IrOpPriorityConfig](https://docs.vllm.ai#vllm.config.kernel.IrOpPriorityConfig)Configuration for vLLM IR op priority for dispatching/lowering during the

-
–[KernelConfig](https://docs.vllm.ai#vllm.config.kernel.KernelConfig)Configuration for kernel selection and warmup behavior.


Functions:

-
–[validate_flashinfer_moe_ep_model](https://docs.vllm.ai#vllm.config.kernel.validate_flashinfer_moe_ep_model)Reject flashinfer moe_ep backends for models that lack the FI path.


##

`IrOpPriorityConfig`

[¶](https://docs.vllm.ai#vllm.config.kernel.IrOpPriorityConfig)

Configuration for vLLM IR op priority for dispatching/lowering during the forward pass. Each member is a list of strings, which will be installed in worker init via vllm.ir.ops.

If specified manually, platform defaults will be appended to the lists. See KernelConfig.set_platform_defaults().

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.kernel.IrOpPriorityConfig.compute_hash)Produces a hash unique to the pass configuration.

-
–[set_default](https://docs.vllm.ai#vllm.config.kernel.IrOpPriorityConfig.set_default)Permanently set the IR op priority for all op members.

-
–[set_priority](https://docs.vllm.ai#vllm.config.kernel.IrOpPriorityConfig.set_priority)Context manager to set the IR op priority for all op members.

-
–[with_default](https://docs.vllm.ai#vllm.config.kernel.IrOpPriorityConfig.with_default)A helper to create an IrOpPriorityConfig where fields not specified in kwargs


Attributes:

-
([fused_add_rms_norm](https://docs.vllm.ai#vllm.config.kernel.IrOpPriorityConfig.fused_add_rms_norm)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Priority list for vllm.ir.ops.fused_add_rms_norm

-
([gelu_and_mul_sparse](https://docs.vllm.ai#vllm.config.kernel.IrOpPriorityConfig.gelu_and_mul_sparse)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Priority list for vllm.ir.ops.gelu_and_mul_sparse

-
([rms_norm](https://docs.vllm.ai#vllm.config.kernel.IrOpPriorityConfig.rms_norm)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Priority list for vllm.ir.ops.rms_norm


## Source code in `vllm/config/kernel.py`


|
|

###

`fused_add_rms_norm = Field(default_factory=list)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kernel.IrOpPriorityConfig.fused_add_rms_norm)

Priority list for vllm.ir.ops.fused_add_rms_norm

###

`gelu_and_mul_sparse = Field(default_factory=list)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kernel.IrOpPriorityConfig.gelu_and_mul_sparse)

Priority list for vllm.ir.ops.gelu_and_mul_sparse

###

`rms_norm = Field(default_factory=list)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kernel.IrOpPriorityConfig.rms_norm)

Priority list for vllm.ir.ops.rms_norm

###

`_iter_op_priorities()`

[¶](https://docs.vllm.ai#vllm.config.kernel.IrOpPriorityConfig._iter_op_priorities)

Yield (IrOp, priority_list) for each field, after importing platform kernels and validating each entry.

## Source code in `vllm/config/kernel.py`


###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.kernel.IrOpPriorityConfig.compute_hash)

Produces a hash unique to the pass configuration. Any new fields that affect compilation should be added to the hash. Any future fields that don't affect compilation should be excluded.

Also, manually add IR op impl UUIDs to make sure they affect the compile cache.

## Source code in `vllm/config/kernel.py`


###

`set_default()`

[¶](https://docs.vllm.ai#vllm.config.kernel.IrOpPriorityConfig.set_default)

###

`set_priority()`

[¶](https://docs.vllm.ai#vllm.config.kernel.IrOpPriorityConfig.set_priority)

Context manager to set the IR op priority for all op members. It also imports IR kernel implementations for the current platform to ensure all implementations are made available.

## Source code in `vllm/config/kernel.py`


###

`with_default(default, /, **kwargs)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.kernel.IrOpPriorityConfig.with_default)

A helper to create an IrOpPriorityConfig where fields not specified in kwargs use the given default list.

## Source code in `vllm/config/kernel.py`


##

`KernelConfig`

[¶](https://docs.vllm.ai#vllm.config.kernel.KernelConfig)

Configuration for kernel selection and warmup behavior.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.kernel.KernelConfig.compute_hash)Produces a hash unique to the pass configuration.

-
–[set_platform_defaults](https://docs.vllm.ai#vllm.config.kernel.KernelConfig.set_platform_defaults)Set platform-specific defaults for the kernel config.


Attributes:

-
([enable_cutedsl_warmup](https://docs.vllm.ai#vllm.config.kernel.KernelConfig.enable_cutedsl_warmup)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Deprecated: run legacy CuTeDSL warmup providers.

-
([enable_flashinfer_autotune](https://docs.vllm.ai#vllm.config.kernel.KernelConfig.enable_flashinfer_autotune)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If True, run FlashInfer autotuning during kernel warmup.

-
([enable_jit_warmup](https://docs.vllm.ai#vllm.config.kernel.KernelConfig.enable_jit_warmup)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If True, run JIT compile warmup during kernel warmup.

-
([ir_op_priority](https://docs.vllm.ai#vllm.config.kernel.KernelConfig.ir_op_priority)

) –[IrOpPriorityConfig](https://docs.vllm.ai#vllm.config.kernel.IrOpPriorityConfig)vLLM IR op priority for dispatching/lowering during the forward pass.

-
([linear_backend](https://docs.vllm.ai#vllm.config.kernel.KernelConfig.linear_backend)`LinearBackend`

) –Backend for linear layer GEMM kernels. Available options:

-
([linear_backend_per_quant](https://docs.vllm.ai#vllm.config.kernel.KernelConfig.linear_backend_per_quant)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), LinearBackend] | NoneBackend overrides keyed by linear quantization scheme. Overrides take

-
([moe_backend](https://docs.vllm.ai#vllm.config.kernel.KernelConfig.moe_backend)`MoEBackend`

) –Backend for MoE expert computation kernels. Available options:

-
([sparse_indexer_topk_backend](https://docs.vllm.ai#vllm.config.kernel.KernelConfig.sparse_indexer_topk_backend)`SparseIndexerTopkBackend`

) –Backend for the DSA sparse indexer decode top-k kernel. Available options:


## Source code in `vllm/config/kernel.py`


|
|

###

`enable_cutedsl_warmup = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kernel.KernelConfig.enable_cutedsl_warmup)

Deprecated: run legacy CuTeDSL warmup providers.

###

`enable_flashinfer_autotune = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kernel.KernelConfig.enable_flashinfer_autotune)

If True, run FlashInfer autotuning during kernel warmup.

###

`enable_jit_warmup = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kernel.KernelConfig.enable_jit_warmup)

If True, run JIT compile warmup during kernel warmup.

###

`ir_op_priority = Field(default_factory=IrOpPriorityConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kernel.KernelConfig.ir_op_priority)

vLLM IR op priority for dispatching/lowering during the forward pass. Platform defaults appended automatically during VllmConfig.**post_init**.

###

`linear_backend = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kernel.KernelConfig.linear_backend)

Backend for linear layer GEMM kernels. Available options:

Layer types without an implementation from the requested backend use automatic selection.

- "auto": Automatically select the best backend based on model and hardware
- "cutlass": Use CUTLASS-based kernels
- "flashinfer_cutlass": Use FlashInfer with CUTLASS kernels
- "flashinfer_cutedsl": Use FlashInfer with CuTe-DSL kernels (BF16, NVFP4, MXFP8, W4A16_NVFP4)
- "flashinfer_trtllm": Use FlashInfer with TensorRT-LLM kernels
- "flashinfer_cudnn": Use FlashInfer with cuDNN kernels
- "flashinfer_b12x": Use FlashInfer b12x CuteDSL NVFP4 GEMM (SM120+)
- "b12x": Use native B12X FP8 and FP4 linear kernels on SM12x
- "marlin": Use Marlin kernels
- "triton": Use Triton-based kernels
- "deep_gemm": Use DeepGEMM kernels
- "torch": Use PyTorch native scaled_mm kernels
- "aiter": Use AMD AITer kernels (ROCm only)
- "machete": Use Machete kernels (mixed-precision)
- "fbgemm": Use FBGEMM kernels
- "conch": Use Conch mixed-precision kernels
- "exllama": Use Exllama mixed-precision kernels
- "emulation": Use slow dequant-to-BF16 emulation (for testing only)
- "xpu": Use XPU kernels
- "xpu_woq": Use XPU kernels for weight-only quantization (e.g. W8A16)

###

`linear_backend_per_quant = Field(default=None, min_length=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kernel.KernelConfig.linear_backend_per_quant)

Backend overrides keyed by linear quantization scheme. Overrides take precedence over `linear_backend`

; for example, `{"nvfp4_w4a16": "humming"}`

.

###

`moe_backend = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kernel.KernelConfig.moe_backend)

Backend for MoE expert computation kernels. Available options:

- "auto": Automatically select the best backend based on model and hardware
- "triton": Use Triton-based fused MoE kernels
- "batched_triton": Use batched Triton experts (moe_mmk) on the batched activation format ([E_local, max_num_tokens, K])
- "deep_gemm": Use DeepGEMM kernels (FP8 block-quantized only)
- "deep_gemm_mega_moe": Use DeepGEMM mega MoE kernels
- "cutlass": Use vLLM CUTLASS kernels
- "flashinfer_trtllm": Use FlashInfer with TRTLLM-GEN kernels
- "flashinfer_cutlass": Use FlashInfer with CUTLASS kernels
- "flashinfer_cutedsl": Use FlashInfer with CuteDSL kernels (FP4 only)
- "flashinfer_b12x": Use FlashInfer CuteDSL fused MoE for SM12x (RTX Pro 6000 / DGX Spark)
- "b12x": Use b12x FP4 MoE kernels on SM12x
- "flashinfer_moe_ep_mega_deep_gemm": Use the FlashInfer moe_ep expert-parallel mega-MoE with the DeepGEMM megakernel, which consumes an MXFP4 checkpoint verbatim (Blackwell, requires expert parallel; DeepSeek-V4 only)
- "flashinfer_moe_ep_mega_cutedsl": Same, with the CuteDSL megakernel (additionally requires NVSHMEM). The checkpoint selects the weight path: an NVFP4 checkpoint is consumed prequantized, MXFP4 weights are requantized at load
- "marlin": Use Marlin kernels (weight-only quantization)
- "humming": Use Humming Mixed Precision kernels
- "triton_unfused": Use Triton unfused MoE kernels
- "aiter": Use AMD AITer kernels (ROCm only)
- "aiter_triton_mxfp4_bf16": Use the AITER Triton MXFP4 W4A16 (moe_gemm_a16w4) MoE kernel (ROCm gfx942/gfx950/gfx1250)
- "flydsl": Use AMD FlyDSL kernels (ROCm only)
- "rdna3": Use the fused RDNA3 W4A16 HIP kernel (ROCm gfx1100 only)
- "hpc": Use HPC kernels (FP8 and Hopper only)
- "emulation": use BF16/FP16 GEMM, dequantizing weights and running QDQ on activations.

###

`sparse_indexer_topk_backend = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.kernel.KernelConfig.sparse_indexer_topk_backend)

Backend for the DSA sparse indexer decode top-k kernel. Available options:

- "auto": The pre-existing chain (cooperative -> persistent -> per_row); the other backends are opt-in
- "deep_select": Use DeepSelect kernels (SM100a/SM103a only)
- "cooperative": Use vLLM's cooperative_topk kernel
- "persistent": Use vLLM's persistent_topk kernel
- "per_row": Use vLLM's top_k_per_row_decode kernel
- "flashinfer": Use FlashInfer's top_k_ragged_transform kernel
- "torch": Use a plain torch.topk implementation (debug reference)

Explicit values raise RuntimeError when their constraints are not met.

###

`_skip_none_validation(value, handler)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.kernel.KernelConfig._skip_none_validation)

Skip validation if the value is `None`

when initialization is delayed.

## Source code in `vllm/config/kernel.py`


###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.kernel.KernelConfig.compute_hash)

Produces a hash unique to the pass configuration. Any new fields that affect compilation should be added to the hash. Any future fields that don't affect compilation should be excluded.

## Source code in `vllm/config/kernel.py`


###

`set_platform_defaults(vllm_config)`

[¶](https://docs.vllm.ai#vllm.config.kernel.KernelConfig.set_platform_defaults)

Set platform-specific defaults for the kernel config.

## Source code in `vllm/config/kernel.py`


##

`validate_flashinfer_moe_ep_model(moe_backend, architectures)`

[¶](https://docs.vllm.ai#vllm.config.kernel.validate_flashinfer_moe_ep_model)

Reject flashinfer moe_ep backends for models that lack the FI path.