source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/mamba/ops/causal_conv1d/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.mamba.ops.causal_conv1d`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.causal_conv1d)

Functions:

-
–[causal_conv1d_fn](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.causal_conv1d.causal_conv1d_fn)Support varlen + continuous batching when x is 2D tensor.

-
–[causal_conv1d_update](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.causal_conv1d.causal_conv1d_update)x: Input tensor which can take the following shapes:


##

`causal_conv1d_fn(x, weight, bias, conv_states, query_start_loc, cache_indices=None, has_initial_state=None, activation='silu', pad_slot_id=PAD_SLOT_ID, null_block_id=NULL_BLOCK_ID, block_idx_first_scheduled_token=None, block_idx_last_scheduled_token=None, initial_state_idx=None, num_computed_tokens=None, block_size_to_align=0, metadata=None, validate_data=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.causal_conv1d.causal_conv1d_fn)

Support varlen + continuous batching when x is 2D tensor.

## (dim,cu_seq_len)

cu_seq_len = total tokens of all seqs in that batch sequences are concatenated from left to right for varlen

weight: (dim, width) conv_states: (...,dim,width - 1) itype updated inplace if cache_indices are not provided [it use `cache_indices`

to get the index to the cache of conv_state for that sequence

```
conv_state[cache_indices[i]] for seq-i - to be used as initial_state when has_initial_state[i] = True
and after that conv_state[cache_indices[i]] need to be shift-left and updated with values from 'x'
]
```


query_start_loc: (batch + 1) int32 The cumulative sequence lengths of the sequences in the batch, used to index into sequence. prepended by 0. if x = [5, 1, 1, 1] <- continuous batching (batch=4) then query_start_loc = [0, 5, 6, 7, 8] <- the starting index of the next sequence; while the last value is the ending index of the last sequence [length(query_start_loc)-1 == batch] for example: query_start_loc = torch.Tensor([0,10,16,17]), x.shape=(dim,17) cache_indices: (batch) int32 indicates the corresponding state index, like so: conv_state = conv_states[cache_indices[batch_id]] has_initial_state: (batch) bool indicates whether should the kernel take the current state as initial state for the calculations [single boolean for each sequence in the batch: True or False] bias: (dim,) activation: either None or "silu" or "swish" or True pad_slot_id: int if cache_indices is passed, lets the kernel identify padded entries that will not be processed, for example: cache_indices = [pad_slot_id, 1, 20, pad_slot_id] in this case, the kernel will not process entries at indices 0 and 3 block_idx_first_scheduled_token: (batch,), dtype int32 The pointer into cache_indices, where the first cache block to be filled is located. block_idx_last_scheduled_token: (batch,), dtype int32 The pointer into cache_indices, where the last cache block to be filled is located. initial_state_idx: (batch,), dtype int32 The pointer into cache_indices, where the cache block containing the initial state is located. num_computed_tokens: (batch,), dtype int32 The number of tokens already completed for each sequence block_size_to_align: int The block size to align the cached states to out: same shape as `x`


## Source code in `vllm/model_executor/layers/mamba/ops/causal_conv1d.py`


|
|

##

`causal_conv1d_update(x, conv_state, weight, bias=None, activation=None, conv_state_indices=None, num_accepted_tokens=None, query_start_loc=None, max_query_len=-1, null_block_id=NULL_BLOCK_ID, block_idx_last_scheduled_token=None, initial_state_idx=None, validate_data=False, out=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.causal_conv1d.causal_conv1d_update)

x: Input tensor which can take the following shapes:

`[batch, dim]`

- single token prediction`[batch, dim, seqlen]`

- single or multiple tokens prediction`[num_tokens, dim]`

- continuous batching, where num_tokens is the total tokens of all sequences in that batch

conv_state: (..., dim, state_len), where state_len >= width - 1 weight: (dim, width) bias: (dim,) conv_state_indices: (batch,), dtype int32 If not None, the conv_state is a larger tensor along the batch dim, and we are selecting the batch coords specified by conv_state_indices. Useful for a continuous batching scenario. block_idx_last_scheduled_token: (batch,), dtype int32 The pointer into conv_state_indices, where the last cache block to be filled is located. initial_state_idx: (batch,), dtype int32 The pointer into conv_state_indices, where the cache block containing the initial state is located. num_accepted_tokens: (batch,), dtype int32 If not None, it indicates the number of accepted tokens for each sequence in the batch. This is used in speculative decoding, where the conv_state is updated in a sliding window manner. query_start_loc: (batch + 1,) int32 If not None, the inputs is given in a varlen fashion and this indicates the starting index of each sequence in the batch. max_query_len: int If query_start_loc is not None, this indicates the maximum query length in the batch. null_block_id: int Block ID used to identify padded entries in conv_state_indices. Block 0 is the null block. for example: conv_state_indices = [null_block_id, 1, 20, null_block_id] in this case, the kernel will not process entries at indices 0 and 3 out: optional output tensor with the same shape as `x`

. When omitted, the input is overwritten.

## Source code in `vllm/model_executor/layers/mamba/ops/causal_conv1d.py`


|
|