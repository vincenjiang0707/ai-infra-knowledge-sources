source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/utils/flashinfer_mxint4_moe/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.quantization.utils.flashinfer_mxint4_moe`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_mxint4_moe)

Utility helpers for MxInt4 + FlashInfer fused-MoE path.

Functions:

-
–[flashinfer_trtllm_mxint4_moe](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_mxint4_moe.flashinfer_trtllm_mxint4_moe)Apply FlashInfer TensorRT-LLM MxInt4 MoE kernel.

-
–[is_flashinfer_mxint4_moe_available](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_mxint4_moe.is_flashinfer_mxint4_moe_available)Return

`True`

when FlashInfer MxInt4 kernels can be used. -
–[prepare_static_weights_for_trtllm_mxint4_moe](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_mxint4_moe.prepare_static_weights_for_trtllm_mxint4_moe)Prepare MxInt4 weights for TRT-LLM kernel.


##

`flashinfer_trtllm_mxint4_moe(x, router_logits, w13_weight_packed, w13_weight_scale, w2_weight_packed, w2_weight_scale, global_num_experts, top_k, intermediate_size_per_partition, local_num_experts, ep_rank=0, num_expert_group=None, topk_group=None, e_score_correction_bias=None, routing_method_type=None, routing_replay_out=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_mxint4_moe.flashinfer_trtllm_mxint4_moe)

Apply FlashInfer TensorRT-LLM MxInt4 MoE kernel.

Parameters:

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_mxint4_moe.flashinfer_trtllm_mxint4_moe(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input hidden states. dtype: bfloat16

-

(`router_logits`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_mxint4_moe.flashinfer_trtllm_mxint4_moe(router_logits))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Router logits for expert selection. dtype: bfloat16/float32

-

(`w13_weight_packed`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_mxint4_moe.flashinfer_trtllm_mxint4_moe(w13_weight_packed))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Packed gate+up weights. dtype: uint8

-

(`w13_weight_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_mxint4_moe.flashinfer_trtllm_mxint4_moe(w13_weight_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Scales for gate+up weights. dtype: bfloat16

-

(`w2_weight_packed`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_mxint4_moe.flashinfer_trtllm_mxint4_moe(w2_weight_packed))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Packed down weights. dtype: uint8

-

(`w2_weight_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_mxint4_moe.flashinfer_trtllm_mxint4_moe(w2_weight_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Scales for down weights. dtype: bfloat16

-

(`global_num_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_mxint4_moe.flashinfer_trtllm_mxint4_moe(global_num_experts))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Total number of experts across all ranks

-

(`top_k`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_mxint4_moe.flashinfer_trtllm_mxint4_moe(top_k))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of experts to select per token

-

(`intermediate_size_per_partition`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_mxint4_moe.flashinfer_trtllm_mxint4_moe(intermediate_size_per_partition))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Intermediate size per partition

-

(`local_num_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_mxint4_moe.flashinfer_trtllm_mxint4_moe(local_num_experts))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of experts on this rank

-

(`ep_rank`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_mxint4_moe.flashinfer_trtllm_mxint4_moe(ep_rank))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –Expert parallelism rank (default: 0)

-

(`num_expert_group`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_mxint4_moe.flashinfer_trtllm_mxint4_moe(num_expert_group))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Number of expert groups (default: None -> 0)

-

(`topk_group`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_mxint4_moe.flashinfer_trtllm_mxint4_moe(topk_group))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Top-k within groups (default: None -> 0)

-

(`routing_replay_out`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_mxint4_moe.flashinfer_trtllm_mxint4_moe(routing_replay_out))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional buffer receiving the routing decisions so they can be replayed later

-

(`e_score_correction_bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_mxint4_moe.flashinfer_trtllm_mxint4_moe(e_score_correction_bias))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional routing bias. dtype: bfloat16

-

(`routing_method_type`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_mxint4_moe.flashinfer_trtllm_mxint4_moe(routing_method_type))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –FlashInfer RoutingMethodType enum value


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output tensor from MoE layer. dtype: same as x (bfloat16)


## Source code in `vllm/model_executor/layers/quantization/utils/flashinfer_mxint4_moe.py`


|
|

##

`is_flashinfer_mxint4_moe_available()`

`cached`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_mxint4_moe.is_flashinfer_mxint4_moe_available)

Return `True`

when FlashInfer MxInt4 kernels can be used.

## Source code in `vllm/model_executor/layers/quantization/utils/flashinfer_mxint4_moe.py`


##

`prepare_static_weights_for_trtllm_mxint4_moe(gemm1_weights, gemm1_scales, gemm2_weights, gemm2_scales)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_mxint4_moe.prepare_static_weights_for_trtllm_mxint4_moe)

Prepare MxInt4 weights for TRT-LLM kernel.

## Input

gemm1_weights: [num_experts, 2*intermediate_size, hidden_size//8] int32 (checkpoint uint4b8 packed) or uint8 (already packed signed int4) gemm1_scales: [num_experts, 2*intermediate_size, hidden_size//32] bf16 gemm2_weights: [num_experts, hidden_size, intermediate_size//8] int32 (checkpoint uint4b8 packed) or uint8 (already packed signed int4) gemm2_scales: [num_experts, hidden_size, intermediate_size//32] bf16

Returns:

-

–[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]Dict with keys 'gemm1_weights', 'gemm1_scales', 'gemm2_weights', 'gemm2_scales' containing shuffled/packed tensors ready for kernel


## Source code in `vllm/model_executor/layers/quantization/utils/flashinfer_mxint4_moe.py`


|
|