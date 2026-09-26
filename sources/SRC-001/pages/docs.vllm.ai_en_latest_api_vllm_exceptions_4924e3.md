source: https://docs.vllm.ai/en/latest/api/vllm/exceptions/
lastmod: 2026-09-24

#

`vllm.exceptions`

[¶](https://docs.vllm.ai#vllm.exceptions)

Custom exceptions for vLLM.

Classes:

-
–[GenerationError](https://docs.vllm.ai#vllm.exceptions.GenerationError)raised when finish_reason indicates internal server error (500)

-
–[GracefulHTTPError](https://docs.vllm.ai#vllm.exceptions.GracefulHTTPError)Exception that should be translated into an HTTP error response.

-
–[LoRAAdapterNotFoundError](https://docs.vllm.ai#vllm.exceptions.LoRAAdapterNotFoundError)Exception raised when a LoRA adapter is not found.

-
–[MaxQueuedTokensError](https://docs.vllm.ai#vllm.exceptions.MaxQueuedTokensError)Raised when the pending prefill tokens exceed the configured limit.

-
–[QueueOverflowError](https://docs.vllm.ai#vllm.exceptions.QueueOverflowError)Raised when admitting a request would exceed the request queue limit.

-
–[VLLMClientError](https://docs.vllm.ai#vllm.exceptions.VLLMClientError)Base class for errors caused by the client request (4xx).

-
–[VLLMError](https://docs.vllm.ai#vllm.exceptions.VLLMError)Base class for all vLLM-specific errors.

-
–[VLLMNotFoundError](https://docs.vllm.ai#vllm.exceptions.VLLMNotFoundError)vLLM-specific NotFoundError.

-
–[VLLMServerError](https://docs.vllm.ai#vllm.exceptions.VLLMServerError)Base class for errors caused by the server (5xx).

-
–[VLLMUnprocessableEntityError](https://docs.vllm.ai#vllm.exceptions.VLLMUnprocessableEntityError)vLLM-specific error for unprocessable entity requests.

-
–[VLLMValidationError](https://docs.vllm.ai#vllm.exceptions.VLLMValidationError)vLLM-specific validation error for request validation failures.


##

`GenerationError`

[¶](https://docs.vllm.ai#vllm.exceptions.GenerationError)

Bases: [VLLMServerError](https://docs.vllm.ai#vllm.exceptions.VLLMServerError)

raised when finish_reason indicates internal server error (500)

## Source code in `vllm/exceptions.py`


##

`GracefulHTTPError`

[¶](https://docs.vllm.ai#vllm.exceptions.GracefulHTTPError)

Bases: [VLLMError](https://docs.vllm.ai#vllm.exceptions.VLLMError)

Exception that should be translated into an HTTP error response.

These are expected to occur during normal operation (e.g. admission control rejections) and should be surfaced to the client with the explicit HTTP status code they carry, rather than being mapped to a generic 4xx/5xx by the client/server split.

## Source code in `vllm/exceptions.py`


##

`LoRAAdapterNotFoundError`

[¶](https://docs.vllm.ai#vllm.exceptions.LoRAAdapterNotFoundError)

Bases: [VLLMNotFoundError](https://docs.vllm.ai#vllm.exceptions.VLLMNotFoundError)

Exception raised when a LoRA adapter is not found.

This exception is thrown when a requested LoRA adapter does not exist in the system.

Attributes:

-
(`message`


) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The error message string describing the exception


## Source code in `vllm/exceptions.py`


##

`MaxQueuedTokensError`

[¶](https://docs.vllm.ai#vllm.exceptions.MaxQueuedTokensError)

Bases: [GracefulHTTPError](https://docs.vllm.ai#vllm.exceptions.GracefulHTTPError)

Raised when the pending prefill tokens exceed the configured limit.

Returns HTTP 503 (Service Unavailable) so that load balancers and client SDKs retry the request on a different instance.

## Source code in `vllm/exceptions.py`


##

`QueueOverflowError`

[¶](https://docs.vllm.ai#vllm.exceptions.QueueOverflowError)

Bases: [GracefulHTTPError](https://docs.vllm.ai#vllm.exceptions.GracefulHTTPError)

Raised when admitting a request would exceed the request queue limit.

Returns HTTP 503 (Service Unavailable) so that load balancers and client SDKs retry the request on a different instance.

## Source code in `vllm/exceptions.py`


##

`VLLMClientError`

[¶](https://docs.vllm.ai#vllm.exceptions.VLLMClientError)

##

`VLLMError`

[¶](https://docs.vllm.ai#vllm.exceptions.VLLMError)

Bases: [Exception](https://docs.python.org/3/builtins/exceptions.html#Exception)

Base class for all vLLM-specific errors.

Subclasses are split into `VLLMClientError`

(caused by the request, mapped to 4xx) and `VLLMServerError`

(caused by the server, mapped to 5xx). Dispatching on this hierarchy lets the entrypoints decide the HTTP status without relying on raw Python exception types such as `ValueError`

.

## Source code in `vllm/exceptions.py`


##

`VLLMNotFoundError`

[¶](https://docs.vllm.ai#vllm.exceptions.VLLMNotFoundError)

Bases: [VLLMClientError](https://docs.vllm.ai#vllm.exceptions.VLLMClientError)

vLLM-specific NotFoundError.

##

`VLLMServerError`

[¶](https://docs.vllm.ai#vllm.exceptions.VLLMServerError)

##

`VLLMUnprocessableEntityError`

[¶](https://docs.vllm.ai#vllm.exceptions.VLLMUnprocessableEntityError)

Bases: [VLLMClientError](https://docs.vllm.ai#vllm.exceptions.VLLMClientError)

vLLM-specific error for unprocessable entity requests.

This exception is raised when the request content is invalid or cannot be processed, such as when an image URL points to a non-existent or inaccessible resource (404, 403, DNS failure, etc.).

Parameters:

-

(`message`

[¶](https://docs.vllm.ai#vllm.exceptions.VLLMUnprocessableEntityError(message))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The error message describing the unprocessable entity.

-

(`parameter`

[¶](https://docs.vllm.ai#vllm.exceptions.VLLMUnprocessableEntityError(parameter))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –Optional parameter name that failed validation.

-

(`value`

[¶](https://docs.vllm.ai#vllm.exceptions.VLLMUnprocessableEntityError(value))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`None`

) –Optional value that was rejected during validation.


## Source code in `vllm/exceptions.py`


##

`VLLMValidationError`

[¶](https://docs.vllm.ai#vllm.exceptions.VLLMValidationError)

Bases: [VLLMClientError](https://docs.vllm.ai#vllm.exceptions.VLLMClientError)

vLLM-specific validation error for request validation failures.

Parameters:

-

(`message`

[¶](https://docs.vllm.ai#vllm.exceptions.VLLMValidationError(message))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The error message describing the validation failure.

-

(`parameter`

[¶](https://docs.vllm.ai#vllm.exceptions.VLLMValidationError(parameter))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –Optional parameter name that failed validation.

-

(`value`

[¶](https://docs.vllm.ai#vllm.exceptions.VLLMValidationError(value))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`None`

) –Optional value that was rejected during validation.