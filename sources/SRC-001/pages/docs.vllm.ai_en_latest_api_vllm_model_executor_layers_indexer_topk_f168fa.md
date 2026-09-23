source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/indexer_topk/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.indexer_topk`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.indexer_topk)

Top-k kernels for the DSA sparse attention indexer.

Classes:

-
–[SparseIndexerTopk](https://docs.vllm.ai#vllm.model_executor.layers.indexer_topk.SparseIndexerTopk)The sparse indexer's decode top-k stage.


Functions:

-
–[deep_select_topk](https://docs.vllm.ai#vllm.model_executor.layers.indexer_topk.deep_select_topk)Select the top-k indices per row of

`input`

with DeepSelect. -
–[get_deep_select_stride_requirement](https://docs.vllm.ai#vllm.model_executor.layers.indexer_topk.get_deep_select_stride_requirement)Stride alignment requirement (input, output) in bytes.

-
–[is_deep_select_supported](https://docs.vllm.ai#vllm.model_executor.layers.indexer_topk.is_deep_select_supported)Whether the kernel accepts this input (dtype/stride/topk constraints).


##

`SparseIndexerTopk`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.indexer_topk.SparseIndexerTopk)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

The sparse indexer's decode top-k stage.

Selects among the available top-k kernels (see kernel_config.sparse_indexer_topk_backend) and runs the chosen one.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.layers.indexer_topk.SparseIndexerTopk.forward)Run the resolved decode top-k implementation, writing into

-
–[resolve_backend](https://docs.vllm.ai#vllm.model_executor.layers.indexer_topk.SparseIndexerTopk.resolve_backend)Resolve the decode top-k implementation from the configured


## Source code in `vllm/model_executor/layers/indexer_topk.py`


|
|

###

`_cooperative_constraints(logits, topk_tokens, num_rows)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.indexer_topk.SparseIndexerTopk._cooperative_constraints)

Unmet constraints of cooperative_topk (empty when applicable).

## Source code in `vllm/model_executor/layers/indexer_topk.py`


###

`_resolve_auto(logits, topk_tokens, num_rows)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.indexer_topk.SparseIndexerTopk._resolve_auto)

The priority chain: cooperative -> persistent -> per_row. deep_select/flashinfer/torch are opt-in only.

cooperative_topk is preferred whenever it is applicable, i.e. within its AUTO_COOPERATIVE_MAX_ROWS row limit; larger batches go to persistent_topk.

## Source code in `vllm/model_executor/layers/indexer_topk.py`


###

`_row_ends(seq_lens, next_n, num_rows)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.indexer_topk.SparseIndexerTopk._row_ends)

Per-row exclusive end offsets (int32, (num_rows,)) for top-k kernels that take ragged lengths (DeepSelect, FlashInfer, torch reference).

seq_lens is (B, next_n) per-row effective lens for native spec decode and (B, 1) otherwise, in which case per-row lens are derived the same way as the other decode top-k kernels.

## Source code in `vllm/model_executor/layers/indexer_topk.py`


###

`forward(logits, seq_lens, next_n, topk_indices, topk_tokens, max_seq_len)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.indexer_topk.SparseIndexerTopk.forward)

Run the resolved decode top-k implementation, writing into topk_indices (int32, -1 fill for rows shorter than topk_tokens).

## Source code in `vllm/model_executor/layers/indexer_topk.py`


|
|

###

`resolve_backend(logits, topk_tokens, num_rows)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.indexer_topk.SparseIndexerTopk.resolve_backend)

Resolve the decode top-k implementation from the configured backend ("auto" = the pre-existing chain, or a validated explicit value).

## Source code in `vllm/model_executor/layers/indexer_topk.py`


##

`_get_empty_and_aligned_tensor(dim0, dim1, device, dtype)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.indexer_topk._get_empty_and_aligned_tensor)

Tensor with shape (dim0, dim1) whose stride(0) is 32B-aligned.

## Source code in `vllm/model_executor/layers/indexer_topk.py`


##

`deep_select_topk(input, topk, end=None, output_idx=None, indices_dtype=torch.int32)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.indexer_topk.deep_select_topk)

Select the top-k indices per row of `input`

with DeepSelect.

Parameters:

-

(`input`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.indexer_topk.deep_select_topk(input))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(num_rows, vocab_size), bf16 or fp32. stride(1) must be 1 and stride(0) must be 1024B-aligned.

-

(`topk`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.indexer_topk.deep_select_topk(topk))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of elements to select per row; must be <= 4096.

-

(`end`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.indexer_topk.deep_select_topk(end))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional (num_rows,) int32 tensor with the exclusive right boundary of each row. Rows with

`end[i] < topk`

get their remaining indices filled with -1. -

(`output_idx`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.indexer_topk.deep_select_topk(output_idx))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional preallocated (num_rows, topk) output tensor whose stride(0) is 32B-aligned (e.g. a slice of a wider buffer).

-

(`indices_dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.indexer_topk.deep_select_topk(indices_dtype))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)`int32`

) –Output dtype when

`output_idx`

is not provided.

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The (num_rows, topk) indices tensor.


## Source code in `vllm/model_executor/layers/indexer_topk.py`


##

`get_deep_select_stride_requirement()`

`cached`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.indexer_topk.get_deep_select_stride_requirement)

Stride alignment requirement (input, output) in bytes.

##

`is_deep_select_supported(input, topk)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.indexer_topk.is_deep_select_supported)

Whether the kernel accepts this input (dtype/stride/topk constraints).