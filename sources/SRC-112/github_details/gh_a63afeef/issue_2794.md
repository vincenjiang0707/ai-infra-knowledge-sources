# [Issue #2794] Add GLM-5.3-Flash (320B-A18B, hybrid KDA+DSA attention) as its own model prefix for AgentX

source: https://github.com/SemiAnalysisAI/InferenceX/issues/2794
state: closed | updated: 2026-09-03T00:17:17Z
labels: 

## 正文

The 2026/08 README line and the dashboard's `GLM5.2/GLM5.3 744B` entry both refer to the 744B MoE. GLM-5.3-Flash is a different model — 320B total / 18B active, 45 text layers of which 34 are KDA linear attention and 11 are DSA sparse, plus mHC and a native MTP draft layer, 1M context, MIT weights. It won't ride the `glm5.2` alias any more than DeepSeek-V4-Flash rides `dsv4` or Qwen3.8-Flash-Next rides `qwen3.5`.

Why it seems worth its own prefix:

- It was the #1 model on OpenRouter's day board on 2026-08-26 (356.7B prompt / 4.09B completion tokens across 5.27M requests), and its stealth predecessor `stealth/ox-alpha` was running 3.94T prompt tokens/day there.
- Its entire design claim is long-context agentic serving cost — Z.ai state 3.01x less attention compute and a 4.44x smaller KV cache than GLM-5.3 — which is exactly what AgentX measures and which nothing public currently covers. Every community measurement so far is DGX Spark / RTX PRO 6000 class at concurrency <= 8, on 8K prompts.
- Day-0 support already exists: `lmsysorg/sglang:glm-5.3-flash`, with cookbook-verified GB300 TP4/EP4 and H100/H200 TP8/EP8 recipes. vLLM >= 0.27.0 also serves it.

Is a `glm5.3flash` prefix and an agentic launcher on the roadmap? Happy to help test if that's useful.


## 评论 (1)

### functionstackx · 2026-09-03

glm5.3 referring to https://huggingface.co/zai-org/GLM-5.3 and not glm5.3-flash
