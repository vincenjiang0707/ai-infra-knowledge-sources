# [Issue #366] [Feature] Will DeepGEMM support more advanced epilogue fusion for GEMM kernels?

source: https://github.com/deepseek-ai/DeepGEMM/issues/366
state: closed | updated: 2026-09-16T16:26:52Z
labels: 

## 正文

https://github.com/deepseek-ai/DeepGEMM/pull/347 has support BF16 accumulation, which can help a lot for large problem sizes. However, I'm wondering if DeepGEMM will consider support direct FP8 output GEMMs in the future and potentially other activation functions too?

## 评论 (2)

### hiSandog · 2026-07-02

A useful way to frame this feature request may be to separate API surface from kernel support. Direct FP8 output has different accuracy and scaling implications from BF16 accumulation, while activation fusion adds epilogue shape/layout constraints. If the maintainers are open to it, a target matrix such as `accumulator dtype -> output dtype -> supported epilogues` would make it clearer which combinations are intended to stay in DeepGEMM versus be handled by a follow-up kernel.


### b8zhong · 2026-09-16

Solved by https://github.com/deepseek-ai/DeepGEMM/pull/432
