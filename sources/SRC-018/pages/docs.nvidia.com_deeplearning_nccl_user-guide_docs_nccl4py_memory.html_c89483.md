source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/nccl4py/memory.html

# Memory Management[](https://docs.nvidia.com#memory-management)

NCCL-backed device memory allocation; see [Memory Allocator](https://docs.nvidia.com/usage/bufferreg.html#mem-allocator) for
usage details. For zero-copy registration of existing buffers, see
[ Communicator.register_buffer()](https://docs.nvidia.com/communicator/registration.html#nccl.core.Communicator.register_buffer) and

[.](https://docs.nvidia.com/communicator/registration.html#nccl.core.Communicator.register_window)

`Communicator.register_window()`

## mem_alloc[](https://docs.nvidia.com#mem-alloc)

-
nccl.core.mem_alloc(
*size: int*,*device:*)[Device](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Device.html#cuda.core.Device)| int | None = None[Buffer](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Buffer.html#cuda.core.Buffer)[](https://docs.nvidia.com#nccl.core.mem_alloc) Allocates GPU buffer memory using NCCL’s memory allocator.

The actual allocated size may be larger than requested due to buffer granularity requirements from NCCL optimizations. The returned buffer can be explicitly freed with

or automatically freed when garbage collected.`mem_free()`

- Parameters:
**size**– Number of bytes to allocate.**device**– Target CUDA device. Defaults to the current device.

- Returns:
A CUDA buffer object backed by NCCL-managed memory. The buffer is allocated on the specified device; the current device is restored after allocation.



## mem_free[](https://docs.nvidia.com#mem-free)

-
nccl.core.mem_free(
*buf:*) None[Buffer](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Buffer.html#cuda.core.Buffer)[](https://docs.nvidia.com#nccl.core.mem_free) Frees memory allocated by

.`mem_alloc()`

Explicit deallocation is optional. Memory is automatically freed when the Buffer object is garbage collected.

- Parameters:
**buf**– The buffer to free.