source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/utils/api_utils/
lastmod: 2026-09-24

#

`vllm.entrypoints.serve.utils.api_utils`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.utils.api_utils)

Functions:

-
–[listen_for_disconnect](https://docs.vllm.ai#vllm.entrypoints.serve.utils.api_utils.listen_for_disconnect)Returns if a disconnect message is received.

-
–[redact_sensitive_args](https://docs.vllm.ai#vllm.entrypoints.serve.utils.api_utils.redact_sensitive_args)Return a copy of

`args`

with sensitive values redacted for logging. -
–[with_cancellation](https://docs.vllm.ai#vllm.entrypoints.serve.utils.api_utils.with_cancellation)Decorator that allows a route handler to be cancelled by client


##

`listen_for_disconnect(request)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.utils.api_utils.listen_for_disconnect)

Returns if a disconnect message is received.

## Source code in `vllm/entrypoints/serve/utils/api_utils.py`


##

`redact_sensitive_args(args)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.utils.api_utils.redact_sensitive_args)

Return a copy of `args`

with sensitive values redacted for logging.

## Source code in `vllm/entrypoints/serve/utils/api_utils.py`


##

`with_cancellation(handler_func)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.utils.api_utils.with_cancellation)

Decorator that allows a route handler to be cancelled by client disconnections.

This does *not* use request.is_disconnected, which does not work with middleware. Instead this follows the pattern from starlette.StreamingResponse, which simultaneously awaits on two tasks- one to wait for an http disconnect message, and the other to do the work that we want done. When the first task finishes, the other is cancelled.

A core assumption of this method is that the body of the request has already been read. This is a safe assumption to make for fastapi handlers that have already parsed the body of the request into a pydantic model for us. This decorator is unsafe to use elsewhere, as it will consume and throw away all incoming messages for the request while it looks for a disconnect message.

In the case where a `StreamingResponse`

is returned by the handler, this wrapper will stop listening for disconnects and instead the response object will start listening for disconnects.