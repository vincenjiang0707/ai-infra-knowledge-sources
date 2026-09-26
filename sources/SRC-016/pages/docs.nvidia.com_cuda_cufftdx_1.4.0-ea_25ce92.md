source: https://docs.nvidia.com/cuda/cufftdx/1.4.0-ea

# NVIDIA cuFFTDx + cuFFT LTO EA Preview[#](https://docs.nvidia.com#nvidia-cufftdx-cufft-lto-ea-preview)

Welcome to the documentation for the preview release of cuFFTDx with cuFFT-enabled Link Time Optimization Early Access (cuFFTDx + cuFFT LTO EA).

The cuFFTDx + cuFFT LTO EA preview allows you to extend the cuFFTDx library with additional features and performance by reusing optimized code from cuFFT.
The new cuFFT API in this preview allows users to get blobs of device code from cuFFT. These blobs can be linked (offline, or at runtime) with existing cuFFTDx
kernels in order to extract more performance for certain FFT cases.
This preview version currently only supports adding sizes for improved performance and to remove [workspace requirements](https://docs.nvidia.com/cuda/cufftdx/api/traits.html#requiresworkspace-block-trait-label),
but we have plans to extend these features in
the future. Stay tuned!

The documentation consists of four main components:


A quick start guide on how to

[Augment cuFFTDx with LTO].A

[cuFFTDx API Reference]highlighting the newly added cuFFTDx operators and traits in this preview.A

[cuFFT API Reference]for a overview of the cuFFT device APIs added in this preview.

The cuFFTDx + cuFFT LTO EA preview can be found in [NVIDIA cuFFTDx + cuFFT LTO EA Preview](https://developer.nvidia.com/cufftea).

Note

In this documentation, we only document the new cuFFTDx functionalities offered in the cuFFTDx + cuFFT LTO EA preview.
For a comprehensive overview of what cuFFTDx provides, please refer to the [official cuFFTDx documentation](https://docs.nvidia.com/cuda/cufftdx/).

# Highlights[#](https://docs.nvidia.com#highlights)

A new way of enhancing your cuFFTDx project via our cuFFT host library.

Over 1000 additional sizes supported with improved performance and without workspace requirements, via code sharing across our libraries enabled by LTO.

Supporting both offline builds (NVCC) and runtime builds (NVRTC / nvJitLink).

Additional link time optimization in cuFFTDx applications.


Note

The cuFFTDx + cuFFT LTO EA preview, unlike the version of cuFFTDx and cuFFT shipped as part of the MathDx and the CUDA Toolkit respectively, is not a production-ready package. It is meant as a way for users to test LTO-augmented cuFFTDx functionalities, and to provide feedback so that we can improve the experience before this feature makes it into production as part of both cuFFTDx and cuFFT. While we do our best to ship this code without issues, you might encounter occasional bugs.

Please direct any feedback you might have to Melody Shih <[melodys@nvidia.com](mailto:melodys%40nvidia.com)>, or Miguel Ferrer Avila <[mferreravila@nvidia.com](mailto:mferreravila%40nvidia.com)>.