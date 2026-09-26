# [Issue #3558] think_end_token support needed for local-chat-completions mode

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3558
state: closed | updated: 2026-08-20T16:02:10Z
labels: 

## 正文

think_end_token is essential for tasks like ifeval.
currently this is only used when doing local inference, and not for api based completions.
can we pleaes have support for it?

## 评论 (1)

### yaodong-shen · 2026-07-28

I reproduced this on current `main` (`f4d4b3d`): `LocalChatCompletion.parse_generations()` returns the full `<think>...</think> final answer` response unchanged. I can work on a focused fix that accepts a string `think_end_token` for OpenAI-compatible chat backends, reuses the existing shared post-processing semantics (strip through the last delimiter), preserves today's output when the option is unset, and adds parser regression tests plus documentation. I'll keep this scoped to generated chat text; no API payload or loglikelihood behavior changes.

