# [Issue #3524] Example 64 (Ada FP8 grouped GEMM) refuses capable GPUs via exact CC 8.9 gate

source: https://github.com/NVIDIA/cutlass/issues/3524
state: open | updated: 2026-09-05T04:38:00Z
labels: CUTLASS C++

## 正文

### Description

examples/64_ada_fp8_gemm_grouped/ada_fp8_gemm_grouped.cu (~line 1107) gates execution on exactly compute capability 8.9:

```cpp
if (!(properties.major == 8 && properties.minor == 9)) {
    std::cerr << "... requires a device of compute capability 89." ...
```

The grouped FP8 kernels here compile cleanly for newer architectures, and the sibling example 58_ada_fp8_gemm uses the inclusive form:

```cpp
if (properties.major < 8 || (properties.major == 8 && properties.minor < 9))
```

On an RTX 5060 Ti (sm_120a, CUDA 12.8.1) the stock binary exits immediately with the capability message; with the gate relaxed to the sibling's form the example builds and runs to completion including device-reference verification (`Passed`). Example 64 is therefore refusing capable hardware for no functional reason.

### Suggested fix

Use the same `major*10+minor < 89` / `major < 8 || (major == 8 && minor < 9)` inclusive check as example 58.


## 评论 (1)

### SAR2652 · 2026-09-05

Hi @VaggelisGian I opened #3586  with the inclusive gate fix and verified it on sm_120a
