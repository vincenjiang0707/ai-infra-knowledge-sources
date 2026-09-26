source: https://docs.nvidia.com/deeplearning/tensorrt/index.html

# NVIDIA TensorRT Documentation[#](https://docs.nvidia.com#nvidia-tensorrt-documentation)

NVIDIA® TensorRT™ is an SDK for optimizing deep learning inference on NVIDIA GPUs. It takes trained models from frameworks such as PyTorch and ONNX, and compiles them into engines for GPU deployment with support for mixed precision (FP32/FP16/BF16/FP8/INT8/FP4/INT4), dynamic shapes, and specialized optimizations for transformers and large language models (LLMs). Measure latency and throughput on your own model and hardware; refer to [Best Practices](https://docs.nvidia.com/performance/best-practices.html#best-practices).

## Quick Start[#](https://docs.nvidia.com#quick-start)

**New to NVIDIA TensorRT?**→**Install first**, then verify, then build your first engine:[Installation Guide Overview](https://docs.nvidia.com/installing-tensorrt/overview.html#install-guide)and[Installing TensorRT](https://docs.nvidia.com/installing-tensorrt/installing.html#installing)(Debian/RPM, tar/zip, or container for the ~10-minute CLI tutorial)Verify:

`trtexec --help`

(non-pip) or`import tensorrt; print(tensorrt.__version__)`

(pip)[Build Your First Engine](https://docs.nvidia.com/getting-started/build-your-first-engine.html#build-your-first-engine)(requires`trtexec`

, which is not included in pip wheels)

**Python API only (pip)?**→[Method 1: Python Package Index (pip)](https://docs.nvidia.com/installing-tensorrt/install-pip.html#installing-pip)(`pip install tensorrt`

). Pip installs bindings and libraries only, with**no**`trtexec`

. For the first-engine CLI tutorial, use Debian/RPM, tar/zip, or container instead.**C++ or CLI workflows?**→ Choose Debian/RPM, tar/zip, or container on[Installing TensorRT](https://docs.nvidia.com/installing-tensorrt/installing.html#installing); run`trtexec`

from the package`bin`

directory**Ready for the full workflow menu?**→ After your first engine, use the[Quick Start Guide](https://docs.nvidia.com/getting-started/quick-start-guide.html#quick-start-guide)for PyTorch and ONNX export paths, multiple runtimes, dynamic shapes, and quantization**Upgrading from 11.2 or earlier?**→ Refer to[What’s New in 11.3.0](https://docs.nvidia.com#whats-new-11-3-0)below**Upgrading from TensorRT 10.x?**→ Use the[NVIDIA TensorRT Migration Guide](https://docs.nvidia.com/api/migration-guide.html#migration-guide)to plan your API and builder changes**Need help with a specific task?**→ Jump to the[Inference Library Overview](https://docs.nvidia.com/inference-library/index.html#inference-library-overview)for API walkthroughs, dynamic shapes, quantization, and more, or the[Troubleshooting](https://docs.nvidia.com/reference/troubleshooting.html#troubleshooting)section**Optimize inference performance**→[Best Practices](https://docs.nvidia.com/performance/best-practices.html#best-practices)

## What’s New in NVIDIA TensorRT 11.3.0[#](https://docs.nvidia.com#what-s-new-in-nvidia-tensorrt-11-3-0)

Release Highlights

**CUDA Toolkit 13.4 dependency upgrade**: TensorRT 11.3.0 packages are built against**CUDA® Toolkit 13.4**; Debian, RPM, tar, and zip package filenames use`cuda-13.4`

. TensorRT 11.3.1 DriveOS packages use CUDA Toolkit 13.4. Refer to the[TensorRT Support Matrix](https://docs.nvidia.com/getting-started/support-matrix.html#support-matrix)for supported CUDA releases per platform and to[Prerequisites](https://docs.nvidia.com/installing-tensorrt/prerequisites.html)for installer prerequisites.**NVIDIA Vera Rubin support added in TensorRT 11.3.0**: NVIDIA Vera Rubin GPUs are supported by TensorRT 11.3.0 Enterprise (general-release). Linux x86, Linux SBSA, and Windows x64 support NVIDIA Vera Rubin GPUs with compute capability version 10.7. Refer to the[TensorRT Support Matrix](https://docs.nvidia.com/getting-started/support-matrix.html#support-matrix).**Refit enhancement in TensorRT 11.3.0**: High-precision weights used in FP4 double quantization are now refittable. If you use`BuilderFlag::kREFIT`

, refer to Known Issues in the[TensorRT 11.3.0 Release Notes](https://docs.nvidia.com/getting-started/release-notes-11/11.3.0.html#rel-11-3-0). Refer to[Refitting an Engine](https://docs.nvidia.com/inference-library/refitting-engines.html#refitting-engine-c).**Limitations in TensorRT 11.3.0**: DLA is not supported in TensorRT 11.3.0 or in TensorRT 11.3.1 for DriveOS (last DLA release is 10.7). NVIDIA JetPack is not supported; Jetson deployments must remain on a TensorRT 10.x release supported by their JetPack version. Refer to the[TensorRT 11.3.0 Release Notes](https://docs.nvidia.com/getting-started/release-notes-11/11.3.0.html#rel-11-3-0).

## Previous Releases[#](https://docs.nvidia.com#previous-releases)

## Release 11.2.1 Highlights

**Platform dependency upgrades**: Updates internal build dependencies for TensorRT 11.2.1. TensorRT 11.2.1 packages are built against**CUDA 13.3 update 1**; Debian, RPM, tar, and zip package filenames continue to use`cuda-13.3`

.**GridSample 3D support**: Extends`GridSample`

from 2D-only to 3D (rank-5 input) with FP32, FP16, and BF16**ONNX DFT operator support**: Adds a cuFFT-based plugin for forward and inverse C2C, R2C, and C2R transforms**PluginV2 to PluginV3 migration sample**: Adds a Python sample with PluginV2-to-PluginV3 method mappings**Improved CMake support**: Tar and Zip packages include CMake configuration files under the`cmake`

directory

## Release 11.1.0 Highlights

**CUDA 13.3 dependency upgrade**: Updated CUDA Toolkit baseline across Linux x86-64, Windows x64, and SBSA platforms**Ubuntu 26.04 support**: Adds Ubuntu 26.04 LTS to the supported Linux x86-64 and SBSA platform lists alongside the existing Ubuntu 22.04/24.04 packages**Python 3.14 bindings**: Extends the Python wheel matrix to Python 3.14 on supported platforms**NVFP4 dual-GEMM fusion for SM121**: Fuses the gate and up projection GEMMs in NVFP4 MoE/MLP blocks on NVIDIA DGX Spark (compute capability 12.1)**Global Performance Tuner**: Automates`trtexec`

build-route search to explore internal builder knobs, benchmark candidate engines, and optionally validate accuracy before selecting a route. Measure the benefit on your model and GPU. Refer to[Global Performance Tuning](https://docs.nvidia.com/performance/tuning.html#tuning).

## Release 11.0.0 Highlights

**Strongly typed networks are now the default**: Weak-typing APIs (`setPrecision`

,`setDynamicRange`

, the per-precision`BuilderFlag`

family) and implicit quantization (`IInt8Calibrator`

) have been removed. Use the[NVIDIA TensorRT Migration Guide](https://docs.nvidia.com/api/migration-guide.html#migration-guide)to plan your upgrade**IPluginV2 has been removed**: The entire`IPluginV2`

family is gone; migrate custom plugins to`IPluginV3`

with`addPluginV3()`

. Refer to the[V2 → V3 walkthrough](https://docs.nvidia.com/inference-library/plugins-api-migration.html#v2-to-v3-api-mapping)for a side-by-side API mapping**Multi-Device Inference is generally available**: Preview flag retired, plus new`AllToAll`

,`Gather`

, and`Scatter`

collective ops, automatic NCCL library fallback, and a new context-parallel attention sample. Refer to[Multi-Device Inference](https://docs.nvidia.com/inference-library/multi-device-inference.html#multi-device-inference)**Ragged batching for attention**:`IAttention`

and`IKVCacheUpdateLayer`

now support packed (`kPACKED_NHD`

) layouts so variable-length sequences can be concatenated end-to-end without padding. Refer to[Fused Attention](https://docs.nvidia.com/inference-library/transformers-fused-attention.html#mha-fusion)**MoE inference performance**: NVIDIA Blackwell architecture (SM10x/SM110) backend improvements for common MoE patterns; the previous “keep`seqLen`

≤ 16” guidance no longer applies. Benchmark your own workload. Refer to[MoE (Mixture of Experts)](https://docs.nvidia.com/inference-library/transformers-moe.html#moe-mixture-of-experts)**Rewritten Best Practices and Benchmarking guide**: Reframed as a measure-then-optimize loop with side-by-side ONNX-TRT (`trtexec`

) and Torch-TRT workflows in synchronized tabs covering quantization, dynamic shapes, CUDA graphs, profiling, and Nsight Systems timeline reading. Refer to[Performance Benchmarking](https://docs.nvidia.com/performance/benchmarking.html#performance-benchmarking)**Platform updates**: RHEL 10 / Rocky Linux 10 RPM and tar packages, and a new[TensorRT 10.x to 11.x migration path](https://docs.nvidia.com/api/migration/tensorrt-10x-to-11x.html)with dedicated DriveOS and Jetson/JetPack chapters

## Archived Releases

Earlier TensorRT releases with key highlights:

[TensorRT 10.x.x Releases](https://docs.nvidia.com/deeplearning/tensorrt/10.x.x/index.html)- Release Notes and documentation for TensorRT 10.x.x

## Legacy Versions

TensorRT 8.6.1 Release

[(GitHub)](https://github.com/NVIDIA/TensorRT/releases/tag/v8.6.1)and[(Documentation)](https://archive.docs.nvidia.com/tensorrt/tensorrt-861/index.html)

Note

For complete version history and detailed changelogs, visit the [Release Notes](https://docs.nvidia.com/getting-started/release-notes.html#release-notes) section or the [TensorRT GitHub Releases](https://github.com/NVIDIA/TensorRT/releases).