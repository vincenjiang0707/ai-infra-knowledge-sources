# [Issue #2442] Refactor interactive scenario to not be a benchmark

source: https://github.com/mlcommons/inference/issues/2442
state: closed | updated: 2026-08-04T15:59:14Z
labels: 

## 正文

[6.0 post-mortem] Follow-up of #2191 
We are having many more interactive scenarios in the suite, and each will add a new "benchmark" to the loadgen mlperf.conf as in `gpt-oss-120b-interactive` instead of an optional scenarios.

E.g.: https://github.com/mlcommons/inference/blob/7651400aadb765f2183047203aaa1381f4a0f9d5/loadgen/mlperf.conf#L143

This is inconsistent with the submission checker, where the interactive is treated as a scenario. We should unify the logic

cc: @v-shobhit @pgmpablo157321 

## 评论 (1)

### hanyunfan · 2026-08-04

WG: Pablo confirmed this can be closed 
