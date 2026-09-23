source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/mimo_v2_omni/
lastmod: 2026-09-23

#

`vllm.model_executor.models.mimo_v2_omni`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni)

Classes:

-
–[MiMoV2OmniForCausalLM](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoV2OmniForCausalLM) -
–[MiMoV2OmniMultiModalProcessor](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoV2OmniMultiModalProcessor)vLLM multimodal processor for MiMo-Omni (image + video).

-
–[MiMoVisionAttention](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoVisionAttention) -
–[MiMoVisionTransformer](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoVisionTransformer)

##

`MiMoV2OmniForCausalLM`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoV2OmniForCausalLM)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsMultiModal](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal)

, [SupportsPP](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsPP)

, [SupportsQuant](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsQuant)[SupportsEagle3](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsEagle3)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoV2OmniForCausalLM.forward)Run forward pass for Qwen2.5-VL.


## Source code in `vllm/model_executor/models/mimo_v2_omni.py`


|
|

###

`forward(input_ids, positions, intermediate_tensors=None, inputs_embeds=None, **kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoV2OmniForCausalLM.forward)

Run forward pass for Qwen2.5-VL.

Parameters:

-

(`input_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoV2OmniForCausalLM.forward(input_ids))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NoneFlattened (concatenated) input_ids corresponding to a batch.

-

(`positions`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoV2OmniForCausalLM.forward(positions))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Flattened (concatenated) position ids corresponding to a batch.

**NOTE**: If mrope is enabled (default setting for Qwen2.5-VL opensource models), the shape will be`(3, seq_len)`

, otherwise it will be `(seq_len,). -

(`intermediate_tensors`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoV2OmniForCausalLM.forward(intermediate_tensors))

, default:[IntermediateTensors](https://docs.vllm.ai/sequence/#vllm.sequence.IntermediateTensors)| None`None`

) –Intermediate tensors from prior forward pass.

-

(`inputs_embeds`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoV2OmniForCausalLM.forward(inputs_embeds))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional tensor of input embeddings.


## Source code in `vllm/model_executor/models/mimo_v2_omni.py`


##

`MiMoV2OmniMultiModalProcessor`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoV2OmniMultiModalProcessor)

Bases: [BaseMultiModalProcessor](https://docs.vllm.ai/multimodal/processing/#vllm.multimodal.processing.BaseMultiModalProcessor)[MiMoV2OmniProcessingInfo]

vLLM multimodal processor for MiMo-Omni (image + video).

Key differences from Qwen2.5-VL: - Videos use timestamp tokens between temporal grid positions. - The HF processor expects `(TCHW_tensor, timestamps_T_tensor)`

video tuples rather than plain numpy arrays. - `video_start_times`

is tracked so prompt-update reconstruction can regenerate the exact same timestamp token IDs.

## Source code in `vllm/model_executor/models/mimo_v2_omni.py`


|
|

###

`_get_hf_mm_inputs(mm_items, hf_kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoV2OmniMultiModalProcessor._get_hf_mm_inputs)

Convert numpy video arrays to (TCHW, timestamps) tuples for MiMo.

## Source code in `vllm/model_executor/models/mimo_v2_omni.py`


|
|

##

`MiMoVisionAttention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoVisionAttention)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoVisionAttention.forward)Args:


## Source code in `vllm/model_executor/models/mimo_v2_omni.py`


|
|

###

`_forward_window_attn(q, k, v, cu_seqlens, max_seqlen)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoVisionAttention._forward_window_attn)

Window attention with the per-head sink applied to key 0.

The reference adds `sinks[h]`

to the logit of each sequence's first key, which the Triton prefill kernel supports directly, so the softmax normalizes over the biased scores in one pass.

## Source code in `vllm/model_executor/models/mimo_v2_omni.py`


###

`forward(x, cu_seqlens, rotary_pos_emb_cos, rotary_pos_emb_sin, max_seqlen, full_attn=True)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoVisionAttention.forward)

Args: x: [seq_len, batch=1, embed_dim] (seq-first convention) cu_seqlens: cumulative sequence lengths [num_seqs+1], int32 rotary_pos_emb_cos: [seq_len, qk_channels // 2] rotary_pos_emb_sin: [seq_len, qk_channels // 2] max_seqlen: maximum sequence length full_attn: if True, full attention; if False, window attention

## Source code in `vllm/model_executor/models/mimo_v2_omni.py`


|
|

##

`MiMoVisionTransformer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoVisionTransformer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[apply_index](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoVisionTransformer.apply_index)Reindex tensor at the spatial_merge_unit granularity.

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoVisionTransformer.forward)Args:

-
–[get_window_index_1d](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoVisionTransformer.get_window_index_1d)Compute 1D window indices for col-based or row-based SWA reordering.

-
–[rot_pos_emb](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoVisionTransformer.rot_pos_emb)Compute 2D rotary position embedding cos/sin for given grid sizes.


## Source code in `vllm/model_executor/models/mimo_v2_omni.py`


|
|

###

`apply_index(tensor, index)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoVisionTransformer.apply_index)

Reindex tensor at the spatial_merge_unit granularity.

## Source code in `vllm/model_executor/models/mimo_v2_omni.py`


###

`forward(x, grid_thw)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoVisionTransformer.forward)

Parameters:

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoVisionTransformer.forward(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[total_tokens, C] pre-flattened patches

-

(`grid_thw`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoVisionTransformer.forward(grid_thw))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[num_images, 3] tensor of (t, h, w) for each image/video


Returns: [merged_tokens, out_hidden_size]

## Source code in `vllm/model_executor/models/mimo_v2_omni.py`


|
|

###

`get_window_index_1d(grid_thw, col=True)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoVisionTransformer.get_window_index_1d)

Compute 1D window indices for col-based or row-based SWA reordering.

## Source code in `vllm/model_executor/models/mimo_v2_omni.py`


###

`rot_pos_emb(grid_thw)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.mimo_v2_omni.MiMoVisionTransformer.rot_pos_emb)

Compute 2D rotary position embedding cos/sin for given grid sizes.

Returns: