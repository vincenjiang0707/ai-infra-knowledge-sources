source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/interfaces/
lastmod: 2026-09-23

#

`vllm.model_executor.models.interfaces`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces)

Classes:

-
–[DiarizedTranscriptionSegment](https://docs.vllm.ai#vllm.model_executor.models.interfaces.DiarizedTranscriptionSegment)A timestamped, speaker-attributed segment produced by an ASR model.

-
–[HasInnerState](https://docs.vllm.ai#vllm.model_executor.models.interfaces.HasInnerState)The interface required for all models that has inner state.

-
–[IsAttentionFree](https://docs.vllm.ai#vllm.model_executor.models.interfaces.IsAttentionFree)The interface required for all models like Mamba that lack attention,

-
–[IsHybrid](https://docs.vllm.ai#vllm.model_executor.models.interfaces.IsHybrid)The interface required for all models like Jamba that have both

-
–[LocalArgmaxMixin](https://docs.vllm.ai#vllm.model_executor.models.interfaces.LocalArgmaxMixin)Mixin for draft model heads in speculative decoding.

-
–[MixtureOfExperts](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts)Check if the model is a mixture of experts (MoE) model.

-
–[StreamingTranscriptionPostProcessor](https://docs.vllm.ai#vllm.model_executor.models.interfaces.StreamingTranscriptionPostProcessor)Stateful streaming post-processor for transcription deltas.

-
–[SupportsCrossEncoding](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsCrossEncoding)The interface required for all models that support cross encoding.

-
–[SupportsEagle](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEagle)The interface required for models that support

-
–[SupportsEagle3](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEagle3)The interface required for models that support

-
–[SupportsEagleBase](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEagleBase)Base interface for models that support EAGLE-based speculative decoding.

-
–[SupportsEncoderCudaGraph](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph)Interface for models whose vision encoder supports CUDA graph

-
–[SupportsLateInteraction](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsLateInteraction)The interface required for all models that support late interaction.

-
–[SupportsLoRA](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsLoRA)The interface required for all models that support LoRA.

-
–[SupportsMRoPE](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMRoPE)The interface required for all models that support M-RoPE.

-
–[SupportsMambaPrefixCaching](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMambaPrefixCaching)The interface for models whose mamba layers support prefix caching.

-
–[SupportsMultiModal](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal)The interface required for all multi-modal models.

-
–[SupportsMultiModalEmbeddings](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModalEmbeddings)The interface for models that can merge external multimodal embeddings.

-
–[SupportsMultiModalPruning](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModalPruning)The interface required for models that support returning both input

-
–[SupportsPP](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsPP)The interface required for all models that support pipeline parallel.

-
–[SupportsQuant](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsQuant)The interface required for all models that support quantization.

-
–[SupportsRealtime](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsRealtime)The interface required for all models that support transcription.

-
–[SupportsReplaySSM](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsReplaySSM)The interface for models whose recurrent layers support ReplaySSM

-
–[SupportsScoreTemplate](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsScoreTemplate)The interface required for all models that support score template.

-
–[SupportsTranscription](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription)The interface required for all models that support transcription.


Functions:

-
–[get_mixture_of_experts_model](https://docs.vllm.ai#vllm.model_executor.models.interfaces.get_mixture_of_experts_model)Return the MixtureOfExperts contained within an arbitrary model.

-
–[supports_any_eagle](https://docs.vllm.ai#vllm.model_executor.models.interfaces.supports_any_eagle)Check if model supports any EAGLE variant (1, 2, or 3).


Attributes:

-
([MultiModalEmbeddings](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MultiModalEmbeddings)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)The output embeddings must be one of the following formats:


##

`MultiModalEmbeddings = list[Tensor] | Tensor | tuple[Tensor, ...]`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MultiModalEmbeddings)

The output embeddings must be one of the following formats:

- A list or tuple of 2D tensors, where each tensor corresponds to each input multimodal data item (e.g, image).
- A single 3D tensor, with the batch dimension grouping the 2D tensors.

##

`DiarizedTranscriptionSegment`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.DiarizedTranscriptionSegment)

A timestamped, speaker-attributed segment produced by an ASR model.

## Source code in `vllm/model_executor/models/interfaces.py`


##

`HasInnerState`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.HasInnerState)

Bases: [Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

The interface required for all models that has inner state.

Attributes:

-
([has_inner_state](https://docs.vllm.ai#vllm.model_executor.models.interfaces.HasInnerState.has_inner_state)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)[True]A flag that indicates this model has inner state.


## Source code in `vllm/model_executor/models/interfaces.py`


###

`has_inner_state = True`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.HasInnerState.has_inner_state)

A flag that indicates this model has inner state. Models that has inner state usually need access to the scheduler_config for max_num_seqs, etc. True for e.g. both Mamba and Jamba.

##

`IsAttentionFree`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.IsAttentionFree)

Bases: [Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

The interface required for all models like Mamba that lack attention, but do have state whose size is constant wrt the number of tokens.

Attributes:

-
([is_attention_free](https://docs.vllm.ai#vllm.model_executor.models.interfaces.IsAttentionFree.is_attention_free)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)[True]A flag that indicates this model has no attention.


## Source code in `vllm/model_executor/models/interfaces.py`


###

`is_attention_free = True`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.IsAttentionFree.is_attention_free)

A flag that indicates this model has no attention. Used for block manager and attention backend selection. True for Mamba but not Jamba.

##

`IsHybrid`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.IsHybrid)

Bases: [Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

The interface required for all models like Jamba that have both attention and mamba blocks, indicates that hf_config has 'layers_block_type'

Methods:

-
–[get_mamba_state_copy_func](https://docs.vllm.ai#vllm.model_executor.models.interfaces.IsHybrid.get_mamba_state_copy_func)Calculate copy-function callables for each Mamba state.

-
–[get_mamba_state_shape_from_config](https://docs.vllm.ai#vllm.model_executor.models.interfaces.IsHybrid.get_mamba_state_shape_from_config)Calculate shapes for Mamba's convolutional and state caches.


Attributes:

## Source code in `vllm/model_executor/models/interfaces.py`


###

`is_hybrid = True`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.IsHybrid.is_hybrid)

A flag that indicates this model has both mamba and attention blocks , also indicates that the model's hf_config has 'layers_block_type'

###

`get_mamba_state_copy_func()`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.IsHybrid.get_mamba_state_copy_func)

Calculate copy-function callables for each Mamba state.

Returns:

-

–[MambaStateCopyFunc](https://docs.vllm.ai/layers/mamba/mamba_utils/#vllm.model_executor.layers.mamba.mamba_utils.MambaStateCopyFunc)A tuple of MambaStateCopyFunc callables that correspond, in order,

-
`...`

–to the Mamba states produced by the model. Each callable accepts

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[MambaStateCopyFunc](https://docs.vllm.ai/layers/mamba/mamba_utils/#vllm.model_executor.layers.mamba.mamba_utils.MambaStateCopyFunc), ...](state, block_ids, cur_block_idx, num_accepted_tokens) and returns

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[MambaStateCopyFunc](https://docs.vllm.ai/layers/mamba/mamba_utils/#vllm.model_executor.layers.mamba.mamba_utils.MambaStateCopyFunc), ...]a MambaCopySpec describing the memory-copy parameters for prefix

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[MambaStateCopyFunc](https://docs.vllm.ai/layers/mamba/mamba_utils/#vllm.model_executor.layers.mamba.mamba_utils.MambaStateCopyFunc), ...]caching in align mode.


## Source code in `vllm/model_executor/models/interfaces.py`


###

`get_mamba_state_shape_from_config(vllm_config)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.IsHybrid.get_mamba_state_shape_from_config)

Calculate shapes for Mamba's convolutional and state caches.

Parameters:

-

(`vllm_config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.IsHybrid.get_mamba_state_shape_from_config(vllm_config))

) –[VllmConfig](https://docs.vllm.ai/config/#vllm.config.VllmConfig)vLLM config


Returns:

-
`MambaStateShapes`

–Shapes for each state cache used by the model.


## Source code in `vllm/model_executor/models/interfaces.py`


##

`LocalArgmaxMixin`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.LocalArgmaxMixin)

Mixin for draft model heads in speculative decoding.

Provides a D2T-aware `get_top_tokens`

that preserves the local-argmax communication reduction even when the draft vocabulary is smaller than the target vocabulary.

When `draft_id_to_target_id`

is present (shape `(draft_vocab_size,)`

, containing per-token offset to target vocab id), the draft argmax index `k`

is mapped to the target vocab id via::

```
target_id = k + draft_id_to_target_id[k]
```


This is mathematically equivalent to computing the full-vocab scatter logits and taking the global argmax, but requires only O(batch * 2 * tp_size) communication instead of O(batch * vocab_size).

## Requires the subclass to expose

`self.logits_processor`

: LogitsProcessor `self.lm_head`

: ParallelLMHead `self.draft_id_to_target_id`

(optional): nn.Parameter

Methods:

-
–[get_top_tokens](https://docs.vllm.ai#vllm.model_executor.models.interfaces.LocalArgmaxMixin.get_top_tokens)Vocab-parallel argmax with optional D2T remapping.


## Source code in `vllm/model_executor/models/interfaces.py`


###

`get_top_tokens(hidden_states)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.LocalArgmaxMixin.get_top_tokens)

Vocab-parallel argmax with optional D2T remapping.

## Source code in `vllm/model_executor/models/interfaces.py`


##

`MixtureOfExperts`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts)

Bases: [Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

Check if the model is a mixture of experts (MoE) model.

Methods:

-
–[set_eplb_state](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts.set_eplb_state)Register the EPLB state in the MoE model.


Attributes:

-
([expert_weights](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts.expert_weights)

) –[MutableSequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSequence)[[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]]Expert weights saved in this rank.

-
([moe_layers](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts.moe_layers)

) –[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[MoERunner](https://docs.vllm.ai/layers/fused_moe/#vllm.model_executor.layers.fused_moe.MoERunner)]List of MoE layers in this model.

-
([num_expert_groups](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts.num_expert_groups)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of expert groups in this model.

-
([num_local_physical_experts](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts.num_local_physical_experts)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of local physical experts in this model.

-
([num_logical_experts](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts.num_logical_experts)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of logical experts in this model.

-
([num_moe_layers](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts.num_moe_layers)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of MoE layers in this model.

-
([num_physical_experts](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts.num_physical_experts)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of physical experts in this model.

-
([num_redundant_experts](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts.num_redundant_experts)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of redundant experts in this model.

-
([num_routed_experts](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts.num_routed_experts)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of routed experts in this model.

-
([num_shared_experts](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts.num_shared_experts)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of shared experts in this model.


## Source code in `vllm/model_executor/models/interfaces.py`


|
|

###

`expert_weights`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts.expert_weights)

Expert weights saved in this rank.

The first dimension is the layer, and the second dimension is different parameters in the layer, e.g. up/down projection weights.

###

`moe_layers`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts.moe_layers)

List of MoE layers in this model.

###

`num_expert_groups`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts.num_expert_groups)

Number of expert groups in this model.

###

`num_local_physical_experts`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts.num_local_physical_experts)

Number of local physical experts in this model.

###

`num_logical_experts`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts.num_logical_experts)

Number of logical experts in this model.

###

`num_moe_layers`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts.num_moe_layers)

Number of MoE layers in this model.

###

`num_physical_experts`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts.num_physical_experts)

Number of physical experts in this model.

###

`num_redundant_experts`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts.num_redundant_experts)

Number of redundant experts in this model.

###

`num_routed_experts`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts.num_routed_experts)

Number of routed experts in this model.

###

`num_shared_experts`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts.num_shared_experts)

Number of shared experts in this model.

###

`set_eplb_state(expert_load_view, logical_to_physical_map, logical_replica_count)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts.set_eplb_state)

Register the EPLB state in the MoE model.

Since these are views of the actual EPLB state, any changes made by the EPLB algorithm are automatically reflected in the model's behavior without requiring additional method calls to set new states.

You should also collect model's `expert_weights`

here instead of in the weight loader, since after initial weight loading, further processing like quantization may be applied to the weights.

Parameters:

-

(`expert_load_view`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts.set_eplb_state(expert_load_view))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)A view of the expert load metrics tensor.

-

(`logical_to_physical_map`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts.set_eplb_state(logical_to_physical_map))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Mapping from logical to physical experts.

-

(`logical_replica_count`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts.set_eplb_state(logical_replica_count))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Count of replicas for each logical expert.


## Source code in `vllm/model_executor/models/interfaces.py`


##

`StreamingTranscriptionPostProcessor`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.StreamingTranscriptionPostProcessor)

Stateful streaming post-processor for transcription deltas.

## Source code in `vllm/model_executor/models/interfaces.py`


##

`SupportsCrossEncoding`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsCrossEncoding)

Bases: [Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

The interface required for all models that support cross encoding.

## Source code in `vllm/model_executor/models/interfaces.py`


##

`SupportsEagle`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEagle)

Bases:

, [SupportsEagleBase](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEagleBase)[Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

The interface required for models that support EAGLE-1 and EAGLE-2 speculative decoding.

Attributes:

-
([supports_eagle](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEagle.supports_eagle)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)[True]A flag that indicates this model supports EAGLE-1 and EAGLE-2


## Source code in `vllm/model_executor/models/interfaces.py`


###

`supports_eagle = True`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEagle.supports_eagle)

A flag that indicates this model supports EAGLE-1 and EAGLE-2 speculative decoding.

## Note

There is no need to redefine this flag if this class is in the MRO of your model class.

##

`SupportsEagle3`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEagle3)

Bases:

, [SupportsEagleBase](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEagleBase)[Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

The interface required for models that support EAGLE-3 speculative decoding.

Methods:

-
–[get_eagle3_default_aux_hidden_state_layers](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEagle3.get_eagle3_default_aux_hidden_state_layers)Get the default layer indices that should output auxiliary hidden states

-
–[set_aux_hidden_state_layers](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEagle3.set_aux_hidden_state_layers)Set which layers should output auxiliary hidden states for EAGLE-3.


Attributes:

-
([supports_eagle3](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEagle3.supports_eagle3)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)[True]A flag that indicates this model supports EAGLE-3


## Source code in `vllm/model_executor/models/interfaces.py`


###

`supports_eagle3 = True`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEagle3.supports_eagle3)

A flag that indicates this model supports EAGLE-3 speculative decoding.

## Note

There is no need to redefine this flag if this class is in the MRO of your model class.

###

`get_eagle3_default_aux_hidden_state_layers()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEagle3.get_eagle3_default_aux_hidden_state_layers)

Get the default layer indices that should output auxiliary hidden states for EAGLE-3 for this model. Models can override this method to provide different default layers based on their architecture, but it is encouraged to instead include the layer specification in the model's config if possible.

Returns:

## Source code in `vllm/model_executor/models/interfaces.py`


###

`set_aux_hidden_state_layers(layers)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEagle3.set_aux_hidden_state_layers)

Set which layers should output auxiliary hidden states for EAGLE-3.

Parameters:

## Source code in `vllm/model_executor/models/interfaces.py`


##

`SupportsEagleBase`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEagleBase)

Bases: [Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

Base interface for models that support EAGLE-based speculative decoding.

Attributes:

-
([has_own_embed_tokens](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEagleBase.has_own_embed_tokens)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)A flag that indicates this model has trained its own input embeddings.

-
([has_own_lm_head](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEagleBase.has_own_lm_head)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)A flag that indicates this model has trained its own lm_head.


## Source code in `vllm/model_executor/models/interfaces.py`


##

`SupportsEncoderCudaGraph`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph)

Bases: [Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

Interface for models whose vision encoder supports CUDA graph capture/replay.

Models implement these methods to provide the :class:`EncoderCudaGraphManager`

with all model-specific logic (input handling, metadata computation, forward pass) without the manager needing to know model internals.

Methods:

-
–[encoder_cudagraph_forward](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.encoder_cudagraph_forward)Run the encoder forward pass with precomputed buffers.

-
–[encoder_eager_forward](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.encoder_eager_forward)Run the encoder forward pass without precomputed buffers.

-
–[get_encoder_cudagraph_budget_range](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.get_encoder_cudagraph_budget_range)Return (min_token_budget, max_token_budget) for auto-inference.

-
–[get_encoder_cudagraph_item_specs](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.get_encoder_cudagraph_item_specs)Return specs describing each item in the batch.

-
–[get_input_modality](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.get_input_modality)Return the modality of the inputs (default: image-only).

-
–[get_max_frames_per_video](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.get_max_frames_per_video)Return model-specific max frames per video.

-
–[postprocess_encoder_output](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.postprocess_encoder_output)Post-process encoder output, directly call scatter_output_slices by default.

-
–[prepare_encoder_cudagraph_capture_inputs](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.prepare_encoder_cudagraph_capture_inputs)Create dummy inputs and buffers for CUDA graph capture.

-
–[prepare_encoder_cudagraph_replay_buffers](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.prepare_encoder_cudagraph_replay_buffers)Compute buffer values from actual batch inputs for replay.

-
–[select_encoder_cudagraph_items](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.select_encoder_cudagraph_items)Select a subset of items and return mm_kwargs for the sub-batch.


## Source code in `vllm/model_executor/models/interfaces.py`


|
|

###

`encoder_cudagraph_forward(inputs, path='default')`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.encoder_cudagraph_forward)

Run the encoder forward pass with precomputed buffers.

Used during both CUDA graph capture and replay.

## Source code in `vllm/model_executor/models/interfaces.py`


###

`encoder_eager_forward(mm_kwargs, path='default')`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.encoder_eager_forward)

Run the encoder forward pass without precomputed buffers.

Used as eager fallback when inputs exceed all budgets.

## Source code in `vllm/model_executor/models/interfaces.py`


###

`get_encoder_cudagraph_budget_range(vllm_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.get_encoder_cudagraph_budget_range)

Return (min_token_budget, max_token_budget) for auto-inference.

- min_token_budget: estimated smallest possible encoder input (e.g. 64 for a 224x224 image)
- max_token_budget: estimated largest budget worth capturing (e.g. max_num_batched_tokens)

Used when `encoder_cudagraph_token_budgets`

and/or `encoder_cudagraph_max_vision_items_per_batch`

are not explicitly specified by the user.

## Source code in `vllm/model_executor/models/interfaces.py`


###

`get_encoder_cudagraph_item_specs(mm_kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.get_encoder_cudagraph_item_specs)

Return specs describing each item in the batch.

Replaces the former separate methods for num_items, per_item_output_tokens, and per_item_input_sizes. The manager derives all three from this single return value.

## Source code in `vllm/model_executor/models/interfaces.py`


###

`get_input_modality(mm_kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.get_input_modality)

###

`get_max_frames_per_video()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.get_max_frames_per_video)

###

`postprocess_encoder_output(outputs, indices, per_item_out_tokens, dest, clone=False, batch_mm_kwargs=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.postprocess_encoder_output)

Post-process encoder output, directly call scatter_output_slices by default.

By default, delegates directly to scatter_output_slices. Override this for models that require additional processing on the raw encoder output prior to scattering, e.g. Step3-VL, which merges features according to dynamic patch counts before scattering.

## Source code in `vllm/model_executor/models/interfaces.py`


###

`prepare_encoder_cudagraph_capture_inputs(token_budget, max_batch_size, max_frames_per_batch, device, dtype, path='default', axis_keys=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.prepare_encoder_cudagraph_capture_inputs)

Create dummy inputs and buffers for CUDA graph capture.

Parameters:

-

(`token_budget`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.prepare_encoder_cudagraph_capture_inputs(token_budget))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Token budget the capture is sized for.

-

(`max_batch_size`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.prepare_encoder_cudagraph_capture_inputs(max_batch_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum number of items in a captured batch.

-

(`max_frames_per_batch`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.prepare_encoder_cudagraph_capture_inputs(max_frames_per_batch))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum number of frames in a captured batch.

-

(`device`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.prepare_encoder_cudagraph_capture_inputs(device))

) –[device](https://pytorch.org/docs/stable/tensor_attributes.html#torch.device)Device the dummy inputs and buffers are created on.

-

(`dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.prepare_encoder_cudagraph_capture_inputs(dtype))

) –[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)Dtype of the dummy inputs and buffers.

-

(`path`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.prepare_encoder_cudagraph_capture_inputs(path))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'default'`

) –Configured encoder path.

-

(`axis_keys`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.prepare_encoder_cudagraph_capture_inputs(axis_keys))

, default:[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Hashable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable), ...] | None`None`

) –The resolved capture-axis keys (one per axis of

`EncoderCudaGraphConfig.capture_axes`

) this capture is for. None or empty when no capture axes are configured; models without capture axes ignore it.

## Source code in `vllm/model_executor/models/interfaces.py`


###

`prepare_encoder_cudagraph_replay_buffers(mm_kwargs, max_batch_size, max_frames_per_batch, path='default')`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.prepare_encoder_cudagraph_replay_buffers)

Compute buffer values from actual batch inputs for replay.

## Source code in `vllm/model_executor/models/interfaces.py`


###

`select_encoder_cudagraph_items(mm_kwargs, indices)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsEncoderCudaGraph.select_encoder_cudagraph_items)

Select a subset of items and return mm_kwargs for the sub-batch.

Called by the manager during greedy packing and DP sharding to extract inputs for a specific set of items (e.g. images at indices [0, 3, 5]). The implementation is model-specific because input formats differ:

- Qwen-family: slice concatenated pixel_values by cumulative patch offsets, subset grid_thw by indices.
- Batched models (CLIP): index pixel_values along dim 0.

Models that configure `EncoderCudaGraphConfig.capture_axes`

must additionally store the resolved per-axis keys (one key per axis, in order) under `ENCODER_CUDAGRAPH_AXIS_KEYS_KWARG`

in the returned dict; the manager pops it before the kwargs are used elsewhere.

## Source code in `vllm/model_executor/models/interfaces.py`


##

`SupportsLateInteraction`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsLateInteraction)

Bases: [Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

The interface required for all models that support late interaction.

Late interaction models (like ColBERT) encode queries and documents separately into per-token embeddings, then compute similarity via MaxSim (max over document tokens, sum over query tokens).

## Source code in `vllm/model_executor/models/interfaces.py`


##

`SupportsLoRA`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsLoRA)

Bases: [Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

The interface required for all models that support LoRA.

Attributes:

-
([supports_lora](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsLoRA.supports_lora)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)[True]A flag that indicates this model supports LoRA.


## Source code in `vllm/model_executor/models/interfaces.py`


###

`supports_lora = True`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsLoRA.supports_lora)

A flag that indicates this model supports LoRA.

## Note

There is no need to redefine this flag if this class is in the MRO of your model class.

##

`SupportsMRoPE`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMRoPE)

Bases: [Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

The interface required for all models that support M-RoPE.

Methods:

-
–[get_mrope_input_positions](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMRoPE.get_mrope_input_positions)Get M-RoPE input positions and delta value for this specific model.


Attributes:

-
([supports_mrope](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMRoPE.supports_mrope)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)[True]A flag that indicates this model supports M-RoPE.


## Source code in `vllm/model_executor/models/interfaces.py`


###

`supports_mrope = True`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMRoPE.supports_mrope)

A flag that indicates this model supports M-RoPE.

## Note

There is no need to redefine this flag if this class is in the MRO of your model class.

###

`get_mrope_input_positions(input_tokens, mm_features)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMRoPE.get_mrope_input_positions)

Get M-RoPE input positions and delta value for this specific model.

This method should be implemented by each model that supports M-RoPE to provide model-specific logic for computing input positions.

Parameters:

-

(`input_tokens`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMRoPE.get_mrope_input_positions(input_tokens))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]List of input token IDs

-

(`mm_features`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMRoPE.get_mrope_input_positions(mm_features))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[MultiModalFeatureSpec](https://docs.vllm.ai/multimodal/inputs/#vllm.multimodal.inputs.MultiModalFeatureSpec)]Information about each multi-modal data item


Returns:

-
(`llm_positions`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Tensor of shape

`[num_dims, num_tokens]`

, one row per M-RoPE position channel (e.g. T/H/W). -
(`mrope_position_delta`


) –[int](https://docs.python.org/3/builtins/functions.html#int)Delta for position calculations.


## Source code in `vllm/model_executor/models/interfaces.py`


##

`SupportsMambaPrefixCaching`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMambaPrefixCaching)

Bases: [Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

The interface for models whose mamba layers support prefix caching.

This is currently experimental.

Methods:

-
–[get_mamba_state_copy_func](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMambaPrefixCaching.get_mamba_state_copy_func)Return copy functions for the model's Mamba states.

-
–[get_mamba_state_copy_funcs](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMambaPrefixCaching.get_mamba_state_copy_funcs)Map legacy copy functions to each requested Mamba backend.


## Source code in `vllm/model_executor/models/interfaces.py`


###

`get_mamba_state_copy_func()`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMambaPrefixCaching.get_mamba_state_copy_func)

###

`get_mamba_state_copy_funcs(mamba_types)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMambaPrefixCaching.get_mamba_state_copy_funcs)

Map legacy copy functions to each requested Mamba backend.

## Source code in `vllm/model_executor/models/interfaces.py`


##

`SupportsMultiModal`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal)

Bases:

, [SupportsMultiModalEmbeddings](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModalEmbeddings)[Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

The interface required for all multi-modal models.

Methods:

-
–[configure_mm_token_handling](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal.configure_mm_token_handling)Check if any multimodal tokens are out of vocabulary. If so, we will

-
–[embed_input_ids](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal.embed_input_ids)Apply token embeddings to

`input_ids`

. -
–[embed_multimodal](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal.embed_multimodal)Returns multimodal embeddings generated from multimodal kwargs

-
–[get_language_model](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal.get_language_model)Returns the underlying language model used for text generation.

-
–[get_mm_lora_token_counts](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal.get_mm_lora_token_counts)Return

`(tower_tokens, connector_tokens)`

for multimodal LoRA mappings. -
–[get_placeholder_str](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal.get_placeholder_str)Get the placeholder text for the

`i`

th`modality`

item in the prompt.

Attributes:

-
([requires_raw_input_tokens](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal.requires_raw_input_tokens)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)A flag that indicates this model processes input id tokens

-
([supports_encoder_tp_data](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal.supports_encoder_tp_data)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)A flag that indicates whether this model supports

-
([supports_mm_device_do_normalize](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal.supports_mm_device_do_normalize)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)A flag that indicates whether this model supports

-
([supports_multimodal](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal.supports_multimodal)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)[True]A flag that indicates this model supports multi-modal inputs.

-
([supports_multimodal_raw_input_only](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal.supports_multimodal_raw_input_only)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)A flag that indicates this model supports multi-modal inputs and processes

-
([supports_tower_connector_lora](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal.supports_tower_connector_lora)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)A flag that indicates whether this model supports


## Source code in `vllm/model_executor/models/interfaces.py`


|
|

###

`_has_oov_mm_tokens = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal._has_oov_mm_tokens)

In general, this should be set at init time by invoking `configure_mm_token_handling`

models & passing all potentially OOV multimodal tokens.

###

`_language_model_names = []`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal._language_model_names)

Set internally by `_mark_language_model`

.

###

`_processor_factory`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal._processor_factory)

Set internally by `MultiModalRegistry.register_processor`

.

###

`_tower_model_names = []`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal._tower_model_names)

Set internally by `_mark_tower_model`

.

###

`requires_raw_input_tokens = False`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal.requires_raw_input_tokens)

A flag that indicates this model processes input id tokens in their raw form and not input embeddings.

###

`supports_encoder_tp_data = False`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal.supports_encoder_tp_data)

A flag that indicates whether this model supports `multimodal_config.mm_encoder_tp_mode="data"`

.

###

`supports_mm_device_do_normalize = False`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal.supports_mm_device_do_normalize)

A flag that indicates whether this model supports `multimodal_config.mm_device_do_normalize`

.

###

`supports_multimodal = True`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal.supports_multimodal)

A flag that indicates this model supports multi-modal inputs.

## Note

There is no need to redefine this flag if this class is in the MRO of your model class.

###

`supports_multimodal_raw_input_only = False`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal.supports_multimodal_raw_input_only)

A flag that indicates this model supports multi-modal inputs and processes them in their raw form and not embeddings.

###

`supports_tower_connector_lora = False`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal.supports_tower_connector_lora)

A flag that indicates whether this model supports `lora_config.enable_tower_connector_lora`

.

###

`_mark_composite_model(vllm_config, *, language_targets, tower_targets)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal._mark_composite_model)

Composite wrapper over `_mark_language_model`

and `_mark_tower_model`

by modality.

## Source code in `vllm/model_executor/models/interfaces.py`


###

`_mark_language_model(vllm_config, *, targets=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal._mark_language_model)

Mark each child module that was assigned to this model during this context as a language model component.

Language model components are automatically skipped in `--mm-encoder-only`

mode.

If `targets`

is set, instead include descendants that are an instance of `targets`

, even if they aren't direct children.

## Source code in `vllm/model_executor/models/interfaces.py`


###

`_mark_tower_model(vllm_config, modalities, *, targets=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal._mark_tower_model)

Mark each child module that was assigned to this model during this context as a tower model component.

Tower model components are automatically skipped when `--limit-mm-per-prompt`

is set to zero for all of their modalities.

If `targets`

is set, instead include descendants that are an instance of `targets`

, even if they aren't direct children.

Marked components are also routed through the active offloader (when it supports tower offloading), since `make_layers`

only ever sees the decoder layer stack.

## Source code in `vllm/model_executor/models/interfaces.py`


###

`configure_mm_token_handling(vocab_size, mm_token_ids)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal.configure_mm_token_handling)

Check if any multimodal tokens are out of vocabulary. If so, we will explicitly mask all multimodal tokens out when computing text embeddings, since the multimodal embeddings will be scattered over the results.

## Source code in `vllm/model_executor/models/interfaces.py`


###

`embed_input_ids(input_ids, multimodal_embeddings=None, *, is_multimodal=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal.embed_input_ids)

Apply token embeddings to `input_ids`

.

If `multimodal_embeddings`

is passed, scatter them into `input_ids`

according to the mask `is_multimodal`

.

NOTE: If this model has multimodal tokens that are of vocabulary (i.e., self._has_oov_mm_tokens=True), the input_ids will be copied and masked to 0 during the forward pass for the text embeddings.

## Source code in `vllm/model_executor/models/interfaces.py`


###

`embed_multimodal(**kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal.embed_multimodal)

Returns multimodal embeddings generated from multimodal kwargs to be merged with text embeddings.

## Note

The returned multimodal embeddings must be in the same order as the appearances of their corresponding multimodal data item in the input prompt.

## Source code in `vllm/model_executor/models/interfaces.py`


###

`get_language_model()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal.get_language_model)

Returns the underlying language model used for text generation.

This is typically the `torch.nn.Module`

instance responsible for processing the merged multimodal embeddings and producing hidden states

Returns:

-

–[VllmModel](https://docs.vllm.ai/interfaces_base/#vllm.model_executor.models.interfaces_base.VllmModel)torch.nn.Module: The core language model component.


## Source code in `vllm/model_executor/models/interfaces.py`


###

`get_mm_lora_token_counts(*, modality, mm_kwargs, num_mm_embeds)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal.get_mm_lora_token_counts)

Return `(tower_tokens, connector_tokens)`

for multimodal LoRA mappings.

MM LoRA uses these counts to build adapter mappings for the tower and connector forwards. Models with multiple modalities can override this when each modality has different encoder padding or pooling behavior.

## Source code in `vllm/model_executor/models/interfaces.py`


###

`get_placeholder_str(modality, i)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal.get_placeholder_str)

##

`SupportsMultiModalEmbeddings`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModalEmbeddings)

Bases: [Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

The interface for models that can merge external multimodal embeddings.

## Source code in `vllm/model_executor/models/interfaces.py`


##

`SupportsMultiModalPruning`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModalPruning)

Bases: [Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

The interface required for models that support returning both input embeddings and positions. Model may require custom positions for dynamic pruning of multimodal embeddings.

Methods:

-
–[recompute_mrope_positions](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModalPruning.recompute_mrope_positions)Update part of input mrope positions (starting with


Attributes:

-
([supported_video_pruning_methods](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModalPruning.supported_video_pruning_methods)

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[VideoPruningMethod, ...]Video pruning methods (as reported by


## Source code in `vllm/model_executor/models/interfaces.py`


###

`supported_video_pruning_methods = ('evs',)`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModalPruning.supported_video_pruning_methods)

Video pruning methods (as reported by `MultiModalConfig.get_video_pruning_spec`

) implemented by this model. Models supporting methods beyond EVS should override this.

###

`recompute_mrope_positions(input_ids, multimodal_embeddings, mrope_positions, num_computed_tokens)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModalPruning.recompute_mrope_positions)

Update part of input mrope positions (starting with num_computed_tokens index). Original mrope_positions are computed for unpruned sequence and becomes incorrect once pruning occurs, so once we prune media tokens we should reflect this in the mrope_positions before we feed it to LLM.

Parameters:

-

(`input_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModalPruning.recompute_mrope_positions(input_ids))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] |[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(N,) All input tokens of the prompt containing entire sequence. Either a host-side list or an already device-resident tensor.

-

(`multimodal_embeddings`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModalPruning.recompute_mrope_positions(multimodal_embeddings))

) –[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]Sequence of multimodal embeddings that fits into the prefill chunk that is being processed.

-

(`mrope_positions`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModalPruning.recompute_mrope_positions(mrope_positions))`LongTensor`

) –Existing mrope positions (3, N) for entire sequence

-

(`num_computed_tokens`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModalPruning.recompute_mrope_positions(num_computed_tokens))

) –[int](https://docs.python.org/3/builtins/functions.html#int)A number of computed tokens so far.


Returns:

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)],[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[int](https://docs.python.org/3/builtins/functions.html#int)]Tuple of (multimodal_embeddings, mrope_positions, mrope_position_delta).


## Source code in `vllm/model_executor/models/interfaces.py`


##

`SupportsPP`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsPP)

Bases: [Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

The interface required for all models that support pipeline parallel.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsPP.forward)Accept

when`IntermediateTensors`


Attributes:

-
([make_empty_intermediate_tensors](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsPP.make_empty_intermediate_tensors)`_MakeEmptyIntermediateTensors`

) –Called when PP rank > 0 for profiling purposes.

-
([supports_pp](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsPP.supports_pp)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)[True]A flag that indicates this model supports pipeline parallel.


## Source code in `vllm/model_executor/models/interfaces.py`


###

`make_empty_intermediate_tensors`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsPP.make_empty_intermediate_tensors)

Called when PP rank > 0 for profiling purposes.

###

`supports_pp = True`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsPP.supports_pp)

A flag that indicates this model supports pipeline parallel.

## Note

There is no need to redefine this flag if this class is in the MRO of your model class.

###

`forward(input_ids, positions, *, intermediate_tensors)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsPP.forward)

Accept [ IntermediateTensors](https://docs.vllm.ai/sequence/#vllm.sequence.IntermediateTensors) when PP rank > 0.

Return [ IntermediateTensors](https://docs.vllm.ai/sequence/#vllm.sequence.IntermediateTensors) only for the last PP rank.

## Source code in `vllm/model_executor/models/interfaces.py`


##

`SupportsQuant`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsQuant)

The interface required for all models that support quantization.

## Source code in `vllm/model_executor/models/interfaces.py`


###

`_find_quant_config(*args, **kwargs)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsQuant._find_quant_config)

Find quant config passed through model constructor args

## Source code in `vllm/model_executor/models/interfaces.py`


###

`_maybe_apply_model_mapping()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsQuant._maybe_apply_model_mapping)

Apply model mappings to config for proper config-model matching

## Source code in `vllm/model_executor/models/interfaces.py`


##

`SupportsRealtime`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsRealtime)

Bases: [Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

The interface required for all models that support transcription.

Attributes:

-
([realtime_max_tokens](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsRealtime.realtime_max_tokens)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum tokens to generate per streaming audio segment.


## Source code in `vllm/model_executor/models/interfaces.py`


###

`realtime_max_tokens = 1`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsRealtime.realtime_max_tokens)

Maximum tokens to generate per streaming audio segment. Override in subclasses based on the model's expected output length.

##

`SupportsReplaySSM`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsReplaySSM)

Bases: [Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

The interface for models whose recurrent layers support ReplaySSM cached decode.

This is currently experimental.

## Source code in `vllm/model_executor/models/interfaces.py`


##

`SupportsScoreTemplate`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsScoreTemplate)

Bases: [Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

The interface required for all models that support score template.

Methods:

-
–[get_score_template](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsScoreTemplate.get_score_template)Generate a full prompt by populating the score template with query and document content.

-
–[post_process_tokens](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsScoreTemplate.post_process_tokens)Perform architecture-specific manipulations on the input tokens.


Attributes:

-
([supports_score_template](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsScoreTemplate.supports_score_template)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)[True]A flag that indicates this model supports score template.


## Source code in `vllm/model_executor/models/interfaces.py`


###

`supports_score_template = True`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsScoreTemplate.supports_score_template)

A flag that indicates this model supports score template.

## Note

There is no need to redefine this flag if this class is in the MRO of your model class.

###

`get_score_template(query, document)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsScoreTemplate.get_score_template)

Generate a full prompt by populating the score template with query and document content.

###

`post_process_tokens(prompt)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsScoreTemplate.post_process_tokens)

##

`SupportsTranscription`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription)

Bases: [Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

The interface required for all models that support transcription.

Methods:

-
–[get_generation_prompt](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.get_generation_prompt)Get the prompt for the ASR model.

-
–[get_language_detection_prompt](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.get_language_detection_prompt)Return a prompt that triggers language detection.

-
–[get_language_token_ids](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.get_language_token_ids)Return token IDs that represent valid language tokens.

-
–[get_num_audio_tokens](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.get_num_audio_tokens)Map from audio duration to number of audio tokens produced by the ASR

-
–[get_speech_to_text_config](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.get_speech_to_text_config)Get the speech to text config for the ASR model.

-
–[get_streaming_post_processor_cls](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.get_streaming_post_processor_cls)Return a stateful post-processor class for streaming output deltas.

-
–[parse_diarized_transcript](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.parse_diarized_transcript)Parse the model-specific diarized transcript format.

-
–[parse_language_detection_output](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.parse_language_detection_output)Parse the detected language from model output token IDs.

-
–[post_process_output](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.post_process_output)Post-process the raw model output text.

-
–[validate_language](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.validate_language)Ensure the language specified in the transcription request


Attributes:

-
([no_space_languages](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.no_space_languages)

) –[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Languages that don't need a space between words.

-
([supports_diarized_transcription](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.supports_diarized_transcription)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enables the

`diarized_json`

response format for the model. -
([supports_explicit_language_detection](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.supports_explicit_language_detection)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Transcription models that require an explicit language detection step

-
([supports_segment_timestamp](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.supports_segment_timestamp)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enables the segment timestamp option for supported models by setting this to

`True`

. -
([supports_transcription_only](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.supports_transcription_only)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Transcription models can opt out of text generation by setting this to


## Source code in `vllm/model_executor/models/interfaces.py`


|
|

###

`no_space_languages = {'ja', 'zh'}`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.no_space_languages)

Languages that don't need a space between words. For example, Japanese (ja) and Chinese (zh) don't need a space between words.

###

`supports_diarized_transcription = False`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.supports_diarized_transcription)

Enables the `diarized_json`

response format for the model.

###

`supports_explicit_language_detection = False`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.supports_explicit_language_detection)

Transcription models that require an explicit language detection step (e.g. Whisper needs a separate forward pass to predict the language token) should set this to `True`

and implement :meth:`get_language_detection_prompt`

and :meth:`parse_language_detection_output`

and :meth:`get_language_token_ids`

.

###

`supports_segment_timestamp = False`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.supports_segment_timestamp)

Enables the segment timestamp option for supported models by setting this to `True`

.

###

`supports_transcription_only = False`

`class-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.supports_transcription_only)

Transcription models can opt out of text generation by setting this to `True`

.

###

`get_generation_prompt(stt_params)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.get_generation_prompt)

Get the prompt for the ASR model. The model has control over the construction, as long as it returns a valid PromptType.

## Source code in `vllm/model_executor/models/interfaces.py`


###

`get_language_detection_prompt(audio, stt_config)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.get_language_detection_prompt)

Return a prompt that triggers language detection.

Only needs to be implemented when `supports_explicit_language_detection`

is `True`

.

## Source code in `vllm/model_executor/models/interfaces.py`


###

`get_language_token_ids(tokenizer)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.get_language_token_ids)

Return token IDs that represent valid language tokens.

Used to constrain language detection to only produce valid language tokens.

Only needs to be implemented when `supports_explicit_language_detection`

is `True`

.

## Source code in `vllm/model_executor/models/interfaces.py`


###

`get_num_audio_tokens(audio_duration_s, stt_config, model_config)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.get_num_audio_tokens)

Map from audio duration to number of audio tokens produced by the ASR model, without running a forward pass. This is used for estimating the amount of processing for this audio.

## Source code in `vllm/model_executor/models/interfaces.py`


###

`get_speech_to_text_config(model_config, task_type)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.get_speech_to_text_config)

Get the speech to text config for the ASR model.

###

`get_streaming_post_processor_cls()`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.get_streaming_post_processor_cls)

Return a stateful post-processor class for streaming output deltas.

Each instance receives the next decoded text delta and whether the request output is final. It returns the cleaned delta that should be sent to the client.

## Source code in `vllm/model_executor/models/interfaces.py`


###

`parse_diarized_transcript(text)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.parse_diarized_transcript)

Parse the model-specific diarized transcript format.

Only models that set `supports_diarized_transcription`

must override this method.

## Source code in `vllm/model_executor/models/interfaces.py`


###

`parse_language_detection_output(token_ids, tokenizer)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.parse_language_detection_output)

Parse the detected language from model output token IDs.

Only needs to be implemented when `supports_explicit_language_detection`

is `True`

.

## Source code in `vllm/model_executor/models/interfaces.py`


###

`post_process_output(text)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.post_process_output)

Post-process the raw model output text.

Some ASR models output structured formats (e.g., language tags, special tokens) that need to be stripped before returning to the user.

Parameters:

Returns:

-

–[str](https://docs.python.org/3/builtins/stdtypes.html#str)Cleaned transcription text.


## Source code in `vllm/model_executor/models/interfaces.py`


###

`validate_language(language)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsTranscription.validate_language)

Ensure the language specified in the transcription request is a valid ISO 639-1 language code. If the request language is valid, but not natively supported by the model, trigger a warning (but not an exception).

## Source code in `vllm/model_executor/models/interfaces.py`


##

`_require_is_multimodal(is_multimodal)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces._require_is_multimodal)

A helper function to be used in the context of [vllm.model_executor.models.interfaces.SupportsMultiModal.embed_input_ids](https://docs.vllm.ai#vllm.model_executor.models.interfaces.SupportsMultiModal.embed_input_ids) to provide a better error message.

## Source code in `vllm/model_executor/models/interfaces.py`


##

`get_mixture_of_experts_model(model)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.get_mixture_of_experts_model)

Return the MixtureOfExperts contained within an arbitrary model.

- If the model itself is a MixtureOfExperts, return the model directly.
- If the model is a multi-modal model, and its
`language_model`

is a MixtureOfExperts, return the`language_model`

. - If neither, return None.

Parameters:

Returns:

-

–[MixtureOfExperts](https://docs.vllm.ai#vllm.model_executor.models.interfaces.MixtureOfExperts)| NoneThe MixtureOfExperts instance contained within the model, or None.


## Source code in `vllm/model_executor/models/interfaces.py`


##

`supports_any_eagle(model)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.interfaces.supports_any_eagle)

Check if model supports any EAGLE variant (1, 2, or 3).