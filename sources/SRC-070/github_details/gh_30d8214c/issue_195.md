# [Issue #195] Perf regression since sha f85ec6

source: https://github.com/deepseek-ai/DeepGEMM/issues/195
state: open | updated: 2025-10-20T13:09:19Z
labels: 

## 正文

Hi team, I am investigating a regression in performance for `m_grouped_gemm_fp8_fp8_bf16_nt_masked`. Benchmarking script to repro: https://gist.github.com/hj-mistral/d38801ce8e35860a7faba1e1688546cc.

## Env
GPU: H200
CUDA: 12.9

## Script output

### On sha 79f48ee15a82dd5fad5cd9beaa393c1f755e6b55 (current head)
```
Average time per iteration: 26.55 us
Bandwidth: 1030.01 GB/s
```

### On sha ea9c5d9270226c5dd7a577c212e9ea385f6ef048
```
Average time per iteration: 26.70 us
Bandwidth: 1024.26 GB/s
```

### On sha 3254b758e27a5b2f2ae68279314acb1adcb6c1bc
```
Average time per iteration: 20.16 us
Bandwidth: 1356.20 GB/s
```

Can you confirm?

## 评论 (2)

### zheanxu · 2025-09-25

Compared to commit 3254b75, the latest commit has optimized the shape configuration used by the actual inference service (tested in `test_fp8.py`). However, in some other scenarios, performance degradation is possible, as the current heuristic is difficult to cover all cases.
You can set the `DG_PRINT_CONFIGS=1` environment variable to print out the configuration differences, and choose the optimal configuration based on your use case.

### hj-mistral · 2025-10-20

Thanks! Is there a way to override the configurations without maintaining a fork? With some env variables or flags?
