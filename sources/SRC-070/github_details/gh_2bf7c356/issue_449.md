# [Issue #449] `num_qps_per_rank` equal to the number of local experts.

source: https://github.com/deepseek-ai/DeepEP/issues/449
state: closed | updated: 2026-09-18T09:50:16Z
labels: 

## 正文

Hi!
https://github.com/deepseek-ai/DeepEP/blob/main/deep_ep/buffer.py#L48-L49
I am wondering here, why does the  `num_qps_per_rank` need to equal to the number of local experts? Thank you!

## 评论 (1)

### sphish · 2025-10-11

Since the number of local experts on each GPU are identical, this essentially assigns one QP to each remote expert. This is intended to minimize unnecessary data dependencies as much as possible.
