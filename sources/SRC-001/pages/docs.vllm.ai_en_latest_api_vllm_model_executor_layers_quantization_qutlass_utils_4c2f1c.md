source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/qutlass_utils/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.quantization.qutlass_utils`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.qutlass_utils)

Functions:

-
–[to_blocked](https://docs.vllm.ai#vllm.model_executor.layers.quantization.qutlass_utils.to_blocked)Rearrange a large matrix by breaking it into blocks and applying

-
–[triton_mx_block_rearrange](https://docs.vllm.ai#vllm.model_executor.layers.quantization.qutlass_utils.triton_mx_block_rearrange)Rearranges an E8M0 tensor scale from row-major format to

-
–[triton_scale_swizzle](https://docs.vllm.ai#vllm.model_executor.layers.quantization.qutlass_utils.triton_scale_swizzle)Rearranges tensor data from row-major to block-scaled swizzle format.


##

`to_blocked(input_matrix, backend='triton')`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.qutlass_utils.to_blocked)

Rearrange a large matrix by breaking it into blocks and applying the rearrangement pattern.

## See

https://docs.nvidia.com/cuda/cublas/index.html#d-block-scaling-factors-layout

Parameters:

-

(`input_matrix`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.qutlass_utils.to_blocked(input_matrix))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor of shape (H, W)

-

(`backend`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.qutlass_utils.to_blocked(backend))

, default:[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['torch', 'triton']`'triton'`

) –"torch" (PyTorch path) or "triton" (Triton kernel)


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Rearranged flattened tensor of size (32

*cdiv(H,128) * 16*cdiv(W,4))

## Source code in `vllm/model_executor/layers/quantization/qutlass_utils.py`


##

`triton_mx_block_rearrange(scale_tensor)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.qutlass_utils.triton_mx_block_rearrange)

Rearranges an E8M0 tensor scale from row-major format to block-scaled swizzle format.

This format is suitable for Tmem as described in NVIDIA documentation: https://docs.nvidia.com/cuda/cublas/index.html#d-block-scaling-factors-layout

Parameters:

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Rearranged tensor in block-scaled swizzle format


## Source code in `vllm/model_executor/layers/quantization/qutlass_utils.py`


##

`triton_scale_swizzle(scale_ptr, scale_rows, scale_cols, output_ptr, input_row_stride, output_block_stride, BLOCK_ROWS, BLOCK_COLS)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.qutlass_utils.triton_scale_swizzle)

Rearranges tensor data from row-major to block-scaled swizzle format.

Parameters:

-

(`scale_ptr`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.qutlass_utils.triton_scale_swizzle(scale_ptr))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Pointer to the input scale tensor

-

(`scale_rows`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.qutlass_utils.triton_scale_swizzle(scale_rows))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of rows in the scale tensor

-

(`scale_cols`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.qutlass_utils.triton_scale_swizzle(scale_cols))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of columns in the scale tensor

-

(`output_ptr`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.qutlass_utils.triton_scale_swizzle(output_ptr))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Pointer to the output tensor

-

(`input_row_stride`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.qutlass_utils.triton_scale_swizzle(input_row_stride))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Stride between rows in the input tensor

-

(`output_block_stride`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.qutlass_utils.triton_scale_swizzle(output_block_stride))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Stride between blocks in the output tensor

-

(`BLOCK_ROWS`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.qutlass_utils.triton_scale_swizzle(BLOCK_ROWS))`constexpr`

) –Number of rows in a tile (compile-time constant)

-

(`BLOCK_COLS`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.qutlass_utils.triton_scale_swizzle(BLOCK_COLS))`constexpr`

) –Number of columns in a tile (compile-time constant)