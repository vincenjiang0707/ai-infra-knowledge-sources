# [Issue #283] Hardcoded Draft Tokens Probabilities

source: https://github.com/SafeAILab/EAGLE/issues/283
state: closed | updated: 2025-08-17T20:35:29Z
labels: 

## 正文

https://github.com/SafeAILab/EAGLE/blob/6a44f65b8c109fd48dbdb145d03bbf5b3f1f0547/eagle/model/utils.py#L398C21-L398C29

In the `utils.evaluate_posterior` function, which is responsible for verification, the qx is hardcoded, and the acceptance probability is computed based on qx=1, which I believe is not correct. If this is done on purpose, can you elaborate on the reason?

## 评论 (1)

### hongyanz · 2025-08-16

This is done on purpose. Please refer to this issue: https://github.com/SafeAILab/EAGLE/issues/183
