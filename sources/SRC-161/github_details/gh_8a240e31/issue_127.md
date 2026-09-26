# [Issue #127] FlashInfer Solutions Benchmarking?

source: https://github.com/flashinfer-ai/flashinfer-bench/issues/127
state: closed | updated: 2025-12-16T01:54:57Z
labels: 

## 正文

Currently, for FlashInfer-based solutions, `plan()` is invoked inside the solution body. As a result, the benchmark harness seems to include the planning overhead in the measured execution time, and the results cannot match the latency shown here: https://bench.flashinfer.ai/ 

## 评论 (2)

### zanderjiang · 2025-12-15

Thanks Shiyi for raising the issue. The FlashInfer wrapper solutions in the dataset are outdated. When we benchmarked the attention kernels for https://bench.flashinfer.ai/, we cached planned wrappers across calls and only re-planned when metadata changed, which better represents the actual usage. We'll update the `flashinfer_wrapper` solutions to the new version.

### xslingcn · 2025-12-16

Done with https://huggingface.co/datasets/flashinfer-ai/flashinfer-trace/commit/82c9ec675206904379dd1c6218633202bb52d168
