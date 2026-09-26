# [Issue #1772] When creating a claude skill for puzzletron, quantization tests fails slowing down development process

source: https://github.com/NVIDIA/Model-Optimizer/issues/1772
state: open | updated: 2026-06-26T06:45:55Z
labels: bug

## 正文

I made a claude skill for puzzletron algo, then on CI a quantization test failed.

https://github.com/NVIDIA/Model-Optimizer/actions/runs/27755920751/job/82119078253?pr=1769

from pull request: https://github.com/NVIDIA/Model-Optimizer/pull/1769

it happened multiple times before, slowing down development process in modelopt.  

how about making modelopt more modular so that different parts could be developed in a more isolated way?

## 评论 (1)

### danielkorzekwa · 2026-06-26

similar issue again: https://github.com/NVIDIA/Model-Optimizer/actions/runs/28220116030/job/83600326898?pr=1831
