# [Issue #5] Benchmarks

source: https://github.com/FasterDecoding/Medusa/issues/5
state: closed | updated: 2023-09-13T22:50:07Z
labels: 

## 正文

It would be nice if the readme (or blog) included some of the common benchmarks which compare the quality of speculatively decoded inference vs the original model’s quality.

## 评论 (2)

### leeyeehoo · 2023-09-12

We use [MT Bench](https://github.com/lm-sys/FastChat/blob/main/fastchat/llm_judge/data/mt_bench/question.jsonl) from FastChat. The results are shown in [the blog Appendix](https://sites.google.com/view/medusa-llm#h.2yq1gf32dw1x). If the temperature is set to 0, it should be exactly the same output as the original model's greedy-decoding output as the demo shows. If you have further questions feel free to reopen the issue!

### someone13574 · 2023-09-13

Is there data on how the MT Bench score changes with changes in head count and for different model sizes? Or is benchmark performance most dominantly controlled by typical acceptance and other factors negligible?
