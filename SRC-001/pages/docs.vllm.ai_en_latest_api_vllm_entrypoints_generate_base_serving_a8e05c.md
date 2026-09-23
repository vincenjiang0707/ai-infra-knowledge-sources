source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/generate/base/serving/
lastmod: 2026-09-23

#

`vllm.entrypoints.generate.base.serving`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.base.serving)

Classes:

Functions:

-
–[build_per_request_timing_metrics](https://docs.vllm.ai#vllm.entrypoints.generate.base.serving.build_per_request_timing_metrics)Build per-request timing metrics from

`RequestStateStats`

. -
–[build_spec_decoding_metrics](https://docs.vllm.ai#vllm.entrypoints.generate.base.serving.build_spec_decoding_metrics)Build per-request spec-decode acceptance metrics from the single output

-
–[resolve_token_id_placeholder](https://docs.vllm.ai#vllm.entrypoints.generate.base.serving.resolve_token_id_placeholder)Decode a 'token_id:N' placeholder back to a token string and UTF-8 bytes.


##

`GenerateBaseServing`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.base.serving.GenerateBaseServing)

Bases:

, [BaseServing](https://docs.vllm.ai/serve/engine/serving/#vllm.entrypoints.serve.engine.serving.BaseServing)[BeamSearchOnlineMixin](https://docs.vllm.ai/beam_search/online/#vllm.entrypoints.generate.beam_search.online.BeamSearchOnlineMixin)

## Source code in `vllm/entrypoints/generate/base/serving.py`


|
|

###

`_convert_generation_error_to_streaming_response(e)`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.base.serving.GenerateBaseServing._convert_generation_error_to_streaming_response)

Convert GenerationError to streaming error response.

## Source code in `vllm/entrypoints/generate/base/serving.py`


###

`_get_data_parallel_rank(raw_request)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.base.serving.GenerateBaseServing._get_data_parallel_rank)

Pulls the data parallel rank from a header, if provided.

## Source code in `vllm/entrypoints/generate/base/serving.py`


###

`_preflight(n=1)`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.base.serving.GenerateBaseServing._preflight)

Engine checks that must run before a response is started.

This is required for the streaming case, where we return a success status before we actually start generating text :).

Parameters:

## Source code in `vllm/entrypoints/generate/base/serving.py`


###

`_raise_if_error(finish_reason, request_id)`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.base.serving.GenerateBaseServing._raise_if_error)

Raise GenerationError if finish_reason indicates an error.

## Source code in `vllm/entrypoints/generate/base/serving.py`


###

`_with_kv_transfer_rejection_cleanup(awaitable, request, raw_request)`

`async`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.base.serving.GenerateBaseServing._with_kv_transfer_rejection_cleanup)

Wrap a `create_*`

coroutine so that, if it raises or returns an ErrorResponse (i.e. the request never reached the engine), the KV connector is notified to free any pinned remote-prefill blocks.

## Source code in `vllm/entrypoints/generate/base/serving.py`


##

`build_per_request_timing_metrics(metrics, num_generation_tokens)`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.base.serving.build_per_request_timing_metrics)

Build per-request timing metrics from `RequestStateStats`

.

`generation_time_ms`

is the decode interval only (first output token to last output token); it excludes both queue wait and prefill/TTFT. `tokens_per_second`

is overall output throughput: all generated tokens over the inference interval (scheduling to last output token), so it counts the prefill/TTFT phase and is not simply the reciprocal of `mean_itl_ms`

. Each field is left `None`

when the timestamps it depends on are unavailable.

## Source code in `vllm/entrypoints/generate/base/serving.py`


##

`build_spec_decoding_metrics(final_res)`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.base.serving.build_spec_decoding_metrics)

Build per-request spec-decode acceptance metrics from the single output sequence, or `None`

when unavailable (metrics disabled, or no sequence yet).

Only meaningful for single-sequence requests; callers suppress it for n>1.

## Source code in `vllm/entrypoints/generate/base/serving.py`


##

`resolve_token_id_placeholder(token, tokenizer)`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.base.serving.resolve_token_id_placeholder)

Decode a 'token_id:N' placeholder back to a token string and UTF-8 bytes.

Returns (token, None) unchanged if token is not a placeholder. This is the inverse of format_token_id_placeholder / _get_decoded_token when return_as_token_id=True.