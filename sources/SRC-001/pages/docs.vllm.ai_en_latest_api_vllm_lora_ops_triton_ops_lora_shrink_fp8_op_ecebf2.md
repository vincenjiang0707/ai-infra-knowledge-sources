source: https://docs.vllm.ai/en/latest/api/vllm/lora/ops/triton_ops/lora_shrink_fp8_op/
lastmod: 2026-09-23

#

`vllm.lora.ops.triton_ops.lora_shrink_fp8_op`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.lora_shrink_fp8_op)

Based on: Chen, L., Ye, Z., Wu, Y., Zhuo, D., Ceze, L., & Krishnamurthy, A. (2023). Punica: Multi-Tenant LoRA Serving. https://arxiv.org/abs/2310.18547

##

`_get_shrink_lora_scale_ptr(lora_scale_weights, device)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.lora_shrink_fp8_op._get_shrink_lora_scale_ptr)

`_SHRINK_LORA_SCALE_PTR_DICT`

collects the required information during `profile_run`

. After this, it remains constant and subsequent usage is through LUT.

Returns a tuple of (scale_ptr_tensor, l_stride, n_stride, k_stride).

Supports scale tensors of varying dimensionality: - 1D: (lora_num,) — tensor-wise quantization - 2D: (lora_num, N) — per-channel quantization - 3D: (lora_num, N, K) — block-wise quantization - 4D: (lora_num, 1, N, K) — block-wise with extra dim (squeezed to 3D)

Refer to: https://github.com/triton-lang/triton/blob/release/3.1.x/python/tutorials/08-grouped-gemm.py

## Source code in `vllm/lora/ops/triton_ops/lora_shrink_fp8_op.py`


##

`_lora_shrink_fp8(inputs, lora_a_weights, output_tensor, token_lora_mapping, token_indices_sorted_by_lora_ids, num_tokens_per_lora, lora_token_start_loc, lora_ids, no_lora_flag_cpu, num_active_loras, scaling, b_scale, a_scale=None, group_k=0, group_n=0, use_fp8_w8a8=False, per_channel_quant=False)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.lora_shrink_fp8_op._lora_shrink_fp8)

Args: inputs: FP8 or FP16/BF16 input tensor [num_tokens, hidden_size] lora_a_weights: List of FP8 or FP16/BF16 LoRA A weights per slice output_tensor: Output tensor (FP16/BF16/FP32) token_lora_mapping: Token to LoRA ID mapping token_indices_sorted_by_lora_ids: Sorted token indices num_tokens_per_lora: Number of tokens per LoRA lora_token_start_loc: Start location for each LoRA's tokens lora_ids: LoRA IDs to process scaling: LoRA scaling factor a_scale: Activation quantization scales b_scale: Weight quantization scales per slice group_k: Block size for K dimension quantization group_n: Block size for N dimension quantization use_fp8_w8a8: Whether to use FP8 weights and activations per_channel_quant: Whether to use per-channel quantization

## Source code in `vllm/lora/ops/triton_ops/lora_shrink_fp8_op.py`


|
|