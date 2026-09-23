source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/oracle/fp8/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_moe.oracle.fp8`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.fp8)

Functions:

-
–[make_fp8_moe_quant_config](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.fp8.make_fp8_moe_quant_config)Create FusedMoEQuantConfig for the specified FP8 Backend.

-
–[map_fp8_backend](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.fp8.map_fp8_backend)Map user's MoEBackend to Fp8MoeBackend.

-
–[pad_tp_shard_to_weight_blocks](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.fp8.pad_tp_shard_to_weight_blocks)Pad the TP shard to whole checkpoint blocks, keeping scales rank-local.

-
–[refine_fp8_moe_block_shape](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.fp8.refine_fp8_moe_block_shape)Compute a refined block shape for block-quantized FP8 MoE weights whose

-
–[resolve_fp8_moe_weight_block_shape](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.fp8.resolve_fp8_moe_weight_block_shape)Return the TP-adapted block shape and refine factor:

-
–[select_fp8_moe_backend](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.fp8.select_fp8_moe_backend)Select the primary FP8 MoE backend


##

`_get_priority_backends(moe_config, weight_key, activation_key)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.fp8._get_priority_backends)

Get available backends in priority order based on platform and config.

This function can be extended to become more complex as needed.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/fp8.py`


##

`_humming_fp8_weight_schema(layer, weight, weight_scale)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.fp8._humming_fp8_weight_schema)

Build the humming weight schema from the canonical on-device fp8/mxfp8 tensors (scale dtype/shape, block size), not the producing quant method.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/fp8.py`


##

`make_fp8_moe_quant_config(fp8_backend, w1_scale, w2_scale, a1_scale, a2_scale, w1_bias=None, w2_bias=None, block_shape=None, per_act_token_quant=False, per_out_ch_quant=False, swiglu_limit=None, gemm1_alpha=None, gemm1_beta=None, layer=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.fp8.make_fp8_moe_quant_config)

Create FusedMoEQuantConfig for the specified FP8 Backend. The FusedMoEQuantConfig holds the scales that are used at runtime by the Modular Kernel abstraction.

Note that certain kernels (e.g. Flashinfer CUTLASS) need special Quant configs to handle non-standard inputs to their kernel interfaces.

In a future PR, we will have this function should be a method of the modular kernel itself.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/fp8.py`


|
|

##

`map_fp8_backend(runner_backend)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.fp8.map_fp8_backend)

Map user's MoEBackend to Fp8MoeBackend.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/fp8.py`


##

`pad_tp_shard_to_weight_blocks(config, weight_block_size)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.fp8.pad_tp_shard_to_weight_blocks)

Pad the TP shard to whole checkpoint blocks, keeping scales rank-local.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/fp8.py`


##

`refine_fp8_moe_block_shape(config, weight_block_size)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.fp8.refine_fp8_moe_block_shape)

Compute a refined block shape for block-quantized FP8 MoE weights whose checkpoint blocks cannot be sharded exactly across TP ranks.

TP shards the intermediate dim of the expert weights, so a per-shard size that is not a multiple of the checkpoint's block size makes the checkpoint's block scales impossible to shard exactly. When a finer block size (>= 32) divides both the checkpoint blocks and all involved dims, the weight scales can be refined to that granularity at load time (a lossless upsampling, since the refined block divides the checkpoint block). Only Triton-based kernels can consume the refined block shape: they take it as a runtime argument, while the other backends require the native 128x128 blocks. The refined shape is encoded in the QuantKey used for backend selection, so backends that only support 128x128 blocks are rejected by the oracle automatically.

Returns the refined [block_n, block_k] shape, or None if no refinement is needed or possible.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/fp8.py`


##

`resolve_fp8_moe_weight_block_shape(config, weight_block_size, activation_key, is_checkpoint_fp8_serialized)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.fp8.resolve_fp8_moe_weight_block_shape)

Return the TP-adapted block shape and refine factor: refine if kernels allow, else pad to the TP shard.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/fp8.py`


##

`select_fp8_moe_backend(config, weight_key, activation_key, allow_vllm_cutlass=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.fp8.select_fp8_moe_backend)

Select the primary FP8 MoE backend Note: Shape-specific fallbacks may still occur at runtime.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/fp8.py`


|
|