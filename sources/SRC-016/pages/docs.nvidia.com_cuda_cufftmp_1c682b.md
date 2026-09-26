source: https://docs.nvidia.com/cuda/cufftmp/

# NVIDIA cuFFTMp documentation[#](https://docs.nvidia.com#nvidia-cufftmp-documentation)

Welcome to the cuFFTMp (cuFFT Multi-process) library.

You can find here:


A

[Quick start]guideA

[How to use cuFFTMp]section, describing the requirements and general usage of cuFFTMpAn

[API reference]section, with a comprehensive description of all of cuFFTMp’s APIs

cuFFTMp is distributed as part of the [NVIDIA HPC-SDK](https://developer.nvidia.com/hpc-sdk) and through [NVIDIA Developer Zone](https://developer.nvidia.com/cufftmp-downloads).

# Highlights[#](https://docs.nvidia.com#highlights)

2D and 3D multi-GPU, multi-node (MGMN) FFTs

Slabs (1D) and pencils (2D) data decomposition, with arbitrary block sizes

MPI-compatible interface

Low-latency implementation using NVSHMEM, optimized for single-node and multi-node FFTs

`x86_64`

and`aarch64`

support (see[Hardware and software requirements](https://docs.nvidia.com/usage/requirements.html#requirements-label))