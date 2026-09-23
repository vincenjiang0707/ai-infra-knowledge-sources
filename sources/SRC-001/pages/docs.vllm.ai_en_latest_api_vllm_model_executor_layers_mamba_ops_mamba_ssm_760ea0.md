source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/mamba/ops/mamba_ssm/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.mamba.ops.mamba_ssm`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.mamba_ssm)

Functions:

-
–[get_ssm_config_file_name](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.mamba_ssm.get_ssm_config_file_name)Return the JSON filename for the given kernel shape.

-
–[get_ssm_configs](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.mamba_ssm.get_ssm_configs)Return tuned (BLOCK_SIZE_M, num_warps) configs for

*selective_state_update* -
–[override_ssm_config](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.mamba_ssm.override_ssm_config)Pin

`try_get_optimal_ssm_config`

to`config`

for the duration of -
–[selective_scan_fn](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.mamba_ssm.selective_scan_fn)u: (dim, total_length) for varlen or (batch, dim, seqlen)

-
–[selective_state_update](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.mamba_ssm.selective_state_update)Argument:

-
–[try_get_optimal_ssm_config](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.mamba_ssm.try_get_optimal_ssm_config)Return (BLOCK_SIZE_M, num_warps) for the given kernel shape.


##

`_canonical_cache_dtype(cache_dtype)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.mamba_ssm._canonical_cache_dtype)

Canonical key for config lookup. bf16 and fp16 share the same tuned configs because the kernel only sees bit width when accessing state.

## Source code in `vllm/model_executor/layers/mamba/ops/mamba_ssm.py`


##

`_get_default_ssm_launch_config(dstate, is_blackwell)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.mamba_ssm._get_default_ssm_launch_config)

Hard-coded fallback heuristic used when no tuned config is available.

## Source code in `vllm/model_executor/layers/mamba/ops/mamba_ssm.py`


##

`_try_get_optimal_ssm_config_cached(headdim, dstate, batch, nheads, cache_dtype, is_blackwell)`

`cached`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.mamba_ssm._try_get_optimal_ssm_config_cached)

Cached resolution. See :func:`try_get_optimal_ssm_config`

.

## Source code in `vllm/model_executor/layers/mamba/ops/mamba_ssm.py`


##

`get_ssm_config_file_name(headdim, dstate, cache_dtype, device_name)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.mamba_ssm.get_ssm_config_file_name)

Return the JSON filename for the given kernel shape.

Layout: `configs/selective_state_update/ headdim=<H>,dstate=<D>,device_name=<dev>,cache_dtype=<dt>.json`

.

## Source code in `vllm/model_executor/layers/mamba/ops/mamba_ssm.py`


##

`get_ssm_configs(headdim, dstate, cache_dtype)`

`cached`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.mamba_ssm.get_ssm_configs)

Return tuned (BLOCK_SIZE_M, num_warps) configs for *selective_state_update* keyed by `effective_batch = batch * nheads`

, or `None`

if no config file is found for the (headdim, dstate, cache_dtype, device) combination.

## They can be generated with

benchmarks/kernels/benchmark_selective_state_update.py --save-configs

## Source code in `vllm/model_executor/layers/mamba/ops/mamba_ssm.py`


##

`override_ssm_config(config)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.mamba_ssm.override_ssm_config)

Pin `try_get_optimal_ssm_config`

to `config`

for the duration of the context. Used by the tuning benchmark to time specific configs.

## Source code in `vllm/model_executor/layers/mamba/ops/mamba_ssm.py`


##

`selective_scan_fn(u, ssm_states, delta, A, B, C, D=None, z=None, delta_bias=None, delta_softplus=False, query_start_loc=None, cache_indices=None, has_initial_state=None, null_block_id=NULL_BLOCK_ID, block_size=1024, block_idx_first_scheduled_token=None, block_idx_last_scheduled_token=None, initial_state_idx=None, cu_chunk_seqlen=None, last_chunk_indices=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.mamba_ssm.selective_scan_fn)

## (dim, total_length) for varlen or (batch, dim, seqlen)

applies changes in place.

ssm_states: (batch, dim, dstate) or (batch, nheads, dim, dstate) applies changes in place. delta: (dim, total_length) for varlen or (batch, dim, seqlen) A: (dim, dstate) B: (ngroups, dstate, total_length) for varlen or (batch,ngroups,dstate,seqlen) C: (ngroups, dstate, total_length) for varlen or (batch,ngroups,dstate,seqlen) D: (dim,) z: (dim, total_length) for varlen or (batch, dim, seqlen) dt_bias: (dim,) or (dim) query_start_loc: (batch + 1) int32 The cumulative sequence lengths of the sequences in the batch, used to index into sequence. prepended with 0. for example: query_start_loc = torch.Tensor([0,10,16,17]), x.shape=(dim,17) cache_indices: (batch) int32 A tensor with each cell is a correspondent input and output ssm_state indices - Without APC: (batch,) - single state index per batch item - With APC: (batch, max_positions) - cache block indices for read/write Each non-zero value indicates a cache block to load from and/or write to. has_initial_state: (batch) bool A tensor populated with ones and zeros, indicate if the ssm_state at the corresponding index should be used as initial state. Not providing argument assumes there's no initial state null_block_id: int if cache_indices is passed, lets the kernel identify padding entries that will not be processed, for example: cache_indices = [null_block_id, 1 ,20 ,null_block_id] in this case, the kernel will not process entries at indices 0 and 3 block_size: int The block size to align the cached states to block_idx_first_scheduled_token: (batch,), dtype int32 The pointer into cache_indices, where the first cache block to be filled is located. block_idx_last_scheduled_token: (batch,), dtype int32 The pointer into cache_indices, where the last cache block to be filled is located. initial_state_idx: (batch,), dtype int32 The pointer into cache_indices, where the cache block containing the initial state is located.

#### Returns[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.mamba_ssm.selective_scan_fn--returns)

```
output: (dim, total_length) for varlen or (batch, dim, seqlen)
supports inplace replacement
```


## Source code in `vllm/model_executor/layers/mamba/ops/mamba_ssm.py`


|
|

##

`selective_state_update(state, x, dt, A, B, C, D, dt_bias, z=None, dt_softplus=False, state_batch_indices=None, dst_state_batch_indices=None, null_block_id=NULL_BLOCK_ID, out=None, num_accepted_tokens=None, cu_seqlens=None, is_blackwell=False, enable_stochastic_rounding=False, cache_philox_rounds=0)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.mamba_ssm.selective_state_update)

Argument: state: (batch, dim, dstate) or (batch, nheads, dim, dstate) x: (batch, dim) or (batch, nheads, dim) dt: (batch, dim) or (batch, nheads, dim) A: (dim, dstate) or (nheads, dim, dstate) B: (batch, dstate) or (batch, ngroups, dstate) C: (batch, dstate) or (batch, ngroups, dstate) D: (dim,) or (nheads, dim) z: (batch, dim) or (batch, nheads, dim) dt_bias: (dim,) or (nheads, dim) null_block_id: int if state_batch_indices is passed, lets the kernel identify padded entries that will not be processed, for example: state_batch_indices = [null_block_id, 1, 20, null_block_id] in this case, the kernel will not process entries at indices 0 and 3 out: Preallocated ssm output tensor. Assume same shape as x. In-place updated. num_accepted_tokens: (batch,) number of accepted tokens from previous verification step, tells the kernel which initial state to use cu_seqlens: (batch,) length per sequence, for variable length in speculative decoding cases

## Source code in `vllm/model_executor/layers/mamba/ops/mamba_ssm.py`


|
|

##

`try_get_optimal_ssm_config(headdim, dstate, batch, nheads, cache_dtype, is_blackwell)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.mamba_ssm.try_get_optimal_ssm_config)

Return (BLOCK_SIZE_M, num_warps) for the given kernel shape.

Tuning is keyed on `effective_batch = batch * nheads`

(the kernel grid scales with the product), so configs transfer across (model, TP) combos sharing `(headdim, dstate, cache_dtype)`

.