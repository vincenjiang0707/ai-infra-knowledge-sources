source: https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/m2n_source/
lastmod: 2026-09-27

Trainer-side weight sources for the NCCL M2N backend.

m2n plans a transfer from both sides' layouts, so the trainer has to say how it holds each parameter — which the base `WeightSource`

/ `ParamMeta`

pair does not express. This module supplies the m2n flavor of both, and the DTensor-backed implementation that covers the common trainer.

A source declares its mesh once (`mesh()`

) and a placement per parameter, since one topology describes every tensor on the side.

Classes:

Functions:

##

`DTensorModuleSource`


Bases: [M2NWeightSource](#vllm.distributed.weight_transfer.m2n_source.M2NWeightSource)


`M2NWeightSource`

over `module.named_parameters()`

.

Covers both the FSDP/DTensor trainer (placement read off each parameter, local shard yielded via `to_local()`

) and the plain replicated trainer, with no special casing. Trainers with a custom producer (a Megatron export, MoE re-fusing) subclass `M2NWeightSource`

instead.

Methods:

-
[__init__](#vllm.distributed.weight_transfer.m2n_source.DTensorModuleSource.__init__)

– Wrap `module`

; `num_trainer_ranks`

sizes the mesh for plain tensors.

-
[__iter__](#vllm.distributed.weight_transfer.m2n_source.DTensorModuleSource.__iter__)

– Yield each parameter's local shard (`to_local()`

), or the tensor itself.

-
[mesh](#vllm.distributed.weight_transfer.m2n_source.DTensorModuleSource.mesh)

– The mesh every sharded parameter agrees on.

-
[metadata](#vllm.distributed.weight_transfer.m2n_source.DTensorModuleSource.metadata)

– Read global shape/dtype and placements without gathering shards.


## Source code in `vllm/distributed/weight_transfer/m2n_source.py`


| class DTensorModuleSource(M2NWeightSource):
"""`M2NWeightSource` over `module.named_parameters()`.
Covers both the FSDP/DTensor trainer (placement read off each parameter,
local shard yielded via `to_local()`) and the plain replicated trainer, with
no special casing. Trainers with a custom producer (a Megatron export, MoE
re-fusing) subclass `M2NWeightSource` instead.
"""
def __init__(self, module: torch.nn.Module, num_trainer_ranks: int) -> None:
"""Wrap `module`; `num_trainer_ranks` sizes the mesh for plain tensors."""
self._module = module
self._num_trainer_ranks = num_trainer_ranks
def mesh(self) -> M2NMesh:
"""The mesh every sharded parameter agrees on.
Replicated parameters span the trainer without a device mesh of their
own, so they never decide this; a model whose *sharded* parameters
disagree cannot be described by one side mesh and is rejected.
"""
meshes = {
mesh_from_tensor(p, self._num_trainer_ranks)
for _, p in self._module.named_parameters()
if placements_from_tensor(p) is not REPLICATED
}
if len(meshes) > 1:
raise ValueError(
"nccl_m2n needs one mesh per side, but this module's sharded "
f"parameters span several: {sorted(m.dims for m in meshes)}"
)
return meshes.pop() if meshes else M2NMesh((self._num_trainer_ranks, 1), 0)
def metadata(self) -> list[ParamMeta]:
"""Read global shape/dtype and placements without gathering shards."""
return [
M2NParamMeta(name, p.dtype, tuple(p.shape), placements_from_tensor(p))
for name, p in self._module.named_parameters()
]
def __iter__(self) -> Iterator[tuple[str, torch.Tensor]]:
"""Yield each parameter's local shard (`to_local()`), or the tensor itself."""
for name, param in self._module.named_parameters():
to_local = getattr(param, "to_local", None)
yield name, (to_local() if callable(to_local) else param)
|

###

`__init__(module, num_trainer_ranks)`


Wrap `module`

; `num_trainer_ranks`

sizes the mesh for plain tensors.

## Source code in `vllm/distributed/weight_transfer/m2n_source.py`


| def __init__(self, module: torch.nn.Module, num_trainer_ranks: int) -> None:
"""Wrap `module`; `num_trainer_ranks` sizes the mesh for plain tensors."""
self._module = module
self._num_trainer_ranks = num_trainer_ranks
|

###

`__iter__()`


Yield each parameter's local shard (`to_local()`

), or the tensor itself.

## Source code in `vllm/distributed/weight_transfer/m2n_source.py`


| def __iter__(self) -> Iterator[tuple[str, torch.Tensor]]:
"""Yield each parameter's local shard (`to_local()`), or the tensor itself."""
for name, param in self._module.named_parameters():
to_local = getattr(param, "to_local", None)
yield name, (to_local() if callable(to_local) else param)
|

###

`mesh()`


The mesh every sharded parameter agrees on.

Replicated parameters span the trainer without a device mesh of their own, so they never decide this; a model whose *sharded* parameters disagree cannot be described by one side mesh and is rejected.

## Source code in `vllm/distributed/weight_transfer/m2n_source.py`


| def mesh(self) -> M2NMesh:
"""The mesh every sharded parameter agrees on.
Replicated parameters span the trainer without a device mesh of their
own, so they never decide this; a model whose *sharded* parameters
disagree cannot be described by one side mesh and is rejected.
"""
meshes = {
mesh_from_tensor(p, self._num_trainer_ranks)
for _, p in self._module.named_parameters()
if placements_from_tensor(p) is not REPLICATED
}
if len(meshes) > 1:
raise ValueError(
"nccl_m2n needs one mesh per side, but this module's sharded "
f"parameters span several: {sorted(m.dims for m in meshes)}"
)
return meshes.pop() if meshes else M2NMesh((self._num_trainer_ranks, 1), 0)
|

Read global shape/dtype and placements without gathering shards.

## Source code in `vllm/distributed/weight_transfer/m2n_source.py`


| def metadata(self) -> list[ParamMeta]:
"""Read global shape/dtype and placements without gathering shards."""
return [
M2NParamMeta(name, p.dtype, tuple(p.shape), placements_from_tensor(p))
for name, p in self._module.named_parameters()
]
|

##

`M2NWeightSource`


Bases: [WeightSource](../base/#vllm.distributed.weight_transfer.base.WeightSource)


A `WeightSource`

that also describes how the trainer holds its weights.

Unlike `ModuleSource`

, iteration yields each rank's **local shard**, not a materialized full tensor: gathering is exactly the cost m2n removes.

Methods:

-
[__iter__](#vllm.distributed.weight_transfer.m2n_source.M2NWeightSource.__iter__)

– Yield `(name, local shard)`

pairs in the same order as `metadata()`

.

-
[mesh](#vllm.distributed.weight_transfer.m2n_source.M2NWeightSource.mesh)

– The trainer's rank topology, shared by every parameter.

-
[metadata](#vllm.distributed.weight_transfer.m2n_source.M2NWeightSource.metadata)

– Name, dtype, full shape, and trainer placement for each parameter.


## Source code in `vllm/distributed/weight_transfer/m2n_source.py`


| class M2NWeightSource(WeightSource):
"""A `WeightSource` that also describes how the trainer holds its weights.
Unlike `ModuleSource`, iteration yields each rank's **local shard**, not a
materialized full tensor: gathering is exactly the cost m2n removes.
"""
def mesh(self) -> M2NMesh:
"""The trainer's rank topology, shared by every parameter."""
raise NotImplementedError
def metadata(self) -> list[ParamMeta]:
"""Name, dtype, full shape, and trainer placement for each parameter."""
raise NotImplementedError
def __iter__(self) -> Iterator[tuple[str, torch.Tensor]]:
"""Yield `(name, local shard)` pairs in the same order as `metadata()`."""
raise NotImplementedError
|

###

`__iter__()`


Yield `(name, local shard)`

pairs in the same order as `metadata()`

.

## Source code in `vllm/distributed/weight_transfer/m2n_source.py`


| def __iter__(self) -> Iterator[tuple[str, torch.Tensor]]:
"""Yield `(name, local shard)` pairs in the same order as `metadata()`."""
raise NotImplementedError
|

###

`mesh()`


The trainer's rank topology, shared by every parameter.

## Source code in `vllm/distributed/weight_transfer/m2n_source.py`


| def mesh(self) -> M2NMesh:
"""The trainer's rank topology, shared by every parameter."""
raise NotImplementedError
|

Name, dtype, full shape, and trainer placement for each parameter.

## Source code in `vllm/distributed/weight_transfer/m2n_source.py`


| def metadata(self) -> list[ParamMeta]:
"""Name, dtype, full shape, and trainer placement for each parameter."""
raise NotImplementedError
|

##

`_placement_code(placement)`


Map a `torch.distributed`

placement onto an m2n placement code.

## Source code in `vllm/distributed/weight_transfer/m2n_source.py`


| def _placement_code(placement: Any) -> int:
"""Map a `torch.distributed` placement onto an m2n placement code."""
name = type(placement).__name__
if name == "Replicate":
return REPLICATE
if name == "Shard":
return int(placement.dim)
raise ValueError(
f"nccl_m2n cannot express the {name} placement; only Replicate and "
"Shard are supported"
)
|

##

`mesh_from_tensor(tensor, num_trainer_ranks)`


The mesh a parameter lives on, as an `M2NMesh`

.

A plain tensor is identical on every trainer rank, so it spans all of them.

## Source code in `vllm/distributed/weight_transfer/m2n_source.py`


| def mesh_from_tensor(tensor: torch.Tensor, num_trainer_ranks: int) -> M2NMesh:
"""The mesh a parameter lives on, as an `M2NMesh`.
A plain tensor is identical on every trainer rank, so it spans all of them.
"""
device_mesh = getattr(tensor, "device_mesh", None)
if device_mesh is None:
return M2NMesh((num_trainer_ranks, 1), 0)
grid = device_mesh.mesh
ranks = grid.flatten().tolist()
if ranks != list(range(len(ranks))):
raise ValueError(
"nccl_m2n requires the trainer's device mesh to cover the "
f"contiguous rank interval [0, {len(ranks)}); got {ranks}"
)
if grid.ndim > 2:
raise ValueError(
f"nccl_m2n supports 1-D and 2-D device meshes, got {grid.ndim}-D"
)
dims = tuple(grid.shape)
return M2NMesh(dims if len(dims) == 2 else (dims[0], 1), 0)
|

##

`placements_from_tensor(tensor)`


How a parameter is placed over its mesh, or `REPLICATED`

.

`REPLICATED`

is returned rather than a `(REPLICATE, REPLICATE)`

pair: m2n cannot express that, and the size-1-axis encoding it needs instead is applied later by `resolve_layout`

, which owns that workaround.

## Source code in `vllm/distributed/weight_transfer/m2n_source.py`


| def placements_from_tensor(tensor: torch.Tensor) -> Placements | None:
"""How a parameter is placed over its mesh, or `REPLICATED`.
`REPLICATED` is returned rather than a `(REPLICATE, REPLICATE)` pair: m2n
cannot express that, and the size-1-axis encoding it needs instead is
applied later by `resolve_layout`, which owns that workaround.
"""
placements = getattr(tensor, "placements", None)
if placements is None:
return REPLICATED
codes = [_placement_code(p) for p in placements]
if all(code == REPLICATE for code in codes):
return REPLICATED
if len(codes) == 1:
return (codes[0], REPLICATE)
return (codes[0], codes[1])
|