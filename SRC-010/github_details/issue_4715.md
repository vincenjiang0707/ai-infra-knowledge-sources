# [Issue #4715] [Bug] 在使用qwen3.5-122B的时候，模型是多模态模型，但是在使用lmdeploy收到请求的时候，报错了

source: https://github.com/InternLM/lmdeploy/issues/4715
state: closed | updated: 2026-08-04T04:44:51Z
labels: awaiting response, Stale

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

INFO:     172.22.0.4:42970 - "POST /v1/chat/completions HTTP/1.1" 200 OK
Exception in callback _raise_exception_on_finish(<Future finis...y image_url')>) at /opt/py3/lib/python3.12/site-packages/lmdeploy/vl/engine.py:63
handle: <Handle _raise_exception_on_finish(<Future finis...y image_url')>) at /opt/py3/lib/python3.12/site-packages/lmdeploy/vl/engine.py:63>
Traceback (most recent call last):
  File "/usr/lib/python3.12/asyncio/events.py", line 88, in _run
    self._context.run(self._callback, *self._args)
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/vl/engine.py", line 70, in _raise_exception_on_finish
    raise e
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/vl/engine.py", line 66, in _raise_exception_on_finish
    task.result()
  File "/usr/lib/python3.12/concurrent/futures/thread.py", line 59, in run
    result = self.fn(*self.args, **self.kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/vl/model/base.py", line 150, in preprocess
    raise ValueError(f'unsupported modality {modality}')
ValueError: unsupported modality image_url
2026-06-29 04:59:05,479 - lmdeploy - ERROR - async_engine.py:562 - [generate] error in prompt processing
Traceback (most recent call last):
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/serve/core/async_engine.py", line 540, in generate
    prompt_input = await self.prompt_processor.get_prompt_input(prompt=prompt,
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/serve/processors/multimodal.py", line 243, in get_prompt_input
    return await self._get_multimodal_prompt_input(messages=prompt,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/serve/processors/multimodal.py", line 397, in _get_multimodal_prompt_input
    results = await self.vl_encoder.preprocess(messages,
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/vl/engine.py", line 121, in preprocess
    outputs = await future


### Reproduction

我是在codex中让模型读取一个图片然后我就看到lmdeploy中的log出现了错误

### Environment

```Shell
ubuntu2204 
lmdeploy openmmlab/lmdeploy:latest-cu12.8
```

### Error traceback

```Shell

```

## 评论 (3)

### CUHKSZzxy · 2026-06-30

https://github.com/InternLM/lmdeploy/pull/4680

应该是多模态工具调用的 bug，可以试一下这个 PR 看能否解决

### github-actions[bot] · 2026-07-30

This issue is marked as stale because it has been marked as invalid or awaiting response for 7 days without any further response. It will be closed in 5 days if the stale label is not removed or if there is no further response.

### github-actions[bot] · 2026-08-04

This issue is closed because it has been stale for 5 days. Please open a new issue if you have similar issues or you have any new updates now.
