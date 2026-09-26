# [Issue #359] [feature suggestion] instead of using random datasets, it should use real datasets / [feature suggestion] 应使用真实数据集而非随机数据集

source: https://github.com/SemiAnalysisAI/InferenceX/issues/359
state: closed | updated: 2026-07-08T15:57:25Z
labels: 

## 正文

Almost all benchmark configurations set `max_model_len` or for TensorRT `--max_seq_len`, which controls the maximum supported length of request (inclusive of the prompt and any generated output). It is typically set to [ISL + OSL + tiny_margin](https://github.com/InferenceMAX/InferenceMAX/blob/84320a0aadacae1114265b553830f48b56231817/benchmarks/gptoss_fp4_b200_docker.sh#L22) (where tiny_margin may be 20 or 200 tokens). This is also [done in generate_sweep_configs.py](https://github.com/InferenceMAX/InferenceMAX/blob/84320a0aadacae1114265b553830f48b56231817/utils/matrix_logic/generate_sweep_configs.py). These options of course impact memory allocation and so maximum achievable batch size.

It's understandable for a benchmark to be showing something approaching the peak obtainable results, but tuning the inference engine to the precise benchmark workload in this way seems to be going against the idea that "[We want server configs to reflect real world deployments as much as possible](https://newsletter.semianalysis.com/p/inferencemax-open-source-inference)" and the goal "to provide benchmarks that both emulate real world applications as much as possible and reflect the continuous pace of software innovation.". I struggle to think of a real world application of DeepSeek that would be able to run with a ~2k maximum sequence length for instance.

## 中文说明
应使用真实数据集而非随机数据集进行基准测试。


## 评论 (3)

### cquil11 · 2025-12-21

Yes, a good point and something we have discussed. This is sort of solved by no longer using random datasets and instead using real datasets. Something we are discussing.

### asb · 2026-01-04

Using real datasets _might_ address the issue, depending on whether the datasets cover a sufficiently large variety of ISLs (and expected OSLs) that make tuning to a specific length in a way that that could never be done in a real-world deployment is ineffective.

I think it would be better to set some explicit rules for benchmark participants on this kind of tuning (which had been suggested in my original title), and this may be necessary even if real datasets are used. The retitling of this issue to "feature suggestion] instead of using random datasets, it should use real datasets" doesn't really reflect my suggestion.

### Marviel · 2026-02-25

We've been running experiments with Qwen3-8B-FP8 on H100 and noticed this exact issue.

We've noticed that random token ID inputs distort results: optimizations that exploit output repetitiveness get artificially inflated acceptance rates because small models tend to produce structured, repetitive output in response to incoherent input. On real text the output distribution is far more diverse and the same techniques are much less effective.

Also agree that explicit rules against max_model_len tuning are also worth formalising, independent of the dataset question.
