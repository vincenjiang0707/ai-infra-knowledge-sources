# [Issue #1786] Using lm-eval for puzzletron fails - lm-eval not installed

source: https://github.com/NVIDIA/Model-Optimizer/issues/1786
state: closed | updated: 2026-07-29T16:30:21Z
labels: documentation, torch.pruning

## 正文

ModelOpt: main from 6/22/26

Using lm-eval for puzzletron fails - lm-eval not installed.

there is no info in [the docs](https://github.com/NVIDIA/Model-Optimizer/blob/main/examples/puzzletron/README.md#evaluation) that lm-eval must be installed

## 评论 (1)

### kevalmorabia97 · 2026-06-22

Feel free to submit a PR for updating this. We already have puzzletron section in llm_eval/readme.md so better to just cross link there here instead of keeping 2 copies: https://github.com/NVIDIA/Model-Optimizer/blob/main/examples/llm_eval/README.md#heterogeneous-pruned-checkpoints-puzzletron
