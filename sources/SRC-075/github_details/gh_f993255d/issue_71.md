# [Issue #71] More Robust Dataset Object

source: https://github.com/ScalingIntelligence/KernelBench/issues/71
state: closed | updated: 2026-01-18T21:03:58Z
labels: 

## 正文

Since KernelBench problems are 1-indexed (logically) and a lot of the logic in current repo is zero indexed (indexing in a list after a file scan), it could cause some confusion with arbitary off-by-errors. Goal is to add a `KernelBenchDataset` object for easy access. 

I sent @pythonomar22 a basic example from my prev repo and we will integrate throughout this. 

## 评论 (1)

### simonguozirui · 2026-01-18

Should be done now in #95 and much easier / cleaner to use.
Hopefully with this people can plug in their own custom programs / levels / data as they wish easily.
