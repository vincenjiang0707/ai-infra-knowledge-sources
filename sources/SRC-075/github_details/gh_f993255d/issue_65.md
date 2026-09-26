# [Issue #65] pydra module：ImportError

source: https://github.com/ScalingIntelligence/KernelBench/issues/65
state: closed | updated: 2025-12-27T04:29:08Z
labels: 

## 正文

I executed this command for testing
`python3 scripts/generate_and_eval_single_sample.py dataset_src="huggingface" level=2 problem_id=40`
The following error is generated：
```
(kernel-bench) [root@localhost KernelBench]# python3 scripts/generate_and_eval_single_sample.py dataset_src="huggingface" level=2 problem_id=40
Traceback (most recent call last):
  File "/home/hcz/KernelBench/scripts/generate_and_eval_single_sample.py", line 3, in <module>
    from pydra import REQUIRED, Config
ImportError: cannot import name 'REQUIRED' from 'pydra' (/root/miniconda3/envs/kernel-bench/lib/python3.10/site-packages/pydra/__init__.py)
```

I have tried methods such as changing the pydra version and using a conda environment, but the issue remains unresolved. Thank you for your assistance, and I hope you can provide a solution to this problem.

## 评论 (1)

### simonguozirui · 2025-12-27

I think the lastest version of `pydra` (installed from `pydra-config`, which @jordan-benjamin's variant of hydra) has the REQUIRED field.

We recently moved from conda and pip to uv-based package management (#112). Mind giving it a try with that stack? 
