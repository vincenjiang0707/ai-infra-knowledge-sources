source: https://rocm.docs.amd.com/projects/hipFFT/en/latest

# hipFFT and hipFFTW documentation[#](https://rocm.docs.amd.com#hipfft-and-hipfftw-documentation)

hipFFT is an FFT (fast Fourier transform) marshalling library. It supports either [rocFFT](https://rocm.docs.amd.com/projects/rocFFT/en/latest/index.html) or
NVIDIA CUDA [cuFFT](https://developer.nvidia.com/cufft) as the backend. hipFFT sits between the
application and the backend FFT library, marshalling inputs into the
backend and results back to the application.
hipFFT requires its computational input and output data to be GPU-visible. Data residing in device memory is
recommended as it typically delivers the best performance.

hipFFTW is a GPU-aware library for fast Fourier transforms using [rocFFT](https://rocm.docs.amd.com/projects/rocFFT/en/latest/index.html) as the backend. It
exports an interface borrowing the most commonly-used symbols of [FFTW](https://www.fftw.org/). hipFFTW does not require its
computational input and output to be directly accessible by the GPU.

For more information, see the [Overview of hipFFT and hipFFTW](https://rocm.docs.amd.com/conceptual/overview.html#overview-of-hipfft-and-hipfftw).

hipFFT and hipFFTW share the same public repository located at [ROCm/rocm-libraries](https://github.com/ROCm/rocm-libraries/tree/develop/projects/hipfft).

Note

The hipFFT repository for ROCm 6.4.3 and earlier is located at [ROCm/hipFFT](https://github.com/ROCm/hipFFT).

To contribute to the documentation, see [Contributing to ROCm](https://rocm.docs.amd.com/en/latest/contribute/contributing.html).

You can find licensing information on the [Licensing](https://rocm.docs.amd.com/en/latest/about/license.html) page.