source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/commandr/
lastmod: 2026-09-24

#

`vllm.model_executor.models.commandr`

[¶](https://docs.vllm.ai#vllm.model_executor.models.commandr)

PyTorch Cohere model.

Functions:

-
–[select_norm_impl](https://docs.vllm.ai#vllm.model_executor.models.commandr.select_norm_impl)Returns the normalization layer class and epsilon value to use.


##

`select_norm_impl(config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.commandr.select_norm_impl)

Returns the normalization layer class and epsilon value to use. If `config.rms_norm_eps`

is present, use RMSNorm. Otherwise default to LayerNorm with `config.layer_norm_eps`

.