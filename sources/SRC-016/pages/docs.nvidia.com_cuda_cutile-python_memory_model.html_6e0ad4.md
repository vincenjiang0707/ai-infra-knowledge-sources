source: https://docs.nvidia.com/cuda/cutile-python/memory_model.html

# Memory Model[#](https://docs.nvidia.com#memory-model)

cuTile’s memory model permits the compiler and hardware to reorder operations
for performance. Without explicit synchronization, the ordering of memory
accesses across [blocks](https://docs.nvidia.com/execution.html#block) is not guaranteed.

To coordinate memory accesses between [blocks](https://docs.nvidia.com/execution.html#block), cuTile provides two attributes
for atomic operations:

**Memory Order**— defines the ordering semantics of an atomic operation.**Memory Scope**— defines the set of[blocks](https://docs.nvidia.com/execution.html#block)that participate in ordering.

Synchronization operates at per-element granularity: each element in the array participates independently in the memory model.

For further details, see the Memory Model section of the [Tile IR documentation](https://docs.nvidia.com/cuda/tile-ir/).

## Memory Order[#](https://docs.nvidia.com#memory-order)

-
*class*cuda.tile.MemoryOrder[#](https://docs.nvidia.com#cuda.tile.MemoryOrder) Memory ordering semantics of a memory operation.

-
WEAK
*= 'weak'*[#](https://docs.nvidia.com#cuda.tile.MemoryOrder.WEAK) Weak (non-atomic) ordering. The default for load/store operations.


-
RELAXED
*= 'relaxed'*[#](https://docs.nvidia.com#cuda.tile.MemoryOrder.RELAXED) No ordering guarantees. Cannot be used to synchronize between threads.


-
ACQUIRE
*= 'acquire'*[#](https://docs.nvidia.com#cuda.tile.MemoryOrder.ACQUIRE) Acquire semantics. When this reads a value written by a release, the releasing thread’s prior writes become visible. Subsequent reads/writes within the same block cannot be reordered before this operation.


-
RELEASE
*= 'release'*[#](https://docs.nvidia.com#cuda.tile.MemoryOrder.RELEASE) Release semantics. When an acquire reads the value written by this, this thread’s prior writes become visible to the acquiring thread. Prior reads/writes within the same block cannot be reordered after this operation.


-
ACQ_REL
*= 'acq_rel'*[#](https://docs.nvidia.com#cuda.tile.MemoryOrder.ACQ_REL) Combined acquire and release semantics.


-
WEAK

## Memory Scope[#](https://docs.nvidia.com#memory-scope)

-
*class*cuda.tile.MemoryScope[#](https://docs.nvidia.com#cuda.tile.MemoryScope) The scope of threads that participate in memory ordering.

-
NONE
*= 'none'*[#](https://docs.nvidia.com#cuda.tile.MemoryScope.NONE) No memory scope. Used for load/store operations with WEAK memory ordering.


-
BLOCK
*= 'block'*[#](https://docs.nvidia.com#cuda.tile.MemoryScope.BLOCK) Ordering guarantees apply to threads within the same block.


-
CLUSTER
*= 'cluster'*[#](https://docs.nvidia.com#cuda.tile.MemoryScope.CLUSTER) Ordering guarantees apply to all threads within the same thread-block cluster. cuda.lang only.


-
DEVICE
*= 'device'*[#](https://docs.nvidia.com#cuda.tile.MemoryScope.DEVICE) Ordering guarantees apply to all threads on the same GPU.


-
SYS
*= 'sys'*[#](https://docs.nvidia.com#cuda.tile.MemoryScope.SYS) Ordering guarantees apply to all threads across the entire system, including multiple GPUs and the host.


-
NONE