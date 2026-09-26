# [Issue #335] Does shifting by one position when constructing the input break the causal chain? For example:  input_ids_target = input_ids[:, 1:]

source: https://github.com/SafeAILab/EAGLE/issues/335
state: open | updated: 2026-06-03T13:50:51Z
labels: 

## 正文

Dear Author,

When constructing the input, does shifting input_ids_target to the right break the causal dependency chain among the input tokens?

Or is the causal relationship already implicitly captured in the hidden states by default?

Thank you.

## 评论 (0)
