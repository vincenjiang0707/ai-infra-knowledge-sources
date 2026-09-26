source: https://docs.vllm.ai/en/latest/api/vllm/lora/ops/triton_ops/kernel_utils/
lastmod: 2026-09-24

#

`vllm.lora.ops.triton_ops.kernel_utils`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.kernel_utils)

Utilities for Punica kernel construction.

Functions:

-
–[do_expand_kernel](https://docs.vllm.ai#vllm.lora.ops.triton_ops.kernel_utils.do_expand_kernel)Given an array of integers that identifies the rows of A, ram,

-
–[do_shrink_kernel](https://docs.vllm.ai#vllm.lora.ops.triton_ops.kernel_utils.do_shrink_kernel)Given an array of integers that identifies the rows of A, ram,

-
–[mm_k](https://docs.vllm.ai#vllm.lora.ops.triton_ops.kernel_utils.mm_k)Given a_ptr and b_ptr, that identify the rows of A (m x k) and columns of


##

`do_expand_kernel(pid_n, lora_index, slice_id, input_ptr, lora_ptr, out_ptr, N, K, M_LEN, ram, slice_start_loc, input_d0_stride, input_d1_stride, input_d2_stride, ls_d0_ptr, ls_d1_ptr, ls_d2_ptr, output_d0_stride, output_d1_stride, BLOCK_M, BLOCK_N, BLOCK_K, SAME_STRIDE, SLICE_NUM, EVEN_K, CAST_TYPE, ADD_INPUTS, USE_GDC)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.kernel_utils.do_expand_kernel)

Given an array of integers that identifies the rows of A, ram, a lora index that identifies which LoRA to use from lora_ptr, lora_index, a slice_id that identifies the input/output slice, compute the matrix product and store in the appropriate output location. Given that this is an expand kernel, we don't perform any split-K reduction as the K dimension is assumed to be small.

## Source code in `vllm/lora/ops/triton_ops/kernel_utils.py`


|
|

##

`do_shrink_kernel(pid_n, pid_sk, slice_id, lora_index, input_ptr, lora_ptr, out_ptr, N, K, M_LEN, ram, input_d0_stride, input_d1_stride, lora_d0_stride, lora_d1_stride, lora_d2_stride, output_d0_stride, output_d1_stride, output_d2_stride, scaling, BLOCK_M, BLOCK_N, BLOCK_K, EVEN_K, SPLIT_K, SLICE_NUM, USE_GDC)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.kernel_utils.do_shrink_kernel)

Given an array of integers that identifies the rows of A, ram, a lora index that identifies which LoRA to use from lora_ptr, lora_index, a slice_id that identifies the input/output slice, compute the matrix product and store in the appropriate output location.

## Source code in `vllm/lora/ops/triton_ops/kernel_utils.py`


|
|

##

`mm_k(a_ptr, b_ptr, ak_stride, bk_stride, offset_k, K, BLOCK_M, BLOCK_N, BLOCK_K, EVEN_K, SPLIT_K, CAST_TYPE, b_dtype, USE_GDC, base_k)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.kernel_utils.mm_k)

Given a_ptr and b_ptr, that identify the rows of A (m x k) and columns of B (k x n), iterate, through the K dimension to compute the partial/complete matrix block product. If SPLIT_K == 1, the output m x n product is complete. If SPLIT_K > 1, the thread block computes partial outputs. The partial outputs are then atomically summed in the caller code.

Parameters:

-

(`a_ptr`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.kernel_utils.mm_k(a_ptr))`tensor`

) –Array of pointers, identifying rows of A

-

(`b_ptr`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.kernel_utils.mm_k(b_ptr))`tensor`

) –Array of pointers, identifying columns of B

-

(`ak_stride`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.kernel_utils.mm_k(ak_stride))

) –[int](https://docs.python.org/3/builtins/functions.html#int)K dimension stride of the A matrix

-

(`bk_stride`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.kernel_utils.mm_k(bk_stride))

) –[int](https://docs.python.org/3/builtins/functions.html#int)K dimension stride of the B matrix

-

(`offset_k`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.kernel_utils.mm_k(offset_k))`tensor`

) –Offsets within the current BLOCK_K tile along K

-

(`K`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.kernel_utils.mm_k(K))`constexpr`

) –Length of the K dimension

-

(`BLOCK_M`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.kernel_utils.mm_k(BLOCK_M))`constexpr`

) –M dimension of the output block m x n

-

(`BLOCK_N`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.kernel_utils.mm_k(BLOCK_N))`constexpr`

) –N dimension of the output block m x n

-

(`BLOCK_K`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.kernel_utils.mm_k(BLOCK_K))`constexpr`

) –K dimension atom

-

(`EVEN_K`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.kernel_utils.mm_k(EVEN_K))`constexpr`

) –True if the blocks of A and B can be loaded without any masking.

-

(`SPLIT_K`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.kernel_utils.mm_k(SPLIT_K))`constexpr`

) –Parameter signifying parallelism in the K dimension.

-

(`CAST_TYPE`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.kernel_utils.mm_k(CAST_TYPE))`constexpr`

) –if True, cast the values from the A matrix to the B matrix dtype.

-

(`b_dtype`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.kernel_utils.mm_k(b_dtype))`constexpr`

) –datatype of the B matrix

-

(`USE_GDC`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.kernel_utils.mm_k(USE_GDC))`constexpr`

) –Whether to use PDL. True indicates use.

-

(`base_k`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.kernel_utils.mm_k(base_k))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Base offset along K dimension for current SPLIT_K group


## Source code in `vllm/lora/ops/triton_ops/kernel_utils.py`


|
|