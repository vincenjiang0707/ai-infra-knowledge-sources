source: https://docs.nvidia.com/cuda/cublasdx

# NVIDIA cuBLASDx[#](https://docs.nvidia.com#nvidia-cublasdx)

The cuBLAS Device Extensions (cuBLASDx) library enables you to perform selected linear algebra functions known from
[cuBLAS](https://docs.nvidia.com/cuda/cublas/) inside your CUDA kernel.
Available routines include General Matrix Multiplication (GEMM) and Triangular Solve (TRSM).
Fusing linear algebra routines with other operations can decrease the latency and improve the overall performance of
your application.

The documentation consists of the following components:

A GEMM quick start guide,

[Using cuBLASDx GEMM](https://docs.nvidia.com/using_cublasdx.html#intro1-label).A TRSM quick start guide,

[Using cuBLASDx TRSM](https://docs.nvidia.com/using_trsm.html#intro3-label).An advanced pipelining API guide,

[Using Pipelined GEMM](https://docs.nvidia.com/using_pipelines.html#intro2-label).A learning path through examples,

[Learning Path Through Examples](https://docs.nvidia.com/examples_learning_path.html#examples-learning-path-label).An

[API Reference](https://docs.nvidia.com/api/index.html#api-reference-label)for a comprehensive overview of the provided functionality.

If you are implementing GEMM from scratch, start with [Quick Installation Guide](https://docs.nvidia.com/installation.html#quick-installation-guide-label), then read
[Using cuBLASDx GEMM](https://docs.nvidia.com/using_cublasdx.html#intro1-label), and use [Learning Path Through Examples](https://docs.nvidia.com/examples_learning_path.html#examples-learning-path-label) to choose the nearest working example before tuning.

## The cuBLASDx Library Currently Provides:[#](https://docs.nvidia.com#the-cublasdx-library-currently-provides)

Customizability, options to adjust BLAS routines for different needs (size, precision, type, targeted CUDA architecture, etc.).

Flexibility of performing accumulation and fusion in either shared memory or registers.

Ability to fuse BLAS kernels with other operations in order to save global memory trips.

Compatibility with future versions of the CUDA Toolkit.

- Autovectorizing high performance data movement between shared and global memory.
Opaque analytical generation of swizzled layouts for best performance.

Currently dispatches to either vectorized

`LDG+STS`

or`LDGSTS`

.



## The Pipelining Extension To cuBLASDx (`0.5.0+`

) Offers:[#](https://docs.nvidia.com#the-pipelining-extension-to-cublasdx-0-5-0-offers)

- Automatic N-buffer staged pipelined GEMM execution.
Overlaps asynchronous load stages with asynchronous compute stages; multiple stages of both kinds can be in flight.

Runs one epilogue stage after K-stage accumulation completes.

Increases the number of bytes and instructions in flight during computation.

Better exposing GPU asynchronicity to

`cuBLASDx`

users.Barrier based synchronization, compatible with Turing+ GPUs.



- Automatic dispatching between
`TMA / LDGSTS / LDG+STS`

for global to shared transfers. Fully asynchronous transfers where possible.

Automatic maximal vectorization and equal work division among threads.

Opaque generation of swizzled layouts for shared memory.



- Automatic dispatching between
Automatic internal exposure of selected

`WGMMA / 1SM UTCMMA`

instructions.Automatic opaque warp specialization in selected cases.

Automatic opaque register trading in selected cases.

The same interface on all CUDA architectures.