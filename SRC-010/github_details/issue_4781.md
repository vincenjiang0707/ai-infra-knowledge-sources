# [Issue #4781] [Bug] legacy /generate's non-streaming disconnect branch discards its 400 response, returns 200 null instead

source: https://github.com/InternLM/lmdeploy/issues/4781
state: closed | updated: 2026-08-24T03:15:35Z
labels: 

## 正文

### Describe the bug

The non-streaming `/generate` endpoint (`generate` in `lmdeploy/serve/openai/api_server.py`) aborts the session correctly on client disconnect, but the caller never sees the `400` it computed: it gets `HTTP 200` with a `null` body instead.

`generate`'s inner helper returns the error response from inside an `async with` block:

```python
response = None

async def _inner_call():
    ...
    async with aclosing(_with_request_cleanup(result_generator, [result_generator], [session])) as generator:
        async for res in generator:
            if await raw_request.is_disconnected():
                # Abort the request if the client disconnects.
                await session.async_abort()
                return create_error_response(HTTPStatus.BAD_REQUEST, 'Client disconnected')
            ...

    nonlocal response
    ...
    response = GenerateReqOutput(text=text, output_ids=output_ids, meta_info=meta)

await _inner_call()
return response
```

The call site is a bare `await _inner_call()`: its return value (the `400` `create_error_response(...)`) is discarded. `response` is a `nonlocal` initialized to `None` before the call and is only assigned inside the non-disconnect branch, after the `async with` exits normally. On disconnect, `_inner_call` returns early from inside the `async with`, so that assignment is never reached, and `generate` returns the still-`None` `response` instead of the `400`.

`session.async_abort()` does fire correctly; only the response propagation is lost. This is the same discard-the-inner-return shape as #4776, in the sibling `/generate` endpoint instead of `/v1/completions`.

### Reproduction

Docker (`python:3.11-slim`, CPU-only `torch`/`transformers`/etc., no GPU needed), current `main` (`9140d372`). Imported the real, unmodified `generate`, `VariableInterface`, `GenerateReqInput`, `SessionManager`, and `GenOut`, and drove the endpoint directly with a fake `AsyncEngine.generate()` that yields one item and a fake `raw_request.is_disconnected()` that returns `True`:

```python
request = GenerateReqInput(prompt='hello', stream=False)
result = await generate(request, fake_raw_request)
assert isinstance(result, JSONResponse)  # fails: result is None
```

### Environment

Reproduced against `InternLM/lmdeploy` at commit `9140d372bbf42209db66394a4268eeadaf05330c` (2026-07-24), not tied to a specific GPU/OS environment (the fault is in request-handling logic, not a backend).

### Error traceback

```
AssertionError: assert False
 +  where False = isinstance(None, <class 'starlette.responses.JSONResponse'>)
```

I have a fix ready (capture `_inner_call`'s return value and return it directly when not `None`, mirroring how #4777 fixed the analogous `/v1/completions` case) and will open a PR referencing this issue.


## 评论 (1)

### ErenAta16 · 2026-07-31

Reproduced the control flow, and the same shape is in `/v1/completions` too, which the report doesn't mention.

Running the pattern in isolation — inner coroutine returning from inside `async with`, call site discarding the return value:

```
disconnect=False  mevcut -> '200 GenerateReqOutput'  duzeltilmis -> '200 GenerateReqOutput'
disconnect=True   mevcut -> None                     duzeltilmis -> '400 Client disconnected'
```

so on the disconnect path `generate` returns `None` and FastAPI serialises that as `200` with a `null` body, exactly as described. The normal path is unaffected either way.

**`/v1/completions` has the same defect, by a different route.** `_inner_call` there (`api_server.py:925`) also returns `create_error_response(...)` on disconnect at line 936, and the call site is:

```python
await asyncio.gather(*[_inner_call(i, generators[i], sessions[i]) for i in range(len(generators))])
...
response = CompletionResponse(...)
```

`asyncio.gather` collects those return values into a list that is discarded, so the `400` is lost the same way. It's arguably worse there: after the early return, `final_res` stays `None` for that index, so the `assert final_res is not None` on line 947 never runs for the disconnected entry and the response is assembled from the choices that did complete — a `200` with a short choices list rather than an error.

**The chat endpoint is fine and shows the intended shape.** In `/v1/chat/completions` the `async with` and its `return create_error_response(...)` sit directly in the endpoint body (around line 675), so the return leaves the endpoint. That's the difference: the two broken ones moved the loop into a nested coroutine but kept `return` as the error channel.

For `generate`, `return await _inner_call() or response` at line 1084 is a one-line fix that preserves the existing behaviour when `_inner_call` returns `None`. `/v1/completions` needs a bit more, since gather returns a list — checking the results for a non-`None` entry and returning the first one would match.

Read against `main` at the current checkout; the numbers above come from running the control-flow pattern locally, not a live server.

