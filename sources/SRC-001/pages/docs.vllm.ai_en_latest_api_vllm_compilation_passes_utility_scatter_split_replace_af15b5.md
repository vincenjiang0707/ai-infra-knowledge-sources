source: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/utility/scatter_split_replace/
lastmod: 2026-09-24

#

`vllm.compilation.passes.utility.scatter_split_replace`

[¶](https://docs.vllm.ai#vllm.compilation.passes.utility.scatter_split_replace)

Replace `slice_scatter`

and `split_with_sizes`

nodes with a single assignment if there are no users for the inplace tensor written to by the slice_scatter call.

The inplace rotary_embedding custom op takes in mutable query and key inputs that are split+getitem outputs of a single qkv tensor. When functionalized, we fetch the rotated query and key from the functionalized op using `getitem`

calls. However, we also write to the qkv tensor inplace using a `slice_scatter`

, then split the inplace tensor to get the output tensors again. Instead, if the inplace tensor has no subsequent users, we can just replace the `slice_scatter`

and `split_with_sizes`

nodes with the `getitem`

calls.

This is already done in fix_functionalization::FixFunctionalizationPass, but writing a custom pass for it before defunctionalization allows matching against the qkv split+rotary_embedding subpattern as part of e.g. the RoPE+KVCache fusion pass.

Classes:

-
–[ScatterSplitReplacementPass](https://docs.vllm.ai#vllm.compilation.passes.utility.scatter_split_replace.ScatterSplitReplacementPass)Replace getitem+slice_scatter+split nodes with a single getitem when


##

`ScatterSplitReplacementPass`

[¶](https://docs.vllm.ai#vllm.compilation.passes.utility.scatter_split_replace.ScatterSplitReplacementPass)

Bases: [VllmInductorPass](https://docs.vllm.ai/vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmInductorPass)

Replace getitem+slice_scatter+split nodes with a single getitem when the inplace subtensor written to by the slice_scatter has no other users.

Here's an example graph with q_size = 512, kv_size = 64: split_with_sizes_1 = torch.ops.aten.split_with_sizes.default(qkv, (512, 64, 64), -1) at = auto_functionalized(torch.ops._C.rotary_embedding.default(positions, q, k)) q = operator.getitem(at, 1) k = operator.getitem(at, 2) torch.ops.aten.slice_scatter.default(qkv, q, [0, 512], -1) torch.ops.aten.slice_scatter.default(qkv, k, [512, 512 + 64], -1) split_with_sizes_2 = torch.ops.aten.split_with_sizes.default(qkv, (512, 64, 64), -1) q = operator.getitem(split_with_sizes_2, 0) k = operator.getitem(split_with_sizes_2, 1) v = operator.getitem(split_with_sizes_2, 2)

After this pass, this sequence of nodes is replaced with: split_with_sizes_1 = torch.ops.aten.split_with_sizes.default(qkv, (512, 64, 64), -1) at = auto_functionalized(torch.ops._C.rotary_embedding.default(positions, q, k)) q = operator.getitem(at, 1) k = operator.getitem(at, 2) v = operator.getitem(split_with_sizes_1, 2)

## Source code in `vllm/compilation/passes/utility/scatter_split_replace.py`


|
|