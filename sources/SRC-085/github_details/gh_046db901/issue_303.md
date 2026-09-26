# [Issue #303] Eagle3 draft model embedding table and LM Head/Draft model sampling length

source: https://github.com/SafeAILab/EAGLE/issues/303
state: closed | updated: 2025-10-20T07:59:07Z
labels: 

## 正文

Hello! After read the source code, I want to confirm does draft model in Eagle3 not share same parameters on **Embedding Layer and LM Head** with the target model?

And how to determine the sampling length in one inference？
Thanks a lot!

## 评论 (1)

### hongyanz · 2025-10-20

The Embedding Layer is shared, while the LM head is not shared.

The sampling length in one inference is a hyperparameter that depends on your batch size and hardware. For example, when bs=1, we typically set the sampling length to be 8.
