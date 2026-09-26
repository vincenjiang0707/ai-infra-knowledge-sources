source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/mamba/mamba_utils/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.mamba.mamba_utils`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.mamba_utils)

Classes:

-
–[MambaCopySpec](https://docs.vllm.ai#vllm.model_executor.layers.mamba.mamba_utils.MambaCopySpec)Data class specifying the memory-copy parameters for Mamba states used for

-
–[MambaStateDtypeCalculator](https://docs.vllm.ai#vllm.model_executor.layers.mamba.mamba_utils.MambaStateDtypeCalculator) -
–[MambaStateShapeCalculator](https://docs.vllm.ai#vllm.model_executor.layers.mamba.mamba_utils.MambaStateShapeCalculator)

Functions:

-
–[get_conv_copy_spec](https://docs.vllm.ai#vllm.model_executor.layers.mamba.mamba_utils.get_conv_copy_spec)Return a MambaCopySpec for copying a convolutional state slice.

-
–[get_conv_state_layout](https://docs.vllm.ai#vllm.model_executor.layers.mamba.mamba_utils.get_conv_state_layout)Return the SSM conv state layout.

-
–[get_temporal_copy_spec](https://docs.vllm.ai#vllm.model_executor.layers.mamba.mamba_utils.get_temporal_copy_spec)Return a MambaCopySpec for copying a temporal state slice.

-
–[is_conv_state_dim_first](https://docs.vllm.ai#vllm.model_executor.layers.mamba.mamba_utils.is_conv_state_dim_first)True when the conv state is stored as (dim, state_len) per block.


Attributes:

-
([MambaStateCopyFunc](https://docs.vllm.ai#vllm.model_executor.layers.mamba.mamba_utils.MambaStateCopyFunc)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)Type alias for a function that computes a MambaCopySpec for copying state slices.


##

`MambaStateCopyFunc = Callable[[torch.Tensor, list[int], int, int], MambaCopySpec]`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.mamba_utils.MambaStateCopyFunc)

Type alias for a function that computes a MambaCopySpec for copying state slices. Parameters: state: torch.Tensor - the Mamba state tensor (e.g., conv or temporal states). block_ids: list[int] - the list of block indices for the state to copy. cur_block_idx: int - current block index within `block_ids`

to copy from. num_accepted_tokens: int - number of accepted tokens used to compute the copy offset. Range: 1 .. 1 + num_speculative_tokens (inclusive).

##

`MambaCopySpec`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.mamba_utils.MambaCopySpec)

Data class specifying the memory-copy parameters for Mamba states used for prefix caching in align mode.

Attributes:

-
(`start_addr`


) –[int](https://docs.python.org/3/builtins/functions.html#int)Starting address for the memory copy operation.

-
(`num_elements`


) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of elements to copy from the starting address.


## Source code in `vllm/model_executor/layers/mamba/mamba_utils.py`


##

`MambaStateDtypeCalculator`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.mamba_utils.MambaStateDtypeCalculator)

Methods:

-
–[append_replayssm_ring](https://docs.vllm.ai#vllm.model_executor.layers.mamba.mamba_utils.MambaStateDtypeCalculator.append_replayssm_ring)Append the ReplaySSM ring dtypes to a base

`(conv, ssm)`

tuple:

## Source code in `vllm/model_executor/layers/mamba/mamba_utils.py`


|
|

###

`append_replayssm_ring(base_dtypes, model_dtype)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.mamba_utils.MambaStateDtypeCalculator.append_replayssm_ring)

Append the ReplaySSM ring dtypes to a base `(conv, ssm)`

tuple: `(x_cache, dt_cache, B_cache)`

= `(activation, fp32, activation)`

.

## Source code in `vllm/model_executor/layers/mamba/mamba_utils.py`


##

`MambaStateShapeCalculator`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.mamba_utils.MambaStateShapeCalculator)

Methods:

-
–[append_replayssm_ring](https://docs.vllm.ai#vllm.model_executor.layers.mamba.mamba_utils.MambaStateShapeCalculator.append_replayssm_ring)Append the physical ReplaySSM ring shapes.

-
–[extra_groups_for_head_shards](https://docs.vllm.ai#vllm.model_executor.layers.mamba.mamba_utils.MambaStateShapeCalculator.extra_groups_for_head_shards)Compute the increase in group numbers to account for


## Source code in `vllm/model_executor/layers/mamba/mamba_utils.py`


|
|

###

`_orient_conv_shape(dim, state_len)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.mamba_utils.MambaStateShapeCalculator._orient_conv_shape)

Return (dim, state_len) for DS layout, (state_len, dim) for SD.

## Source code in `vllm/model_executor/layers/mamba/mamba_utils.py`


###

`append_replayssm_ring(base_shapes, n_groups, tp_world_size, logical_window, backend)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.mamba_utils.MambaStateShapeCalculator.append_replayssm_ring)

Append the physical ReplaySSM ring shapes.

`base_shapes[1]`

is `(nheads // tp, head_dim, state_size)`

; B_cache uses the un-extended `n_groups`

.

## Source code in `vllm/model_executor/layers/mamba/mamba_utils.py`


###

`extra_groups_for_head_shards(ngroups, tp_size)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.mamba_utils.MambaStateShapeCalculator.extra_groups_for_head_shards)

Compute the increase in group numbers to account for replication in order to accompany the head shards.

## Source code in `vllm/model_executor/layers/mamba/mamba_utils.py`


##

`get_conv_copy_spec(state, block_ids, cur_block_idx, num_accepted_tokens)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.mamba_utils.get_conv_copy_spec)

Return a MambaCopySpec for copying a convolutional state slice.

Works for both SD layout `(num_blocks, state_len, dim)`

and DS layout `(num_blocks, dim, state_len)`

.

## Source code in `vllm/model_executor/layers/mamba/mamba_utils.py`


##

`get_conv_state_layout()`

`cached`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.mamba_utils.get_conv_state_layout)

Return the SSM conv state layout.

SD = (state_len, dim) — dim is the innermost contiguous dimension. DS = (dim, state_len) — TP-sharded dim is on dim-1 (like HND for KV cache), consistent with SSM temporal state layout.

## Source code in `vllm/model_executor/layers/mamba/mamba_utils.py`


##

`get_temporal_copy_spec(state, block_ids, cur_block_idx, num_accepted_tokens)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.mamba_utils.get_temporal_copy_spec)

Return a MambaCopySpec for copying a temporal state slice.