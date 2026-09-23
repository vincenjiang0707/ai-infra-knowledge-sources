source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/dev/cache/api_router/
lastmod: 2026-09-23

#

`vllm.entrypoints.serve.dev.cache.api_router`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.dev.cache.api_router)

Functions:

-
–[reset_encoder_cache](https://docs.vllm.ai#vllm.entrypoints.serve.dev.cache.api_router.reset_encoder_cache)Reset the encoder cache. Note that we currently do not check if the

-
–[reset_mm_cache](https://docs.vllm.ai#vllm.entrypoints.serve.dev.cache.api_router.reset_mm_cache)Reset the multi-modal cache. Note that we currently do not check if the

-
–[reset_prefix_cache](https://docs.vllm.ai#vllm.entrypoints.serve.dev.cache.api_router.reset_prefix_cache)Reset the local prefix cache.


##

`reset_encoder_cache(raw_request)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.dev.cache.api_router.reset_encoder_cache)

Reset the encoder cache. Note that we currently do not check if the encoder cache is successfully reset in the API server.

## Source code in `vllm/entrypoints/serve/dev/cache/api_router.py`


##

`reset_mm_cache(raw_request)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.dev.cache.api_router.reset_mm_cache)

Reset the multi-modal cache. Note that we currently do not check if the multi-modal cache is successfully reset in the API server.

## Source code in `vllm/entrypoints/serve/dev/cache/api_router.py`


##

`reset_prefix_cache(raw_request, reset_running_requests=Query(default=False), reset_external=Query(default=False))`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.dev.cache.api_router.reset_prefix_cache)

Reset the local prefix cache.

Optionally, if the query parameter `reset_external=true`

also resets the external (connector-managed) prefix cache.

Returns `{"success": bool}`

. The reset fails (`success=false`

) while blocks are still held, e.g. by running requests or in-flight async KV offload transfers; callers may retry.

## Example

POST /reset_prefix_cache?reset_external=true