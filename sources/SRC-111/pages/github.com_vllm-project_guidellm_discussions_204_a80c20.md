source: https://github.com/vllm-project/guidellm/discussions/204

#
How to use the `/v1/chat/completions`

endpoint?
#204

|
My deployment only support ```
guidellm benchmark \
--target "http://localhost:25252" \
--backend-type openai_http \
--model my_custom_model \
--rate-type concurrent --rate 16 \
--max-seconds 300 \
--warmup-percent 0.0 --cooldown-percent 0.0 \
--data '{"messages":[{"role":"user","content":"hello!"}]}' \
--random-seed 42
```
```
Creating backend...
2025-06-18T14:43:26.046879+0000 | text_completions | ERROR - OpenAIHTTPBackend request with headers: {'Content-Type': 'application/json'} and payload: {'prompt': 'Test connection', 'model': 'my_custom_model', 'stream': True, 'stream_options': {'include_usage': True}, 'max_tokens': 1, 'max_completion_tokens': 1, 'stop': None, 'ignore_eos': True} failed: Client error '422 Unprocessable Entity' for url 'http://localhost:25252/v1/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/422
Traceback (most recent call last):
File "/opt/data/miniforge3/bin/guidellm", line 8, in <module>
sys.exit(cli())
^^^^^
File "/opt/data/miniforge3/lib/python3.12/site-packages/click/core.py", line 1161, in __call__
return self.main(*args, **kwargs)
^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/opt/data/miniforge3/lib/python3.12/site-packages/click/core.py", line 1082, in main
rv = self.invoke(ctx)
^^^^^^^^^^^^^^^^
File "/opt/data/miniforge3/lib/python3.12/site-packages/click/core.py", line 1697, in invoke
return _process_result(sub_ctx.command.invoke(sub_ctx))
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/opt/data/miniforge3/lib/python3.12/site-packages/click/core.py", line 1443, in invoke
return ctx.invoke(self.callback, **ctx.params)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/opt/data/miniforge3/lib/python3.12/site-packages/click/core.py", line 788, in invoke
return __callback(*args, **kwargs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/opt/data/miniforge3/lib/python3.12/site-packages/guidellm/__main__.py", line 255, in benchmark
asyncio.run(
File "/opt/data/miniforge3/lib/python3.12/asyncio/runners.py", line 195, in run
return runner.run(main)
^^^^^^^^^^^^^^^^
File "/opt/data/miniforge3/lib/python3.12/asyncio/runners.py", line 118, in run
return self._loop.run_until_complete(task)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/opt/data/miniforge3/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
return future.result()
^^^^^^^^^^^^^^^
File "/opt/data/miniforge3/lib/python3.12/site-packages/guidellm/benchmark/entrypoints.py", line 59, in benchmark_generative_text
await backend.validate()
File "/opt/data/miniforge3/lib/python3.12/site-packages/guidellm/backend/backend.py", line 124, in validate
async for _ in self.text_completions(
File "/opt/data/miniforge3/lib/python3.12/site-packages/guidellm/backend/openai.py", line 237, in text_completions
raise ex
File "/opt/data/miniforge3/lib/python3.12/site-packages/guidellm/backend/openai.py", line 220, in text_completions
async for resp in self._iterative_completions_request(
File "/opt/data/miniforge3/lib/python3.12/site-packages/guidellm/backend/openai.py", line 489, in _iterative_completions_request
stream.raise_for_status()
File "/opt/data/miniforge3/lib/python3.12/site-packages/httpx/_models.py", line 829, in raise_for_status
raise HTTPStatusError(message, request=request, response=self)
httpx.HTTPStatusError: Client error '422 Unprocessable Entity' for url 'http://localhost:25252/v1/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/422
``` |

Answered by

[sjmonson](https://github.com/sjmonson)Jun 24, 2025
## Replies: 1 comment 2 replies

|
You can set |

2 replies

Answer selected by

You can set

`GUIDELLM__PREFERRED_ROUTE="chat_completions"`

to use the chat endpoint (run`guidellm config`

to see all env options).