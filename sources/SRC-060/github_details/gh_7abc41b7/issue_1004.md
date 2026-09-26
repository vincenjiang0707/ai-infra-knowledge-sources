# [Issue #1004] RuntimeError: (NotFound) The kernel `expand_modality_expert_id` is not registered.

source: https://github.com/PaddlePaddle/ERNIE/issues/1004
state: closed | updated: 2025-10-09T12:00:50Z
labels: 

## 正文

训练 ERNIE-4.5-21B-A3B 的时候出现 RuntimeError: (NotFound) The kernel `expand_modality_expert_id` is not registered. 怎么解决呢？训练MOE模型才会出现的问题。

## 评论 (2)

### fjjF77 · 2025-07-10

请检查一下您的CUDA版本和paddle版本，该算子要求CUDA版本>12，paddle版本为最新版本（3.1）。

### nepeplwu · 2025-10-09

The issue has no response for a long time and will be closed. You can reopen or new another issue if are still confused.

---
_From Bot_
