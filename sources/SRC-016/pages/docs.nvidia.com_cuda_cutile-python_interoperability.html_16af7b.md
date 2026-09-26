source: https://docs.nvidia.com/cuda/cutile-python/interoperability.html

# Interoperability[#](https://docs.nvidia.com#interoperability)

## Machine Representation[#](https://docs.nvidia.com#machine-representation)

cuTile executes Python [tile code](https://docs.nvidia.com/execution.html#tile-code) on NVIDIA GPUs by translating the Python code into a *machine representation* that can be executed by CUDA devices.
Functions, types, and objects all have a machine representation.

Machine representations are defined in terms of corresponding CUDA C++ entities.
Example: `cuda.tile.float16`

has the same machine representation as `__half`

in CUDA C++.

## Interoperability with SIMT[#](https://docs.nvidia.com#interoperability-with-simt)

### Inter-Kernel[#](https://docs.nvidia.com#inter-kernel)

Inter-kernel interoperability refers to all interoperability concerns that do not cross the kernel boundary - everything except mixing tile and SIMT code in a kernel. This includes:

Writing tile and SIMT kernels in the same source file.

Linking tile and SIMT kernels into the same binary.

Passing the same kinds of arrays to both tile and SIMT kernels.


Intra-kernel interoperability will be supported in the future.

## JAX FFI[#](https://docs.nvidia.com#jax-ffi)

cuTile kernels can be launched from JAX-traced graphs via
[ cuda.tile.jax.cutile_call()](https://docs.nvidia.com/generated/cuda.tile.jax.cutile_call.html#cuda.tile.jax.cutile_call), which threads buffers, scalar, and
tuple arguments through the JAX FFI call site so the kernel runs as a
regular op inside a

`jax.jit`

-compiled graph.See [ cuda.tile.jax.cutile_call()](https://docs.nvidia.com/generated/cuda.tile.jax.cutile_call.html#cuda.tile.jax.cutile_call) for the full argument convention,
along with

[and](https://docs.nvidia.com/generated/cuda.tile.jax.OutputPlaceholder.html#cuda.tile.jax.OutputPlaceholder)

`cuda.tile.jax.OutputPlaceholder`

[for declaring outputs and in-place updates.](https://docs.nvidia.com/generated/cuda.tile.jax.InputOutput.html#cuda.tile.jax.InputOutput)

`cuda.tile.jax.InputOutput`