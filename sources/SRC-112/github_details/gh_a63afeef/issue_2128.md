# [Issue #2128] DeepSeek-V4-Pro FP8 on H200 (tp-8) crashes at SGLang init — --mem-fraction-static 0.88 underbudgets the KV-cache pool

source: https://github.com/SemiAnalysisAI/InferenceX/issues/2128
state: closed | updated: 2026-09-09T21:14:05Z
labels: 

## 正文

**Describe the bug**
`benchmarks/single_node/fixed_seq_len/dsv4_fp8_h200_sglang.sh` and `dsv4_fp8_h200_sglang_mtp.sh` launch `sglang serve … --tp 8 … --mem-fraction-static 0.88`. On an H200 (~140.4 GB/GPU), the DeepSeek-V4-Pro FP8 weights occupy ~125.65 GB/GPU at tp-8, so a 0.88 static fraction (~123.5 GB) is smaller than the weights. SGLang's memory-pool profiler then finds no room for the KV cache and aborts at scheduler init before serving any request. Recent SGLang builds emit a precise minimum-viable fraction: **0.9113** for the non-speculative script and **0.9335** for the MTP script (the EAGLE/NextN draft weights add ~3.07 GB and are now counted).

**To Reproduce**
1. Container `lmsysorg/sglang:deepseek-v4-hopper` on 8xH200 (~140 GB each).
2. Run `dsv4_fp8_h200_sglang.sh` (or `_mtp.sh`) with `MODEL=deepseek-ai/DeepSeek-V4-Pro TP=8 ISL=8192 OSL=1024 CONC=1`.
3. Server launches with `--tp 8 --mem-fraction-static 0.88`.
4. Init aborts.

**Expected behavior**
The server initializes with a positive KV-cache pool and serves the benchmark.

**Actual behavior / logs**
```
Load weight end. quant=fp8, fmt=e4m3, avail mem=12.25 GB, mem usage=125.65 GB.
# non-MTP:
ValueError: Loaded weights leave no GPU memory for the KV cache under --mem-fraction-static=0.88.
  Raise --mem-fraction-static above 0.912 (minimum viable = 1 - available/pre = 0.9113).
# MTP (EAGLE): DeepseekV4ForCausalLMNextN draft adds mem usage=3.07 GB
ValueError: … Raise --mem-fraction-static above 0.934 (minimum viable = 0.9335).
  If using speculative decoding, draft weights are now counted.
```
(Older SGLang builds raised the same condition as `RuntimeError: Not enough memory. Please try to increase --mem-fraction-static.` at `pool_configurator.py:56`.)

**Proposed fix**
Raise `--mem-fraction-static` from `0.88` to `0.94` in both `dsv4_fp8_h200_sglang.sh` and `dsv4_fp8_h200_sglang_mtp.sh`. `0.94` clears both floors (non-MTP 0.9113, MTP 0.9335) with headroom. Validated on 8xH200: both speculative (EAGLE/MTP) and non-speculative variants initialize and serve, isl 1024/8192, concurrency 1->64 (KV pool available_bytes -4.31 GB -> +3.97 GB, full_token -> 109312).

**Environment**
8xH200 (143771 MiB/GPU); container `lmsysorg/sglang:deepseek-v4-hopper`; model `deepseek-ai/DeepSeek-V4-Pro` (FP8); `--tp 8`. Exact SGLang/CUDA/Python versions are those baked into the pinned `deepseek-v4-hopper` image; the nvidia-smi/env capture command was not runnable in the CI artifact context.

_This issue was drafted with assistance from the `opus` AI model._

## 评论 (1)

### janbernloehr · 2026-09-09

Closing as resolved by the SGLang image update; no recipe change is needed.  
Current InferenceX pins `deepseek-v4-hopper@sha256:1bf5d508…`. With the existing `--mem-fraction-static 0.88`, weight usage dropped from ~125.7 GB to ~103–104 GB/GPU, leaving a positive KV-cache budget. Both non-MTP and MTP variants now initialize and serve successfully.  
The proposed 0.94 change is therefore unnecessary. This issue remains relevant only for older or unpinned images with the larger weight footprint.
