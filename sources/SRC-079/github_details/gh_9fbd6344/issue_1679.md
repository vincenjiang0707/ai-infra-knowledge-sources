# [Issue #1679] Add MBridge distillation for puzzletron

source: https://github.com/NVIDIA/Model-Optimizer/issues/1679
state: open | updated: 2026-06-24T13:15:49Z
labels: feature request

## 正文

### Detailed description of the requested feature
After the puzzletron prunes the model, we want a repair phase that will run distillation from the teacher (original model, but possibly any other model) to the pruned model

### Timeline
Work in progress. Requires "general" support of heterogeneous models in Mcore. The idea is to patch the mbridge-mcore model creation using the block_configs from anymodel.
This also requires some updates (PRs) to MBridge code as well 

## 评论 (1)

### chochowski · 2026-06-11

The branch with the distillation https://github.com/NVIDIA/Model-Optimizer/tree/mchochowski/puzzletron_distillation 
Needs to be cleaned and rebased on current main
Plan is as follows:
1. clear and rebase ETA 15/06
2. add all possible fixes directly to MBrige to minimize patching ETA 19/06
3. add example configs for KD to supported models ETA 19/06
4. merge (start process ETA 19/06)
