# [Issue #29] benchmark_eval_analysis.py: cannot import name 'REQUIRED' from 'pydra'

source: https://github.com/ScalingIntelligence/KernelBench/issues/29
state: closed | updated: 2025-03-25T06:51:24Z
labels: 

## 正文

python3 scripts/benchmark_eval_analysis.py run_name=test_hf_level_1 level=1 baseline=baseline_time_torch

Traceback (most recent call last):
  File "***/KernelBench/scripts/benchmark_eval_analysis.py", line 4, in <module>
    from pydra import REQUIRED, Config
ImportError: cannot import name 'REQUIRED' from 'pydra' (unknown location)

I'm using pydra 0.24.


## 评论 (0)
