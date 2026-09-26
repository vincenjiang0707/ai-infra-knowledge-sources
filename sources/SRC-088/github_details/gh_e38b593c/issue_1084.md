# [Issue #1084] test_render_conversation_sends_truncation_options always fails

source: https://github.com/vllm-project/speculators/issues/1084
state: closed | updated: 2026-09-04T19:13:49Z
labels: 

## 正文

## Summary

`tests/integration/datagen/test_render_boundary.py::test_render_conversation_sends_truncation_options` always fails with `httpx.ConnectError: [Errno -2] Name or service not known`.

## Root cause

The test (line 201) patches `render_client.httpx.post`, but `render_conversation` calls `_post()` which uses the module-level `_client.post()` (an `httpx.Client` instance). The monkeypatch never intercepts the call, so the real HTTP request to the dummy URL `http://x` fails with a DNS error.

Other tests in the same file (e.g. `test_render_conversation_missing_token_ids_raises`) correctly patch `render_client._post` directly.

## Fix

Change line 201 from:
```python
monkeypatch.setattr(render_client.httpx, "post", post)
```
to:
```python
monkeypatch.setattr(render_client, "_post", post)
```

(adjusting the mock signature to match `_post`'s call convention)

## Introduced by

#1079 (`ae96c74c`)

## 评论 (2)

### orestis-z · 2026-09-04

The test passed on #1079's own CI because that branch was likely based on a `render_client.py` that still used top-level `httpx.post`. The `_post`/`_client` refactor (from #1013) was already on main, so the test broke on merge — classic base-branch incompatibility.

### fynnsu · 2026-09-04

Working on a fix
