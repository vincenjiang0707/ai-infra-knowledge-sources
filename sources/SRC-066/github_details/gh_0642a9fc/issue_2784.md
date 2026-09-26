# [Issue #2784] [QST] Build failure of cutlass_profiler on Jetson AGX Thor: SMEM usage exceeded capacity in sm100_gemm_array_tma_warpspecialized

source: https://github.com/NVIDIA/cutlass/issues/2784
state: closed | updated: 2026-09-24T16:54:31Z
labels: question, ? - Needs Triage, inactive-90d

## 正文

Environment

- Hardware: Jetson AGX Thor
- CUTLASS Version: main branch as of 2025-11-13
- CUDA Version: 13.0.48
- Compiler: Build cuda_13.0.r13.0/compiler.36260728_0
- Operating System: JetPack 7.0

```TEXT
./deviceQuery Starting...

 CUDA Device Query (Runtime API) version (CUDART static linking)

Detected 1 CUDA Capable device(s)

Device 0: "NVIDIA Thor"
  CUDA Driver Version / Runtime Version          13.0 / 13.0
  CUDA Capability Major/Minor version number:    11.0
  Total amount of global memory:                 125772 MBytes (131881680896 bytes)
  (020) Multiprocessors, (128) CUDA Cores/MP:    2560 CUDA Cores
  GPU Max Clock rate:                            1049 MHz (1.05 GHz)
  Memory Clock rate:                             0 Mhz
  Memory Bus Width:                              0-bit
  L2 Cache Size:                                 33554432 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        233472 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  1536
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 1 copy engine(s)
  Run time limit on kernels:                     Yes
  Integrated GPU sharing Host Memory:            Yes
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Disabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 1 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

deviceQuery, CUDA Driver = CUDART, CUDA Driver Version = 13.0, CUDA Runtime Version = 13.0, NumDevs = 1
```

I'm trying to build the CUTLASS profiler to test GEMM performance with FP4 and FP8 data types on Jetson AGX Thor.

Steps to Reproduce
1. Clone the CUTLASS repository.
2. Navigate to the build directory (e.g., `mkdir build && cd build`).
3. Run the following CMake command:
```TEXT
cmake .. -DCUTLASS_NVCC_ARCHS="110a" -DCUTLASS_LIBRARY_KERNELS=all -DCUTLASS_UNITY_BUILD_ENABLED=ON
```
4. Build the profiler:
```TEXT
make cutlass_profiler -j$(nproc)
```

Error Log
The build fails with the following error:
```TEXT
cutlass/include/cutlass/gemm/kernel/sm100_gemm_array_tma_warpspecialized.hpp(553): error: static assertion failed with "SMEM usage exceeded capacity."
      static_assert(SharedStorageSize <= cutlass::arch::sm100_smem_capacity_bytes, "SMEM usage exceeded capacity.");
      ^
```

Additional Details
- This seems related to shared memory (SMEM) capacity limits on the SM100 architecture (targeted via -DCUTLASS_NVCC_ARCHS="110a" for Jetson AGX Thor).
- The build succeeds without errors if I exclude certain kernels or change architectures, but I need all kernels for comprehensive FP4/FP8 GEMM testing.
- Has anyone encountered this on similar hardware? Is there a workaround, such as adjusting SMEM limits or excluding specific kernels?

Thanks for any help!

## 评论 (3)

### Andy1314Chen · 2025-11-25

I commented out this line of code, `cutlass/include/cutlass/gemm/kernel/sm100_gemm_array_tma_warpspecialized.hpp(553): error: static assertion failed with "SMEM usage exceeded capacity."`, and then `cutlass_profiler` can compile normally. Although I don't know what problems this will bring.

### Zhao-Dongyu · 2025-12-24

I've tested the fix mentioned in [issue #2727](https://github.com/NVIDIA/cutlass/issues/2727) and it works for me on the Thor platform.

**Problem:**
The original code directly uses `sizeof` to get the shared memory size of the pipeline without considering alignment requirements, which can lead to inaccurate shared memory capacity calculations.

**Solution:**
Modify `include/cutlass/gemm/collective/builders/sm100_blockscaled_umma_builder.inl`:

```cpp
// Original (incorrect):
// constexpr auto mainloop_pipeline_bytes = sizeof(typename cutlass::PipelineTmaUmmaAsync<1>::SharedStorage);

// Fixed version:
constexpr auto mainloop_pipeline_bytes = cutlass::round_up(sizeof(typename cutlass::PipelineTmaUmmaAsync<1>::SharedStorage), 128);
```

**Explanation:**
This alignment fix uses `cutlass::round_up` to align the shared memory size to a 128-byte boundary, ensuring proper memory alignment and accurate capacity calculations. This resolves the shared memory capacity calculation issue.

**Verification:**
Tested and confirmed working on **NVIDIA Thor 5000** platform.

### github-actions[bot] · 2026-03-24

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.
