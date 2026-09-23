source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/exception_handling/handlers/validation/
lastmod: 2026-09-23

#

`vllm.entrypoints.serve.exception_handling.handlers.validation`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.exception_handling.handlers.validation)

Functions:

-
–[clean_loc_for_param](https://docs.vllm.ai#vllm.entrypoints.serve.exception_handling.handlers.validation.clean_loc_for_param)Join a Pydantic error

`loc`

tuple into a clean dotted`param`


##

`_format_error(err)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.exception_handling.handlers.validation._format_error)

Render one validation error, bounded in size.

## Source code in `vllm/entrypoints/serve/exception_handling/handlers/validation.py`


##

`_is_internal_loc_segment(segment)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.exception_handling.handlers.validation._is_internal_loc_segment)

True if `segment`

is a Pydantic-internal wrapper/union-branch marker rather than a user-meaningful field name or list index.

## Source code in `vllm/entrypoints/serve/exception_handling/handlers/validation.py`


##

`_summarize_error_input(value)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.exception_handling.handlers.validation._summarize_error_input)

A size-bounded stand-in for a validation error's `input`

value.

Containers are described rather than rendered: `repr()`

of a large list materializes the whole string first, which is the cost this is meant to avoid.

## Source code in `vllm/entrypoints/serve/exception_handling/handlers/validation.py`


##

`clean_loc_for_param(loc)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.exception_handling.handlers.validation.clean_loc_for_param)

Join a Pydantic error `loc`

tuple into a clean dotted `param`

path, dropping internal wrapper/union-branch markers that don't correspond to a real field name an API consumer would recognize.

E.g. ('body', 'function-wrap[**log_extra_fields**()]', 'prompt') -> "body.prompt", not "body.function-wrap[**log_extra_fields**()].prompt".