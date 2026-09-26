source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/mixed_precision/triton_w4a16/
lastmod: 2026-09-24

#

`vllm.model_executor.kernels.linear.mixed_precision.triton_w4a16`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.triton_w4a16)

Triton-based W4A16 GEMM kernel for ROCm MI300.

Implements fused int4-weight dequantization + fp16 GEMM in a single kernel, using GPTQ sequential packing (8 int4 values per int32, shifts [0,4,...,28]). Plugs into the MPLinearKernel selection system and is preferred over MarlinLinearKernel/ExllamaLinearKernel on ROCm.

Weight layout expected by this kernel (post-process_weights_after_loading): qweight: [K, N//8] int32 — rows=K (input), cols=N//8 (N is packed) scales: [K//G, N] fp16/bf16 qzeros: [K//G, N//8] int32 (optional; None for symmetric uint4b8)

## Checkpoint layout from compressed_tensors_wNa16 create_weights

weight_packed: [N, K//8] int32 (output_dim=0, input_dim=1, packed_dim=1) weight_scale: [N, K//G] fp16 (output_dim=0, input_dim=1) weight_zero_point: [N//8, K//G] int32 (output_dim=0, packed_dim=0)

Classes:

-
–[TritonW4A16LinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.triton_w4a16.TritonW4A16LinearKernel)Triton-based W4A16 GEMM kernel for ROCm (MI300 and newer).


Functions:

-
–[triton_w4a16_gemm_kernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.triton_w4a16.triton_w4a16_gemm_kernel)Fused W4A16 GEMM: C[M,N] = A[M,K] @ dequant(B)[K,N].


##

`TritonW4A16LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.triton_w4a16.TritonW4A16LinearKernel)

Bases: `MPLinearKernel`


Triton-based W4A16 GEMM kernel for ROCm (MI300 and newer).

Supports GPTQ-format int4 weights (uint4b8 symmetric, uint4 asymmetric) with grouped quantization. Weight tensors are transposed from the compressed-tensors checkpoint layout to the kernel's [K, N//8] layout.

Methods:

-
–[process_weights_after_loading](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.triton_w4a16.TritonW4A16LinearKernel.process_weights_after_loading)Convert compressed-tensors checkpoint layout to kernel layout.


## Source code in `vllm/model_executor/kernels/linear/mixed_precision/triton_w4a16.py`


|
|

###

`process_weights_after_loading(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.triton_w4a16.TritonW4A16LinearKernel.process_weights_after_loading)

Convert compressed-tensors checkpoint layout to kernel layout.

Checkpoint (from compressed_tensors_wNa16.create_weights): weight_packed: [N, K//8] int32 input_dim=1, output_dim=0, packed_dim=1 weight_scale: [N, K//G] fp16 input_dim=1, output_dim=0 weight_zero_point: [N//8, K//G] int32 output_dim=0, packed_dim=0

## Kernel needs

qweight: [K, N//8] int32 (transpose weight_packed) scales: [K//G, N] fp16 (transpose weight_scale) qzeros: [K//G, N//8] int32 (transpose weight_zero_point)

## Source code in `vllm/model_executor/kernels/linear/mixed_precision/triton_w4a16.py`


|
|

##

`_triton_w4a16_gemm_impl(a, b_q, scales, qzeros, group_size, zp_bias=8)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.triton_w4a16._triton_w4a16_gemm_impl)

Fused W4A16 GEMM using GPTQ-packed int4 weights.

Parameters:

-

(`a`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.triton_w4a16._triton_w4a16_gemm_impl(a))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Activation matrix [M, K], float16 or bfloat16.

-

(`b_q`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.triton_w4a16._triton_w4a16_gemm_impl(b_q))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Packed weight matrix [K, N//8], int32 (GPTQ sequential).

-

(`scales`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.triton_w4a16._triton_w4a16_gemm_impl(scales))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Per-group scales [K//G, N], same dtype as a.

-

(`qzeros`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.triton_w4a16._triton_w4a16_gemm_impl(qzeros))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NonePer-group packed zero points [K//G, N//8] int32, or None for symmetric quantization (uses zp_bias instead).

-

(`group_size`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.triton_w4a16._triton_w4a16_gemm_impl(group_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Quantization group size (resolved from -1 to K by caller).

-

(`zp_bias`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.triton_w4a16._triton_w4a16_gemm_impl(zp_bias))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`8`

) –Constant zero used when qzeros is None (default 8 for uint4b8).


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output matrix [M, N], same dtype as a.


## Source code in `vllm/model_executor/kernels/linear/mixed_precision/triton_w4a16.py`


|
|

##

`triton_w4a16_gemm_kernel(a_ptr, b_ptr, scales_ptr, zeros_ptr, c_ptr, M, N, K, stride_am, stride_ak, stride_bk, stride_bn, stride_cm, stride_cn, group_size, HAS_ZP, ZP_BIAS, BLOCK_M, BLOCK_N, BLOCK_K)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mixed_precision.triton_w4a16.triton_w4a16_gemm_kernel)

Fused W4A16 GEMM: C[M,N] = A[M,K] @ dequant(B)[K,N].

B is stored as [K, N//8] int32 using GPTQ sequential packing: each int32 packs 8 consecutive N-values at bit offsets [0,4,8,12,16,20,24,28].

## w_fp = (w_int4 - zero) * scale

HAS_ZP=True: zero is loaded from zeros_ptr and unpacked HAS_ZP=False: zero = ZP_BIAS constant (e.g. 8 for uint4b8 symmetric)

## Source code in `vllm/model_executor/kernels/linear/mixed_precision/triton_w4a16.py`


|
|