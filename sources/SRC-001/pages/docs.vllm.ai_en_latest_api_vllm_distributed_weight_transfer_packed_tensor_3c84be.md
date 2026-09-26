source: https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/packed_tensor/
lastmod: 2026-09-24

#

`vllm.distributed.weight_transfer.packed_tensor`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor)

Packed tensor utilities for efficient weight transfer.

Classes:

-
–[PackedBufferImporter](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.PackedBufferImporter)One-slot cache for the consumer-side mapping of a packed IPC buffer.

-
–[PackedChunk](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.PackedChunk)Result of packing tensors into a single contiguous uint8 buffer.

-
–[PackedIpcChunk](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.PackedIpcChunk)Metadata and IPC handle for a single packed chunk.


Functions:

-
–[pack_tensors](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.pack_tensors)Pack tensors from an iterator into a single contiguous uint8 buffer.

-
–[packed_ipc_consumer](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_ipc_consumer)Unpack a single packed IPC chunk into named tensors.

-
–[packed_ipc_producer](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_ipc_producer)Pack tensors into a reusable IPC buffer and yield handles.

-
–[packed_nccl_broadcast_consumer](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_nccl_broadcast_consumer)Consume packed tensors and unpack them into a list of tensors.

-
–[packed_nccl_broadcast_producer](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_nccl_broadcast_producer)Broadcast tensors in a packed manner from trainer to workers.

-
–[unpack_tensor](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.unpack_tensor)Unpack a packed uint8 tensor into a list of named tensors.


##

`PackedBufferImporter`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.PackedBufferImporter)

One-slot cache for the consumer-side mapping of a packed IPC buffer.

torch's cross-process refcount pairs one `reduce_tensor`

export with one consumer rebuild-release cycle. The producer exports its buffer once and ships the same args with every chunk, so rebuilding and releasing per chunk decrements the counter once per chunk, drives it negative, and the dropped buffer is then never reclaimable by `ipc_collect`

on the producer side (it leaks one buffer per transfer). Caching the rebuilt buffer keyed by the rebuild args restores the pairing: chunks of one transfer reuse the mapping (it aliases producer memory, so it always reads the current chunk's bytes), and replacing the entry when the next export arrives — or `close()`

— releases the previous mapping exactly once.

The importer that consumes a multi-chunk transfer must be one object reused across chunks; a fresh importer per chunk reintroduces the per-chunk release. `IPCWeightTransferEngine`

owns one instance per engine and closes it on shutdown.

Methods:

-
–[close](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.PackedBufferImporter.close)Release the held mapping (one producer-side refcount decrement).


## Source code in `vllm/distributed/weight_transfer/packed_tensor.py`


##

`PackedChunk`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.PackedChunk)

Result of packing tensors into a single contiguous uint8 buffer.

## Source code in `vllm/distributed/weight_transfer/packed_tensor.py`


##

`PackedIpcChunk`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.PackedIpcChunk)

Metadata and IPC handle for a single packed chunk.

## Source code in `vllm/distributed/weight_transfer/packed_tensor.py`


##

`pack_tensors(iterator, post_iter_func, buffer_size_bytes, tensor_list=None, current_size=0)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.pack_tensors)

Pack tensors from an iterator into a single contiguous uint8 buffer.

Consumes from the iterator until the accumulated size exceeds buffer_size_bytes or the iterator is exhausted, then returns a PackedChunk. Returns None if no tensors were consumed.

Parameters:

-

(`iterator`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.pack_tensors(iterator))

) –[Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]]Iterator of (name, tensor) pairs

-

(`post_iter_func`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.pack_tensors(post_iter_func))

) –[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]],[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]Applied to each item before linearizing to uint8

-

(`buffer_size_bytes`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.pack_tensors(buffer_size_bytes))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Max bytes before flushing

-

(`tensor_list`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.pack_tensors(tensor_list))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)] | None`None`

) –Pre-existing tensor list to append to (for NCCL multi-buffer reuse). If None, a fresh list is created.

-

(`current_size`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.pack_tensors(current_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –Byte count already accumulated in tensor_list


## Source code in `vllm/distributed/weight_transfer/packed_tensor.py`


##

`packed_ipc_consumer(ipc_handle, names, shapes, dtype_names, tensor_sizes, device_index, importer=None)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_ipc_consumer)

Unpack a single packed IPC chunk into named tensors.

Reconstructs the packed buffer via rebuild_cuda_tensor, unpacks into individual tensors, and clones each into independent storage before returning.

The clone is intentional: the producer reuses one IPC buffer across chunks, so any tensor view that aliases the buffer would observe the *next* chunk's bytes as soon as the producer's generator is resumed. Callers that retain references past their own update_weights call (notably vLLM's layerwise reload, which buffers `bound_args`

for replay in `_layerwise_process`

) would otherwise replay against stale data and silently corrupt multi-chunk weight transfers.

Parameters:

-

(`ipc_handle`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_ipc_consumer(ipc_handle))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)]Mapping of GPU UUID to rebuild_cuda_tensor args tuple

-

(`names`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_ipc_consumer(names))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Parameter names in the packed buffer

-

(`shapes`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_ipc_consumer(shapes))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]Parameter shapes

-

(`dtype_names`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_ipc_consumer(dtype_names))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Parameter dtype name strings (e.g. "float16")

-

(`tensor_sizes`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_ipc_consumer(tensor_sizes))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]Size in bytes of each parameter in the packed buffer

-

(`device_index`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_ipc_consumer(device_index))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Local CUDA device index

-

(`importer`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_ipc_consumer(importer))

, default:[PackedBufferImporter](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.PackedBufferImporter)| None`None`

) –Import cache that must be shared across all chunks of one export so the buffer mapping is opened and released exactly once (see

`PackedBufferImporter`

).`None`

builds an ephemeral one, which is only safe for single-chunk consumption.

## Source code in `vllm/distributed/weight_transfer/packed_tensor.py`


##

`packed_ipc_producer(iterator, gpu_uuid, post_iter_func, buffer_size_bytes=DEFAULT_PACKED_BUFFER_SIZE_BYTES)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_ipc_producer)

Pack tensors into a reusable IPC buffer and yield handles.

Allocates a single GPU buffer of `buffer_size_bytes`

and registers it for IPC once via `reduce_tensor`

. Each chunk's packed data is copied into this buffer before yielding, so only one IPC-shared allocation exists for the lifetime of the transfer.

Callers **must** ensure the consumer has finished reading the buffer (e.g. `ray.get`

returned) before resuming the generator for the next chunk.

Parameters:

-

(`iterator`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_ipc_producer(iterator))

) –[Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]]Iterator of (name, tensor) pairs.

-

(`gpu_uuid`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_ipc_producer(gpu_uuid))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Physical GPU UUID string for this rank.

-

(`post_iter_func`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_ipc_producer(post_iter_func))

) –[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]],[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]Applied to each (name, tensor) before packing.

-

(`buffer_size_bytes`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_ipc_producer(buffer_size_bytes))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`DEFAULT_PACKED_BUFFER_SIZE_BYTES`

) –Exact capacity of the reusable IPC buffer. Every chunk is guaranteed to fit within this size. A

`ValueError`

is raised if any single tensor exceeds it.

## Source code in `vllm/distributed/weight_transfer/packed_tensor.py`


|
|

##

`packed_nccl_broadcast_consumer(iterator, group, src, post_unpack_func, buffer_size_bytes=DEFAULT_PACKED_BUFFER_SIZE_BYTES, num_buffers=DEFAULT_PACKED_NUM_BUFFERS, device='cuda')`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_nccl_broadcast_consumer)

Consume packed tensors and unpack them into a list of tensors.

Parameters:

-

(`iterator`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_nccl_broadcast_consumer(iterator))

) –[Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)],[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)]]]Iterator of parameter metadata. Returns (name, (shape, dtype))

-

(`group`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_nccl_broadcast_consumer(group))

) –[Any](https://docs.python.org/3/library/typing.html#typing.Any)Process group (PyNcclCommunicator)

-

(`src`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_nccl_broadcast_consumer(src))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Source rank (0 in current implementation)

-

(`post_unpack_func`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_nccl_broadcast_consumer(post_unpack_func))

) –[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]]], None]Function to apply to each list of (name, tensor) after unpacking

-

(`buffer_size_bytes`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_nccl_broadcast_consumer(buffer_size_bytes))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`DEFAULT_PACKED_BUFFER_SIZE_BYTES`

) –Size in bytes for each packed tensor buffer. Both producer and consumer must use the same value.

-

(`num_buffers`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_nccl_broadcast_consumer(num_buffers))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`DEFAULT_PACKED_NUM_BUFFERS`

) –Number of buffers for double/triple buffering. Both producer and consumer must use the same value.

-

(`device`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_nccl_broadcast_consumer(device))

, default:[device](https://pytorch.org/docs/stable/tensor_attributes.html#torch.device)|[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'cuda'`

) –Device for the receive buffers. Must match the device the NCCL communicator was created on (the worker's assigned device).


## Source code in `vllm/distributed/weight_transfer/packed_tensor.py`


|
|

##

`packed_nccl_broadcast_producer(iterator, group, src, post_iter_func, buffer_size_bytes=DEFAULT_PACKED_BUFFER_SIZE_BYTES, num_buffers=DEFAULT_PACKED_NUM_BUFFERS)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_nccl_broadcast_producer)

Broadcast tensors in a packed manner from trainer to workers.

Parameters:

-

(`iterator`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_nccl_broadcast_producer(iterator))

) –[Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]]Iterator of model parameters. Returns a tuple of (name, tensor)

-

(`group`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_nccl_broadcast_producer(group))

) –[Any](https://docs.python.org/3/library/typing.html#typing.Any)Process group (PyNcclCommunicator)

-

(`src`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_nccl_broadcast_producer(src))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Source rank (0 in current implementation)

-

(`post_iter_func`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_nccl_broadcast_producer(post_iter_func))

) –[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]],[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]Function to apply to each (name, tensor) pair before packing, should return a tensor

-

(`buffer_size_bytes`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_nccl_broadcast_producer(buffer_size_bytes))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`DEFAULT_PACKED_BUFFER_SIZE_BYTES`

) –Size in bytes for each packed tensor buffer. Both producer and consumer must use the same value.

-

(`num_buffers`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.packed_nccl_broadcast_producer(num_buffers))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`DEFAULT_PACKED_NUM_BUFFERS`

) –Number of buffers for double/triple buffering. Both producer and consumer must use the same value.


## Source code in `vllm/distributed/weight_transfer/packed_tensor.py`


##

`unpack_tensor(packed_tensor, names, shapes, dtypes, tensor_sizes)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.unpack_tensor)

Unpack a packed uint8 tensor into a list of named tensors.

The returned tensors are **views** of `packed_tensor`

(the `.contiguous()`

call is a no-op on already-contiguous row-slices). If `packed_tensor`

lives in storage that may be reused — e.g. a reused CUDA IPC buffer — callers must clone the results before the underlying storage is overwritten.

Parameters:

-

(`packed_tensor`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.unpack_tensor(packed_tensor))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The packed torch.uint8 tensor to unpack

-

(`names`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.unpack_tensor(names))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]List of tensor names

-

(`shapes`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.unpack_tensor(shapes))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]List of tensor shapes

-

(`dtypes`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.unpack_tensor(dtypes))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)]List of tensor dtypes

-

(`tensor_sizes`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.packed_tensor.unpack_tensor(tensor_sizes))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]List of tensor sizes in bytes