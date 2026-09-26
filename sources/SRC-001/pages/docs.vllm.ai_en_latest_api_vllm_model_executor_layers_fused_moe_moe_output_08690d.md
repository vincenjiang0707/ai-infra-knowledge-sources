source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/moe_output/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.fused_moe.moe_output`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_output)

Output contract between a MoE layer and a consumer that fuses its tail.

Classes:

-
–[MoEOutput](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_output.MoEOutput)A MoE layer's output with its final reduction still open.

-
–[UnfinalizedMoEOutput](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_output.UnfinalizedMoEOutput)Unfinalized output of a monolithic MoE kernel.


Functions:

-
–[convert_flashinfer_moe_output](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_output.convert_flashinfer_moe_output)Normalize the two FlashInfer TRTLLM MoE return layouts.


##

`MoEOutput`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_output.MoEOutput)

A MoE layer's output with its final reduction still open.

Returned by layers whose MoE runs un-reduced (`reduce_results=False`

) so that the consumer -- typically the next layer's RMSNorm -- can fuse the tensor-parallel all-reduce into itself instead of paying for a standalone one. Keeping the shared-expert output and the routed scale separate leaves that reduction the consumer's to schedule; when the routed output is still unfinalized, the top-k reduction is open too and can fold into the same kernel.

Producers only leave the routed output unfinalized when a fused consumer can actually take that form -- the token ceiling and topology support are theirs to check -- so an `UnfinalizedMoEOutput`

here means the fused path applies, and a consumer need not re-derive that.

## Source code in `vllm/model_executor/layers/fused_moe/moe_output.py`


##

`UnfinalizedMoEOutput`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_output.UnfinalizedMoEOutput)

Unfinalized output of a monolithic MoE kernel.

Kernels that can stop after GEMM2 (the TRTLLM-Gen `do_finalize=False`

path) hand back their permuted, unweighted output plus the routing weights and the permute map, so that the top-k reduction can be fused with whatever follows -- the shared-expert add and the tensor-parallel all-reduce -- instead of running as its own kernel.

The buffers are consumed as-is by the fused kernels, which index `gemm2_permuted`

by row: it must be densely packed at `hidden_dim`

, and its row count (an autotuner-dependent padded value) is never referenced.

## Source code in `vllm/model_executor/layers/fused_moe/moe_output.py`


##

`convert_flashinfer_moe_output(flashinfer_output, *, do_finalize, num_tokens, top_k, finalized_output=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_output.convert_flashinfer_moe_output)

Normalize the two FlashInfer TRTLLM MoE return layouts.

Parameters:

-

(`flashinfer_output`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_output.convert_flashinfer_moe_output(flashinfer_output))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)|[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]Tensor returned by the FlashInfer BF16 wrapper's legacy finalized path, or its mode-dependent tensor list.

-

(`do_finalize`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_output.convert_flashinfer_moe_output(do_finalize))

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether FlashInfer ran its top-k finalize step.

-

(`num_tokens`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_output.convert_flashinfer_moe_output(num_tokens))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of input tokens.

-

(`top_k`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_output.convert_flashinfer_moe_output(top_k))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of routed experts per token.

-

(`finalized_output`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_output.convert_flashinfer_moe_output(finalized_output))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional destination passed to FlashInfer's

`output`

argument.

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)|[UnfinalizedMoEOutput](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_output.UnfinalizedMoEOutput)A finalized tensor or the structured deferred-finalize output.


Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)If FlashInfer returns an unexpected layout.