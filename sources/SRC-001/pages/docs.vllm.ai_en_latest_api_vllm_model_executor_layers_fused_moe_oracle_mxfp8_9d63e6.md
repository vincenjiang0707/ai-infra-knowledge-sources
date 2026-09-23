source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/oracle/mxfp8/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_moe.oracle.mxfp8`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp8)

Functions:

-
–[select_mxfp8_moe_backend](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp8.select_mxfp8_moe_backend)Select the MXFP8 MoE backend and the best expert class.


##

`_mxfp8_backend_to_kernel_cls(backend)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp8._mxfp8_backend_to_kernel_cls)

Resolve the MXFP8 expert classes for a backend.

DeepGEMM resolves directly to `DeepGemmExperts`

(not the `TritonOrDeepGemmExperts`

wrapper, whose Triton fallback cannot handle the MXFP8 1x32 scheme); all other backends defer to the FP8 resolver.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/mxfp8.py`


##

`_select_kernel_cls(backend, config)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp8._select_kernel_cls)

Select the first supported expert class for the MXFP8 config.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/mxfp8.py`


##

`select_mxfp8_moe_backend(config)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp8.select_mxfp8_moe_backend)

Select the MXFP8 MoE backend and the best expert class.

Returns:

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[Fp8MoeBackend,[type](https://docs.python.org/3/builtins/functions.html#type)[[FusedMoEExperts](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts)]]A tuple of (fp8_backend, experts_cls).