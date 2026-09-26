source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/exception_handling/utils/
lastmod: 2026-09-24

#

`vllm.entrypoints.serve.exception_handling.utils`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.exception_handling.utils)

Functions:

-
–[sanitize_message](https://docs.vllm.ai#vllm.entrypoints.serve.exception_handling.utils.sanitize_message)Strip memory addresses, tracebacks, and file paths from error messages.


##

`sanitize_message(message)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.exception_handling.utils.sanitize_message)

Strip memory addresses, tracebacks, and file paths from error messages.