source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/middleware/log_response/
lastmod: 2026-09-24

#

`vllm.entrypoints.serve.middleware.log_response`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.middleware.log_response)

Classes:

-
–[SSEDecoder](https://docs.vllm.ai#vllm.entrypoints.serve.middleware.log_response.SSEDecoder)Robust Server-Sent Events decoder for streaming responses.


##

`SSEDecoder`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.middleware.log_response.SSEDecoder)

Robust Server-Sent Events decoder for streaming responses.

Methods:

-
–[add_content](https://docs.vllm.ai#vllm.entrypoints.serve.middleware.log_response.SSEDecoder.add_content)Add content to the buffer.

-
–[decode_chunk](https://docs.vllm.ai#vllm.entrypoints.serve.middleware.log_response.SSEDecoder.decode_chunk)Decode a chunk of SSE data and return parsed events.

-
–[extract_content](https://docs.vllm.ai#vllm.entrypoints.serve.middleware.log_response.SSEDecoder.extract_content)Extract content from event data.

-
–[get_complete_content](https://docs.vllm.ai#vllm.entrypoints.serve.middleware.log_response.SSEDecoder.get_complete_content)Get the complete buffered content.


## Source code in `vllm/entrypoints/serve/middleware/log_response.py`


###

`add_content(content)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.middleware.log_response.SSEDecoder.add_content)

###

`decode_chunk(chunk)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.middleware.log_response.SSEDecoder.decode_chunk)

Decode a chunk of SSE data and return parsed events.

## Source code in `vllm/entrypoints/serve/middleware/log_response.py`


###

`extract_content(event_data)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.middleware.log_response.SSEDecoder.extract_content)

##

`_extract_content_from_chunk(chunk_data)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.middleware.log_response._extract_content_from_chunk)

Extract content from a streaming response chunk.

## Source code in `vllm/entrypoints/serve/middleware/log_response.py`


##

`_log_non_streaming_response(response_body)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.middleware.log_response._log_non_streaming_response)

Log non-streaming response.

## Source code in `vllm/entrypoints/serve/middleware/log_response.py`


##

`_log_streaming_response(response, response_body)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.middleware.log_response._log_streaming_response)

Log streaming response with robust SSE parsing.