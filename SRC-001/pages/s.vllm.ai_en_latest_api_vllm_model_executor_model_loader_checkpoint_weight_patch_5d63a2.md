source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/checkpoint_weight_patch/
lastmod: 2026-09-23

#

`vllm.model_executor.model_loader.checkpoint_weight_patch`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.checkpoint_weight_patch)

Apply dense or sparse weight updates in checkpoint coordinates.

The model's `load_weights`

method still handles checkpoint-name mapping, TP slicing, and packed parameters. Sparse patches use NaN to mark unchanged checkpoint elements. The supported sparse-loader contract permits only final same-shaped floating-point `Tensor.copy_`

writes. Composed, multi-stage, and custom-write loaders are unsupported.

Classes:

-
–[CheckpointWeightPatch](https://docs.vllm.ai#vllm.model_executor.model_loader.checkpoint_weight_patch.CheckpointWeightPatch)Describe one dense or sparse checkpoint-coordinate update.


Functions:

-
–[load_checkpoint_weight_patches](https://docs.vllm.ai#vllm.model_executor.model_loader.checkpoint_weight_patch.load_checkpoint_weight_patches)Load ordered patches through the model's checkpoint loader.


##

`CheckpointWeightPatch`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.checkpoint_weight_patch.CheckpointWeightPatch)

Bases: [NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple)

Describe one dense or sparse checkpoint-coordinate update.

Attributes:

-
(`name`


) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Checkpoint weight name passed to the model loader.

-
(`shape`


) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int), ...]Full checkpoint tensor shape.

-
(`dtype`


) –[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)Checkpoint tensor dtype.

-
(`values`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The flattened full tensor for a dense patch, or the values at

`indices`

for a sparse patch. -
(`indices`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NoneFlat indices into the full checkpoint tensor described by

`shape`

.`None`

makes`values`

a dense replacement.

## Source code in `vllm/model_executor/model_loader/checkpoint_weight_patch.py`


##

`_load_nan_masked_weights(model, weights)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.checkpoint_weight_patch._load_nan_masked_weights)

Load NaN-masked checkpoint tensors while preserving runtime values at NaNs.

## Source code in `vllm/model_executor/model_loader/checkpoint_weight_patch.py`


##

`load_checkpoint_weight_patches(model, patches, *, max_chunk_bytes=_DEFAULT_PATCH_CHUNK_BYTES, validate_unique_indices=True)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.checkpoint_weight_patch.load_checkpoint_weight_patches)

Load ordered patches through the model's checkpoint loader.

A call may contain either dense or sparse patches, but not both. A repeated name starts a new loader call, so patches for that weight are applied in input order. A later patch may update positions changed by an earlier patch. Each sparse patch creates a full checkpoint-shaped tensor whose NaNs mark unchanged elements. Each locally applied sparse patch must use one final same-shaped floating-point `Tensor.copy_`

. Intermediate or unrelated `copy_`

calls, composed loaders, and custom write paths are unsupported. `max_chunk_bytes`

is a batching target; one tensor may exceed it.

Online checkpoint-format dense updates require the caller to manage vLLM's layerwise reload lifecycle. Sparse online updates modify initialized model tensors in place and must not use that lifecycle. Patch shapes, dtypes, value lengths, and sparse indices are validated before loading begins.

This function does not roll back a partial update. If a loader fails after a write, some destinations may already be changed. Do not serve from the affected worker until a known baseline has been restored or the worker has been restarted.

Parameters:

-

(`model`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.checkpoint_weight_patch.load_checkpoint_weight_patches(model))

) –[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)Model whose native

`load_weights`

method applies the patches. -

(`patches`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.checkpoint_weight_patch.load_checkpoint_weight_patches(patches))

) –[Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable)[[CheckpointWeightPatch](https://docs.vllm.ai#vllm.model_executor.model_loader.checkpoint_weight_patch.CheckpointWeightPatch)]Dense replacements or sparse updates in checkpoint coordinates.

-

(`max_chunk_bytes`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.checkpoint_weight_patch.load_checkpoint_weight_patches(max_chunk_bytes))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`_DEFAULT_PATCH_CHUNK_BYTES`

) –Target checkpoint tensor bytes per

`model.load_weights`

call. A single tensor may exceed this target. -

(`validate_unique_indices`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.checkpoint_weight_patch.load_checkpoint_weight_patches(validate_unique_indices))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –Whether to reject duplicate sparse indices within each patch. Repeated patches may update the same positions. Disable only for a trusted producer that already guarantees unique positions within each patch.


Returns:

## Source code in `vllm/model_executor/model_loader/checkpoint_weight_patch.py`


|
|