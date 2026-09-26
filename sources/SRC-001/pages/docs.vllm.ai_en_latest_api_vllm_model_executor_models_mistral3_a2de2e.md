source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/mistral3/
lastmod: 2026-09-24

#

`vllm.model_executor.models.mistral3`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mistral3)

Classes:

-
–[Mistral3ForConditionalGeneration](https://docs.vllm.ai#vllm.model_executor.models.mistral3.Mistral3ForConditionalGeneration) -
–[Mistral3ImagePixelInputs](https://docs.vllm.ai#vllm.model_executor.models.mistral3.Mistral3ImagePixelInputs)Dimensions:

-
–[Mistral3PatchMerger](https://docs.vllm.ai#vllm.model_executor.models.mistral3.Mistral3PatchMerger)Learned merging of spatial_merge_size ** 2 patches.


##

`Mistral3ForConditionalGeneration`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mistral3.Mistral3ForConditionalGeneration)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsLoRA](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsLoRA)

, [SupportsMultiModal](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal)

, [SupportsPP](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsPP)

, [SupportsEagle](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsEagle)[SupportsEagle3](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsEagle3)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.mistral3.Mistral3ForConditionalGeneration.forward)Run forward pass for Mistral3.

-
–[get_mm_mapping](https://docs.vllm.ai#vllm.model_executor.models.mistral3.Mistral3ForConditionalGeneration.get_mm_mapping)Get the module prefix in multimodal models.


## Source code in `vllm/model_executor/models/mistral3.py`


|
|

###

`forward(input_ids, positions, intermediate_tensors=None, inputs_embeds=None, **kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mistral3.Mistral3ForConditionalGeneration.forward)

Run forward pass for Mistral3.

One key thing to understand is the `input_ids`

already accounts for the positions of the to-be-inserted image embeddings.

Concretely, consider a text prompt: `"USER: <image>\nWhat's the content of the image?\nASSISTANT:"`

.

Tokenizer outputs: `[1, 3148, 1001, 29901, 29871, 32000, 29871, 13, 5618, 29915, 29879, 278, 2793, 310, 278, 1967, 29973, 13, 22933, 9047, 13566, 29901]`

.

To reserve space in KV cache, we have to insert placeholder tokens before they are inputted to the model, so the input processor prepends additional image tokens (denoted as `32000`

), resulting in: `[1, 3148, 1001, 29901, 29871, 32000, ..., 32000, 29871, 13, 5618, 29915, 29879, 278, 2793, 310, 278, 1967, 29973, 13, 22933, 9047, 13566, 29901]`

.

We insert 575 tokens so that including the original image token in the input, there are a total of 576 (24 * 24) image tokens, which corresponds to the number of image tokens inputted to the language model, i.e. the number of image tokens outputted by the visual encoder.

This way, the `positions`

and `attn_metadata`

are consistent with the `input_ids`

.

Parameters:

-

(`input_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mistral3.Mistral3ForConditionalGeneration.forward(input_ids))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NoneFlattened (concatenated) input_ids corresponding to a batch.

-

(`positions`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mistral3.Mistral3ForConditionalGeneration.forward(positions))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Position indices for the input tokens.

-

(`intermediate_tensors`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mistral3.Mistral3ForConditionalGeneration.forward(intermediate_tensors))

, default:[IntermediateTensors](https://docs.vllm.ai/sequence/#vllm.sequence.IntermediateTensors)| None`None`

) –Intermediate tensors from prior forward pass.

-

(`inputs_embeds`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mistral3.Mistral3ForConditionalGeneration.forward(inputs_embeds))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional tensor of input embeddings.

-

(`**kwargs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mistral3.Mistral3ForConditionalGeneration.forward(**kwargs))

, default:[object](https://docs.python.org/3/builtins/functions.html#object)`{}`

) –Multimodal inputs for this batch, forwarded to the multimodal embedding path.


## Source code in `vllm/model_executor/models/mistral3.py`


###

`get_mm_mapping()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mistral3.Mistral3ForConditionalGeneration.get_mm_mapping)

Get the module prefix in multimodal models.

## Source code in `vllm/model_executor/models/mistral3.py`


##

`Mistral3ImagePixelInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mistral3.Mistral3ImagePixelInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - bn: Batch size * number of images - c: Number of channels (3) - h: Height of each image - w: Width of each image

## Source code in `vllm/model_executor/models/mistral3.py`


##

`Mistral3PatchMerger`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mistral3.Mistral3PatchMerger)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Learned merging of spatial_merge_size ** 2 patches.

## Source code in `vllm/model_executor/models/mistral3.py`


##

`_get_num_hidden_layers(hf_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mistral3._get_num_hidden_layers)

Determine the number of hidden layers to initialize up to in the visual encoder.

Parameters:

-

(`hf_config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mistral3._get_num_hidden_layers(hf_config))`Mistral3Config`

) –Model config with vision feature layer(s).