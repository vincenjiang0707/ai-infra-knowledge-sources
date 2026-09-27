# [Issue #4525] fix: seed=0 silently ignored in chat/completions and completions endpoints

source: https://github.com/InternLM/lmdeploy/issues/4525
state: closed | updated: 2026-04-14T08:15:28Z
labels: 

## 正文

## Problem

In `lmdeploy/serve/openai/api_server.py`, the `random_seed` is derived from `request.seed` using a falsy check:

```python
random_seed = request.seed if request.seed else None
```

This appears in two places (lines 463 and 812). The issue is that when a user explicitly passes `seed=0`, the expression `if request.seed` evaluates to `False` (since `0` is falsy in Python), causing `random_seed` to be set to `None` instead of `0`. This means **a deterministic seed of `0` is silently discarded**, and generation becomes non-deterministic despite the user requesting reproducibility.

## Reproducible Example

```python
# User requests deterministic output with seed=0
response = client.chat.completions.create(
    model="...",
    messages=[{"role": "user", "content": "Hello"}],
    seed=0  # Intended: deterministic output
)
# Bug: seed=0 is treated as None → non-deterministic output
```

## Expected

When `seed=0` is provided, it should be passed through to `GenerationConfig` as `random_seed=0`, enabling deterministic generation with seed 0.

## Fix

Replace the falsy check with an explicit `is not None` check:

```python
# Before (buggy):
random_seed = request.seed if request.seed else None

# After (correct):
random_seed = request.seed if request.seed is not None else None
```

This fix applies to two locations in `api_server.py` — one in `chat_completions_v1` (line 463) and one in `completions_v1` (line 812).

## 评论 (0)
