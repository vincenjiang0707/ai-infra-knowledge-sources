source: https://docs.vllm.ai/en/latest/api/vllm/lora/punica_wrapper/utils/
lastmod: 2026-09-24

#

`vllm.lora.punica_wrapper.utils`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.utils)

Functions:

-
–[compute_meta](https://docs.vllm.ai#vllm.lora.punica_wrapper.utils.compute_meta)Get the information required for the sgmv kernel. With the features:

-
–[convert_mapping](https://docs.vllm.ai#vllm.lora.punica_wrapper.utils.convert_mapping)Converts LoRAMapping to index tensors.


##

`compute_meta(token_lora_tensor)`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.utils.compute_meta)

Get the information required for the sgmv kernel. With the features: 1. If consecutive requests in the batch use the same LoRA, this function will combine them into a single request, improving sgmv kernel inference performance. 2. At the beginning of each prefill stage inference, recalculations are needed based on the input, but only once.

## Source code in `vllm/lora/punica_wrapper/utils.py`


##

`convert_mapping(mapping, lora_index_to_id, max_loras, vocab_size, device)`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.utils.convert_mapping)

Converts LoRAMapping to index tensors.

Parameters:

-

(`mapping`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.utils.convert_mapping(mapping))`LoRAMapping`

) –LoRAMapping mapping rows in a batch to LoRA ids.

-

(`lora_index_to_id`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.utils.convert_mapping(lora_index_to_id))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)| None]List mapping LoRA ids to LoRA indices.

-

(`max_loras`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.utils.convert_mapping(max_loras))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum number of LoRAs.

-

(`vocab_size`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.utils.convert_mapping(vocab_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Model vocab size.

-

(`device`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.utils.convert_mapping(device))

) –[device](https://pytorch.org/docs/stable/tensor_attributes.html#torch.device)Device the returned index tensors are created on.


Returns:

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]A tuple of tensors: base_indices: Tensor of shape [batch_size] mapping batch rows to LoRA indices. sampler_indices: Tensor of shape [batch_size] mapping requests to LoRA indices for sampler. For generation, this will be the same as base_indices. For prefill, this will map requests to LoRA indices. sampler_indices_padded: Tensor of shape [batch_size] mapping requests to LoRA indices for sampler with padding. Same as sampler_indices, but -1 is replaced with max_loras. embeddings_indices: Tensor of shape [batch_size] mapping requests to the row offset of their LoRA.lora_a embeddings. indices_len: List of lengths of the above tensors. It contains (base_indices, sampler_indices, sampler_indices_padded, embeddings_indices).


## Source code in `vllm/lora/punica_wrapper/utils.py`


|
|