source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/keye_vl1_5/
lastmod: 2026-09-23

#

`vllm.model_executor.models.keye_vl1_5`

[¶](https://docs.vllm.ai#vllm.model_executor.models.keye_vl1_5)

Classes:

-
–[KeyeVL1_5ImageEmbeddingInputs](https://docs.vllm.ai#vllm.model_executor.models.keye_vl1_5.KeyeVL1_5ImageEmbeddingInputs)Dimensions:

-
–[KeyeVL1_5ImagePixelInputs](https://docs.vllm.ai#vllm.model_executor.models.keye_vl1_5.KeyeVL1_5ImagePixelInputs)Dimensions:

-
–[KeyeVL1_5VideoEmbeddingInputs](https://docs.vllm.ai#vllm.model_executor.models.keye_vl1_5.KeyeVL1_5VideoEmbeddingInputs)Dimensions:

-
–[KeyeVL1_5VideoPixelInputs](https://docs.vllm.ai#vllm.model_executor.models.keye_vl1_5.KeyeVL1_5VideoPixelInputs)Dimensions:


Functions:

-
–[get_num_patches](https://docs.vllm.ai#vllm.model_executor.models.keye_vl1_5.get_num_patches)Return num_patches per video.

-
–[split_thw](https://docs.vllm.ai#vllm.model_executor.models.keye_vl1_5.split_thw)Split grid_thw in t dimension.


##

`KeyeVL1_5ImageEmbeddingInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.keye_vl1_5.KeyeVL1_5ImageEmbeddingInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - nf: Number of image features - hs: Hidden size (must match the hidden size of language model backbone) - ni: Number of images - g: Grid dimensions (3 for t, h, w)

## Source code in `vllm/model_executor/models/keye_vl1_5.py`


##

`KeyeVL1_5ImagePixelInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.keye_vl1_5.KeyeVL1_5ImagePixelInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - bnp: Batch size * Number of patches - c: Number of channels - ps: Patch size - ni: Number of images - g: Grid dimensions (3 for t, h, w)

## Source code in `vllm/model_executor/models/keye_vl1_5.py`


##

`KeyeVL1_5VideoEmbeddingInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.keye_vl1_5.KeyeVL1_5VideoEmbeddingInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - nf: Number of video features - hs: Hidden size (must match the hidden size of language model backbone) - nv: Number of videos - g: Grid dimensions (3 for t, h, w)

## Source code in `vllm/model_executor/models/keye_vl1_5.py`


##

`KeyeVL1_5VideoPixelInputs`

[¶](https://docs.vllm.ai#vllm.model_executor.models.keye_vl1_5.KeyeVL1_5VideoPixelInputs)

Bases: [TensorSchema](https://docs.vllm.ai/utils/tensor_schema/#vllm.utils.tensor_schema.TensorSchema)

Dimensions: - bnp: Batch size * Number of patches - c: Number of channels - ps: Patch size - ni: Number of images - g: Grid dimensions (3 for t, h, w)

## Source code in `vllm/model_executor/models/keye_vl1_5.py`


##

`get_num_patches(grid_thw, num_frames)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.keye_vl1_5.get_num_patches)

Return num_patches per video.

Parameters:

-

(`grid_thw`

[¶](https://docs.vllm.ai#vllm.model_executor.models.keye_vl1_5.get_num_patches(grid_thw))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Tensor with shape [N, 3] containing temporal, height, width dimensions

-

(`num_frames`

[¶](https://docs.vllm.ai#vllm.model_executor.models.keye_vl1_5.get_num_patches(num_frames))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] |[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)List or tensor indicating the number of frames per video


Returns:

Examples:

>>> # Suppose there are 2 videos with a total of 3 grids
>>> grid_thw = torch.tensor(
... [
... [2, 2, 2], # grid 0: 2*2*2=8 patches
... [2, 2, 2], # grid 1: 2*2*2=8 patches
... [1, 1, 1],
... ]
... ) # grid 2: 1*1*1=1 patches
>>> num_frames = [2, 1] # The first video contains 2 grids,
the second contains 1 grid.
>>> get_num_patches(grid_thw, num_frames)
tensor([16, 1]) # Total patches for first video: 8+8=16,
second video: 1.


## Source code in `vllm/model_executor/models/keye_vl1_5.py`


##

`split_thw(grid_thw)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.keye_vl1_5.split_thw)

Split grid_thw in t dimension.

Parameters:

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[Σt, 3] tensor where each row is [1, h, w]


Example:

grid_thw = torch.tensor([[2, 3, 4], [1, 5, 6]]) split_thw(grid_thw) tensor([[1, 3, 4], [1, 3, 4], [1, 5, 6]])