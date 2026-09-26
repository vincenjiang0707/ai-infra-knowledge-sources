# [Issue #3639] HFLM: chat_template_args silently discarded when enable_thinking is None

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3639
state: closed | updated: 2026-07-31T13:30:40Z
labels: 

## 正文

## Bug

When passing `chat_template_args={"enable_thinking": False}` to HFLM without also passing `enable_thinking=False` as a separate kwarg, the `chat_template_args` dict is silently discarded and the model runs with default (thinking-enabled) behavior.

## Root cause

In `lm_eval/models/huggingface.py` lines 259-263:

```python
self.chat_template_args = (
    chat_template_args or {} | dict(enable_thinking=enable_thinking)
    if enable_thinking is not None
    else {}
)
```

When `enable_thinking=None` (the default), the ternary takes the `else` branch and returns `{}`, completely ignoring the user-provided `chat_template_args`.

## Expected behavior

When `enable_thinking` is `None`, `chat_template_args` should be preserved as-is:

```python
if enable_thinking is not None:
    self.chat_template_args = (chat_template_args or {}) | {"enable_thinking": enable_thinking}
else:
    self.chat_template_args = chat_template_args or {}
```

## Impact

This affects any user passing `enable_thinking` (or other kwargs) via `chat_template_args` rather than the dedicated `enable_thinking` parameter. For Qwen3 models, this means non-thinking mode cannot be activated through `chat_template_args`, only through the top-level `enable_thinking` kwarg.

## Reproduction

```python
from lm_eval.models.huggingface import HFLM

model = HFLM(
    pretrained="Qwen/Qwen3-0.6B",
    chat_template_args={"enable_thinking": False},
    # enable_thinking not passed (defaults to None)
)

print(model.chat_template_args)
# Expected: {"enable_thinking": False}
# Actual: {}
```

## Version

lm-eval 0.4.10

## 评论 (2)

### jbbqqf · 2026-05-23

Hi! Triaging older issues — this looks **already fixed in main**, the buggy ternary was reworked in PR #3675.

Evidence:
- The original buggy block at [`lm_eval/models/huggingface.py:259-263`](https://github.com/EleutherAI/lm-evaluation-harness/blob/d021bf84/lm_eval/models/huggingface.py#L259-L263) parsed as `chat_template_args or ({} | dict(...))` due to `|` binding tighter than `or`, so the `else {}` branch dropped the user-provided dict.
- That ternary was rewritten in commit [`c1c4bea3`](https://github.com/EleutherAI/lm-evaluation-harness/commit/c1c4bea3) (PR [#3675](https://github.com/EleutherAI/lm-evaluation-harness/pull/3675)) to `(chat_template_args or {}) | dict(enable_thinking=enable_thinking) if enable_thinking is not None else (chat_template_args or {})` — the `else` branch now preserves `chat_template_args` exactly as you proposed.
- Current code at [`lm_eval/models/huggingface.py:401-405`](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/models/huggingface.py#L401-L405) confirms the fix is live; passing `chat_template_args={"enable_thinking": False}` with `enable_thinking=None` now keeps the dict.

If you're still hitting this on a recent `main` checkout (≥ PR #3675), point me at the version + repro and I'll dig further. Otherwise would you mind closing this out?

---
*Disclosure: I drafted this comment with help from Claude Code while triaging stale issues; the references above were verified manually against the current source.*


### NezLheimeur · 2026-07-31

@jbbqqf thanks for the notification.

I checked current `main` and the fix is indeed live. That matches what #3675 (`c1c4bea3`) reworked, and it's the same shape as the fix I'd proposed in #3640 (which @baberabb closed as already-resolved).

Closing as resolved. Thanks both.
