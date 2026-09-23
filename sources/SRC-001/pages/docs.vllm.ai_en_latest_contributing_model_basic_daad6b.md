source: https://docs.vllm.ai/en/latest/contributing/model/basic/
lastmod: 2026-09-23

# Basic Model[¶](https://docs.vllm.ai#basic-model)

This guide walks you through the steps to implement a basic vLLM model.

## 1. Bring your model code[¶](https://docs.vllm.ai#1-bring-your-model-code)

First, clone the PyTorch model code from the source repository. For instance, vLLM's [ OPT model](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/opt.py) was adapted from HuggingFace's [modeling_opt.py](https://github.com/huggingface/transformers/blob/main/src/transformers/models/opt/modeling_opt.py) file.

Warning

Make sure to review and adhere to the original code's copyright and licensing terms!

## 2. Make your code compatible with vLLM[¶](https://docs.vllm.ai#2-make-your-code-compatible-with-vllm)

To ensure compatibility with vLLM, your model must meet the following requirements:

### Initialization Code[¶](https://docs.vllm.ai#initialization-code)

All vLLM modules within the model must include a `prefix`

argument in their constructor. This `prefix`

is typically the full name of the module in the model's state dictionary and is crucial for:

- Runtime support: vLLM's attention operators are registered in a model's state by their full names. Each attention operator must have a unique prefix as its layer name to avoid conflicts.
- Non-uniform quantization support: A quantized checkpoint can selectively quantize certain layers while keeping others in full precision. By providing the
`prefix`

during initialization, vLLM can match the current layer's`prefix`

with the quantization configuration to determine if the layer should be initialized in quantized mode.

The initialization code should look like this:

## Code

from torch import nn
from vllm.config import VllmConfig
from vllm.model_executor.layers.attention import Attention
class MyAttention(nn.Module):
def __init__(self, vllm_config: VllmConfig, prefix: str):
super().__init__()
self.attn = Attention(prefix=f"{prefix}.attn")
class MyDecoderLayer(nn.Module):
def __init__(self, vllm_config: VllmConfig, prefix: str):
super().__init__()
self.self_attn = MyAttention(prefix=f"{prefix}.self_attn")
class MyModel(nn.Module):
def __init__(self, vllm_config: VllmConfig, prefix: str):
super().__init__()
self.layers = nn.ModuleList(
[MyDecoderLayer(vllm_config, prefix=f"{prefix}.layers.{i}") for i in range(vllm_config.model_config.hf_config.num_hidden_layers)]
)
class MyModelForCausalLM(nn.Module):
def __init__(self, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
self.model = MyModel(vllm_config, prefix=f"{prefix}.model")


### Computation Code[¶](https://docs.vllm.ai#computation-code)

- Add a
`embed_input_ids`

method inside`MyModel`

module that returns the text embeddings given`input_ids`

. This is equivalent to directly calling the text embedding layer, but provides a unified interface in case`MyModel`

is used within a composite multimodal model.

class MyModel(nn.Module):
...
def embed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
...


- Rewrite the
[forward](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.forward)method of your model to remove any unnecessary code, such as training-specific code. Modify the input parameters to treat`input_ids`

and`positions`

as flattened tensors with a single batch size dimension, without a max-sequence length dimension.

def forward(
self,
input_ids: torch.Tensor | None,
positions: torch.Tensor,
intermediate_tensors: IntermediateTensors | None = None,
inputs_embeds: torch.Tensor | None = None,
) -> torch.Tensor:
...


Note

Currently, vLLM supports the basic multi-head attention mechanism and its variant with rotary positional embeddings. If your model employs a different attention mechanism, you will need to implement a new attention layer in vLLM.

For reference, check out our [ Llama implementation](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/llama.py). vLLM already supports a large number of models. It is recommended to find a model similar to yours and adapt it to your model's architecture. Check out [ vllm/model_executor/models](https://github.com/vllm-project/vllm/tree/main/vllm/model_executor/models) for more examples.

## 3. (Optional) Implement tensor parallelism and quantization support[¶](https://docs.vllm.ai#3-optional-implement-tensor-parallelism-and-quantization-support)

If your model is too large to fit into a single GPU, you can use tensor parallelism to manage it. To do this, substitute your model's linear and embedding layers with their tensor-parallel versions. For the embedding layer, you can simply replace [torch.nn.Embedding](https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html#torch.nn.Embedding) with [ VocabParallelEmbedding](https://docs.vllm.ai/api/vllm/model_executor/layers/vocab_parallel_embedding/#vllm.model_executor.layers.vocab_parallel_embedding.VocabParallelEmbedding). For the output LM head, you can use

[. When it comes to the linear layers, we provide the following options to parallelize them:](https://docs.vllm.ai/api/vllm/model_executor/layers/vocab_parallel_embedding/#vllm.model_executor.layers.vocab_parallel_embedding.ParallelLMHead)

`ParallelLMHead`

: Replicates the inputs and weights across multiple GPUs. No memory saving.`ReplicatedLinear`

: The input tensor is partitioned along the hidden dimension. The weight matrix is partitioned along the rows (input dimension). An`RowParallelLinear`

*all-reduce*operation is performed after the matrix multiplication to reduce the results. Typically used for the second FFN layer and the output linear transformation of the attention layer.: The input tensor is replicated. The weight matrix is partitioned along the columns (output dimension). The result is partitioned along the column dimension. Typically used for the first FFN layer and the separated QKV transformation of the attention layer in the original Transformer.`ColumnParallelLinear`

: Column-parallel linear that merges multiple`MergedColumnParallelLinear`

operators. Typically used for the first FFN layer with weighted activation functions (e.g., SiLU). This class handles the sharded weight loading logic of multiple weight matrices.`ColumnParallelLinear`

: Parallel linear layer for the query, key, and value projections of the multi-head and grouped-query attention mechanisms. When number of key/value heads are less than the world size, this class replicates the key/value heads properly. This class handles the weight loading and replication of the weight matrices.`QKVParallelLinear`


Note that all the linear layers above take `linear_method`

as an input. vLLM will set this parameter according to different quantization schemes to support weight quantization.

## 4. Implement the weight loading logic[¶](https://docs.vllm.ai#4-implement-the-weight-loading-logic)

You now need to implement the `load_weights`

method in your `*ForCausalLM`

class. This method should load the weights from the HuggingFace's checkpoint file and assign them to the corresponding layers in your model. Specifically, for [ MergedColumnParallelLinear](https://docs.vllm.ai/api/vllm/model_executor/layers/linear/#vllm.model_executor.layers.linear.MergedColumnParallelLinear) and

[layers, if the original model has separated weight matrices, you need to load the different parts separately.](https://docs.vllm.ai/api/vllm/model_executor/layers/linear/#vllm.model_executor.layers.linear.QKVParallelLinear)

`QKVParallelLinear`

## 5. Register your model[¶](https://docs.vllm.ai#5-register-your-model)

See [this page](https://docs.vllm.ai/registration/) for instructions on how to register your new model to be used by vLLM.

## Frequently Asked Questions[¶](https://docs.vllm.ai#frequently-asked-questions)

### How to support models with interleaving sliding windows?[¶](https://docs.vllm.ai#how-to-support-models-with-interleaving-sliding-windows)

To support a model with interleaving sliding windows, we need to take care of the following details:

- Make sure the model's
`config.json`

contains`layer_types`

. - In the modeling code, parse the correct sliding window value for every layer, and pass it to the attention layer's
`per_layer_sliding_window`

argument. For reference, check[this line](https://github.com/vllm-project/vllm/blob/996357e4808ca5eab97d4c97c7d25b3073f46aab/vllm/model_executor/models/llama.py#L171).

With these two steps, interleaved sliding windows should work with the model.

### How to support models that use Mamba?[¶](https://docs.vllm.ai#how-to-support-models-that-use-mamba)

We consider 3 different scenarios:

- Models that use Mamba layers (either Mamba-1 or Mamba-2) but do not use attention layers.
- Models that combine Mamba layers (either Mamba-1 or Mamba-2) together with attention layers.
- Models that combine Mamba-like mechanisms (e.g., Linear Attention, ShortConv) together with attention layers.

For case (1), we recommend looking at the implementation of [ MambaForCausalLM](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/mamba.py) (for Mamba-1) or

[(for Mamba-2) as a reference. The model should inherit protocol](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/mamba2.py)

`Mamba2ForCausalLM`

[and also implement class methods](https://docs.vllm.ai/api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.IsAttentionFree)

`IsAttentionFree`

`get_mamba_state_dtype_from_config`

and `get_mamba_state_shape_from_config`

to calculate the state shapes and data types from the config. For the mamba layers themselves, please use the [(for Mamba-1) or](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/mamba/mamba_mixer.py)

`MambaMixer`

[(for Mamba-2) classes. The model should also be added to the](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/mamba/mamba_mixer2.py)

`MambaMixer2`

`MODELS_CONFIG_MAP`

dictionary in [vllm/model_executor/models/config.py](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/config.py)to ensure that the runtime defaults are optimized.

For case (2), we recommend using as a reference the implementation of [ JambaForCausalLM](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/jamba.py) (for an example of a model that uses Mamba-1 and attention together) or

[(for an example of a model that uses Mamba-2 and attention together). These models should follow the same instructions as case (1), but they should inherit protocol](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/nemotron_h.py)

`NemotronHForCausalLM`

[(instead of](https://docs.vllm.ai/api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.IsHybrid)

`IsHybrid`

[) and it is](https://docs.vllm.ai/api/vllm/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.IsAttentionFree)

`IsAttentionFree`

*not*necessary to add them to the

`MODELS_CONFIG_MAP`

(their runtime defaults will be inferred from the protocol).For case (3), we recommend looking at the implementation of [ Lfm2ForCausalLM](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/lfm2.py) as a reference, which uses a custom "mamba-like" layer

`ShortConv`

. Please follow the same guidelines as case (2) for implementing these models. We use "mamba-like" to refer to layers that possess a state that is updated in-place, rather than being appended-to (like KV cache for attention). For implementing new custom mamba-like layers, one should inherit from [and implement the methods](https://docs.vllm.ai/api/vllm/model_executor/layers/mamba/abstract/#vllm.model_executor.layers.mamba.abstract.MambaBase)

`MambaBase`

`get_state_dtype`

, `get_state_shape`

to calculate the data types and state shapes at runtime, as well as `mamba_type`

and `get_attn_backend`

. It is also necessary to implement the "attention meta-data" class which handles the meta-data that is common across all layers. Please see [or](https://github.com/vllm-project/vllm/blob/main/vllm/v1/attention/backends/linear_attn.py)

`LinearAttentionMetadata`

[for examples of this. It is also worth noting that we should update](https://github.com/vllm-project/vllm/blob/main/vllm/v1/attention/backends/short_conv_attn.py)

`ShortConvAttentionMetadata`

[in](https://docs.vllm.ai/api/vllm/v1/attention/backends/registry/#vllm.v1.attention.backends.registry.MambaAttentionBackendEnum)

`MambaAttentionBackendEnum`

[when adding a new mamba backend. Finally, if one wants to support torch compile and CUDA graphs, it necessary to wrap the call to the mamba-like layer inside a custom op and register it. Please see the calls to](https://github.com/vllm-project/vllm/blob/main/vllm/v1/attention/backends/registry.py)

`registry.py`

`direct_register_custom_op`

in [vllm/model_executor/layers/mamba/linear/minimax_linear_attn.py](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/mamba/linear/minimax_linear_attn.py)or

[vllm/model_executor/layers/mamba/short_conv.py](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/mamba/short_conv.py)for examples of this. The new custom op should then be added to the list

`_attention_ops`

in [vllm/config/compilation.py](https://github.com/vllm-project/vllm/blob/main/vllm/config/compilation.py)to ensure that piecewise CUDA graphs works as intended.