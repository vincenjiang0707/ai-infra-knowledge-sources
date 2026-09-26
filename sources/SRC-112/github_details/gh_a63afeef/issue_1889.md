# [Issue #1889] Publish VLLM and SGLANG configs where possible / 尽可能同时发布 vLLM 和 SGLang 配置

source: https://github.com/SemiAnalysisAI/InferenceX/issues/1889
state: open | updated: 2026-07-04T05:17:01Z
labels: 

## 正文

All the benchmarks have either VLLM or sglang but not both. I assume this is to avoid twitter fights. I think a lot of people at labs like me are on a fork of one and spend some energy trying to translate one to the other, often poorly. I think it would be great for the community if you published both numbers (or at least encouraged it). Clearly this effort has sparked AMD to do a lot more useful shit so I think it VLLM v sglang competition would also probably be good for the community.  I would also not allow disable_prefix_cache=True type things but I feel less strongly about that. I also think from VLLM and SGLANG people twitter wars, the fights are not that bad (more publicity) and could actually be resolved more gracefully on this platform. 

## 中文说明
建议为每个模型/硬件配置同时发布 vLLM 和 SGLang 两套基准测试结果，而非仅选择其中一个框架。这有助于社区用户（尤其是使用其中一个框架分支的实验室）更好地对比两者性能，也能促进框架间的良性竞争。同时建议禁止 `disable_prefix_cache=True` 等不公平配置。


## 评论 (2)

### sshleifer · 2026-06-23

Paywall fine by me

### functionstackx · 2026-06-24

https://github.com/SemiAnalysisAI/InferenceX/issues/1920#issuecomment-4792918288
