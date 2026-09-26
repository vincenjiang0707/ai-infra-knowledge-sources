# [Issue #296] [Question] How to autotune DeepGemm FP8 to maximize this baseline performance?

source: https://github.com/deepseek-ai/DeepGEMM/issues/296
state: closed | updated: 2026-04-17T02:40:11Z
labels: 

## 正文

To maximize the performance of DeepGemm, do I need to call some pre-configuration / autotuning interface to maximize this performance **for specific shape** below?

```
# auto-tune needed or not?
deep_gemm.fp8_gemm_nt((a_fp8, a_s), (b_fp8, out1)
```


## 评论 (1)

### zheanxu · 2026-04-17

The FP8 GEMM automatically selects a good config based on built-in heuristics, so no explicit autotuning interface is required. If you want to achieve the absolute best performance for your specific shape, you can manually adjust the heuristics.
