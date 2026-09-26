# [Issue #489] [Question] What's the issue fixed by #454

source: https://github.com/deepseek-ai/DeepEP/issues/489
state: closed | updated: 2026-09-18T09:15:17Z
labels: 

## 正文

Hello,

I noticed there was a new pull request https://github.com/deepseek-ai/DeepEP/pull/454， but could not find the issue related. So what's the orignal issue?


Thanks 

## 评论 (2)

### sphish · 2025-11-12

The pr fixed a potential integer overflow in the buffer address offset calculation. If your buffer size exceeds the range of a 32‑bit integer, you may encounter this issue.

### polarstormx · 2026-09-18

Closing as answered by [the maintainer's explanation](https://github.com/deepseek-ai/DeepEP/issues/489#issuecomment-3519696060) of the integer-overflow fix in #454 (commit 4623c67).
