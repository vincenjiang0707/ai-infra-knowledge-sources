source: https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/m2n_common/
lastmod: 2026-09-27

#

`vllm.distributed.weight_transfer.m2n_common`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_common)

Shared helpers for the NCCL M2N (`nccl_m2n`

) weight transfer backend.

M2N reshards a tensor between two disjoint meshes of ranks that live in one communicator: the trainer occupies ranks `[0, T)`

and the inference workers `[T, T + N)`

. This module holds everything both sides need — the optional runtime import, layout descriptors, and the conversion to `nccl.m2n`

types — so the engine module stays about the transfer itself.

Classes:

-
–[M2NMesh](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_common.M2NMesh)One side's rank topology — pure topology, no tensor placement.

-
–[M2NParamMeta](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_common.M2NParamMeta)`ParamMeta`

extended with how the trainer places this tensor.

Functions:

-
–[check_placements](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_common.check_placements)Reject placement pairs m2n cannot express.

-
–[check_plan_limits](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_common.check_plan_limits)Reject plans that exceed m2n's static per-shard fan-in / fan-out arrays.

-
–[check_transferable](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_common.check_transferable)Reject tensors m2n cannot move at all, with the parameter named.

-
–[comm_ptr](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_common.comm_ptr)Raw

`ncclComm_t`

behind vLLM's`PyNcclCommunicator`

. -
–[import_m2n](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_common.import_m2n)Import

`nccl.m2n`

lazily, with an actionable error when it is missing. -
–[publish_destination_placements](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_common.publish_destination_placements)Share the worker-side destination plan with every rank in the group.

-
–[resolve_layout](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_common.resolve_layout)Pair one tensor's placement with the mesh m2n should see for it.

-
–[shard_count](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_common.shard_count)How many pieces this layout splits the tensor into.

-
–[validate_layout](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_common.validate_layout)Check a resolved layout can describe

`shape`

before any collective runs.

##

`M2NMesh`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_common.M2NMesh)

One side's rank topology — pure topology, no tensor placement.

Mirrors `ncclMesh_t`

: a 2-axis mesh owning the contiguous rank interval `[start_rank, start_rank + dims[0] * dims[1])`

. There is no 1-D mesh; a single-axis topology is spelled with a second axis of size 1.

One mesh describes every tensor on its side, so it is exchanged once at the init handshake rather than per parameter.

## Source code in `vllm/distributed/weight_transfer/m2n_common.py`


##

`M2NParamMeta`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_common.M2NParamMeta)

Bases: [ParamMeta](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.ParamMeta)

`ParamMeta`

extended with how the trainer places this tensor.

The base class carries only name / dtype / full shape, which is not enough to plan a reshard. `placements`

is relative to its side's `M2NMesh`

, or `REPLICATED`

when every rank holds the whole tensor.

## Source code in `vllm/distributed/weight_transfer/m2n_common.py`


##

`check_placements(placements, context='placements')`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_common.check_placements)

Reject placement pairs m2n cannot express.

The header requires exactly one SHARD axis and one REPLICATE axis. `{REPLICATE, REPLICATE}`

hits a degenerate prepare branch, which is why full replication is carried as `REPLICATED`

and resolved separately; sharding both axes is not expressible at all.

## Source code in `vllm/distributed/weight_transfer/m2n_common.py`


##

`check_plan_limits(src, dst, name)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_common.check_plan_limits)

Reject plans that exceed m2n's static per-shard fan-in / fan-out arrays.

Only the unambiguous cases are checked: when one side is a single shard it is fed by (or feeds) every shard on the other side, so the count is exactly the other side's shard count. In the general sharded-to-sharded case the overlap depends on the library's chunking, and reproducing that arithmetic here would duplicate internals that can change under us.

m2n re-checks authoritatively and, because the plan is derived from the shared descriptors, fails identically on every rank -- so this is about reporting at init with a message that names the parameter, not about avoiding a hang.

## Source code in `vllm/distributed/weight_transfer/m2n_common.py`


##

`check_transferable(name, dtype, shape)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_common.check_transferable)

Reject tensors m2n cannot move at all, with the parameter named.

## Source code in `vllm/distributed/weight_transfer/m2n_common.py`


##

`comm_ptr(comm)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_common.comm_ptr)

Raw `ncclComm_t`

behind vLLM's `PyNcclCommunicator`

.

m2n links its own NCCL, so the handle only means anything if vLLM loaded the same `libnccl.so`

— set `VLLM_NCCL_SO_PATH`

accordingly.

## Source code in `vllm/distributed/weight_transfer/m2n_common.py`


##

`import_m2n()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_common.import_m2n)

Import `nccl.m2n`

lazily, with an actionable error when it is missing.

Deferred so that importing vLLM — or any other weight transfer backend — never requires the m2n runtime to be present.

## Source code in `vllm/distributed/weight_transfer/m2n_common.py`


##

`publish_destination_placements(comm, first_worker_rank, placements, num_parameters)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_common.publish_destination_placements)

Share the worker-side destination plan with every rank in the group.

The trainer must issue each reshard with the same destination the workers use, but once destinations are per-parameter they depend on the inference model, which only the workers can see. The first worker publishes them here, over the shared NCCL communicator; trainer ranks pass `None`

and receive them, and the other workers pass their own so a disagreement is caught rather than deadlocking later.

Only placements travel: the destination *mesh* is still derived from the rank split, identically on both sides. Use the NCCL communicator directly because unique-id rendezvous deliberately has no bootstrap process group.

## Source code in `vllm/distributed/weight_transfer/m2n_common.py`


##

`resolve_layout(mesh, placements, context='placements')`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_common.resolve_layout)

Pair one tensor's placement with the mesh m2n should see for it.

A replicated tensor needs a size-1 mesh axis to carry a no-op shard, since m2n has no `{REPLICATE, REPLICATE}`

. It is therefore described over the *same rank interval* re-factored as `(size, 1)`

. That re-factoring is sound precisely because replication is order-independent — every rank holds the whole tensor, so it does not matter that `(a, b)`

and `(size, 1)`

walk the interval in a different order. A sharded tensor keeps its side's own factorization, where rank order decides who owns which shard.

## Source code in `vllm/distributed/weight_transfer/m2n_common.py`


##

`shard_count(mesh, placements)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_common.shard_count)

How many pieces this layout splits the tensor into.

## Source code in `vllm/distributed/weight_transfer/m2n_common.py`


##

`validate_layout(mesh, placements, shape, side)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_common.validate_layout)

Check a resolved layout can describe `shape`

before any collective runs.

Called on both sides at init so a bad plan surfaces as an error from the init RPC rather than as a hang inside the first reshard.