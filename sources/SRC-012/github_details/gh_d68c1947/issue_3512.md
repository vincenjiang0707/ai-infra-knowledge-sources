# [Issue #3512] get_generation_config mutates the request's stop list in place when stop is passed as a list

source: https://github.com/mlc-ai/mlc-llm/issues/3512
state: open | updated: 2026-08-04T06:47:02Z
labels: 

## 正文

`openai_api_get_generation_config` in `python/mlc_llm/serve/engine_utils.py` aliases `request.stop` directly into the generation-config kwargs instead of copying it, when `stop` is already a list:

```python
if request.stop is not None:
    kwargs["stop_strs"] = [request.stop] if isinstance(request.stop, str) else request.stop
```

`get_generation_config` then extends that value in place with the model's own stop strings (from the conversation template):

```python
if extra_stop_str is not None:
    stop_strs = kwargs.get("stop_strs", [])
    assert isinstance(stop_strs, list)
    stop_strs += extra_stop_str
    kwargs["stop_strs"] = stop_strs
```

When `request.stop` is a list, `kwargs["stop_strs"]` is that *same* list object (not a copy), so `stop_strs += extra_stop_str` mutates `request.stop` itself.

Both call sites in `engine_base.py` (chat completion and completion request handling) pass `extra_stop_str=conv_template.stop_str`, which is populated from the model's chat template and is non-empty for most models - so this isn't a rare edge case, it's the standard chat-completion path whenever a client sends `stop` as a list rather than a single string.

## Repro

I don't have a working `tvm` build in my environment to exercise the real request/engine classes, so I copied the exact logic verbatim (both functions, unmodified) into a standalone script with a minimal stand-in for the request object - same field names, same code path, same `+=`:

```python
class FakeRequest:
    def __init__(self, stop):
        # ... other fields set to their defaults ...
        self.stop = stop

def openai_api_get_generation_config(request):
    kwargs = {}
    # (verbatim body from engine_utils.py)
    if request.stop is not None:
        kwargs["stop_strs"] = [request.stop] if isinstance(request.stop, str) else request.stop
    return kwargs

def get_generation_config(request, extra_stop_token_ids=None, extra_stop_str=None):
    kwargs = openai_api_get_generation_config(request)
    if extra_stop_str is not None:
        stop_strs = kwargs.get("stop_strs", [])
        stop_strs += extra_stop_str
        kwargs["stop_strs"] = stop_strs
    return kwargs

original_stop_list = ["<|user|>", "<|end|>"]
req = FakeRequest(stop=original_stop_list)
cfg = get_generation_config(req, extra_stop_str=["SYSTEM_INTERNAL_STOP"])

print(cfg["stop_strs"])   # ['<|user|>', '<|end|>', 'SYSTEM_INTERNAL_STOP']
print(req.stop)           # ['<|user|>', '<|end|>', 'SYSTEM_INTERNAL_STOP']  <- mutated!
print(req.stop is cfg["stop_strs"])  # True
```

`req.stop` (standing in for `ChatCompletionRequest.stop`) picks up the template's internal stop string after generation-config processing, even though nothing about handling a request should be writing back into the request object the client sent in.

## Impact

Anywhere the original request object gets reused, logged, echoed back (the completions endpoint already has an `echo` path that reflects request data), or has its generation config recomputed - e.g. retries, speculative-decoding paths, or just inspecting the request after the fact for debugging - it'll show the model's internal stop tokens appended to a field the client never set them on, and repeated recomputation would keep appending duplicates onto the same list each time.

## Suggested fix

Copy instead of alias when `stop` is already a list:

```python
if request.stop is not None:
    kwargs["stop_strs"] = [request.stop] if isinstance(request.stop, str) else list(request.stop)
```

That one change breaks the aliasing while leaving every other behavior (including the string case, which already builds a fresh single-element list) unchanged. Happy to send a PR for this if that's the right direction.

## 评论 (1)

### ErenAta16 · 2026-08-04

Still reproduces on current `main`. Both lines are unchanged since I filed this:

```python
# python/mlc_llm/serve/engine_utils.py:52
kwargs["stop_strs"] = [request.stop] if isinstance(request.stop, str) else request.stop

# python/mlc_llm/serve/engine_utils.py:90
stop_strs += extra_stop_str
```

Adding the effect I did not spell out originally, because it is worse than a single mutation. The caller's list is aliased, and `+=` extends in place, so a list reused across requests grows every time:

```
before          : caller_list=['</s>']
after 1 request : caller_list=['</s>', '<|im_end|>']      aliased=True
after 2 requests: caller_list=['</s>', '<|im_end|>', '<|im_end|>']
after 3 requests: caller_list=['</s>', '<|im_end|>', '<|im_end|>', '<|im_end|>']
```

The duplicates are harmless to matching, but the list is unbounded, and any caller that holds a template `stop` list and reuses it across a conversation is handing back a longer list each turn.

A `stop` passed as a **string** is unaffected, since `[request.stop]` builds a fresh list:

```
request.stop stays: '</s>'   stop_strs=['</s>', '<|im_end|>']
```

so the bug is specific to the list form, which is the shape the OpenAI API documents for multiple stop sequences.

One-line fix, keeping the string branch as it is:

```python
kwargs["stop_strs"] = [request.stop] if isinstance(request.stop, str) else list(request.stop)
```

```
with list(...)  : caller_list=['</s>']   stop_strs=['</s>', '<|im_end|>']
```

Happy to open a PR for that if it is wanted; it is one line plus a test that the caller's list is unchanged after the call.

