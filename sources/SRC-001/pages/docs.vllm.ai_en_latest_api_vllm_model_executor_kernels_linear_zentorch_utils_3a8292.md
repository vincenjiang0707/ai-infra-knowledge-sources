source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/zentorch_utils/
lastmod: 2026-09-23

#

`vllm.model_executor.kernels.linear.zentorch_utils`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.zentorch_utils)

Gates zentorch CPU linear dispatch on platform/op availability.

Functions:

-
–[has_zentorch_op](https://docs.vllm.ai#vllm.model_executor.kernels.linear.zentorch_utils.has_zentorch_op)Return

`True`

when running on Zen CPU with all named ops registered.

##

`_moe_activation_to_str(activation)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.zentorch_utils._moe_activation_to_str)

Normalize activation to a lowercase string (enum-safe).

##

`has_zentorch_op(op_names)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.zentorch_utils.has_zentorch_op)

Return `True`

when running on Zen CPU with all named ops registered.