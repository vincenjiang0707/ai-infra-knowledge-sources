# [Issue #158] run_awq.<locals>.Catcher.forward() error

source: https://github.com/mit-han-lab/llm-awq/issues/158
state: open | updated: 2026-07-16T14:59:43Z
labels: 

## 正文

When i try to add chatGLMv3 model,  got the error.
TypeError: run_awq.<locals>.Catcher.forward() takes 2 positional arguments but 4 were given

I debuged the samples(get_calib_dataset), it's a bs*seqlen tensor, it's normal inputs for Catcher.forward() , not 4 givens

## 评论 (1)

### Chessing234 · 2026-07-16

Fixed in #328 — `Catcher.forward` accepts `*args`.
