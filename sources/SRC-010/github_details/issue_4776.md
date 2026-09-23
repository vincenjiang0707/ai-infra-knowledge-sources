# [Issue #4776] [Bug] legacy /v1/completions disconnect-abort calls nonexistent AsyncEngine.stop_session

source: https://github.com/InternLM/lmdeploy/issues/4776
state: closed | updated: 2026-07-29T04:40:37Z
labels: 

## 正文

### Describe the bug

The non-streaming `/v1/completions` endpoint (`completions_v1` in `lmdeploy/serve/openai/api_server.py`) crashes on client disconnect instead of returning a clean `400`.

`_inner_call`'s disconnect branch calls `VariableInterface.async_engine.stop_session(request.session_id)`:

```python
async for res in cleanup_generator:
    if await raw_request.is_disconnected():
        # Abort the request if the client disconnects.
        await VariableInterface.async_engine.stop_session(request.session_id)
        return create_error_response(HTTPStatus.BAD_REQUEST, 'Client disconnected')
```

`AsyncEngine` has no `stop_session` method (checked by enumerating every method on the class), so this raises `AttributeError` on every disconnect, instead of aborting the session and returning the intended `400`. The three sibling disconnect handlers in the same file (`chat_completions_v1`, the streaming `/generate` non-streaming branch, and `/end_session`) all use the correct `session.async_abort()` call.

Separately, even after routing through `session.async_abort()`, the disconnect response is lost: `_inner_call`'s `return create_error_response(...)` is the return value of a coroutine passed to `asyncio.gather(...)`, and that return value is discarded:

```python
await asyncio.gather(*[_inner_call(i, generators[i], sessions[i]) for i in range(len(generators))])

response = CompletionResponse(
    id=request_id,
    ...
    choices=choices,
    ...
).model_dump()
```

`choices[i]` is never set for the disconnected generator (it stays `None`), so `CompletionResponse` construction raises a pydantic `ValidationError` instead of ever returning the `400`.

### Reproduction

Docker (`python:3.11-slim`, CPU-only `torch`/`transformers`/`xgrammar`/etc., no GPU needed), current `main` (`2aae7d77`). Imported the real, unmodified `completions_v1`, `VariableInterface`, `CompletionRequest`, `SessionManager`, and `GenOut`, and drove the endpoint directly with a fake `AsyncEngine.generate()` that yields one item and a fake `raw_request.is_disconnected()` that returns `True`:

```
AttributeError: 'FakeAsyncEngine' object has no attribute 'stop_session'
  File "lmdeploy/serve/openai/api_server.py", line 935, in _inner_call
    await VariableInterface.async_engine.stop_session(request.session_id)
```

### Environment

Reproduced against `InternLM/lmdeploy` at commit `2aae7d77b73640bc916923cd90cb8ea8015b5d02` (2026-07-22), not tied to a specific GPU/OS environment (the fault is in request-handling logic, not a backend).

### Error traceback

```
Traceback (most recent call last):
  File "repro.py", line 41, in main
    result = await completions_v1(request, raw_request)
  File "lmdeploy/serve/openai/api_server.py", line 963, in completions_v1
    await asyncio.gather(*[_inner_call(i, generators[i], sessions[i]) for i in range(len(generators))])
  File "lmdeploy/serve/openai/api_server.py", line 935, in _inner_call
    await VariableInterface.async_engine.stop_session(request.session_id)
AttributeError: 'FakeAsyncEngine' object has no attribute 'stop_session'
```

I have a fix ready (route the disconnect through the already-in-scope `session.async_abort()`, matching the sibling handlers, and propagate `_inner_call`'s result out of `asyncio.gather` so the `400` actually reaches the caller) and will open a PR referencing this issue.


## 评论 (1)

### lvhan028 · 2026-07-29

This issue is being addressed in PR #4797 
