source: https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/sharded_rdt_fake/
lastmod: 2026-09-24

#

`vllm.distributed.weight_transfer.sharded_rdt_fake`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_fake)

Op-chain recording for the sharded-RDT backend.

The consumer asks the trainer for the exact slice a worker consumes, described as an op chain replayed on the trainer's live tensor. `FakeRDTTensor`

builds the chain by intercepting the model's own weight loaders; `copy_`

is its data sink, `BakeSink`

— the dry run records how each slice would be fetched and where it lands.

Chains are built against meta tensors, so nothing here touches Ray or a GPU.

Classes:

-
–[BakeSink](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_fake.BakeSink)`copy_`

sink for the dry-run bake: record how each slice would be fetched -
–[FakeRDTTensor](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_fake.FakeRDTTensor)Zero-storage tensor that records how to fetch a weight slice.


##

`BakeSink`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_fake.BakeSink)

`copy_`

sink for the dry-run bake: record how each slice would be fetched and where it would land, and move nothing.

`_install_recording_stamps`

sets `current = (leaf_module, param_name)`

around each loader so `accept_copy`

can attribute the copy. An unstamped `copy_`

cannot be attributed and stays unrecorded, so its module fails the coverage gate and takes the plain load. `copies_by_layer`

is keyed by module object, so iterating it yields each leaf module once.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_fake.py`


##

`FakeRDTTensor`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_fake.FakeRDTTensor)

Bases: [Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)

Zero-storage tensor that records how to fetch a weight slice.

`_make_wrapper_subclass`

gives it shape/dtype/device without storage. Every op in `SUPPORTED_OPS`

returns a child with the spec appended; `copy_`

delegates to the installed sink. Anything else reaches `__torch_dispatch__`

and raises `_UnsupportedFakeOp`

, so failures are loud rather than silently fetching the wrong bytes.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_fake.py`


|
|

###

`_intercept(self_, func, op_name, args, kwargs)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_fake.FakeRDTTensor._intercept)

Append the op and return a child, or a tuple of children for multi-return ops. Each child's geometry comes from running the op on a meta tensor.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_fake.py`


###

`_make_child(new_shape, new_dtype, *new_ops)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_fake.FakeRDTTensor._make_child)

Append one or more ops to the chain and return a fresh child.

Variadic so multi-return ops (e.g. chunk) can append both the base op and an indexing op in a single call.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_fake.py`


###

`_meta()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_fake.FakeRDTTensor._meta)

A zero-storage meta tensor of this fake's shape/dtype, so PyTorch itself computes post-op geometry rather than us reimplementing it.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_fake.py`


##

`_Scatter`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_fake._Scatter)

One recorded scatter: pull `src`

, copy it into `layer`

's `param_name`

at the recorded strided region. The bake's output unit; see the engine module's Data flow.

Self-contained so replay needs no lookups. Destination geometry is read off the meta view and rebuilt each sync as `as_strided(shape, stride, offset)`

-- `layer`

is resolved to a param at replay time, never baked, since every sync re-materializes fresh tensors.

`shape`

and `dtype`

also size the slice ON THE WIRE, so `dtype`

is the PRODUCED dtype (the fake's after its op chain), not the source name's: `view(dtype)`

is allowlisted, and taking the source's would size the slice with the wrong itemsize and carve the packed blob differently on the two sides.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_fake.py`


##

`_UnsupportedFakeOp`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_fake._UnsupportedFakeOp)

Bases: [NotImplementedError](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError)

Raised when a weight loader does something to a FakeRDTTensor that cannot be expressed as a slice request.

Surfaced as NotImplementedError so callers can distinguish "this backend can't handle this loader" from genuine bugs.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_fake.py`


##

`_freeze_kwargs(kwargs)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_fake._freeze_kwargs)

Sort kwargs into a tuple of items for hashable storage in OpSpec.

##

`_meta_copy_(dest, src)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_fake._meta_copy_)

Fire `dest.copy_`

from a zero-storage meta source of `src`

's geometry.

Moves no data but still counts against the layer's loaded numel, which drives `_layerwise_process`

; skipping it would leave the layer looking unloaded forever.

A non-meta `dest`

is one the layerwise reload never moved there (the `SKIP_LOAD_TENSORS`

set, e.g. GLM's router bias). Torch forbids `real.copy_(meta)`

, and skipping the count is consistent -- `get_layer_size`

excludes the same set. The caller still RECORDS the copy, so the replay writes the real param.