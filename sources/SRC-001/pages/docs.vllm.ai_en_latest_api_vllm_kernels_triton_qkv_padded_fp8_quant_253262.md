source: https://docs.vllm.ai/en/latest/api/vllm/kernels/triton/qkv_padded_fp8_quant/
lastmod: 2026-09-24

#

`vllm.kernels.triton.qkv_padded_fp8_quant`

[¶](https://docs.vllm.ai#vllm.kernels.triton.qkv_padded_fp8_quant)

Stride-aware FP8 quantization with head_dim padding for ViT attention.

Reads directly from non-contiguous QKV views using 3D strides and pads head_dim to a multiple of 16 for cuDNN compatibility.

Functions:

-
–[quantize_fp8_maybe_pad_head_dim](https://docs.vllm.ai#vllm.kernels.triton.qkv_padded_fp8_quant.quantize_fp8_maybe_pad_head_dim)Quantize a 3D/4D tensor to FP8, padding head_dim to a multiple of 16

-
–[quantize_fp8_pad_head_dim_triton](https://docs.vllm.ai#vllm.kernels.triton.qkv_padded_fp8_quant.quantize_fp8_pad_head_dim_triton)Quantize a 3D/4D tensor to FP8, padding head_dim to a multiple of 16.


##

`quantize_fp8_maybe_pad_head_dim(tensor, scale, fp8_quant, skip_scale=False)`

[¶](https://docs.vllm.ai#vllm.kernels.triton.qkv_padded_fp8_quant.quantize_fp8_maybe_pad_head_dim)

Quantize a 3D/4D tensor to FP8, padding head_dim to a multiple of 16 only when needed.

Accepts (S, H, D) or (B, S, H, D) input. Uses `fp8_quant`

(a :class:`QuantFP8`

CustomOp) when head_dim is already aligned to 16 (no padding); otherwise falls back to a stride-aware Triton kernel that pads head_dim to a multiple of 16.

## Source code in `vllm/kernels/triton/qkv_padded_fp8_quant.py`


##

`quantize_fp8_pad_head_dim_triton(tensor, scale, skip_scale=False, block_m=None, block_n=None, num_warps=None)`

[¶](https://docs.vllm.ai#vllm.kernels.triton.qkv_padded_fp8_quant.quantize_fp8_pad_head_dim_triton)

Quantize a 3D/4D tensor to FP8, padding head_dim to a multiple of 16.

Reads directly from the input using its 3D strides, so non-contiguous views (e.g. Q/K/V slices from an interleaved QKV buffer) are handled without an extra copy. Output is always a fresh contiguous tensor with shape (S, H, padded_D).