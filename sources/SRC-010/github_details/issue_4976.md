# [Issue #4976] [Bug] /v1/completions silently falls back to n=1 instead of rejecting or erroring on n>1

source: https://github.com/InternLM/lmdeploy/issues/4976
state: closed | updated: 2026-09-16T03:03:57Z
labels: 

## 正文

### Describe the bug

`/v1/completions`'s own docstring says `n` is unsupported here ("Only support one here"), but a request with `n > 1` isn't rejected. It passes the endpoint's own validation (`n` is only checked for being positive), and further down the internal generation config forces `n` back to 1 and logs a warning server-side. The client gets an HTTP 200 with exactly 1 choice and nothing in the response indicating anything was downgraded.

For comparison, `/v1/chat/completions` got real `n>1` support last month in #4841 (its docstring was updated to "Accepts values from 1 to 128"), but `/v1/completions`'s docstring and behavior were never touched, so the two endpoints now disagree on how the same documented field behaves.

### Reproduction

I don't have a GPU on hand to bring up a full server, so I traced this against the request-handling code on main rather than driving a live HTTP call:

```python
CompletionRequest(model="m", prompt="hi", n=3)
```

- Validation only checks that `n` is positive, so `n=3` passes.
- The generation-config step forces `n` back to 1 and logs a warning, without raising or returning an error.
- The endpoint builds exactly one choice per prompt regardless of `n`.

So sending `n=3` to `/v1/completions` returns exactly 1 choice with a 200 OK, and the only indication anything happened is a server-side log line, not anything in the response.

### Environment

No GPU available on my end, so I can't paste `lmdeploy check_env` output from a live deployment. This is a code trace against `InternLM/lmdeploy@f8d8d7bd36c54204e39b9090796c432a2d9f3d6b` (main).

### Error traceback

None. The request succeeds and returns a downgraded result rather than raising.


## 评论 (1)

### lvhan028 · 2026-09-16

According to OpenAI, "The completions API endpoint received its final update in July 2023." So we'd like to keep the v1/completions endpoint as is and not update it any further.
