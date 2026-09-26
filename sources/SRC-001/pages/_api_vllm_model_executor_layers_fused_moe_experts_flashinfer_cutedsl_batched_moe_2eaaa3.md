source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/flashinfer_cutedsl_batched_moe/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.fused_moe.experts.flashinfer_cutedsl_batched_moe`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.flashinfer_cutedsl_batched_moe)

Classes:

Functions:

-
–[flashinfer_cutedsl_moe_masked](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.flashinfer_cutedsl_batched_moe.flashinfer_cutedsl_moe_masked)Perform masked Mixture-of-Experts computation with FlashInfer's CuteDSL


##

`FlashInferCuteDSLBatchedExperts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.flashinfer_cutedsl_batched_moe.FlashInferCuteDSLBatchedExperts)

Bases: [FusedMoEExpertsModular](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular)

Methods:

-
–[workspace_shapes](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.flashinfer_cutedsl_batched_moe.FlashInferCuteDSLBatchedExperts.workspace_shapes)Compute the shapes for the temporary and final outputs of the two gemms


## Source code in `vllm/model_executor/layers/fused_moe/experts/flashinfer_cutedsl_batched_moe.py`


|
|

###

`workspace_shapes(M, N, K, topk, global_num_experts, local_num_experts, expert_tokens_meta, activation)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.flashinfer_cutedsl_batched_moe.FlashInferCuteDSLBatchedExperts.workspace_shapes)

Compute the shapes for the temporary and final outputs of the two gemms and activation in the fused expert function. Since the gemms are independent, the workspace for the first gemm can be shared with the workspace for the last gemm.

Returns a tuple of: - workspace13 shape tuple: must be large enough to hold the result of either expert gemm. - workspace2 shape tuple: must be large enough to hold the result of the activation function. - output shape tuple: must be exact size of the final gemm output. - Workspace type: The dtype to use for the workspace tensors. - Note: in order for activation chunking to work, the first dimension of each tuple must be the number of tokens.

## Source code in `vllm/model_executor/layers/fused_moe/experts/flashinfer_cutedsl_batched_moe.py`


##

`flashinfer_cutedsl_moe_masked(hidden_states, input_global_scale, w1, w1_blockscale, w1_alpha, w2, a2_global_scale, w2_blockscale, w2_alpha, masked_m, workspace, out)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.flashinfer_cutedsl_batched_moe.flashinfer_cutedsl_moe_masked)

Perform masked Mixture-of-Experts computation with FlashInfer's CuteDSL kernels.

Parameters:

-

(`hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.flashinfer_cutedsl_batched_moe.flashinfer_cutedsl_moe_masked(hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)|[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]Either of the following case * torch.Tensor: [num_experts, m, k], bf16 * tuple[torch.Tensor, torch.Tensor]: [num_experts, m, k // 2], uint8, [num_experts, m, k // 16], float8_e4m3fn

-

(`input_global_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.flashinfer_cutedsl_batched_moe.flashinfer_cutedsl_moe_masked(input_global_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(l,)

-

(`w1`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.flashinfer_cutedsl_batched_moe.flashinfer_cutedsl_moe_masked(w1))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)fp4 weights, [l, 2 * n, k // 2], uint8

-

(`w1_blockscale`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.flashinfer_cutedsl_batched_moe.flashinfer_cutedsl_moe_masked(w1_blockscale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)blockscale factors, e4m3,

-

(`w1_alpha`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.flashinfer_cutedsl_batched_moe.flashinfer_cutedsl_moe_masked(w1_alpha))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(l,)

-

(`w2`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.flashinfer_cutedsl_batched_moe.flashinfer_cutedsl_moe_masked(w2))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)fp4 weights, [l, k, n // 2], uint8

-

(`a2_global_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.flashinfer_cutedsl_batched_moe.flashinfer_cutedsl_moe_masked(a2_global_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(l,)

-

(`w2_blockscale`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.flashinfer_cutedsl_batched_moe.flashinfer_cutedsl_moe_masked(w2_blockscale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)blockscale factors, e4m3,

-

(`w2_alpha`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.flashinfer_cutedsl_batched_moe.flashinfer_cutedsl_moe_masked(w2_alpha))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(l,)

-

(`out`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.flashinfer_cutedsl_batched_moe.flashinfer_cutedsl_moe_masked(out))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)output tensor written in place, [l, m, k], bf16

-

(`masked_m`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.flashinfer_cutedsl_batched_moe.flashinfer_cutedsl_moe_masked(masked_m))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Masked dimension indices

-

(`workspace`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.flashinfer_cutedsl_batched_moe.flashinfer_cutedsl_moe_masked(workspace))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)For gateup_output


## Notes

- Assumes max(masked_m) <= m.

## Source code in `vllm/model_executor/layers/fused_moe/experts/flashinfer_cutedsl_batched_moe.py`


|
|