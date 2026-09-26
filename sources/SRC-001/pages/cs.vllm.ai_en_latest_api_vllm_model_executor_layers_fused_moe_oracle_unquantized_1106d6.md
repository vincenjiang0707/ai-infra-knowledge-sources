source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/oracle/unquantized/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.fused_moe.oracle.unquantized`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.unquantized)

Classes:

-
–[UnquantizedMoEKernelOracle](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.unquantized.UnquantizedMoEKernelOracle)Class-based view of the unquantized MoE kernel oracle.


Functions:

-
–[map_unquantized_backend](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.unquantized.map_unquantized_backend)Map user's MoEBackend to UnquantizedMoeBackend.

-
–[select_unquantized_moe_backend](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.unquantized.select_unquantized_moe_backend)Select the primary Unquantized MoE backend.

-
–[unquantized_round_up_hidden_size_and_intermediate_size](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.unquantized.unquantized_round_up_hidden_size_and_intermediate_size)Round up dimensions before allocation to satisfy the selected kernel.


##

`UnquantizedMoEKernelOracle`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.unquantized.UnquantizedMoEKernelOracle)

Bases: [MoEKernelOracle](https://docs.vllm.ai/base/#vllm.model_executor.layers.fused_moe.oracle.base.MoEKernelOracle)[UnquantizedMoeBackend]

Class-based view of the unquantized MoE kernel oracle.

Each method delegates to its module-level counterpart so that instantiating and calling this class is bit-identical to calling the standalone functions. Follow-up PRs may move logic from the module-level functions into these methods.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`


##

`_get_priority_backends(moe_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.unquantized._get_priority_backends)

Get available backends in priority order based on platform and config.

This function can be extended to become more complex as needed.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`


##

`_trtllm_bf16_lora_supported(moe_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.unquantized._trtllm_bf16_lora_supported)

Gate for routing LoRA-enabled BF16 MoE to the FlashInfer TRT-LLM gemm1_lora_delta path (PR #3153).

## Source code in `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`


##

`map_unquantized_backend(runner_backend)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.unquantized.map_unquantized_backend)

Map user's MoEBackend to UnquantizedMoeBackend.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`


##

`select_unquantized_moe_backend(moe_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.unquantized.select_unquantized_moe_backend)

Select the primary Unquantized MoE backend. Note: Shape-specific fallbacks may still occur at runtime.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`


|
|

##

`unquantized_round_up_hidden_size_and_intermediate_size(backend, hidden_size, intermediate_size)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.unquantized.unquantized_round_up_hidden_size_and_intermediate_size)

Round up dimensions before allocation to satisfy the selected kernel.