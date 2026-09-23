source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/exception_handling/handlers/vllm_error/
lastmod: 2026-09-23

#

`vllm.entrypoints.serve.exception_handling.handlers.vllm_error`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.exception_handling.handlers.vllm_error)

Functions:

-
–[engine_error_handler](https://docs.vllm.ai#vllm.entrypoints.serve.exception_handling.handlers.vllm_error.engine_error_handler)VLLM V1 AsyncLLM catches exceptions and returns

-
–[generation_error_handler](https://docs.vllm.ai#vllm.entrypoints.serve.exception_handling.handlers.vllm_error.generation_error_handler)Handle GenerationError without logging stack traces.

-
–[vllm_error_handler](https://docs.vllm.ai#vllm.entrypoints.serve.exception_handling.handlers.vllm_error.vllm_error_handler)Dispatch a vLLM-specific error to the appropriate handler.


##

`engine_error_handler(req, exc)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.exception_handling.handlers.vllm_error.engine_error_handler)

VLLM V1 AsyncLLM catches exceptions and returns only two types: EngineGenerateError and EngineDeadError.

EngineGenerateError is raised by the per request generate() method. This error could be request specific (and therefore recoverable - e.g. if there is an error in input processing).

EngineDeadError is raised by the background output_handler method. This error is global and therefore not recoverable.

We register these @app.exception_handlers to return nice responses to the end user if they occur and shut down if needed. See https://fastapi.tiangolo.com/tutorial/handling-errors/ for more details on how exception handlers work.

If an exception is encountered in a StreamingResponse generator, the exception is not raised, since we already sent a 200 status. Rather, we send an error message as the next chunk. Since the exception is not raised, this means that the server will not automatically shut down. Instead, we use the watchdog background task for check for errored state.

## Source code in `vllm/entrypoints/serve/exception_handling/handlers/vllm_error.py`


##

`generation_error_handler(req, exc)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.exception_handling.handlers.vllm_error.generation_error_handler)

Handle GenerationError without logging stack traces.

GenerationError is a known, expected error (e.g. KV cache load failure) that should be returned to the client as a 500 response without polluting server logs with stack traces.

## Source code in `vllm/entrypoints/serve/exception_handling/handlers/vllm_error.py`


##

`vllm_error_handler(req, exc)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.exception_handling.handlers.vllm_error.vllm_error_handler)

Dispatch a vLLM-specific error to the appropriate handler.