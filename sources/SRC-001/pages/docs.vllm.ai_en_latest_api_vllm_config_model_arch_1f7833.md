source: https://docs.vllm.ai/en/latest/api/vllm/config/model_arch/
lastmod: 2026-09-23

#

`vllm.config.model_arch`

[¶](https://docs.vllm.ai#vllm.config.model_arch)

Classes:

-
–[ModelArchitectureConfig](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig)Configuration for model architecture that required by vLLM runtime.


##

`ModelArchitectureConfig`

[¶](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig)

Configuration for model architecture that required by vLLM runtime.

Methods:

-
–[__getitem__](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.__getitem__)ModelArchitectureConfig for a specific layer.

-
–[from_layers](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.from_layers)Whole-model config for a checkpoint whose layers differ.


Attributes:

-
([architectures](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.architectures)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]List of model architecture class names (e.g., ['LlamaForCausalLM']).

-
([derived_max_model_len_and_key](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.derived_max_model_len_and_key)

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[float](https://docs.python.org/3/builtins/functions.html#float),[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None]Derived maximum model length and key from the hf config.

-
([head_size](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.head_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Head dimension of the model.

-
([hidden_size](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.hidden_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Hidden size of the model.

-
([is_deepseek_mla](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.is_deepseek_mla)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether the model is a DeepSeek MLA model.

-
([is_mm_prefix_lm](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.is_mm_prefix_lm)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether the model uses image bidirectional attention.

-
([model_type](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.model_type)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Model type identifier (e.g., 'llama', 'gpt_oss').

-
([num_experts](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.num_experts)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of experts in the model.

-
([num_experts_per_token](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.num_experts_per_token)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of routed experts selected per token.

-
([per_layer_overrides](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.per_layer_overrides)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)]] | NonePer-layer values for the fields that vary,

`None`

unless some field does. -
([quantization_config](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.quantization_config)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | NoneQuantization configuration dictionary containing quantization parameters.

-
([rswa_window](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.rswa_window)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneReference Sliding Window Attention window size (None disables R-SWA).

-
([text_model_type](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.text_model_type)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneText model type identifier (e.g., 'llama4_text').

-
([total_num_attention_heads](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.total_num_attention_heads)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of attention heads in the model.

-
([total_num_hidden_layers](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.total_num_hidden_layers)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of hidden layers in the model.

-
([total_num_kv_heads](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.total_num_kv_heads)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of key value heads in the model.

-
([vocab_size](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.vocab_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Vocabulary size of the model.


## Source code in `vllm/config/model_arch.py`


|
|

###

`architectures`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.architectures)

List of model architecture class names (e.g., ['LlamaForCausalLM']). It can be None upon calling `vllm_config.with_hf_config(config.text_config)`


###

`derived_max_model_len_and_key`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.derived_max_model_len_and_key)

Derived maximum model length and key from the hf config.

###

`head_size`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.head_size)

Head dimension of the model.

###

`hidden_size`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.hidden_size)

Hidden size of the model.

###

`is_deepseek_mla`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.is_deepseek_mla)

Whether the model is a DeepSeek MLA model.

###

`is_mm_prefix_lm`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.is_mm_prefix_lm)

Whether the model uses image bidirectional attention.

###

`model_type`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.model_type)

Model type identifier (e.g., 'llama', 'gpt_oss').

###

`num_experts`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.num_experts)

Number of experts in the model.

###

`num_experts_per_token`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.num_experts_per_token)

Number of routed experts selected per token.

###

`per_layer_overrides = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.per_layer_overrides)

Per-layer values for the fields that vary, `None`

unless some field does.

One dict per layer, holding only the fields whose value differs from the whole-model value above. Everything else is read from the whole-model config, so later edits to it are visible through `self[layer_idx]`

.

###

`quantization_config`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.quantization_config)

Quantization configuration dictionary containing quantization parameters.

###

`rswa_window`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.rswa_window)

Reference Sliding Window Attention window size (None disables R-SWA).

###

`text_model_type`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.text_model_type)

Text model type identifier (e.g., 'llama4_text').

###

`total_num_attention_heads`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.total_num_attention_heads)

Number of attention heads in the model.

###

`total_num_hidden_layers`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.total_num_hidden_layers)

Number of hidden layers in the model.

###

`total_num_kv_heads`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.total_num_kv_heads)

Number of key value heads in the model.

###

`vocab_size`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.vocab_size)

Vocabulary size of the model.

###

`__getitem__(layer_idx)`

[¶](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.__getitem__)

ModelArchitectureConfig for a specific layer.

Returns `self`

when no field varies by layer, so callers never need to branch on heterogeneity. Mirrors `PreTrainedConfig.per_layer_config[i]`

.

## Source code in `vllm/config/model_arch.py`


###

`from_layers(layers)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.model_arch.ModelArchitectureConfig.from_layers)

Whole-model config for a checkpoint whose layers differ.

Fields that agree across layers are taken as they are. Fields that differ are collapsed with `max`

, so buffers are sized for the largest layer, and the differing values are kept per layer. No field is named here: which ones vary is whatever the checkpoint says.