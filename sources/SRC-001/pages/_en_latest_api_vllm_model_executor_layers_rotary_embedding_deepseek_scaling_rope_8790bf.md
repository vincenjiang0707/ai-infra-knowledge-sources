source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/rotary_embedding/deepseek_scaling_rope/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.rotary_embedding.deepseek_scaling_rope`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.rotary_embedding.deepseek_scaling_rope)

Classes:

-
–[DeepseekScalingRotaryEmbedding](https://docs.vllm.ai#vllm.model_executor.layers.rotary_embedding.deepseek_scaling_rope.DeepseekScalingRotaryEmbedding)RotaryEmbedding extended with YaRN method.

-
–[DeepseekV4ScalingRotaryEmbedding](https://docs.vllm.ai#vllm.model_executor.layers.rotary_embedding.deepseek_scaling_rope.DeepseekV4ScalingRotaryEmbedding)RotaryEmbedding extended with YaRN method.


##

`DeepseekScalingRotaryEmbedding`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.rotary_embedding.deepseek_scaling_rope.DeepseekScalingRotaryEmbedding)

Bases: [RotaryEmbeddingBase](https://docs.vllm.ai/base/#vllm.model_executor.layers.rotary_embedding.base.RotaryEmbeddingBase)

RotaryEmbedding extended with YaRN method.

Credits to Peng et al. github.com/jquesnelle/yarn

Methods:

-
–[forward_native](https://docs.vllm.ai#vllm.model_executor.layers.rotary_embedding.deepseek_scaling_rope.DeepseekScalingRotaryEmbedding.forward_native)PyTorch-native implementation equivalent to forward().

-
–[forward_static](https://docs.vllm.ai#vllm.model_executor.layers.rotary_embedding.deepseek_scaling_rope.DeepseekScalingRotaryEmbedding.forward_static)A static implementation of forward().


## Source code in `vllm/model_executor/layers/rotary_embedding/deepseek_scaling_rope.py`


|
|

###

`forward_native(positions, query, key=None, offsets=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.rotary_embedding.deepseek_scaling_rope.DeepseekScalingRotaryEmbedding.forward_native)

PyTorch-native implementation equivalent to forward().

## Source code in `vllm/model_executor/layers/rotary_embedding/deepseek_scaling_rope.py`


###

`forward_static(positions, query, key, head_size, rotary_dim, cos_sin_cache, is_neox_style, offsets=None)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.rotary_embedding.deepseek_scaling_rope.DeepseekScalingRotaryEmbedding.forward_static)

A static implementation of forward().

## Source code in `vllm/model_executor/layers/rotary_embedding/deepseek_scaling_rope.py`


##

`DeepseekV4ScalingRotaryEmbedding`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.rotary_embedding.deepseek_scaling_rope.DeepseekV4ScalingRotaryEmbedding)

Bases: [DeepseekScalingRotaryEmbedding](https://docs.vllm.ai#vllm.model_executor.layers.rotary_embedding.deepseek_scaling_rope.DeepseekScalingRotaryEmbedding)

RotaryEmbedding extended with YaRN method.

Credits to Peng et al. github.com/jquesnelle/yarn

Compared to DeepseekScalingRotaryEmbedding: - Applies RoPE to the last rotary_dim - The forward method requires an inverse parameter to indicate whether to negate the sin - Supports applying RoPE to query only (without key) - cos_sin_cache stored as fp32 for higher precision RoPE

Methods:

-
–[forward_native](https://docs.vllm.ai#vllm.model_executor.layers.rotary_embedding.deepseek_scaling_rope.DeepseekV4ScalingRotaryEmbedding.forward_native)PyTorch-native implementation equivalent to forward().


## Source code in `vllm/model_executor/layers/rotary_embedding/deepseek_scaling_rope.py`


|
|

###

`forward_native(positions, query, key=None, offsets=None, inverse=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.rotary_embedding.deepseek_scaling_rope.DeepseekV4ScalingRotaryEmbedding.forward_native)

PyTorch-native implementation equivalent to forward().