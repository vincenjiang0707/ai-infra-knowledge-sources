# [Issue #1779] Puzzletron OOM during step 6 (one-block scoring) for Qwen 3.5-2B VLM

source: https://github.com/NVIDIA/Model-Optimizer/issues/1779
state: open | updated: 2026-06-21T17:33:41Z
labels: bug

## 正文

branch: dkorzekwa/claude_qwen35

Environment: 2× H100 80GB, Puzzletron full pipeline, nproc_per_node=2

Model: Qwen3.5-2B (model_type: qwen3_5, a VLM with nested text_config)

Failure: torch.OutOfMemoryError on GPU 1 during step 6 ("calculating one block scores"), with ~74 GiB consumed out of 80 GiB.

## 评论 (1)

### danielkorzekwa · 2026-06-21

6/8 step works fine for qwen 3.5 0.8B
