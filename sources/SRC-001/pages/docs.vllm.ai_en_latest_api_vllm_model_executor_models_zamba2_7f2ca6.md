source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/zamba2/
lastmod: 2026-09-24

#

`vllm.model_executor.models.zamba2`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2)

PyTorch Zamba2 model implementation for vLLM.

This module implements the Zamba2 architecture from https://arxiv.org/abs/2411.15242, which combines Mamba and Transformer architectures in a hybrid model optimized for efficient sequence modeling. The model alternates between state space model layers and attention-based layers.

Classes:

-
–[Zamba2Attention](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Attention)Multi-head attention mechanism for the Zamba2 model.

-
–[Zamba2AttentionDecoderLayer](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2AttentionDecoderLayer)Single decoder layer combining attention and feed-forward networks.

-
–[Zamba2ForCausalLM](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2ForCausalLM)Zamba2 model with causal language modeling head.

-
–[Zamba2HybridLayer](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2HybridLayer)Hybrid layer combining Transformer and Mamba architectures.

-
–[Zamba2LoRA](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2LoRA)LoRA layer for the Zamba2 model.

-
–[Zamba2MLP](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MLP)Feed-forward MLP layer for the Zamba2 model.

-
–[Zamba2MambaDecoderLayer](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MambaDecoderLayer)Single Mamba decoder layer with normalization.

-
–[Zamba2Model](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Model)Core Zamba2 model combining transformer and Mamba architectures.


##

`Zamba2Attention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Attention)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Multi-head attention mechanism for the Zamba2 model.

Implements attention with parallel computation, QKV projections, optional adapters and rotary position embeddings. The attention is computed across distributed blocks for efficient processing.

Methods:

## Source code in `vllm/model_executor/models/zamba2.py`


|
|

###

`__init__(config, bare_block_idx, num_hybrid_layers, cache_config=None, quant_config=None, prefix='')`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Attention.__init__)

Initialize the attention layer.

Parameters:

-

(`config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Attention.__init__(config))`Zamba2Config`

) –The Zamba2 model configuration

-

(`bare_block_idx`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Attention.__init__(bare_block_idx))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Index of the bare attention block

-

(`num_hybrid_layers`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Attention.__init__(num_hybrid_layers))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Total number of hybrid layers

-

(`cache_config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Attention.__init__(cache_config))

, default:[CacheConfig](https://docs.vllm.ai/config/#vllm.config.CacheConfig)| None`None`

) –Configuration for key-value caching

-

(`quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Attention.__init__(quant_config))

, default:[QuantizationConfig](https://docs.vllm.ai/layers/quantization/#vllm.model_executor.layers.quantization.QuantizationConfig)| None`None`

) –Configuration for model quantization

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Attention.__init__(prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –Optional prefix for parameter names


## Source code in `vllm/model_executor/models/zamba2.py`


|
|

###

`forward(hidden_states, block_idx, position_ids)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Attention.forward)

Forward pass through the attention layer.

Parameters:

-

(`hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Attention.forward(hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor [batch_size, seq_len, hidden_size]

-

(`position_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Attention.forward(position_ids))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Position IDs for positional embeddings

-

(`block_idx`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Attention.forward(block_idx))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Current shared transformer block index


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output tensor [batch_size, seq_len, hidden_size]


## Source code in `vllm/model_executor/models/zamba2.py`


##

`Zamba2AttentionDecoderLayer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2AttentionDecoderLayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Single decoder layer combining attention and feed-forward networks.

This layer implements a standard transformer block with: - Input layer normalization - Multi-head self-attention - Pre-feed-forward layer normalization - Feed-forward network (MLP)

Methods:

## Source code in `vllm/model_executor/models/zamba2.py`


|
|

###

`__init__(config, bare_block_idx, num_hybrid_layers, cache_config=None, quant_config=None, prefix='')`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2AttentionDecoderLayer.__init__)

Initialize the decoder layer.

Parameters:

-

(`config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2AttentionDecoderLayer.__init__(config))`Zamba2Config`

) –The Zamba2 model configuration

-

(`bare_block_idx`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2AttentionDecoderLayer.__init__(bare_block_idx))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Index of the bare block

-

(`num_hybrid_layers`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2AttentionDecoderLayer.__init__(num_hybrid_layers))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Total number of hybrid layers

-

(`cache_config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2AttentionDecoderLayer.__init__(cache_config))

, default:[CacheConfig](https://docs.vllm.ai/config/#vllm.config.CacheConfig)| None`None`

) –Configuration for key-value caching

-

(`quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2AttentionDecoderLayer.__init__(quant_config))

, default:[QuantizationConfig](https://docs.vllm.ai/layers/quantization/#vllm.model_executor.layers.quantization.QuantizationConfig)| None`None`

) –Configuration for model quantization

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2AttentionDecoderLayer.__init__(prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –Optional prefix for parameter names


## Source code in `vllm/model_executor/models/zamba2.py`


###

`forward(hidden_states, original_hidden_states, block_idx, positions)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2AttentionDecoderLayer.forward)

Forward pass through the decoder layer.

Parameters:

-

(`hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2AttentionDecoderLayer.forward(hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor from previous layer

-

(`original_hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2AttentionDecoderLayer.forward(original_hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Original input tensor for residual connection

-

(`block_idx`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2AttentionDecoderLayer.forward(block_idx))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Current shared transformer block index

-

(`positions`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2AttentionDecoderLayer.forward(positions))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)IDs for positional embeddings


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Transformed hidden states after attention and feed-forward


## Source code in `vllm/model_executor/models/zamba2.py`


##

`Zamba2ForCausalLM`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2ForCausalLM)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [HasInnerState](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.HasInnerState)

, [IsHybrid](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.IsHybrid)[SupportsMambaPrefixCaching](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMambaPrefixCaching)

Zamba2 model with causal language modeling head.

This class wraps the core Zamba2 model and adds: - A language modeling head for next token prediction - Mamba state caching functionality - Support for model parallelism and quantization - Sampling capabilities for text generation

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2ForCausalLM.__init__)Initialize the Zamba2 model for causal language modeling.

-
–[compute_logits](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2ForCausalLM.compute_logits)Compute logits for next token prediction.

-
–[embed_input_ids](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2ForCausalLM.embed_input_ids)Convert input token IDs to embeddings.

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2ForCausalLM.forward)Forward pass through the model.

-
–[get_mamba_state_shape_from_config](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2ForCausalLM.get_mamba_state_shape_from_config)Calculate shapes for Mamba's convolutional and state caches.


## Source code in `vllm/model_executor/models/zamba2.py`


|
|

###

`__init__(*, vllm_config, prefix='')`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2ForCausalLM.__init__)

Initialize the Zamba2 model for causal language modeling.

Parameters:

-

(`vllm_config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2ForCausalLM.__init__(vllm_config))

) –[VllmConfig](https://docs.vllm.ai/config/#vllm.config.VllmConfig)Configuration containing model, cache, quantization, LoRA and scheduler settings

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2ForCausalLM.__init__(prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –Optional prefix for parameter names


Raises:

-

–[AssertionError](https://docs.python.org/3/builtins/exceptions.html#AssertionError)If prefix caching is enabled (not supported by Mamba)


## Source code in `vllm/model_executor/models/zamba2.py`


###

`compute_logits(hidden_states)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2ForCausalLM.compute_logits)

Compute logits for next token prediction.

Parameters:

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NoneLogits for next token prediction


## Source code in `vllm/model_executor/models/zamba2.py`


###

`embed_input_ids(input_ids)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2ForCausalLM.embed_input_ids)

Convert input token IDs to embeddings.

Parameters:

Returns: Embedded representation of the input tokens

## Source code in `vllm/model_executor/models/zamba2.py`


###

`forward(input_ids, positions, inputs_embeds=None, **kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2ForCausalLM.forward)

Forward pass through the model.

Parameters:

-

(`input_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2ForCausalLM.forward(input_ids))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NoneInput token IDs

-

(`positions`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2ForCausalLM.forward(positions))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Position IDs for embeddings

-

(`inputs_embeds`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2ForCausalLM.forward(inputs_embeds))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional pre-computed input embeddings

-

(`**kwargs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2ForCausalLM.forward(**kwargs))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`{}`

) –Additional arguments passed to cache manager


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output hidden states


## Source code in `vllm/model_executor/models/zamba2.py`


###

`get_mamba_state_shape_from_config(vllm_config)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2ForCausalLM.get_mamba_state_shape_from_config)

Calculate shapes for Mamba's convolutional and state caches.

Parameters:

-

(`vllm_config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2ForCausalLM.get_mamba_state_shape_from_config(vllm_config))

) –[VllmConfig](https://docs.vllm.ai/config/#vllm.config.VllmConfig)vLLM config


Returns:

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)]Tuple containing:

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)]- conv_state_shape: Shape for convolutional state cache

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)],[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)]]- temporal_state_shape: Shape for state space model cache


## Source code in `vllm/model_executor/models/zamba2.py`


##

`Zamba2HybridLayer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2HybridLayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Hybrid layer combining Transformer and Mamba architectures.

This layer implements the hybrid architecture described in the Zamba paper, where a shared transformer pathway processes input in parallel with a Mamba pathway. The transformer output is projected and added to the Mamba input for enhanced representation learning.

Methods:

## Source code in `vllm/model_executor/models/zamba2.py`


|
|

###

`__init__(shared_transformer, config, block_idx, model_config=None, cache_config=None, quant_config=None, prefix='')`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2HybridLayer.__init__)

Initialize the hybrid layer.

Parameters:

-

(`shared_transformer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2HybridLayer.__init__(shared_transformer))

) –[Zamba2AttentionDecoderLayer](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2AttentionDecoderLayer)Transformer decoder layer for attention pathway

-

(`config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2HybridLayer.__init__(config))`Zamba2Config`

) –The Zamba2 model configuration

-

(`block_idx`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2HybridLayer.__init__(block_idx))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Index of this hybrid block in the model

-

(`model_config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2HybridLayer.__init__(model_config))

, default:[ModelConfig](https://docs.vllm.ai/config/#vllm.config.ModelConfig)| None`None`

) –The model config, when available

-

(`cache_config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2HybridLayer.__init__(cache_config))

, default:[CacheConfig](https://docs.vllm.ai/config/#vllm.config.CacheConfig)| None`None`

) –The KV cache config, when available

-

(`quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2HybridLayer.__init__(quant_config))

, default:[QuantizationConfig](https://docs.vllm.ai/layers/quantization/#vllm.model_executor.layers.quantization.QuantizationConfig)| None`None`

) –Configuration for model quantization

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2HybridLayer.__init__(prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –Module prefix used for quantization config lookup


## Source code in `vllm/model_executor/models/zamba2.py`


###

`forward(hidden_states, original_hidden_states, positions)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2HybridLayer.forward)

Forward pass through the hybrid layer.

Processes input through parallel transformer and Mamba paths: 1. Transformer path processes input with attention 2. Transformer output is projected to match hidden size 3. Projected output is added to Mamba path input 4. Final output combines both paths' representations

Parameters:

-

(`hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2HybridLayer.forward(hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor [batch_size, seq_len, hidden_size]

-

(`original_hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2HybridLayer.forward(original_hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Original input for transformer residual connection

-

(`positions`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2HybridLayer.forward(positions))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Position IDs for positional embeddings


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output tensor combining transformer and Mamba representations


## Source code in `vllm/model_executor/models/zamba2.py`


##

`Zamba2LoRA`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2LoRA)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

LoRA layer for the Zamba2 model.

Implements a LoRA layer that is used in shared attention and gated MLP blocks.

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2LoRA.__init__)Initialize the attention layer.


## Source code in `vllm/model_executor/models/zamba2.py`


###

`__init__(input_dim, rank, output_dim, quant_config=None, prefix='')`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2LoRA.__init__)

Initialize the attention layer.

Parameters:

-

(`input_dim`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2LoRA.__init__(input_dim))

) –[int](https://docs.python.org/3/builtins/functions.html#int)input dimension

-

(`rank`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2LoRA.__init__(rank))

) –[int](https://docs.python.org/3/builtins/functions.html#int)LoRA rank

-

(`output_dim`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2LoRA.__init__(output_dim))

) –[int](https://docs.python.org/3/builtins/functions.html#int)|[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]output dimension

-

(`quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2LoRA.__init__(quant_config))

, default:[QuantizationConfig](https://docs.vllm.ai/layers/quantization/#vllm.model_executor.layers.quantization.QuantizationConfig)| None`None`

) –Configuration for model quantization

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2LoRA.__init__(prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –Module prefix used for quantization config lookup


## Source code in `vllm/model_executor/models/zamba2.py`


##

`Zamba2MLP`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MLP)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Feed-forward MLP layer for the Zamba2 model.

Implements a gated feed-forward network that projects inputs to a larger intermediate size, applies GELU activation with gating, then projects back to the original size. Includes optional adapter layers for model adaptation.

Methods:

## Source code in `vllm/model_executor/models/zamba2.py`


|
|

###

`__init__(config, bare_block_idx, num_hybrid_layers, quant_config=None, prefix='')`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MLP.__init__)

Initialize the MLP layer.

Parameters:

-

(`config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MLP.__init__(config))`Zamba2Config`

) –The Zamba2 model configuration

-

(`bare_block_idx`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MLP.__init__(bare_block_idx))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Index of the bare block in the model

-

(`num_hybrid_layers`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MLP.__init__(num_hybrid_layers))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)]Total number of hybrid layers

-

(`quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MLP.__init__(quant_config))

, default:[QuantizationConfig](https://docs.vllm.ai/layers/quantization/#vllm.model_executor.layers.quantization.QuantizationConfig)| None`None`

) –Configuration for model quantization

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MLP.__init__(prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –Module prefix used for quantization config lookup


## Source code in `vllm/model_executor/models/zamba2.py`


###

`forward(hidden_states, block_idx)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MLP.forward)

Forward pass through the MLP layer.

Parameters:

-

(`hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MLP.forward(hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor [batch_size, seq_len, hidden_size]

-

(`block_idx`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MLP.forward(block_idx))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Current shared transformer block index


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output tensor [batch_size, seq_len, hidden_size] after applying

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)gated feed-forward transformation


## Source code in `vllm/model_executor/models/zamba2.py`


##

`Zamba2MambaDecoderLayer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MambaDecoderLayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Single Mamba decoder layer with normalization.

This implements a Mamba block. It includes input normalization and can process sequences using either chunked or full computation depending on configuration.

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MambaDecoderLayer.__init__)Initialize the Mamba decoder layer.

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MambaDecoderLayer.forward)Forward pass through the Mamba decoder layer.


## Source code in `vllm/model_executor/models/zamba2.py`


|
|

###

`__init__(config, model_config=None, cache_config=None, quant_config=None, prefix='')`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MambaDecoderLayer.__init__)

Initialize the Mamba decoder layer.

Parameters:

-

(`config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MambaDecoderLayer.__init__(config))`Zamba2Config`

) –The Zamba2 model configuration

-

(`model_config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MambaDecoderLayer.__init__(model_config))

, default:[ModelConfig](https://docs.vllm.ai/config/#vllm.config.ModelConfig)| None`None`

) –The model config, when available

-

(`cache_config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MambaDecoderLayer.__init__(cache_config))

, default:[CacheConfig](https://docs.vllm.ai/config/#vllm.config.CacheConfig)| None`None`

) –The KV cache config, when available

-

(`quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MambaDecoderLayer.__init__(quant_config))

, default:[QuantizationConfig](https://docs.vllm.ai/layers/quantization/#vllm.model_executor.layers.quantization.QuantizationConfig)| None`None`

) –Configuration for model quantization

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MambaDecoderLayer.__init__(prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –Module prefix used for quantization config lookup


## Source code in `vllm/model_executor/models/zamba2.py`


###

`forward(hidden_states, transformer_hidden_states=None, positions=None, original_hidden_states=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MambaDecoderLayer.forward)

Forward pass through the Mamba decoder layer.

Parameters:

-

(`hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MambaDecoderLayer.forward(hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor [batch_size, seq_len, hidden_size]

-

(`transformer_hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MambaDecoderLayer.forward(transformer_hidden_states))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional output from transformer path Added to input if provided (used in hybrid architecture)

-

(`positions`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MambaDecoderLayer.forward(positions))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional position IDs (unused in Mamba)

-

(`original_hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2MambaDecoderLayer.forward(original_hidden_states))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional original inputs (unused in Mamba)


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Transformed hidden states with residual connection applied


## Source code in `vllm/model_executor/models/zamba2.py`


##

`Zamba2Model`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Model)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Core Zamba2 model combining transformer and Mamba architectures.

The model processes input through a sequence of hybrid and Mamba-only layers, using token embeddings and final layer normalization.

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Model.__init__)Initialize the Zamba2 model.

-
–[embed_input_ids](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Model.embed_input_ids)Convert input token IDs to embeddings.

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Model.forward)Forward pass through the model.


## Source code in `vllm/model_executor/models/zamba2.py`


|
|

###

`__init__(*, vllm_config, prefix='')`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Model.__init__)

Initialize the Zamba2 model.

Parameters:

-

(`vllm_config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Model.__init__(vllm_config))

) –[VllmConfig](https://docs.vllm.ai/config/#vllm.config.VllmConfig)Configuration object containing model, cache, quantization and LoRA settings

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Model.__init__(prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –Optional prefix for parameter names in state dict


## Source code in `vllm/model_executor/models/zamba2.py`


|
|

###

`embed_input_ids(input_ids)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Model.embed_input_ids)

Convert input token IDs to embeddings.

Parameters:

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Embedded representation of the input tokens


## Source code in `vllm/model_executor/models/zamba2.py`


###

`forward(input_ids, positions, inputs_embeds=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Model.forward)

Forward pass through the model.

Parameters:

-

(`input_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Model.forward(input_ids))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NoneInput token IDs

-

(`positions`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Model.forward(positions))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Position IDs for embeddings

-

(`inputs_embeds`

[¶](https://docs.vllm.ai#vllm.model_executor.models.zamba2.Zamba2Model.forward(inputs_embeds))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional pre-computed input embeddings


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)|[IntermediateTensors](https://docs.vllm.ai/sequence/#vllm.sequence.IntermediateTensors)Either final hidden states or intermediate tensors for pipeline

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)|[IntermediateTensors](https://docs.vllm.ai/sequence/#vllm.sequence.IntermediateTensors)parallelism