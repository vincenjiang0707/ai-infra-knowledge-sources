source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/nccl4py/communicator/registration.html

# Memory Registration Methods[](https://docs.nvidia.com#memory-registration-methods)

Methods on [ Communicator](https://docs.nvidia.com/class.html#nccl.core.Communicator) for registering buffers and windows for
zero-copy and RMA operations. The returned handle classes are documented
under

[Communicator Resources](https://docs.nvidia.com/resources.html).

## register_buffer[](https://docs.nvidia.com#register-buffer)

-
Communicator.register_buffer(
*buffer:*)[Buffer](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Buffer.html#cuda.core.Buffer)| SupportsDLPack | SupportsCAI[RegisteredBufferHandle](https://docs.nvidia.com/resources.html#nccl.core.RegisteredBufferHandle)[](https://docs.nvidia.com#nccl.core.Communicator.register_buffer) Registers a buffer with this communicator for zero-copy communication.

Registered buffers can enable performance optimizations in NCCL operations. Buffer size is automatically derived from buffer count and dtype. The returned

is tracked by the communicator and may be released explicitly via its`RegisteredBufferHandle`

method, or automatically when the communicator is destroyed or aborted.`close()`

- Parameters:
**buffer**– Buffer to register (array, Buffer, or buffer-like object).- Returns:
for the registered buffer.`RegisteredBufferHandle`

- Raises:
– If the buffer is on the wrong device or the communicator is not initialized.**NcclInvalid**

See also


## register_window[](https://docs.nvidia.com#register-window)

-
Communicator.register_window(
*buffer:*,[Buffer](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Buffer.html#cuda.core.Buffer)| SupportsDLPack | SupportsCAI*flags:*)[WindowFlag](https://docs.nvidia.com#nccl.core.WindowFlag)| None = None[RegisteredWindowHandle](https://docs.nvidia.com/resources.html#nccl.core.RegisteredWindowHandle)[](https://docs.nvidia.com#nccl.core.Communicator.register_window) Collectively registers a local buffer into an NCCL window.

This is a collective call: every rank in the communicator must participate. Buffer size is automatically derived from buffer count and dtype.

If called within a group, the handle value may not be filled until

`ncclGroupEnd`

completes. For non-blocking communicators, the handle may remain`0`

untilreports success.`get_async_error()`

The returned

is tracked by the communicator and may be released explicitly via its`RegisteredWindowHandle`

method, or automatically when the communicator is destroyed or aborted.`close()`

- Parameters:
**buffer**– Local buffer to register as a window.**flags**– Window registration flags. Defaults to`None`

().`DEFAULT`


- Returns:
for the registered window. Its handle remains`RegisteredWindowHandle`

`0`

while registration is pending, or when windows are unsupported on the platform.- Raises:
– If the buffer is on the wrong device or the communicator is not initialized.**NcclInvalid**

See also


## WindowFlag[](https://docs.nvidia.com#windowflag)

-
*class*nccl.core.WindowFlag(*value*,*names=<not given>*,**values*,*module=None*,*qualname=None*,*type=None*,*start=1*,*boundary=None*)[](https://docs.nvidia.com#nccl.core.WindowFlag) Bases:

`IntFlag`

Window registration behavior flags for

.`Communicator.register_window()`

-
DEFAULT
*= 0*[](https://docs.nvidia.com#nccl.core.WindowFlag.DEFAULT) Default window registration.


-
COLL_SYMMETRIC
*= 1*[](https://docs.nvidia.com#nccl.core.WindowFlag.COLL_SYMMETRIC) Collective symmetric window registration.


-
STRICT_ORDERING
*= 2*[](https://docs.nvidia.com#nccl.core.WindowFlag.STRICT_ORDERING) Strict ordering for window operations.


-
GIN_ONLY
*= 4*[](https://docs.nvidia.com#nccl.core.WindowFlag.GIN_ONLY) Register the window for GIN access only (NCCL 2.32+).


-
CFT_COUNTED
*= 8*[](https://docs.nvidia.com#nccl.core.WindowFlag.CFT_COUNTED) Register the window against counted CFT logical endpoints instead of the default non-counted ones (NCCL 2.32+).


-
DEFAULT