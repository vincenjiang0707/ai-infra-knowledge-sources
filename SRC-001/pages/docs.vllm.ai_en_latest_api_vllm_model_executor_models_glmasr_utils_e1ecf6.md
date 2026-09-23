source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/glmasr_utils/
lastmod: 2026-09-23

#

`vllm.model_executor.models.glmasr_utils`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr_utils)

##

`_calculate_conv_output_length(input_length, padding, kernel_size, stride)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr_utils._calculate_conv_output_length)

Calculate Conv1d output length using standard formula.

## Source code in `vllm/model_executor/models/glmasr_utils.py`


##

`_get_audio_output_lengths_for_tower(audio_tower, audio_lengths, merge_factor, conv_params)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr_utils._get_audio_output_lengths_for_tower)

Calculate the output lengths after audio processing.

The output length accounts for: 1. Convolution layers (downsampling) 2. Merge factor (further downsampling during projection)

Parameters:

-

(`audio_tower`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr_utils._get_audio_output_lengths_for_tower(audio_tower))

) –[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)The audio encoder module

-

(`audio_lengths`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr_utils._get_audio_output_lengths_for_tower(audio_lengths))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input feature lengths [batch_size]

-

(`merge_factor`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr_utils._get_audio_output_lengths_for_tower(merge_factor))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Factor for merging adjacent features

-

(`conv_params`

[¶](https://docs.vllm.ai#vllm.model_executor.models.glmasr_utils._get_audio_output_lengths_for_tower(conv_params))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)]]List of (padding, kernel_size, stride) for each conv layer


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output lengths after all processing [batch_size]