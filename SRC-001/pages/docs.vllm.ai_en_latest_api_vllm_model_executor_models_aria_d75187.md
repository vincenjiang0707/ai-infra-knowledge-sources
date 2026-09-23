source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/aria/
lastmod: 2026-09-23

#

`vllm.model_executor.models.aria`

[¶](https://docs.vllm.ai#vllm.model_executor.models.aria)

Classes:

-
–[AriaForConditionalGeneration](https://docs.vllm.ai#vllm.model_executor.models.aria.AriaForConditionalGeneration)Aria model for conditional generation tasks.

-
–[AriaImagePixelInputs](https://docs.vllm.ai#vllm.model_executor.models.aria.AriaImagePixelInputs)Dimensions:

-
–[AriaProjector](https://docs.vllm.ai#vllm.model_executor.models.aria.AriaProjector)A projection module with one cross attention layer and one FFN layer, which

-
–[AriaTextDecoderLayer](https://docs.vllm.ai#vllm.model_executor.models.aria.AriaTextDecoderLayer)Custom Decoder Layer for the AriaMoE model which modifies the standard

-
–[AriaTextMoELayer](https://docs.vllm.ai#vllm.model_executor.models.aria.AriaTextMoELayer)Mixture of Experts (MoE) Layer for the AriaMoE model.

-
–[AriaTextModel](https://docs.vllm.ai#vllm.model_executor.models.aria.AriaTextModel)Custom LlamaModel for the AriaMoE model which modifies the standard


##

`AriaForConditionalGeneration`

[¶](https://docs.vllm.ai#vllm.model_executor.models.aria.AriaForConditionalGeneration)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)[SupportsMultiModal](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal)

Aria model for conditional generation tasks.

This model combines a vision tower, a multi-modal projector, and a language model to perform tasks that involve both image and text inputs.

## Source code in `vllm/model_executor/models/aria.py`


|
|

##

`AriaImagePixelInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.aria.AriaImagePixelInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - b: Batch size - n: Number of images - c: Number of channels - h: Height of each image - w: Width of each image

## Source code in `vllm/model_executor/models/aria.py`


##

`AriaProjector`

[¶](https://docs.vllm.ai#vllm.model_executor.models.aria.AriaProjector)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

A projection module with one cross attention layer and one FFN layer, which projects ViT's outputs into MoE's inputs.

Parameters:

-

(`config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.aria.AriaProjector(config))`AriaConfig`

) –[AriaConfig](https://huggingface.co/docs/transformers/main/model_doc/aria#transformers.AriaConfig)containing projector configuration parameters.

## Outputs

A tensor with the shape of (batch_size, query_number, output_dim)

## Source code in `vllm/model_executor/models/aria.py`


##

`AriaTextDecoderLayer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.aria.AriaTextDecoderLayer)

Bases: [LlamaDecoderLayer](https://docs.vllm.ai/llama/#vllm.model_executor.models.llama.LlamaDecoderLayer)

Custom Decoder Layer for the AriaMoE model which modifies the standard `LlamaDecoderLayer`

by replacing the traditional MLP with a Mixture of Experts (MoE) Layer.

## Source code in `vllm/model_executor/models/aria.py`


##

`AriaTextMoELayer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.aria.AriaTextMoELayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Mixture of Experts (MoE) Layer for the AriaMoE model.

This layer implements the MoE mechanism, which routes input tokens to different experts based on a routing algorithm, processes them through the experts, and then combines the outputs.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.aria.AriaTextMoELayer.forward)Forward pass of the MoE Layer.


## Source code in `vllm/model_executor/models/aria.py`


###

`forward(hidden_states)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.aria.AriaTextMoELayer.forward)

Forward pass of the MoE Layer.

Parameters:

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)torch.Tensor: Output tensor after passing through the MoE layer.


## Source code in `vllm/model_executor/models/aria.py`


##

`AriaTextModel`

[¶](https://docs.vllm.ai#vllm.model_executor.models.aria.AriaTextModel)

Bases: `LlamaModel`

, [SupportsQuant](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsQuant)

Custom LlamaModel for the AriaMoE model which modifies the standard LlamaModel by replacing the `LlamaDecoderLayer`

with `MoEDecoderLayer`

.