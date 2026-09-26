# [Issue #28] Question: Will it affect the baseline/model results if I use a different version of torch/cuda?

source: https://github.com/ScalingIntelligence/KernelBench/issues/28
state: closed | updated: 2025-03-05T01:21:31Z
labels: 

## 正文

I would like to be able to run KernelBench over V100.

## 评论 (1)

### simonguozirui · 2025-03-05

Thanks for your interest in our project.

To run this on V100, there are a few things you need to do. Check out the guide in `results/timing`
1. First, you need to run the baseline time on V100 (your cluster), check out `python3 scripts/generate_baseline_time.py`.
2. When you eval your generated kernels, please set `gpu_arch` to Volta.
3. Then you can compute the speedup of your generated kernel vs your baseline on Volta.  

Let me know if that works.
