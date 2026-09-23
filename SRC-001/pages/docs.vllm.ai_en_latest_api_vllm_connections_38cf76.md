source: https://docs.vllm.ai/en/latest/api/vllm/connections/
lastmod: 2026-09-23

#

`vllm.connections`

[¶](https://docs.vllm.ai#vllm.connections)

Classes:

-
–[HTTPConnection](https://docs.vllm.ai#vllm.connections.HTTPConnection)Helper class to send HTTP requests.

-
–[HTTPResponseSizeExceededError](https://docs.vllm.ai#vllm.connections.HTTPResponseSizeExceededError)Raised when an HTTP response exceeds a caller-supplied byte ceiling.

-
–[MediaDownloadSizeExceededError](https://docs.vllm.ai#vllm.connections.MediaDownloadSizeExceededError)Raised when a remote media download exceeds the configured byte limit.


Attributes:

-
–[global_http_connection](https://docs.vllm.ai#vllm.connections.global_http_connection)The global

instance used`HTTPConnection`


##

`global_http_connection = HTTPConnection()`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.connections.global_http_connection)

The global [ HTTPConnection](https://docs.vllm.ai#vllm.connections.HTTPConnection) instance used by vLLM.

##

`HTTPConnection`

[¶](https://docs.vllm.ai#vllm.connections.HTTPConnection)

Helper class to send HTTP requests.

## Source code in `vllm/connections.py`


|
|

##

`HTTPResponseSizeExceededError`

[¶](https://docs.vllm.ai#vllm.connections.HTTPResponseSizeExceededError)

Bases: [VLLMValidationError](https://docs.vllm.ai/exceptions/#vllm.exceptions.VLLMValidationError)

Raised when an HTTP response exceeds a caller-supplied byte ceiling.

## Source code in `vllm/connections.py`


##

`MediaDownloadSizeExceededError`

[¶](https://docs.vllm.ai#vllm.connections.MediaDownloadSizeExceededError)

Bases: [ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)

Raised when a remote media download exceeds the configured byte limit.

## Source code in `vllm/connections.py`


##

`_async_retry(fn)`

[¶](https://docs.vllm.ai#vllm.connections._async_retry)

Add retry logic with exponential backoff to an async method.

The decorated method must accept `timeout`

as a keyword argument. The decorator replaces it with a per-attempt timeout that grows by `_RETRY_BACKOFF_FACTOR`

on each retry so transient slowness on busy hosts is absorbed.

## Source code in `vllm/connections.py`


##

`_is_retryable(exc)`

[¶](https://docs.vllm.ai#vllm.connections._is_retryable)

Return True for transient errors that are worth retrying.

## Retryable

- Timeouts (aiohttp, requests, stdlib)
- Connection-level failures (refused, reset, DNS)
- Server errors (5xx) -- includes S3 503 SlowDown

Not retryable: - Client errors (4xx) -- bad URL, auth, not-found - Programming errors (ValueError, TypeError, ...)

## Source code in `vllm/connections.py`


##

`_sync_retry(fn)`

[¶](https://docs.vllm.ai#vllm.connections._sync_retry)

Add retry logic with exponential backoff to a sync method.

The decorated method must accept `timeout`

as a keyword argument. The decorator replaces it with a per-attempt timeout that grows by `_RETRY_BACKOFF_FACTOR`

on each retry so transient slowness on busy hosts is absorbed.