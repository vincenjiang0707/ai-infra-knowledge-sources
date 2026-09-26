source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/utils/machete_utils/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.quantization.utils.machete_utils`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.machete_utils)

Functions:

-
–[query_machete_supported_group_sizes](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.machete_utils.query_machete_supported_group_sizes)Queries the supported group sizes for Machete based on the activation type.


##

`query_machete_supported_group_sizes(act_type)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.machete_utils.query_machete_supported_group_sizes)

Queries the supported group sizes for Machete based on the activation type.

Parameters:

Returns:

-

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]A list of supported group sizes. The group size must

-

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]be divisible by

`TileShapeK = 128 * 8 // num_bits(act_type)`

. -

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]-1 indicates per-channel quantization.