# [Issue #1851] Utility to tokenize a dataset for distillation after pruning (puzzletron/minitron) based on DATA_BLEND variable

source: https://github.com/NVIDIA/Model-Optimizer/issues/1851
state: closed | updated: 2026-07-17T08:23:14Z
labels: feature request, torch.pruning

## 正文

The minitron compression tutorial specifies a data blend to use in distillation starting with a DATA_BLEND variable (see in tutorial](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/megatron_bridge/tutorials/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16#data-blend))

The whole dataset is big 100B and involves blending multiple datasets. Preparing a smaller dataset set based on this blend, e.g. 1B, for distillation sanity checks, is cumbersome.

Prepare an utility that would enable to prepare such data blend 1B with a one click, e.g., based on the DATA_BLEND variable only.




## 评论 (1)

### danielkorzekwa · 2026-07-17

Duplicate of https://github.com/NVIDIA/Model-Optimizer/issues/1876
