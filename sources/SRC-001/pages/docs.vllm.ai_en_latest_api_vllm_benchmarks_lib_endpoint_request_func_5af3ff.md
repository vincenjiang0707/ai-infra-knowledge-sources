source: https://docs.vllm.ai/en/latest/api/vllm/benchmarks/lib/endpoint_request_func/
lastmod: 2026-09-24

#

`vllm.benchmarks.lib.endpoint_request_func`

[¶](https://docs.vllm.ai#vllm.benchmarks.lib.endpoint_request_func)

The request function for API endpoints.

Classes:

-
–[RequestFuncInput](https://docs.vllm.ai#vllm.benchmarks.lib.endpoint_request_func.RequestFuncInput)The input for the request function.

-
–[RequestFuncOutput](https://docs.vllm.ai#vllm.benchmarks.lib.endpoint_request_func.RequestFuncOutput)The output of the request function including metrics.

-
–[StreamedResponseHandler](https://docs.vllm.ai#vllm.benchmarks.lib.endpoint_request_func.StreamedResponseHandler)Handles streaming HTTP responses by accumulating chunks until complete


Functions:

-
–[async_request_openai_completions](https://docs.vllm.ai#vllm.benchmarks.lib.endpoint_request_func.async_request_openai_completions)The async request function for the OpenAI Completions API.


##

`RequestFuncInput`

`dataclass`

[¶](https://docs.vllm.ai#vllm.benchmarks.lib.endpoint_request_func.RequestFuncInput)

The input for the request function.

## Source code in `vllm/benchmarks/lib/endpoint_request_func.py`


##

`RequestFuncOutput`

`dataclass`

[¶](https://docs.vllm.ai#vllm.benchmarks.lib.endpoint_request_func.RequestFuncOutput)

The output of the request function including metrics.

## Source code in `vllm/benchmarks/lib/endpoint_request_func.py`


##

`StreamedResponseHandler`

[¶](https://docs.vllm.ai#vllm.benchmarks.lib.endpoint_request_func.StreamedResponseHandler)

Handles streaming HTTP responses by accumulating chunks until complete messages are available.

Methods:

-
–[add_chunk](https://docs.vllm.ai#vllm.benchmarks.lib.endpoint_request_func.StreamedResponseHandler.add_chunk)Add a chunk of bytes to the buffer and return any complete


## Source code in `vllm/benchmarks/lib/endpoint_request_func.py`


###

`add_chunk(chunk_bytes)`

[¶](https://docs.vllm.ai#vllm.benchmarks.lib.endpoint_request_func.StreamedResponseHandler.add_chunk)

Add a chunk of bytes to the buffer and return any complete messages.

## Source code in `vllm/benchmarks/lib/endpoint_request_func.py`


##

`async_request_openai_completions(request_func_input, session, pbar=None)`

`async`

[¶](https://docs.vllm.ai#vllm.benchmarks.lib.endpoint_request_func.async_request_openai_completions)

The async request function for the OpenAI Completions API.

Parameters:

-

(`request_func_input`

[¶](https://docs.vllm.ai#vllm.benchmarks.lib.endpoint_request_func.async_request_openai_completions(request_func_input))

) –[RequestFuncInput](https://docs.vllm.ai#vllm.benchmarks.lib.endpoint_request_func.RequestFuncInput)The input for the request function.

-

(`session`

[¶](https://docs.vllm.ai#vllm.benchmarks.lib.endpoint_request_func.async_request_openai_completions(session))

) –[ClientSession](https://docs.aiohttp.org/en/stable/client_reference.html#aiohttp.ClientSession)The aiohttp session used to issue the request.

-

(`pbar`

[¶](https://docs.vllm.ai#vllm.benchmarks.lib.endpoint_request_func.async_request_openai_completions(pbar))`tqdm | None`

, default:`None`

) –The progress bar to display the progress.


Returns:

-

–[RequestFuncOutput](https://docs.vllm.ai#vllm.benchmarks.lib.endpoint_request_func.RequestFuncOutput)The output of the request function.


## Source code in `vllm/benchmarks/lib/endpoint_request_func.py`


|
|