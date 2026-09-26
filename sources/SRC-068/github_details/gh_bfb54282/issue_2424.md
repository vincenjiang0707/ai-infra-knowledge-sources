# [Issue #2424] [Feature Request] qo_len Invariant CTA Sizes

source: https://github.com/flashinfer-ai/flashinfer/issues/2424
state: closed | updated: 2026-09-19T07:09:10Z
labels: feature request, op: attention

## 正文

Hello!

When testing batch invariant vLLM with FlashInfer attention backend, it was noticed that even with a fixed split size and split KV disabled, there could still be times when batch invariance fails. Specifically, one could reproduce this by batching a longer request with many short ones and compare the long request being batched to the long request being sent on it's own. In this case, the invariance for the long request seems to be from a varied cta_tile_q: 64 when batched with the short requests, while 128 when sent alone.

Would it be possible to expose a qo_len invariant way for determining cta_tile_q for batch invariant purposes? Thanks!

## 评论 (2)

### frankwang28 · 2026-03-18

!claim

### flashinfer-bot · 2026-03-18

Issue assigned to @frankwang28.
