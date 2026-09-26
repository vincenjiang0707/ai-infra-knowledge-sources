source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/warmup/deep_gemm_warmup/
lastmod: 2026-09-24

#

`vllm.model_executor.warmup.deep_gemm_warmup`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.deep_gemm_warmup)

Warmup deep_gemm kernels. DeepGEMM JIT's the kernels. The warmup aims to JIT all the kernels that would be used during model execution beforehand.

##

`_deep_gemm_linear_data(module)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.deep_gemm_warmup._deep_gemm_linear_data)

Return (weight, weight_scale) for a layer whose kernel stamped itself as `deep_gemm_warmup_provider`

in `process_weights_after_loading`

, else None.

## Source code in `vllm/model_executor/warmup/deep_gemm_warmup.py`


##

`_extract_data_from_fused_moe_module(m_)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.deep_gemm_warmup._extract_data_from_fused_moe_module)

Extract weights, weight scales and num_topk from MoERunner module.

## Source code in `vllm/model_executor/warmup/deep_gemm_warmup.py`


##

`_generate_optimal_warmup_m_values(max_tokens, n, device)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.deep_gemm_warmup._generate_optimal_warmup_m_values)

Generate M values that cover all possible DeepGEMM kernel configurations. Reference: https://github.com/deepseek-ai/DeepGEMM/blob/79f48ee15a82dd5fad5cd9beaa393c1f755e6b55/csrc/jit_kernels/heuristics/common.hpp

Parameters:

-

(`max_tokens`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.deep_gemm_warmup._generate_optimal_warmup_m_values(max_tokens))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum number of tokens to warmup for

-

(`n`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.deep_gemm_warmup._generate_optimal_warmup_m_values(n))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The actual N dimension from the weight tensor

-

(`device`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.deep_gemm_warmup._generate_optimal_warmup_m_values(device))

) –[device](https://pytorch.org/docs/stable/tensor_attributes.html#torch.device)The torch device to get properties from.


## Source code in `vllm/model_executor/warmup/deep_gemm_warmup.py`


##

`_get_fp8_gemm_nt_m_values(w, max_tokens)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.deep_gemm_warmup._get_fp8_gemm_nt_m_values)

Get the M values to warmup for a given weight tensor.