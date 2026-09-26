# [Issue #56] [Roadmap] Roadmap for Metal, OpenCL, VHLS, WebGPU, and SPIR-V Support

source: https://github.com/tile-ai/tilelang/issues/56
state: open | updated: 2026-09-09T22:03:20Z
labels: 

## 正文

It's simple for us to extend the codegen and runtime from apache tvm.

- [x] Support Metal
- [ ] Support OpenCL
- [ ] Support VHLS
- [x] Support WebGPU
- [ ] Support SPIR-V
- [ ] Support Hexagon


## 评论 (6)

### fernchen · 2025-01-26

Hi, very excellent job! May I ask that it currently support vector(avx) and matrix(amx) instruction generation for x86 CPUs

### LeiWang1999 · 2025-01-26

@fernchen Absolutely! We can support this. tilelang.language is fully compatible with TVM TensorIR. You can write or wrap an AMV/AMX intrinsic using T.call_extern, similar to the examples provided in TIR.

we currently support cpu codegen, checkout the test: https://github.com/tile-ai/tilelang/blob/main/testing/python/cpu/test_tilelang_cpu_gemm.py

### LeiWang1999 · 2025-09-25

metal support #799 

### FlashBarryAllen · 2025-12-10

It's very cool plan. When will we support `OpenCL` with `tileLang`? I'm looking forwarding to using it.

### LeiWang1999 · 2025-12-12

@FlashBarryAllen Thanks for your interest. While an OpenCL backend would be relatively simple to implement by reusing a lot of TVM's existing code, the main challenge is that we currently lack the bandwidth to maintain such a backend, including its related CI and testing infrastructure. We would be open to including it if an organization were willing to take ownership of that component.

### anerli · 2026-09-09

Any timeline on SPIR-V? What does the implementation path look like? Would be great as an alternative for GPU architectures not supported by other pathways
