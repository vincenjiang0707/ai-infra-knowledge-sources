source: https://docs.nvidia.com/nvpl/latest/fft/index.html

# NVPL FFT Documentation[#](https://docs.nvidia.com#nvpl-fft-documentation)

The [NVIDIA Performance Libraries (NVPL)](https://docs.nvidia.com/index.html) FFT library enables you to perform Fast Fourier Transform (FFT) calculations on ARM CPUs.
For computing FFTs on NVIDIA GPUs, please see the [cuFFT](https://docs.nvidia.com/cuda/cufft/index.html), [cuFFTDx](https://docs.nvidia.com/cuda/cufftdx/index.html) and [cuFFTMp](https://docs.nvidia.com/hpc-sdk/cufftmp/index.html) libraries.

The documentation consists of three main components:


A

[Quick start]guide with a sample snippet.A

[How to use NVPL FFT]section, describing the requirements and the general usage of NVPL FFT.An

[API reference]section, with a description of the supported FFTW APIs.

# Highlights[#](https://docs.nvidia.com#highlights)

The NVPL FFT library:

Provides optimized FFT routines for ARM CPUs using APIs compatible with FFTW (please see the list of supported CPUs in

[Hardware and software requirements](https://docs.nvidia.com/usage/requirements.html#requirements-label)).Provides a single binary

`libnvpl_fftw.so`

for both single- and multi-threaded functionalities.Supports computation of one-, two-, three- dimensional complex-to-complex, real-to-complex, complex-to-real DFTs in single and double precision with arbitrary sizes and strides.


Note

The NVPL FFT beta release includes all functionalities listed in the supported functionalities section while some of the functionalities have not been optimized to the full extent. See [Release Notes](https://docs.nvidia.com/release_notes.html#relnotes-label) for more details.