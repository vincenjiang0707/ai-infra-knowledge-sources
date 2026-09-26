source: https://docs.vllm.ai/en/latest/api/vllm/models/kimi_k3/nvidia/kda/
lastmod: 2026-09-24

class _KimiGDNMergedColumnParallelLinear(MergedColumnParallelLinear):
"""Merged projection with one output replicated across TP ranks."""
def __init__(
self,
input_size: int,
output_sizes: list[int],
replicated_shard_id: int,
tp_size: int,
**kwargs,
) -> None:
self.replicated_shard_id = replicated_shard_id
output_sizes = output_sizes.copy()
output_sizes[replicated_shard_id] *= tp_size
super().__init__(input_size, output_sizes, **kwargs)
def weight_loader(
self,
param: Parameter,
loaded_weight: torch.Tensor,
loaded_shard_id: tuple[int, ...] | int | None = None,
) -> None:
tp_rank = self.tp_rank
param_tp_rank = getattr(param, "tp_rank", None)
replicate_block_scale = (
isinstance(param, BlockQuantScaleParameter)
and loaded_weight.shape[param.output_dim] < self.tp_size
)
if loaded_shard_id == self.replicated_shard_id or replicate_block_scale:
self.tp_rank = 0
if param_tp_rank is not None:
param.tp_rank = 0
try:
super().weight_loader(param, loaded_weight, loaded_shard_id)
finally:
self.tp_rank = tp_rank
if param_tp_rank is not None:
param.tp_rank = param_tp_rank
def weight_loader_v2(
self,
param: BasevLLMParameter,
loaded_weight: torch.Tensor,
loaded_shard_id: tuple[int, ...] | int | None = None,
) -> None:
tp_rank = self.tp_rank
param_tp_rank = getattr(param, "tp_rank", None)
replicate_block_scale = (
isinstance(param, BlockQuantScaleParameter)
and loaded_weight.shape[param.output_dim] < self.tp_size
)
if loaded_shard_id == self.replicated_shard_id or replicate_block_scale:
self.tp_rank = 0
if param_tp_rank is not None:
param.tp_rank = 0
try:
super().weight_loader_v2(param, loaded_weight, loaded_shard_id)
finally:
self.tp_rank = tp_rank
if param_tp_rank is not None:
param.tp_rank = param_tp_rank