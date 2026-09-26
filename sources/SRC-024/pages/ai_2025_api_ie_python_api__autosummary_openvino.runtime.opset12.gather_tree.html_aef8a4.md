source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset12.gather_tree.html
lastmod: 

# openvino.runtime.opset12.gather_tree[#](https://docs.openvino.ai#openvino-runtime-opset12-gather-tree)

-
openvino.runtime.opset12.gather_tree(
*step_ids:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*parent_idx:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*max_seq_len:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*end_token:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset12.gather_tree) Perform GatherTree operation.

- Parameters:
**step_ids**– The tensor with indices from per each step.**parent_idx**– The tensor with with parent beam indices.**max_seq_len**– The tensor with maximum lengths for each sequence in the batch.**end_token**– The scalar tensor with value of the end marker in a sequence.**name**– Optional name for output node.

- Returns:
The new node performing a GatherTree operation.


The GatherTree node generates the complete beams from the indices per each step and the parent beam indices. GatherTree uses the following logic:

for batch in range(BATCH_SIZE): for beam in range(BEAM_WIDTH): max_sequence_in_beam = min(MAX_TIME, max_seq_len[batch]) parent = parent_idx[max_sequence_in_beam - 1, batch, beam] for level in reversed(range(max_sequence_in_beam - 1)): final_idx[level, batch, beam] = step_idx[level, batch, parent] parent = parent_idx[level, batch, parent]