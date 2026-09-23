source: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/ir/clone_elimination/
lastmod: 2026-09-23

Bases: [VllmInductorPass](../../vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmInductorPass)


This pass removes clone nodes that are no longer needed after vLLM IR lowering. It uses donated_input_ids to eliminate clones of donated graph inputs, preserving contents of non-donated graph inputs.

It is "unsafe" because it does not (yet) take aliasing into account. Solving aliasing is an open problem, so this pass intends to support known vLLM cases and not guarantee soundness on general graphs. In the future, this pass will likely support basic forms of aliasing to handle simple views (e.g. qkv -> q,k,v).

## Source code in `vllm/compilation/passes/ir/clone_elimination.py`


| class UnsafeCloneEliminationPass(VllmInductorPass):
"""This pass removes clone nodes that are no longer needed after vLLM IR lowering.
It uses donated_input_ids to eliminate clones of donated graph inputs, preserving
contents of non-donated graph inputs.
It is "unsafe" because it does not (yet) take aliasing into account. Solving
aliasing is an open problem, so this pass intends to support known vLLM cases
and not guarantee soundness on general graphs. In the future, this pass will likely
support basic forms of aliasing to handle simple views (e.g. qkv -> q,k,v).
"""
def __init__(self, vllm_config: VllmConfig) -> None:
super().__init__(vllm_config)
@VllmInductorPass.time_and_log
def __call__(self, graph: fx.Graph) -> None:
count = 0
node_to_idx = {node: i for i, node in enumerate(graph.nodes)}
pass_context = get_pass_context()
donated_input_ids = pass_context.donated_input_ids
logger.debug("Donated input ids: %s", donated_input_ids)
for node in graph.nodes:
if not is_func(node, torch.ops.aten.clone.default):
continue
original_node = node.args[0]
assert isinstance(original_node, fx.Node)
if not clone_preserves_layout(node, original_node):
logger.debug(
"Clone removal not possible, clone changes layout: "
"original_node=%s node=%s",
original_node,
node,
)
continue
# Clone needs to be preserved if node is getting written to and
# the old value is used again.
# This could only happen if an inplace implementation was lowered.
# Then node (the clone) will have one write.
# TODO(luka) hopefully this can be removed once we lower functional graphs.
write_idxs = [
node_to_idx[u] for u in node.users if user_writes_to_node(u, node)
]
assert len(write_idxs) in (0, 1)
if write_idxs:
# Check if a user of original_node occurs after a write
write_idx = write_idxs[0]
if any(
node_to_idx[orig_user] > write_idx
for orig_user in original_node.users
):
logger.debug(
"Clone removal not possible, "
"original_node=%s used after mutation on node=%s",
original_node,
node,
)
continue
# Check if a node is a (non-donated) graph input
if (
original_node.op == "placeholder"
and node_to_idx[original_node] not in donated_input_ids
):
logger.debug(
"Graph input %s not donated, cannot eliminate its clone",
original_node,
)
continue
logger.debug(
"Node %s is a redundant clone node of %s, removing it",
node,
original_node,
)
node.replace_all_uses_with(original_node)
graph.erase_node(node)
count += 1
logger.debug("CloneCleanupPass removed %d clone nodes", count)
|