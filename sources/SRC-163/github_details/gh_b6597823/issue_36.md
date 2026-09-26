# [Issue #36] [Profile] How to use nsight to profile CUDA execution information

source: https://github.com/LLMServe/DistServe/issues/36
state: closed | updated: 2024-08-08T07:18:34Z
labels: 

## 正文

I use nsys cli to profile offline and serving, and found some problem

1. The cuda HW info  cannot be traced when I use example/offline.py
2. Prefill instance cudaHW info cannot be trace when use nsys to start a serving, only decode instance
3. Use nsys in ray actor to profile single Process, still cannot trace cudaHW.

Can I ask for how to profile correctly?

## 评论 (2)

### interestingLSY · 2024-08-08

DistServe uses [Ray](https://www.ray.io/). If you want to profile it by nsys,you may need to refer to [Ray's Document](https://docs.ray.io/en/latest/ray-observability/user-guides/profiling.html)

### vincentccc · 2024-08-08

Thanks for your reply. I found the report seems make sense when I issue more requests
