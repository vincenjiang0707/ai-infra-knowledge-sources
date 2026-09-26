source: https://docs.nvidia.com/cuda/cufftdx/index.html

# NVIDIA cuFFTDx[#](https://docs.nvidia.com#nvidia-cufftdx)

The cuFFT Device Extensions ([cuFFTDx](https://developer.nvidia.com/cufftdx-downloads)) library enables you to perform Fast Fourier Transform (FFT) calculations
inside your CUDA kernel. Fusing FFT with other operations can decrease the latency and improve the performance of
your application.

The documentation consists of three main components:


A quick start guide,

[First FFT Using cuFFTDx].A guide to

[augment cuFFTDx with cuFFT LTO]for additional performance without requiring workspace.An

[cuFFTDx API Reference]for a comprehensive overview of the provided functionality.

# Highlights[#](https://docs.nvidia.com#highlights)

The cuFFTDx library provides:

Fast Fourier Transform (FFT) CUDA functions embeddable into a CUDA kernel.

High performance, no unnecessary data movement from and to global memory.

Customizability, options to adjust selection of FFT routine for different needs (size, precision, number of batches, etc.).

Ability to fuse FFT kernels with other operations in order to save global memory trips.

Compatibility with future versions of the CUDA Toolkit.