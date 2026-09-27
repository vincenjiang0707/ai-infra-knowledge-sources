# [Issue #212] INT 3 support

source: https://github.com/mit-han-lab/llm-awq/issues/212
state: closed | updated: 2024-08-02T10:40:08Z
labels: 

## 正文

Hi, is it possible to run AWQ with W3A16? How were the results in the paper with INT3 obtained?

## 评论 (1)

### DavidePaglieri · 2024-08-02

Upon closer inspection, there is a way to have fake_backend and run INT3 (args.q_backend == "fake"). However the current repo doesn't support INT3 kernels.
