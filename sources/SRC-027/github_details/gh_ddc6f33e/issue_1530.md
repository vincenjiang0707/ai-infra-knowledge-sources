# [Issue #1530] Duplicated BETA in DPO loss

source: https://github.com/AI-Hypercomputer/maxtext/issues/1530
state: closed | updated: 2026-07-15T19:01:56Z
labels: 

## 正文

It seems that there are two BETA in the DPO loss, but there should be only one. Is this intentional?

https://github.com/AI-Hypercomputer/maxtext/blob/acb0433c4832eeae2e4122122cc70e5f276503e5/MaxText/train.py#L317



## 评论 (2)

### rodrigo-f-nogueira · 2025-04-06

cc'ing @rdyro 

### igorts-git · 2026-07-15

This issue is now obsolete. We have recently switched to Tunix-based DPO implementation. Tunix includes its own loss function. We also added a test that compares the results against HuggingFace TRL.
