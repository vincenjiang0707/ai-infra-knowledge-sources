# [Issue #1781] [FEATURE]: Add support for AMD Infinity Storage for DMA to/from AMD GPU memory for storage IO

source: https://github.com/ai-dynamo/nixl/issues/1781
state: open | updated: 2026-07-25T03:10:38Z
labels: rocm-amd

## 正文

NIXL was recently updated to support AMD GPUs. We extend the functionality by adding support for AMD Infinity Storage which is comparable to NVIDIA's GPU Direct Storage.

AMD Infinity Storage is enabled via the [ROCm hipFile][ref-hipfile] library and we integrate NIXL support for this for both local NVMe based storage and shared RDMA-based filesystem storage.

I plan to work on a PR for this. So opening an issue so we can track that.

[ref-hipfile]: https://github.com/ROCm/hipFile

## 评论 (1)

### sbates130272 · 2026-06-17

Note that I plan to break this out and to start with a PR for just a new AIS_MT plugin which is aligned with the existing GDS_MT plugin. And updates to both nixl and nixlbench to support this. After that I will work up something for rocm_ais which will be aligned with cuda_gds. Stay tuned!
