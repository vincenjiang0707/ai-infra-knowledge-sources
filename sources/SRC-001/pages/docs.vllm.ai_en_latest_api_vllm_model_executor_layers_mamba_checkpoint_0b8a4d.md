source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/mamba/checkpoint/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.mamba.checkpoint`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.checkpoint)

Classes:

-
–[MambaPrefillCheckpointBuilder](https://docs.vllm.ai#vllm.model_executor.layers.mamba.checkpoint.MambaPrefillCheckpointBuilder)Build backend-neutral prefill checkpoint locations.

-
–[MambaPrefillCheckpointExporter](https://docs.vllm.ai#vllm.model_executor.layers.mamba.checkpoint.MambaPrefillCheckpointExporter)Export a mid-prefill checkpoint into backend-specific paged states.


Functions:

-
–[compute_mamba_prefill_checkpoints](https://docs.vllm.ai#vllm.model_executor.layers.mamba.checkpoint.compute_mamba_prefill_checkpoints)Per-row internal prefill checkpoint offsets and cache block columns.


##

`MambaPrefillCheckpointBuilder`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.checkpoint.MambaPrefillCheckpointBuilder)

Build backend-neutral prefill checkpoint locations.

## Source code in `vllm/model_executor/layers/mamba/checkpoint.py`


##

`MambaPrefillCheckpointExporter`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.checkpoint.MambaPrefillCheckpointExporter)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Export a mid-prefill checkpoint into backend-specific paged states.

Methods:

-
–[export](https://docs.vllm.ai#vllm.model_executor.layers.mamba.checkpoint.MambaPrefillCheckpointExporter.export)Write checkpoint state into the paged cache.


## Source code in `vllm/model_executor/layers/mamba/checkpoint.py`


###

`export(checkpoint, *args, **kwargs)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.checkpoint.MambaPrefillCheckpointExporter.export)

Write checkpoint state into the paged cache.

##

`compute_mamba_prefill_checkpoints(seq_lens, query_lens, hash_block_size, mamba_block_size, checkpoint_alignment, drop_eagle_block)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.checkpoint.compute_mamba_prefill_checkpoints)

Per-row internal prefill checkpoint offsets and cache block columns.

Backends call this instead of re-deriving the rules, so they decline in lockstep with the scheduler and `MambaManager`

: allocating a checkpoint block without writing it leaves the prefix cache serving uninitialized state.

Returns:

-

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]`(offsets, cols)`

: the checkpoint's offset into each row's query and -

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]its block-table column.

`0`

and`-1`

mean the row has none.