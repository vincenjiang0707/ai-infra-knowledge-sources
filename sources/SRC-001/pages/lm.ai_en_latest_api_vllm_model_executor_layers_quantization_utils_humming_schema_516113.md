source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/utils/humming/schema/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.quantization.utils.humming.schema`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.humming.schema)

Map Humming schemas and handle shared checkpoint quantization settings.

##

`_group_shape(group_size, group_size_n=0)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.humming.schema._group_shape)

Map humming group sizes to QuantKey GroupShape.

group_size: elements per group along K (col); 0 means full dimension. group_size_n: elements per group along N (row); 0 means 1 (per-row).

GroupShape convention: row = N dim, col = K dim.