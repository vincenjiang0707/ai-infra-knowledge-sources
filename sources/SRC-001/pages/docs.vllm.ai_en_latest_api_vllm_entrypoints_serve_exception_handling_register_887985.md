source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/exception_handling/register/
lastmod: 2026-09-24

#

`vllm.entrypoints.serve.exception_handling.register`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.exception_handling.register)

vLLM Exception handlers are registered in four layers: 1. framework errors raised by FastAPI/Starlette 2. vLLM-specific errors dispatched via a single `VLLMError`

handler 3. fallback handlers for raw exceptions not yet migrated to `VLLMError`

4. the raw `Exception`

handler as a safety net Registering specific exception types (rather than only `Exception`

) ensures they are handled by `ExceptionMiddleware`

(inside the Prometheus middleware) rather than `ServerErrorMiddleware`

(outside it), so their status codes are recorded correctly.