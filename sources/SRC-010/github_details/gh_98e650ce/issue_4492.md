# [Issue #4492] [Bug] 工具调用报错asyncio.exceptions.CancelledError: Cancelled by cancel scope 7fe9b6f1ed10

source: https://github.com/InternLM/lmdeploy/issues/4492
state: open | updated: 2026-04-07T06:26:02Z
labels: 

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

工具调用报错：Unknown agent error: RemoteProtocolError: peer closed connection without sending complete message body (incomplete chunked read) (Details: /tmp/copaw_query_error_lecl26n1.json)

### Reproduction

```bash
export CUDA_VISIBLE_DEVICES=6,7
lmdeploy serve api_server Qwen3.5-9B \
    --server-port 20019 \
	--tp 2 \
	--cache-max-entry-count 0.9 \
	--model-name qwen3.5 \
	--enable-prefix-caching  \
	--max-batch-size 10 \
	--tool-call-parser qwen3coder \   qwen3也不行
	--reasoning-parser deepseek-r1\
	--log-level INFO \
```

### Environment

```Shell
lmdeploy                          0.12.2
```

### Error traceback

```Shell
Traceback (most recent call last):
  File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/starlette/responses.py", line 265, in __call__
    await wrap(partial(self.listen_for_disconnect, receive))
  File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/starlette/responses.py", line 261, in wrap
    await func()
  File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/starlette/responses.py", line 238, in listen_for_disconnect
    message = await receive()
  File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/uvicorn/protocols/http/httptools_impl.py", line 553, in receive
    await self.message_event.wait()
  File "/root/miniforge3/envs/LMDeploy/lib/python3.10/asyncio/locks.py", line 214, in wait
    await fut
asyncio.exceptions.CancelledError: Cancelled by cancel scope 7fe9b6f1ed10

During handling of the above exception, another exception occurred:

  + Exception Group Traceback (most recent call last):
  |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/uvicorn/protocols/http/httptools_impl.py", line 399, in run_asgi
  |     result = await app(  # type: ignore[func-returns-value]
  |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/uvicorn/middleware/proxy_headers.py", line 70, in __call__
  |     return await self.app(scope, receive, send)
  |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/fastapi/applications.py", line 1054, in __call__
  |     await super().__call__(scope, receive, send)
  |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/starlette/applications.py", line 123, in __call__
  |     await self.middleware_stack(scope, receive, send)
  |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/starlette/middleware/errors.py", line 186, in __call__
  |     raise exc
  |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/starlette/middleware/errors.py", line 164, in __call__
  |     await self.app(scope, receive, _send)
  |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/starlette/middleware/cors.py", line 85, in __call__
  |     await self.app(scope, receive, send)
  |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/starlette/middleware/exceptions.py", line 65, in __call__
  |     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/starlette/_exception_handler.py", line 64, in wrapped_app
  |     raise exc
  |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
  |     await app(scope, receive, sender)
  |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/starlette/routing.py", line 756, in __call__
  |     await self.middleware_stack(scope, receive, send)
  |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/starlette/routing.py", line 776, in app
  |     await route.handle(scope, receive, send)
  |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/starlette/routing.py", line 297, in handle
  |     await self.app(scope, receive, send)
  |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/starlette/routing.py", line 77, in app
  |     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/starlette/_exception_handler.py", line 64, in wrapped_app
  |     raise exc
  |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
  |     await app(scope, receive, sender)
  |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/starlette/routing.py", line 75, in app
  |     await response(scope, receive, send)
  |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/starlette/responses.py", line 258, in __call__
  |     async with anyio.create_task_group() as task_group:
  |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/anyio/_backends/_asyncio.py", line 680, in __aexit__
  |     raise BaseExceptionGroup(
  | exceptiongroup.ExceptionGroup: unhandled errors in a TaskGroup (1 sub-exception)
  +-+---------------- 1 ----------------
    | Traceback (most recent call last):
    |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/starlette/responses.py", line 261, in wrap
    |     await func()
    |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/starlette/responses.py", line 250, in stream_response
    |     async for chunk in self.body_iterator:
    |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/lmdeploy/serve/openai/api_server.py", line 515, in completion_stream_generator
    |     async for res in result_generator:
    |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/lmdeploy/serve/core/async_engine.py", line 334, in generate
    |     prompt_input = await self.prompt_processor.get_prompt_input(prompt=prompt,
    |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/lmdeploy/serve/processors/multimodal.py", line 253, in get_prompt_input
    |     return await self._get_text_prompt_input(prompt=prompt,
    |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/lmdeploy/serve/processors/multimodal.py", line 379, in _get_text_prompt_input
    |     prompt = chat_template.messages2prompt(prompt,
    |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/lmdeploy/model.py", line 724, in messages2prompt
    |     prompt = self.tokenizer.apply_chat_template(messages,
    |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/transformers/tokenization_utils_base.py", line 1667, in apply_chat_template
    |     rendered_chat, generation_indices = render_jinja_template(
    |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/transformers/utils/chat_template_utils.py", line 539, in render_jinja_template
    |     rendered_chat = compiled_template.render(
    |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/jinja2/environment.py", line 1304, in render
    |     self.environment.handle_exception()
    |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/jinja2/environment.py", line 939, in handle_exception
    |     raise rewrite_traceback_stack(source=source)
    |   File "<template>", line 120, in top-level template code
    |   File "/root/miniforge3/envs/LMDeploy/lib/python3.10/site-packages/jinja2/filters.py", line 248, in do_items
    |     raise TypeError("Can only get item pairs from a mapping.")
    | TypeError: Can only get item pairs from a mapping.
    +------------------------------------
```

## 评论 (2)

### simonjhy · 2026-04-04

我也发现这个错误，https://github.com/InternLM/lmdeploy/issues/4475，但是不知道他们是不是开始解决这个问题了

### lvhan028 · 2026-04-07

@LIUKAI0815 你可以尝试下 main 分支
