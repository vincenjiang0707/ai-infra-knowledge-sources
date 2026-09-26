source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/nccl4py/interop.html

# Framework Interop[](https://docs.nvidia.com#framework-interop)

Lazy-loaded helpers for allocating CuPy arrays and PyTorch tensors backed by
NCCL-managed memory, plus resolvers that translate framework objects into
the `(ptr, count, dtype, device_id)`

tuple NCCL expects. The submodules
are imported on first attribute access via `nccl.core.cupy`

and
`nccl.core.torch`

.

## CuPy[](https://docs.nvidia.com#cupy)

-
nccl.core.interop.cupy.empty(
*shape: int | tuple[int, ...], dtype: str | np.dtype | cupy.dtype | type = <class 'float'>, order: Literal['C', 'F'] = 'C'*) cupy.ndarray[](https://docs.nvidia.com#nccl.core.interop.cupy.empty) Creates an uninitialized CuPy array backed by NCCL-allocated memory.

Returns an array filled with uninitialized data using NCCL’s memory allocator. This provides a CuPy-compatible interface while using NCCL’s memory allocator for efficient GPU memory management in distributed scenarios. Unlike cupy.empty, the underlying memory is allocated through NCCL.

Memory is automatically freed when the array is garbage collected; no explicit free call is required. For zero-copy optimization, register the array using

or`register_buffer()`

.`register_window()`

- Parameters:
**shape**– Shape of the array.**dtype**– Data type specifier. Defaults to`float`

.**order**– Memory layout. ‘C’ for row-major (C-style), ‘F’ for column-major (Fortran-style). Defaults to ‘C’.

- Returns:
An uninitialized CuPy array backed by NCCL-allocated memory.

- Raises:
– If order is not ‘C’ or ‘F’.**NcclInvalid****ModuleNotFoundError**– If CuPy is not installed.



-
nccl.core.interop.cupy.resolve_array(
*array: cupy.ndarray*) tuple[int, int,[NcclDataType](https://docs.nvidia.com/types.html#nccl.core.NcclDataType), int][](https://docs.nvidia.com#nccl.core.interop.cupy.resolve_array) Resolves a CuPy array to its NCCL buffer descriptor.

- Parameters:
**array**– CuPy array to resolve.- Returns:
*Tuple of (ptr, count, dtype, device_id)*– device pointer, element count, NCCL data type, and CUDA device ID.- Raises:
**ModuleNotFoundError**– If CuPy is not installed.– If array is not a CuPy ndarray or its dtype has no NCCL equivalent.**NcclInvalid**



## PyTorch[](https://docs.nvidia.com#pytorch)

-
nccl.core.interop.torch.empty(
**size*,*dtype: torch.dtype | None = None*,*device: torch.device | int | str | None = None*,*morder: Literal['C', 'F'] = 'C'*) torch.Tensor[](https://docs.nvidia.com#nccl.core.interop.torch.empty) Creates an uninitialized PyTorch tensor backed by NCCL-allocated memory.

Returns a tensor filled with uninitialized data using NCCL’s memory allocator. This provides a PyTorch-compatible interface while using NCCL’s memory allocator for efficient GPU memory management in distributed scenarios. Unlike torch.empty, the underlying memory is allocated through NCCL.

Memory is automatically freed when the tensor is garbage collected; no explicit free call is required. For zero-copy optimization, register the tensor using

or`register_buffer()`

.`register_window()`

- Parameters:
***size**– A sequence of integers defining the shape of the output tensor. Can be a variable number of arguments or a single list/tuple.**dtype**– Desired data type of the tensor. If`None`

, uses torch.get_default_dtype(). Defaults to`None`

.**device**– Device of the tensor. If`None`

, uses the current CUDA device. Defaults to`None`

.**morder**– Memory layout. ‘C’ for row-major (C-style), ‘F’ for column-major (Fortran-style). Defaults to ‘C’.

- Returns:
An uninitialized PyTorch tensor backed by NCCL-allocated memory.

- Raises:
– If morder is not ‘C’ or ‘F’, or device is not a CUDA device.**NcclInvalid****ModuleNotFoundError**– If PyTorch is not installed.



-
nccl.core.interop.torch.resolve_tensor(
*tensor: torch.Tensor*) tuple[int, int,[NcclDataType](https://docs.nvidia.com/types.html#nccl.core.NcclDataType), int][](https://docs.nvidia.com#nccl.core.interop.torch.resolve_tensor) Resolves a PyTorch tensor to its NCCL buffer descriptor.

- Parameters:
**tensor**– PyTorch tensor to resolve.- Returns:
*Tuple of (ptr, count, dtype, device_id)*– device pointer, element count, NCCL data type, and CUDA device ID.- Raises:
**ModuleNotFoundError**– If PyTorch is not installed.– If tensor is not a PyTorch tensor or its dtype has no NCCL equivalent.**NcclInvalid**