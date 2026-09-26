# [Issue #1920] Quality Evals that stress longer decode / 压力测试长解码的质量评估

source: https://github.com/SemiAnalysisAI/InferenceX/issues/1920
state: open | updated: 2026-07-04T05:16:46Z
labels: 

## 正文

I love the new Eval benchmarks idea and think you pick one that is less saturated to expose quantization gaps.
AIME 2024/2025  is less saturated and requires more thinking (but still no sandbox) and exposes more quantization gaps in my experiments than gsm8k or MMLU. It will take slightly longer to run but worth it!

## 中文说明
建议选择 AIME 2024/2025 作为质量评估基准测试。与 GSM8K 或 MMLU 相比，AIME 不那么饱和，需要更深入的推理（但无需沙盒），能更好地暴露量化精度差异。运行时间稍长但值得。


## 评论 (2)

### sshleifer · 2026-06-24

happy to send PR for this

### functionstackx · 2026-06-24

@sshleifer evals is top of mind for the upcoming AgentX, can u talk to Simon or Horace or Soumith to add you the thinkingmachine<>semi slack so that we can comms there?
