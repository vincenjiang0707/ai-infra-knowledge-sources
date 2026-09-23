source: https://docs.vllm.ai/en/latest/api/vllm/distributed/ec_transfer/ec_connector/cpu/worker/descriptor_buffers/
lastmod: 2026-09-23

#

`vllm.distributed.ec_transfer.ec_connector.cpu.worker.descriptor_buffers`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.descriptor_buffers)

Reusable pool of (src_ptrs, dst_ptrs, sizes) tensor triples.

Used by ECCPUWorker to batch swap_blocks_batch descriptors without per-step allocation overhead.

Classes:

-
–[DescriptorBufferPool](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.descriptor_buffers.DescriptorBufferPool)Pool of descriptor buffer triples for swap_blocks_batch.

-
–[DescriptorBuffers](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.descriptor_buffers.DescriptorBuffers)

##

`DescriptorBufferPool`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.descriptor_buffers.DescriptorBufferPool)

Pool of descriptor buffer triples for swap_blocks_batch.

Each buffer is a `DescriptorBuffers`

namedtuple of three 1-D tensors (dtype `_PTR_DTYPE`

, platform-dependent) of equal length, paired with numpy aliases used to fill them. Buffers are recycled across steps; if a returned buffer is too small it is discarded and a fresh one allocated.

Methods:

-
–[acquire](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.descriptor_buffers.DescriptorBufferPool.acquire)Get a buffer triple with capacity >=

*n*. -
–[release](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.descriptor_buffers.DescriptorBufferPool.release)Return a buffer triple to the pool for reuse.


## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/worker/descriptor_buffers.py`


###

`acquire(n)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.descriptor_buffers.DescriptorBufferPool.acquire)

Get a buffer triple with capacity >= *n*.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/worker/descriptor_buffers.py`


##

`DescriptorBuffers`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.descriptor_buffers.DescriptorBuffers)

Bases: [NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple)

Methods:

-
–[add_copies](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.descriptor_buffers.DescriptorBuffers.add_copies)Store a batch of copies in these buffers, the first at

*first*.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/worker/descriptor_buffers.py`


###

`add_copies(first, sources, destinations, byte_counts)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.descriptor_buffers.DescriptorBuffers.add_copies)

Store a batch of copies in these buffers, the first at *first*.

One copy is one source address, one destination address, and a number of bytes. `swap_blocks_batch`

performs every copy held in the buffers in a single call, so a caller fills in all of a step's copies before asking for any of them to run, and passes *first* to say where its own copies begin.

Whole batches go in at once because storing a single number into a torch tensor costs microseconds. Adding copies one at a time can take longer than performing them.

TODO(torch>=2.14): write the tensors directly and drop these numpy aliases once the minimum supported torch is 2.14. They exist only because torch's setitem unpacks the value as a signed long long before 2.14 (pytorch#191458), rejecting XPU USM addresses >= 2**63, while the two's-complement rewrite those versions accept is in turn rejected by uint64 from 2.14 on. Numpy casts against the array's own type and so works on either. Byte counts are small enough to need none of this care, and use their alias only to match the addresses.