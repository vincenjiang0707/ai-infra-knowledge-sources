source: https://docs.vllm.ai/en/latest/api/vllm/lora/ops/triton_ops/fp8_kernel_utils/
lastmod: 2026-09-24

#

`vllm.lora.ops.triton_ops.fp8_kernel_utils`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils)

Utilities for Punica kernel construction.

Functions:

-
–[do_expand_kernel_fp8](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.do_expand_kernel_fp8)FP8-compatible expand kernel for LoRA.

-
–[do_shrink_kernel_fp8](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.do_shrink_kernel_fp8)Given an array of integers that identifies the rows of A, ram,

-
–[fp8_mm_k](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.fp8_mm_k)FP8-compatible matrix multiplication kernel with quantization support.


##

`_accumulate_mm(tiled_a, tiled_b, accumulator, a_scale_ptr, b_scale_ptr, a_scale_k_stride, b_scale_k_stride, iter_k, group_k, group_n, use_fp8_w8a8)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils._accumulate_mm)

Core matrix multiplication and accumulation logic with quantization support.

Parameters:

-

(`tiled_a`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils._accumulate_mm(tiled_a))`tensor`

) –Loaded tile from A matrix

-

(`tiled_b`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils._accumulate_mm(tiled_b))`tensor`

) –Loaded tile from B matrix

-

(`accumulator`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils._accumulate_mm(accumulator))`tensor`

) –Current accumulator value

-

(`a_scale_ptr`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils._accumulate_mm(a_scale_ptr))`tensor`

) –Scale pointer for A matrix

-

(`b_scale_ptr`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils._accumulate_mm(b_scale_ptr))`tensor`

) –Scale pointer for B matrix

-

(`a_scale_k_stride`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils._accumulate_mm(a_scale_k_stride))

) –[int](https://docs.python.org/3/builtins/functions.html#int)K dimension stride for A's block-wise scales

-

(`b_scale_k_stride`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils._accumulate_mm(b_scale_k_stride))

) –[int](https://docs.python.org/3/builtins/functions.html#int)K dimension stride for B's block-wise scales

-

(`iter_k`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils._accumulate_mm(iter_k))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Current iteration's global K offset

-

(`group_k`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils._accumulate_mm(group_k))`constexpr`

) –Block size for K dimension in block-wise quantization

-

(`group_n`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils._accumulate_mm(group_n))`constexpr`

) –Block size for N dimension in block-wise quantization

-

(`use_fp8_w8a8`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils._accumulate_mm(use_fp8_w8a8))`constexpr`

) –Whether using FP8 W8A8 quantization


## Source code in `vllm/lora/ops/triton_ops/fp8_kernel_utils.py`


##

`do_expand_kernel_fp8(pid_n, lora_index, slice_id, input_ptr, lora_ptr, out_ptr, a_scale_ptr, b_scale_ptr, N, K, M_LEN, ram, slice_start_loc, input_d0_stride, input_d1_stride, input_d2_stride, ls_d0_ptr, ls_d1_ptr, ls_d2_ptr, a_scale_m_stride, a_scale_k_stride, b_scale_l_stride, b_scale_n_stride, b_scale_k_stride, output_d0_stride, output_d1_stride, group_n, group_k, BLOCK_M, BLOCK_N, BLOCK_K, SAME_STRIDE, SLICE_NUM, EVEN_K, CAST_TYPE, ADD_INPUTS, USE_GDC, use_fp8_w8a8, per_channel_quant)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.do_expand_kernel_fp8)

FP8-compatible expand kernel for LoRA. Given an array of integers that identifies the rows of A, ram, a lora index that identifies which LoRA to use from lora_ptr, lora_index, a slice_id that identifies the input/output slice, compute the matrix product with FP8 quantization support and store in the appropriate output location.

For expand kernel, the input (shrink output) may be in FP32/FP16/BF16, while the LoRA B weights can be in FP8.

Supports: - FP8 W8A8 quantization for LoRA B weights - Block-wise quantization with configurable group_k and group_n - Per-channel quantization - Tensor-wise quantization

## Source code in `vllm/lora/ops/triton_ops/fp8_kernel_utils.py`


|
|

##

`do_shrink_kernel_fp8(pid_n, pid_sk, slice_id, lora_index, input_ptr, lora_ptr, out_ptr, a_scale_ptr, b_scale_ptr, N, K, M_LEN, ram, input_d0_stride, input_d1_stride, lora_d0_stride, lora_d1_stride, lora_d2_stride, a_scale_m_stride, a_scale_k_stride, b_scale_l_stride, b_scale_n_stride, b_scale_k_stride, output_d0_stride, output_d1_stride, output_d2_stride, scaling, group_n, group_k, BLOCK_M, BLOCK_N, BLOCK_K, EVEN_K, SPLIT_K, SLICE_NUM, USE_GDC, use_fp8_w8a8, per_channel_quant, launch_pdl)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.do_shrink_kernel_fp8)

Given an array of integers that identifies the rows of A, ram, a lora index that identifies which LoRA to use from lora_ptr, lora_index, a slice_id that identifies the input/output slice, compute the matrix product and store in the appropriate output location.

## Source code in `vllm/lora/ops/triton_ops/fp8_kernel_utils.py`


|
|

##

`fp8_mm_k(a_ptr, b_ptr, a_scale_ptr, b_scale_ptr, ak_stride, bk_stride, a_scale_k_stride, b_scale_k_stride, offset_k, K, BLOCK_M, BLOCK_N, BLOCK_K, EVEN_K, SPLIT_K, group_k, group_n, use_fp8_w8a8, per_channel_quant, CAST_TYPE, b_dtype, USE_GDC, base_k)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.fp8_mm_k)

FP8-compatible matrix multiplication kernel with quantization support. Given a_ptr and b_ptr, that identify the rows of A (m x k) and columns of B (k x n), iterate through the K dimension to compute the partial/complete matrix block product with proper dequantization.

Parameters:

-

(`a_ptr`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.fp8_mm_k(a_ptr))`tensor`

) –Array of pointers, identifying rows of A (FP8 or other dtype)

-

(`b_ptr`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.fp8_mm_k(b_ptr))`tensor`

) –Array of pointers, identifying columns of B (FP8 dtype)

-

(`a_scale_ptr`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.fp8_mm_k(a_scale_ptr))`tensor`

) –Scale pointer for A matrix (per-token or block-wise)

-

(`b_scale_ptr`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.fp8_mm_k(b_scale_ptr))`tensor`

) –Scale pointer for B matrix (per-channel or block-wise)

-

(`ak_stride`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.fp8_mm_k(ak_stride))

) –[int](https://docs.python.org/3/builtins/functions.html#int)K dimension stride of the A matrix

-

(`bk_stride`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.fp8_mm_k(bk_stride))

) –[int](https://docs.python.org/3/builtins/functions.html#int)K dimension stride of the B matrix

-

(`a_scale_k_stride`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.fp8_mm_k(a_scale_k_stride))

) –[int](https://docs.python.org/3/builtins/functions.html#int)K dimension stride for A's block-wise scales

-

(`b_scale_k_stride`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.fp8_mm_k(b_scale_k_stride))

) –[int](https://docs.python.org/3/builtins/functions.html#int)K dimension stride for B's block-wise scales

-

(`offset_k`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.fp8_mm_k(offset_k))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Base offset along K dimension

-

(`K`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.fp8_mm_k(K))`constexpr`

) –Length of the K dimension

-

(`BLOCK_M`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.fp8_mm_k(BLOCK_M))`constexpr`

) –M dimension of the output block m x n

-

(`BLOCK_N`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.fp8_mm_k(BLOCK_N))`constexpr`

) –N dimension of the output block m x n

-

(`BLOCK_K`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.fp8_mm_k(BLOCK_K))`constexpr`

) –K dimension atom

-

(`EVEN_K`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.fp8_mm_k(EVEN_K))`constexpr`

) –True if the blocks of A and B can be loaded without masking

-

(`SPLIT_K`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.fp8_mm_k(SPLIT_K))`constexpr`

) –Parameter signifying parallelism in the K dimension

-

(`group_k`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.fp8_mm_k(group_k))`constexpr`

) –Block size for K dimension in block-wise quantization

-

(`group_n`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.fp8_mm_k(group_n))`constexpr`

) –Block size for N dimension in block-wise quantization

-

(`use_fp8_w8a8`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.fp8_mm_k(use_fp8_w8a8))`constexpr`

) –Whether using FP8 W8A8 quantization

-

(`per_channel_quant`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.fp8_mm_k(per_channel_quant))`constexpr`

) –Whether using per-channel quantization

-

(`CAST_TYPE`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.fp8_mm_k(CAST_TYPE))`constexpr`

) –if True, cast the values from the A matrix to the B matrix dtype.

-

(`b_dtype`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.fp8_mm_k(b_dtype))`constexpr`

) –datatype of the B matrix

-

(`USE_GDC`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.fp8_mm_k(USE_GDC))`constexpr`

) –Whether to use PDL. True indicates use.

-

(`base_k`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.fp8_kernel_utils.fp8_mm_k(base_k))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Base offset along K dimension for current SPLIT_K group


## Source code in `vllm/lora/ops/triton_ops/fp8_kernel_utils.py`


|
|