source: https://github.com/ggml-org/llama.cpp/releases

# Releases: ggml-org/llama.cpp

## Release list

## b11173

metal : fix graph capture and handle empty graphs ([#29390](https://github.com/ggml-org/llama.cpp/pull/29390))

- return early when the graph has no nodes
- drop the redundant reset of capture_compute: the decrement at the top

of the function already transitions the counter from 0 to -1, so a

capture happens exactly once - hint at METAL_CAPTURE_ENABLED=1 in the capture error message
- pass capture_compute == 0 (not the raw counter) as use_capture to

ggml_metal_op_init, so GPU debug-group markers are only emitted on the

captured compute

Assisted-by: pi:llama.cpp/Qwen3.8-27B

**Website:**

**Attestations:**

**macOS/iOS:**

[macOS Apple Silicon (arm64)](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-bin-macos-arm64.tar.gz)- macOS Apple Silicon (arm64, KleidiAI enabled)
[DISABLED](https://github.com/ggml-org/llama.cpp/pull/23780) [macOS Intel (x64)](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-bin-macos-x64.tar.gz)[iOS XCFramework](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-xcframework.zip)

**Linux:**

[Ubuntu x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-bin-ubuntu-x64.tar.gz)[Ubuntu arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-bin-ubuntu-arm64.tar.gz)[Ubuntu s390x (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-bin-ubuntu-s390x.tar.gz)[Ubuntu x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-bin-ubuntu-vulkan-x64.tar.gz)[Ubuntu arm64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-bin-ubuntu-vulkan-arm64.tar.gz)[Ubuntu x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-bin-ubuntu-cuda-12.8-x64.tar.gz)-[CUDA 12.8 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11173/cudart-llama-b11173-bin-ubuntu-cuda-12.8-x64.tar.gz)[Ubuntu x64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-bin-ubuntu-cuda-13.4-x64.tar.gz)-[CUDA 13.4 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11173/cudart-llama-b11173-bin-ubuntu-cuda-13.4-x64.tar.gz)[Ubuntu arm64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-bin-ubuntu-cuda-13.4-arm64.tar.gz)-[CUDA 13.4 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11173/cudart-llama-b11173-bin-ubuntu-cuda-13.4-arm64.tar.gz)[Ubuntu x64 (ROCm 10.0)](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-bin-ubuntu-rocm-10.0-x64.tar.gz)[Ubuntu x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-bin-ubuntu-openvino-2026.4-x64.tar.gz)[Ubuntu x64 (SYCL FP32)](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-bin-ubuntu-sycl-fp32-x64.tar.gz)[Ubuntu x64 (SYCL FP16)](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-bin-ubuntu-sycl-fp16-x64.tar.gz)[Linux arm64 (Snapdragon: CPU, Adreno GPU, Hexagon NPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-bin-linux-arm64-snapdragon.tar.gz)-[setup guide](https://github.com/ggml-org/llama.cpp/blob/master/docs/backend/snapdragon/linux.md)

**Android:**

**Windows:**

[Windows x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-bin-win-cpu-x64.zip)[Windows arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-bin-win-cpu-arm64.zip)[Windows arm64 (OpenCL Adreno)](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-bin-win-opencl-adreno-arm64.zip)[Windows x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-bin-win-cuda-12.4-x64.zip)-[CUDA 12.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11173/cudart-llama-bin-win-cuda-12.4-x64.zip)[Windows x64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-bin-win-cuda-13.4-x64.zip)-[CUDA 13.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11173/cudart-llama-bin-win-cuda-13.4-x64.zip)[Windows arm64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-bin-win-cuda-13.4-arm64.zip)-[CUDA 13.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11173/cudart-llama-bin-win-cuda-13.4-arm64.zip)[Windows x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-bin-win-vulkan-x64.zip)[Windows x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-bin-win-openvino-2026.4-x64.zip)[Windows x64 (SYCL)](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-bin-win-sycl-x64.zip)[Windows x64 (ROCm 10.0)](https://github.com/ggml-org/llama.cpp/releases/download/b11173/llama-b11173-bin-win-rocm-10.0-x64.zip)

**openEuler:**

[DISABLED](https://github.com/ggml-org/llama.cpp/pull/23705)- openEuler x86 (310p)
- openEuler x86 (910b, ACL Graph)
- openEuler aarch64 (310p)
- openEuler aarch64 (910b, ACL Graph)

**UI:**

## b11172

metal : optimize sparse FA + clean-up ([#29377](https://github.com/ggml-org/llama.cpp/pull/29377))

- metal : cache sparse FA indices in shared memory

Assisted-by: pi:llama.cpp/DeepSeek-V4-Flash-Vision-Exp

- metal : simplify shared memory size calculation

Assisted-by: pi:llama.cpp/DeepSeek-V4-Flash-Vision-Exp

-
pi : update general

-
metal : unroll sparse index load


Assisted-by: pi:llama.cpp/DeepSeek-V4-Flash-Vision-Exp

**Website:**

**Attestations:**

**macOS/iOS:**

[macOS Apple Silicon (arm64)](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-bin-macos-arm64.tar.gz)- macOS Apple Silicon (arm64, KleidiAI enabled)
[DISABLED](https://github.com/ggml-org/llama.cpp/pull/23780) [macOS Intel (x64)](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-bin-macos-x64.tar.gz)[iOS XCFramework](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-xcframework.zip)

**Linux:**

[Ubuntu x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-bin-ubuntu-x64.tar.gz)[Ubuntu arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-bin-ubuntu-arm64.tar.gz)[Ubuntu s390x (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-bin-ubuntu-s390x.tar.gz)[Ubuntu x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-bin-ubuntu-vulkan-x64.tar.gz)[Ubuntu arm64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-bin-ubuntu-vulkan-arm64.tar.gz)[Ubuntu x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-bin-ubuntu-cuda-12.8-x64.tar.gz)-[CUDA 12.8 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11172/cudart-llama-b11172-bin-ubuntu-cuda-12.8-x64.tar.gz)[Ubuntu x64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-bin-ubuntu-cuda-13.4-x64.tar.gz)-[CUDA 13.4 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11172/cudart-llama-b11172-bin-ubuntu-cuda-13.4-x64.tar.gz)[Ubuntu arm64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-bin-ubuntu-cuda-13.4-arm64.tar.gz)-[CUDA 13.4 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11172/cudart-llama-b11172-bin-ubuntu-cuda-13.4-arm64.tar.gz)[Ubuntu x64 (ROCm 10.0)](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-bin-ubuntu-rocm-10.0-x64.tar.gz)[Ubuntu x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-bin-ubuntu-openvino-2026.4-x64.tar.gz)[Ubuntu x64 (SYCL FP32)](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-bin-ubuntu-sycl-fp32-x64.tar.gz)[Ubuntu x64 (SYCL FP16)](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-bin-ubuntu-sycl-fp16-x64.tar.gz)[Linux arm64 (Snapdragon: CPU, Adreno GPU, Hexagon NPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-bin-linux-arm64-snapdragon.tar.gz)-[setup guide](https://github.com/ggml-org/llama.cpp/blob/master/docs/backend/snapdragon/linux.md)

**Android:**

**Windows:**

[Windows x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-bin-win-cpu-x64.zip)[Windows arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-bin-win-cpu-arm64.zip)[Windows arm64 (OpenCL Adreno)](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-bin-win-opencl-adreno-arm64.zip)[Windows x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-bin-win-cuda-12.4-x64.zip)-[CUDA 12.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11172/cudart-llama-bin-win-cuda-12.4-x64.zip)[Windows x64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-bin-win-cuda-13.4-x64.zip)-[CUDA 13.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11172/cudart-llama-bin-win-cuda-13.4-x64.zip)[Windows arm64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-bin-win-cuda-13.4-arm64.zip)-[CUDA 13.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11172/cudart-llama-bin-win-cuda-13.4-arm64.zip)[Windows x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-bin-win-vulkan-x64.zip)[Windows x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-bin-win-openvino-2026.4-x64.zip)[Windows x64 (SYCL)](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-bin-win-sycl-x64.zip)[Windows x64 (ROCm 10.0)](https://github.com/ggml-org/llama.cpp/releases/download/b11172/llama-b11172-bin-win-rocm-10.0-x64.zip)

**openEuler:**

[DISABLED](https://github.com/ggml-org/llama.cpp/pull/23705)- openEuler x86 (310p)
- openEuler x86 (910b, ACL Graph)
- openEuler aarch64 (310p)
- openEuler aarch64 (910b, ACL Graph)

**UI:**

## b11171

sync : ggml ([#29396](https://github.com/ggml-org/llama.cpp/pull/29396))

-
ggml : bump version to 0.25.2 (ggml/1642)

-
ggml : fix ubsan error in

`ggml_graph_nbytes`

(ggml/1644) -
ggml : bump version to 0.25.3 (ggml/1645)

-
sync : ggml


**Website:**

**Attestations:**

**macOS/iOS:**

[macOS Apple Silicon (arm64)](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-bin-macos-arm64.tar.gz)- macOS Apple Silicon (arm64, KleidiAI enabled)
[DISABLED](https://github.com/ggml-org/llama.cpp/pull/23780) [macOS Intel (x64)](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-bin-macos-x64.tar.gz)[iOS XCFramework](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-xcframework.zip)

**Linux:**

[Ubuntu x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-bin-ubuntu-x64.tar.gz)[Ubuntu arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-bin-ubuntu-arm64.tar.gz)[Ubuntu s390x (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-bin-ubuntu-s390x.tar.gz)[Ubuntu x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-bin-ubuntu-vulkan-x64.tar.gz)[Ubuntu arm64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-bin-ubuntu-vulkan-arm64.tar.gz)[Ubuntu x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-bin-ubuntu-cuda-12.8-x64.tar.gz)-[CUDA 12.8 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11171/cudart-llama-b11171-bin-ubuntu-cuda-12.8-x64.tar.gz)[Ubuntu x64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-bin-ubuntu-cuda-13.4-x64.tar.gz)-[CUDA 13.4 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11171/cudart-llama-b11171-bin-ubuntu-cuda-13.4-x64.tar.gz)[Ubuntu arm64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-bin-ubuntu-cuda-13.4-arm64.tar.gz)-[CUDA 13.4 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11171/cudart-llama-b11171-bin-ubuntu-cuda-13.4-arm64.tar.gz)[Ubuntu x64 (ROCm 10.0)](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-bin-ubuntu-rocm-10.0-x64.tar.gz)[Ubuntu x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-bin-ubuntu-openvino-2026.4-x64.tar.gz)[Ubuntu x64 (SYCL FP32)](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-bin-ubuntu-sycl-fp32-x64.tar.gz)[Ubuntu x64 (SYCL FP16)](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-bin-ubuntu-sycl-fp16-x64.tar.gz)[Linux arm64 (Snapdragon: CPU, Adreno GPU, Hexagon NPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-bin-linux-arm64-snapdragon.tar.gz)-[setup guide](https://github.com/ggml-org/llama.cpp/blob/master/docs/backend/snapdragon/linux.md)

**Android:**

**Windows:**

[Windows x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-bin-win-cpu-x64.zip)[Windows arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-bin-win-cpu-arm64.zip)[Windows arm64 (OpenCL Adreno)](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-bin-win-opencl-adreno-arm64.zip)[Windows x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-bin-win-cuda-12.4-x64.zip)-[CUDA 12.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11171/cudart-llama-bin-win-cuda-12.4-x64.zip)[Windows x64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-bin-win-cuda-13.4-x64.zip)-[CUDA 13.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11171/cudart-llama-bin-win-cuda-13.4-x64.zip)[Windows arm64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-bin-win-cuda-13.4-arm64.zip)-[CUDA 13.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11171/cudart-llama-bin-win-cuda-13.4-arm64.zip)[Windows x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-bin-win-vulkan-x64.zip)[Windows x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-bin-win-openvino-2026.4-x64.zip)[Windows x64 (SYCL)](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-bin-win-sycl-x64.zip)[Windows x64 (ROCm 10.0)](https://github.com/ggml-org/llama.cpp/releases/download/b11171/llama-b11171-bin-win-rocm-10.0-x64.zip)

**openEuler:**

[DISABLED](https://github.com/ggml-org/llama.cpp/pull/23705)- openEuler x86 (310p)
- openEuler x86 (910b, ACL Graph)
- openEuler aarch64 (310p)
- openEuler aarch64 (910b, ACL Graph)

**UI:**

## b11170

hexagon: handle multi-sequence in concat_2d ([#29344](https://github.com/ggml-org/llama.cpp/pull/29344))

**Website:**

**Attestations:**

**macOS/iOS:**

[macOS Apple Silicon (arm64)](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-bin-macos-arm64.tar.gz)- macOS Apple Silicon (arm64, KleidiAI enabled)
[DISABLED](https://github.com/ggml-org/llama.cpp/pull/23780) [macOS Intel (x64)](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-bin-macos-x64.tar.gz)[iOS XCFramework](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-xcframework.zip)

**Linux:**

[Ubuntu x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-bin-ubuntu-x64.tar.gz)[Ubuntu arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-bin-ubuntu-arm64.tar.gz)[Ubuntu s390x (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-bin-ubuntu-s390x.tar.gz)[Ubuntu x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-bin-ubuntu-vulkan-x64.tar.gz)[Ubuntu arm64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-bin-ubuntu-vulkan-arm64.tar.gz)[Ubuntu x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-bin-ubuntu-cuda-12.8-x64.tar.gz)-[CUDA 12.8 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11170/cudart-llama-b11170-bin-ubuntu-cuda-12.8-x64.tar.gz)[Ubuntu x64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-bin-ubuntu-cuda-13.4-x64.tar.gz)-[CUDA 13.4 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11170/cudart-llama-b11170-bin-ubuntu-cuda-13.4-x64.tar.gz)[Ubuntu arm64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-bin-ubuntu-cuda-13.4-arm64.tar.gz)-[CUDA 13.4 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11170/cudart-llama-b11170-bin-ubuntu-cuda-13.4-arm64.tar.gz)[Ubuntu x64 (ROCm 10.0)](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-bin-ubuntu-rocm-10.0-x64.tar.gz)[Ubuntu x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-bin-ubuntu-openvino-2026.4-x64.tar.gz)[Ubuntu x64 (SYCL FP32)](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-bin-ubuntu-sycl-fp32-x64.tar.gz)[Ubuntu x64 (SYCL FP16)](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-bin-ubuntu-sycl-fp16-x64.tar.gz)[Linux arm64 (Snapdragon: CPU, Adreno GPU, Hexagon NPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-bin-linux-arm64-snapdragon.tar.gz)-[setup guide](https://github.com/ggml-org/llama.cpp/blob/master/docs/backend/snapdragon/linux.md)

**Android:**

**Windows:**

[Windows x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-bin-win-cpu-x64.zip)[Windows arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-bin-win-cpu-arm64.zip)[Windows arm64 (OpenCL Adreno)](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-bin-win-opencl-adreno-arm64.zip)[Windows x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-bin-win-cuda-12.4-x64.zip)-[CUDA 12.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11170/cudart-llama-bin-win-cuda-12.4-x64.zip)[Windows x64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-bin-win-cuda-13.4-x64.zip)-[CUDA 13.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11170/cudart-llama-bin-win-cuda-13.4-x64.zip)[Windows arm64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-bin-win-cuda-13.4-arm64.zip)-[CUDA 13.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11170/cudart-llama-bin-win-cuda-13.4-arm64.zip)[Windows x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-bin-win-vulkan-x64.zip)[Windows x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-bin-win-openvino-2026.4-x64.zip)[Windows x64 (SYCL)](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-bin-win-sycl-x64.zip)[Windows x64 (ROCm 10.0)](https://github.com/ggml-org/llama.cpp/releases/download/b11170/llama-b11170-bin-win-rocm-10.0-x64.zip)

**openEuler:**

[DISABLED](https://github.com/ggml-org/llama.cpp/pull/23705)- openEuler x86 (310p)
- openEuler x86 (910b, ACL Graph)
- openEuler aarch64 (310p)
- openEuler aarch64 (910b, ACL Graph)

**UI:**

## b11169

llama-grammar: fix numeric truncation for token_id parsing ([#29382](https://github.com/ggml-org/llama.cpp/pull/29382))

**Website:**

**Attestations:**

**macOS/iOS:**

[macOS Apple Silicon (arm64)](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-bin-macos-arm64.tar.gz)- macOS Apple Silicon (arm64, KleidiAI enabled)
[DISABLED](https://github.com/ggml-org/llama.cpp/pull/23780) [macOS Intel (x64)](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-bin-macos-x64.tar.gz)[iOS XCFramework](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-xcframework.zip)

**Linux:**

[Ubuntu x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-bin-ubuntu-x64.tar.gz)[Ubuntu arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-bin-ubuntu-arm64.tar.gz)[Ubuntu s390x (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-bin-ubuntu-s390x.tar.gz)[Ubuntu x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-bin-ubuntu-vulkan-x64.tar.gz)[Ubuntu arm64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-bin-ubuntu-vulkan-arm64.tar.gz)[Ubuntu x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-bin-ubuntu-cuda-12.8-x64.tar.gz)-[CUDA 12.8 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11169/cudart-llama-b11169-bin-ubuntu-cuda-12.8-x64.tar.gz)[Ubuntu x64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-bin-ubuntu-cuda-13.4-x64.tar.gz)-[CUDA 13.4 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11169/cudart-llama-b11169-bin-ubuntu-cuda-13.4-x64.tar.gz)[Ubuntu arm64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-bin-ubuntu-cuda-13.4-arm64.tar.gz)-[CUDA 13.4 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11169/cudart-llama-b11169-bin-ubuntu-cuda-13.4-arm64.tar.gz)[Ubuntu x64 (ROCm 10.0)](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-bin-ubuntu-rocm-10.0-x64.tar.gz)[Ubuntu x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-bin-ubuntu-openvino-2026.4-x64.tar.gz)[Ubuntu x64 (SYCL FP32)](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-bin-ubuntu-sycl-fp32-x64.tar.gz)[Ubuntu x64 (SYCL FP16)](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-bin-ubuntu-sycl-fp16-x64.tar.gz)[Linux arm64 (Snapdragon: CPU, Adreno GPU, Hexagon NPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-bin-linux-arm64-snapdragon.tar.gz)-[setup guide](https://github.com/ggml-org/llama.cpp/blob/master/docs/backend/snapdragon/linux.md)

**Android:**

**Windows:**

[Windows x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-bin-win-cpu-x64.zip)[Windows arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-bin-win-cpu-arm64.zip)[Windows arm64 (OpenCL Adreno)](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-bin-win-opencl-adreno-arm64.zip)[Windows x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-bin-win-cuda-12.4-x64.zip)-[CUDA 12.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11169/cudart-llama-bin-win-cuda-12.4-x64.zip)[Windows x64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-bin-win-cuda-13.4-x64.zip)-[CUDA 13.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11169/cudart-llama-bin-win-cuda-13.4-x64.zip)[Windows arm64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-bin-win-cuda-13.4-arm64.zip)-[CUDA 13.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11169/cudart-llama-bin-win-cuda-13.4-arm64.zip)[Windows x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-bin-win-vulkan-x64.zip)[Windows x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-bin-win-openvino-2026.4-x64.zip)[Windows x64 (SYCL)](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-bin-win-sycl-x64.zip)[Windows x64 (ROCm 10.0)](https://github.com/ggml-org/llama.cpp/releases/download/b11169/llama-b11169-bin-win-rocm-10.0-x64.zip)

**openEuler:**

[DISABLED](https://github.com/ggml-org/llama.cpp/pull/23705)- openEuler x86 (310p)
- openEuler x86 (910b, ACL Graph)
- openEuler aarch64 (310p)
- openEuler aarch64 (910b, ACL Graph)

**UI:**

## b11168

hexagon: dynamic quantizer improvements ([#29395](https://github.com/ggml-org/llama.cpp/pull/29395))

-
hexagon: fix accuracy issue in Q8_0 N=1 MUL_MAT

-
hex-quant: fix register spills

-
hex-mm: use dma for all dyn.quant paths


Co-authored-by: Aparna M P [aparmp@qti.qualcomm.com](mailto:aparmp@qti.qualcomm.com)

-
hex-mm: remove obsolete run_quant_task

-
hex-mm: update tracing to properly wrap the events

-
hex-mm: use act for activation data in all paths

-
hex-mm: use act_ instead of src1_ to avoid confusion in fused kernels

-
hex-mm: remove/reroute the rest of the non-DMA act (aka src1) logic

-
hex-dma64: yet another pass at cleaning up the dma_addr_t casts

-
Update ggml/src/ggml-hexagon/htp/matmul-ops.h


Co-authored-by: Sigbjørn Skjæret [sigbjorn.skjaeret@huggingface.co](mailto:sigbjorn.skjaeret@huggingface.co)

- Update ggml/src/ggml-hexagon/htp/matmul-ops.c

Co-authored-by: Sigbjørn Skjæret [sigbjorn.skjaeret@huggingface.co](mailto:sigbjorn.skjaeret@huggingface.co)

- Update ggml/src/ggml-hexagon/htp/matmul-ops.c

Co-authored-by: Sigbjørn Skjæret [sigbjorn.skjaeret@huggingface.co](mailto:sigbjorn.skjaeret@huggingface.co)

- Update ggml/src/ggml-hexagon/htp/matmul-ops.c

Co-authored-by: Sigbjørn Skjæret [sigbjorn.skjaeret@huggingface.co](mailto:sigbjorn.skjaeret@huggingface.co)

Co-authored-by: Max Krasnyansky [maxk@qti.qualcomm.com](mailto:maxk@qti.qualcomm.com)

Co-authored-by: Aparna M P [aparmp@qti.qualcomm.com](mailto:aparmp@qti.qualcomm.com)

Co-authored-by: Sigbjørn Skjæret [sigbjorn.skjaeret@huggingface.co](mailto:sigbjorn.skjaeret@huggingface.co)

**Website:**

**Attestations:**

**macOS/iOS:**

[macOS Apple Silicon (arm64)](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-bin-macos-arm64.tar.gz)- macOS Apple Silicon (arm64, KleidiAI enabled)
[DISABLED](https://github.com/ggml-org/llama.cpp/pull/23780) [macOS Intel (x64)](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-bin-macos-x64.tar.gz)[iOS XCFramework](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-xcframework.zip)

**Linux:**

[Ubuntu x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-bin-ubuntu-x64.tar.gz)[Ubuntu arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-bin-ubuntu-arm64.tar.gz)[Ubuntu s390x (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-bin-ubuntu-s390x.tar.gz)[Ubuntu x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-bin-ubuntu-vulkan-x64.tar.gz)[Ubuntu arm64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-bin-ubuntu-vulkan-arm64.tar.gz)[Ubuntu x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-bin-ubuntu-cuda-12.8-x64.tar.gz)-[CUDA 12.8 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11168/cudart-llama-b11168-bin-ubuntu-cuda-12.8-x64.tar.gz)[Ubuntu x64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-bin-ubuntu-cuda-13.4-x64.tar.gz)-[CUDA 13.4 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11168/cudart-llama-b11168-bin-ubuntu-cuda-13.4-x64.tar.gz)[Ubuntu arm64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-bin-ubuntu-cuda-13.4-arm64.tar.gz)-[CUDA 13.4 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11168/cudart-llama-b11168-bin-ubuntu-cuda-13.4-arm64.tar.gz)[Ubuntu x64 (ROCm 10.0)](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-bin-ubuntu-rocm-10.0-x64.tar.gz)[Ubuntu x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-bin-ubuntu-openvino-2026.4-x64.tar.gz)[Ubuntu x64 (SYCL FP32)](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-bin-ubuntu-sycl-fp32-x64.tar.gz)[Ubuntu x64 (SYCL FP16)](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-bin-ubuntu-sycl-fp16-x64.tar.gz)[Linux arm64 (Snapdragon: CPU, Adreno GPU, Hexagon NPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-bin-linux-arm64-snapdragon.tar.gz)-[setup guide](https://github.com/ggml-org/llama.cpp/blob/master/docs/backend/snapdragon/linux.md)

**Android:**

**Windows:**

[Windows x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-bin-win-cpu-x64.zip)[Windows arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-bin-win-cpu-arm64.zip)[Windows arm64 (OpenCL Adreno)](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-bin-win-opencl-adreno-arm64.zip)[Windows x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-bin-win-cuda-12.4-x64.zip)-[CUDA 12.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11168/cudart-llama-bin-win-cuda-12.4-x64.zip)[Windows x64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-bin-win-cuda-13.4-x64.zip)-[CUDA 13.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11168/cudart-llama-bin-win-cuda-13.4-x64.zip)[Windows arm64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-bin-win-cuda-13.4-arm64.zip)-[CUDA 13.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11168/cudart-llama-bin-win-cuda-13.4-arm64.zip)[Windows x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-bin-win-vulkan-x64.zip)[Windows x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-bin-win-openvino-2026.4-x64.zip)[Windows x64 (SYCL)](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-bin-win-sycl-x64.zip)[Windows x64 (ROCm 10.0)](https://github.com/ggml-org/llama.cpp/releases/download/b11168/llama-b11168-bin-win-rocm-10.0-x64.zip)

**openEuler:**

[DISABLED](https://github.com/ggml-org/llama.cpp/pull/23705)- openEuler x86 (310p)
- openEuler x86 (910b, ACL Graph)
- openEuler aarch64 (310p)
- openEuler aarch64 (910b, ACL Graph)

**UI:**

## b11167

hexagon: support I32 CPY and CONT ([#29379](https://github.com/ggml-org/llama.cpp/pull/29379))

Assisted-by: OpenCode

**Website:**

**Attestations:**

**macOS/iOS:**

[macOS Apple Silicon (arm64)](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-bin-macos-arm64.tar.gz)- macOS Apple Silicon (arm64, KleidiAI enabled)
[DISABLED](https://github.com/ggml-org/llama.cpp/pull/23780) [macOS Intel (x64)](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-bin-macos-x64.tar.gz)[iOS XCFramework](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-xcframework.zip)

**Linux:**

[Ubuntu x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-bin-ubuntu-x64.tar.gz)[Ubuntu arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-bin-ubuntu-arm64.tar.gz)[Ubuntu s390x (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-bin-ubuntu-s390x.tar.gz)[Ubuntu x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-bin-ubuntu-vulkan-x64.tar.gz)[Ubuntu arm64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-bin-ubuntu-vulkan-arm64.tar.gz)[Ubuntu x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-bin-ubuntu-cuda-12.8-x64.tar.gz)-[CUDA 12.8 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11167/cudart-llama-b11167-bin-ubuntu-cuda-12.8-x64.tar.gz)[Ubuntu x64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-bin-ubuntu-cuda-13.4-x64.tar.gz)-[CUDA 13.4 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11167/cudart-llama-b11167-bin-ubuntu-cuda-13.4-x64.tar.gz)[Ubuntu arm64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-bin-ubuntu-cuda-13.4-arm64.tar.gz)-[CUDA 13.4 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11167/cudart-llama-b11167-bin-ubuntu-cuda-13.4-arm64.tar.gz)[Ubuntu x64 (ROCm 10.0)](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-bin-ubuntu-rocm-10.0-x64.tar.gz)[Ubuntu x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-bin-ubuntu-openvino-2026.4-x64.tar.gz)[Ubuntu x64 (SYCL FP32)](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-bin-ubuntu-sycl-fp32-x64.tar.gz)[Ubuntu x64 (SYCL FP16)](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-bin-ubuntu-sycl-fp16-x64.tar.gz)[Linux arm64 (Snapdragon: CPU, Adreno GPU, Hexagon NPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-bin-linux-arm64-snapdragon.tar.gz)-[setup guide](https://github.com/ggml-org/llama.cpp/blob/master/docs/backend/snapdragon/linux.md)

**Android:**

**Windows:**

[Windows x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-bin-win-cpu-x64.zip)[Windows arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-bin-win-cpu-arm64.zip)[Windows arm64 (OpenCL Adreno)](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-bin-win-opencl-adreno-arm64.zip)[Windows x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-bin-win-cuda-12.4-x64.zip)-[CUDA 12.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11167/cudart-llama-bin-win-cuda-12.4-x64.zip)[Windows x64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-bin-win-cuda-13.4-x64.zip)-[CUDA 13.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11167/cudart-llama-bin-win-cuda-13.4-x64.zip)[Windows arm64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-bin-win-cuda-13.4-arm64.zip)-[CUDA 13.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11167/cudart-llama-bin-win-cuda-13.4-arm64.zip)[Windows x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-bin-win-vulkan-x64.zip)[Windows x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-bin-win-openvino-2026.4-x64.zip)[Windows x64 (SYCL)](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-bin-win-sycl-x64.zip)[Windows x64 (ROCm 10.0)](https://github.com/ggml-org/llama.cpp/releases/download/b11167/llama-b11167-bin-win-rocm-10.0-x64.zip)

**openEuler:**

[DISABLED](https://github.com/ggml-org/llama.cpp/pull/23705)- openEuler x86 (310p)
- openEuler x86 (910b, ACL Graph)
- openEuler aarch64 (310p)
- openEuler aarch64 (910b, ACL Graph)

**UI:**

## b11166

cuda : add F16 kernel support for CONV_2D_DW ([#29064](https://github.com/ggml-org/llama.cpp/pull/29064))

**Website:**

**Attestations:**

**macOS/iOS:**

[macOS Apple Silicon (arm64)](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-bin-macos-arm64.tar.gz)- macOS Apple Silicon (arm64, KleidiAI enabled)
[DISABLED](https://github.com/ggml-org/llama.cpp/pull/23780) [macOS Intel (x64)](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-bin-macos-x64.tar.gz)[iOS XCFramework](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-xcframework.zip)

**Linux:**

[Ubuntu x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-bin-ubuntu-x64.tar.gz)[Ubuntu arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-bin-ubuntu-arm64.tar.gz)[Ubuntu s390x (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-bin-ubuntu-s390x.tar.gz)[Ubuntu x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-bin-ubuntu-vulkan-x64.tar.gz)[Ubuntu arm64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-bin-ubuntu-vulkan-arm64.tar.gz)[Ubuntu x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-bin-ubuntu-cuda-12.8-x64.tar.gz)-[CUDA 12.8 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11166/cudart-llama-b11166-bin-ubuntu-cuda-12.8-x64.tar.gz)[Ubuntu x64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-bin-ubuntu-cuda-13.4-x64.tar.gz)-[CUDA 13.4 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11166/cudart-llama-b11166-bin-ubuntu-cuda-13.4-x64.tar.gz)[Ubuntu arm64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-bin-ubuntu-cuda-13.4-arm64.tar.gz)-[CUDA 13.4 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11166/cudart-llama-b11166-bin-ubuntu-cuda-13.4-arm64.tar.gz)[Ubuntu x64 (ROCm 10.0)](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-bin-ubuntu-rocm-10.0-x64.tar.gz)[Ubuntu x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-bin-ubuntu-openvino-2026.4-x64.tar.gz)[Ubuntu x64 (SYCL FP32)](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-bin-ubuntu-sycl-fp32-x64.tar.gz)[Ubuntu x64 (SYCL FP16)](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-bin-ubuntu-sycl-fp16-x64.tar.gz)[Linux arm64 (Snapdragon: CPU, Adreno GPU, Hexagon NPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-bin-linux-arm64-snapdragon.tar.gz)-[setup guide](https://github.com/ggml-org/llama.cpp/blob/master/docs/backend/snapdragon/linux.md)

**Android:**

**Windows:**

[Windows x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-bin-win-cpu-x64.zip)[Windows arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-bin-win-cpu-arm64.zip)[Windows arm64 (OpenCL Adreno)](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-bin-win-opencl-adreno-arm64.zip)[Windows x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-bin-win-cuda-12.4-x64.zip)-[CUDA 12.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11166/cudart-llama-bin-win-cuda-12.4-x64.zip)[Windows x64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-bin-win-cuda-13.4-x64.zip)-[CUDA 13.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11166/cudart-llama-bin-win-cuda-13.4-x64.zip)[Windows arm64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-bin-win-cuda-13.4-arm64.zip)-[CUDA 13.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11166/cudart-llama-bin-win-cuda-13.4-arm64.zip)[Windows x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-bin-win-vulkan-x64.zip)[Windows x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-bin-win-openvino-2026.4-x64.zip)[Windows x64 (SYCL)](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-bin-win-sycl-x64.zip)[Windows x64 (ROCm 10.0)](https://github.com/ggml-org/llama.cpp/releases/download/b11166/llama-b11166-bin-win-rocm-10.0-x64.zip)

**openEuler:**

[DISABLED](https://github.com/ggml-org/llama.cpp/pull/23705)- openEuler x86 (310p)
- openEuler x86 (910b, ACL Graph)
- openEuler aarch64 (310p)
- openEuler aarch64 (910b, ACL Graph)

**UI:**

## b11165

test: flush status ([#28352](https://github.com/ggml-org/llama.cpp/pull/28352))

**Website:**

**Attestations:**

**macOS/iOS:**

[macOS Apple Silicon (arm64)](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-bin-macos-arm64.tar.gz)- macOS Apple Silicon (arm64, KleidiAI enabled)
[DISABLED](https://github.com/ggml-org/llama.cpp/pull/23780) [macOS Intel (x64)](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-bin-macos-x64.tar.gz)[iOS XCFramework](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-xcframework.zip)

**Linux:**

[Ubuntu x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-bin-ubuntu-x64.tar.gz)[Ubuntu arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-bin-ubuntu-arm64.tar.gz)[Ubuntu s390x (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-bin-ubuntu-s390x.tar.gz)[Ubuntu x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-bin-ubuntu-vulkan-x64.tar.gz)[Ubuntu arm64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-bin-ubuntu-vulkan-arm64.tar.gz)[Ubuntu x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-bin-ubuntu-cuda-12.8-x64.tar.gz)-[CUDA 12.8 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11165/cudart-llama-b11165-bin-ubuntu-cuda-12.8-x64.tar.gz)[Ubuntu x64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-bin-ubuntu-cuda-13.4-x64.tar.gz)-[CUDA 13.4 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11165/cudart-llama-b11165-bin-ubuntu-cuda-13.4-x64.tar.gz)[Ubuntu arm64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-bin-ubuntu-cuda-13.4-arm64.tar.gz)-[CUDA 13.4 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11165/cudart-llama-b11165-bin-ubuntu-cuda-13.4-arm64.tar.gz)[Ubuntu x64 (ROCm 10.0)](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-bin-ubuntu-rocm-10.0-x64.tar.gz)[Ubuntu x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-bin-ubuntu-openvino-2026.4-x64.tar.gz)[Ubuntu x64 (SYCL FP32)](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-bin-ubuntu-sycl-fp32-x64.tar.gz)[Ubuntu x64 (SYCL FP16)](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-bin-ubuntu-sycl-fp16-x64.tar.gz)[Linux arm64 (Snapdragon: CPU, Adreno GPU, Hexagon NPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-bin-linux-arm64-snapdragon.tar.gz)-[setup guide](https://github.com/ggml-org/llama.cpp/blob/master/docs/backend/snapdragon/linux.md)

**Android:**

**Windows:**

[Windows x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-bin-win-cpu-x64.zip)[Windows arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-bin-win-cpu-arm64.zip)[Windows arm64 (OpenCL Adreno)](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-bin-win-opencl-adreno-arm64.zip)[Windows x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-bin-win-cuda-12.4-x64.zip)-[CUDA 12.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11165/cudart-llama-bin-win-cuda-12.4-x64.zip)[Windows x64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-bin-win-cuda-13.4-x64.zip)-[CUDA 13.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11165/cudart-llama-bin-win-cuda-13.4-x64.zip)[Windows arm64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-bin-win-cuda-13.4-arm64.zip)-[CUDA 13.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11165/cudart-llama-bin-win-cuda-13.4-arm64.zip)[Windows x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-bin-win-vulkan-x64.zip)[Windows x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-bin-win-openvino-2026.4-x64.zip)[Windows x64 (SYCL)](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-bin-win-sycl-x64.zip)[Windows x64 (ROCm 10.0)](https://github.com/ggml-org/llama.cpp/releases/download/b11165/llama-b11165-bin-win-rocm-10.0-x64.zip)

**openEuler:**

[DISABLED](https://github.com/ggml-org/llama.cpp/pull/23705)- openEuler x86 (310p)
- openEuler x86 (910b, ACL Graph)
- openEuler aarch64 (310p)
- openEuler aarch64 (910b, ACL Graph)

**UI:**

## b11163

llama: add llama_batch_ext ([#24669](https://github.com/ggml-org/llama.cpp/pull/24669))

-
(wip) add llama_batch_ext

-
wip

-
updated design

-
updated impl

-
change signature

-
unused var

-
demo common_prompt_batch_decode

-
fix pos

-
tmp disable test-batch-alloc

-
fix compat

-
nits: add const

-
no more pos_max

-
add comment about llama_batch_ext_set_embd_state

-
handle n_embd_out properly

-
rename api --> embd_token

-
llama_embd

-
stub llama_batch_ext_set_embd_state

-
support both token + embd + state in batch

-
llama_batch_ext_add_embd

-
upstream some changes

-
nits

-
fix test-batch-alloc

-
add test for compat


**Website:**

**Attestations:**

**macOS/iOS:**

[macOS Apple Silicon (arm64)](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-bin-macos-arm64.tar.gz)- macOS Apple Silicon (arm64, KleidiAI enabled)
[DISABLED](https://github.com/ggml-org/llama.cpp/pull/23780) [macOS Intel (x64)](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-bin-macos-x64.tar.gz)[iOS XCFramework](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-xcframework.zip)

**Linux:**

[Ubuntu x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-bin-ubuntu-x64.tar.gz)[Ubuntu arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-bin-ubuntu-arm64.tar.gz)[Ubuntu s390x (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-bin-ubuntu-s390x.tar.gz)[Ubuntu x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-bin-ubuntu-vulkan-x64.tar.gz)[Ubuntu arm64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-bin-ubuntu-vulkan-arm64.tar.gz)[Ubuntu x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-bin-ubuntu-cuda-12.8-x64.tar.gz)-[CUDA 12.8 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11163/cudart-llama-b11163-bin-ubuntu-cuda-12.8-x64.tar.gz)[Ubuntu x64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-bin-ubuntu-cuda-13.4-x64.tar.gz)-[CUDA 13.4 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11163/cudart-llama-b11163-bin-ubuntu-cuda-13.4-x64.tar.gz)[Ubuntu arm64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-bin-ubuntu-cuda-13.4-arm64.tar.gz)-[CUDA 13.4 libraries](https://github.com/ggml-org/llama.cpp/releases/download/b11163/cudart-llama-b11163-bin-ubuntu-cuda-13.4-arm64.tar.gz)[Ubuntu x64 (ROCm 10.0)](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-bin-ubuntu-rocm-10.0-x64.tar.gz)[Ubuntu x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-bin-ubuntu-openvino-2026.4-x64.tar.gz)[Ubuntu x64 (SYCL FP32)](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-bin-ubuntu-sycl-fp32-x64.tar.gz)[Ubuntu x64 (SYCL FP16)](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-bin-ubuntu-sycl-fp16-x64.tar.gz)[Linux arm64 (Snapdragon: CPU, Adreno GPU, Hexagon NPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-bin-linux-arm64-snapdragon.tar.gz)-[setup guide](https://github.com/ggml-org/llama.cpp/blob/master/docs/backend/snapdragon/linux.md)

**Android:**

**Windows:**

[Windows x64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-bin-win-cpu-x64.zip)[Windows arm64 (CPU)](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-bin-win-cpu-arm64.zip)[Windows arm64 (OpenCL Adreno)](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-bin-win-opencl-adreno-arm64.zip)[Windows x64 (CUDA 12)](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-bin-win-cuda-12.4-x64.zip)-[CUDA 12.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11163/cudart-llama-bin-win-cuda-12.4-x64.zip)[Windows x64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-bin-win-cuda-13.4-x64.zip)-[CUDA 13.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11163/cudart-llama-bin-win-cuda-13.4-x64.zip)[Windows arm64 (CUDA 13)](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-bin-win-cuda-13.4-arm64.zip)-[CUDA 13.4 DLLs](https://github.com/ggml-org/llama.cpp/releases/download/b11163/cudart-llama-bin-win-cuda-13.4-arm64.zip)[Windows x64 (Vulkan)](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-bin-win-vulkan-x64.zip)[Windows x64 (OpenVINO)](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-bin-win-openvino-2026.4-x64.zip)[Windows x64 (SYCL)](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-bin-win-sycl-x64.zip)[Windows x64 (ROCm 10.0)](https://github.com/ggml-org/llama.cpp/releases/download/b11163/llama-b11163-bin-win-rocm-10.0-x64.zip)

**openEuler:**

[DISABLED](https://github.com/ggml-org/llama.cpp/pull/23705)- openEuler x86 (310p)
- openEuler x86 (910b, ACL Graph)
- openEuler aarch64 (310p)
- openEuler aarch64 (910b, ACL Graph)

**UI:**