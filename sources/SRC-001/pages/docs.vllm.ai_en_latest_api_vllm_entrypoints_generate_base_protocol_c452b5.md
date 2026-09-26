source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/generate/base/protocol/
lastmod: 2026-09-24

#

`vllm.entrypoints.generate.base.protocol`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.base.protocol)

Classes:

-
–[SpeculativeDecodingMetrics](https://docs.vllm.ai#vllm.entrypoints.generate.base.protocol.SpeculativeDecodingMetrics)Per-request speculative-decoding acceptance metrics.


Functions:

-
–[structured_outputs_from_response_format](https://docs.vllm.ai#vllm.entrypoints.generate.base.protocol.structured_outputs_from_response_format)Apply

`response_format`

overrides to`structured_outputs`

. -
–[validate_cache_salt](https://docs.vllm.ai#vllm.entrypoints.generate.base.protocol.validate_cache_salt)Validate cache salts before they reach downstream cache backends.

-
–[validate_structural_tag_response_format](https://docs.vllm.ai#vllm.entrypoints.generate.base.protocol.validate_structural_tag_response_format)Validate structural tags before they are sent to the engine.


##

`SpeculativeDecodingMetrics`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.base.protocol.SpeculativeDecodingMetrics)

Bases: `OpenAIBaseModel`


Per-request speculative-decoding acceptance metrics.

Experimental, subject to change. Only populated for single-sequence requests (`n == 1`

); `null`

for `n > 1`

, mirroring the timing metrics.

## Source code in `vllm/entrypoints/generate/base/protocol.py`


##

`structured_outputs_from_response_format(structured_outputs, response_format)`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.base.protocol.structured_outputs_from_response_format)

Apply `response_format`

overrides to `structured_outputs`

.

## Source code in `vllm/entrypoints/generate/base/protocol.py`


##

`validate_cache_salt(cache_salt)`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.base.protocol.validate_cache_salt)

Validate cache salts before they reach downstream cache backends.

## Source code in `vllm/entrypoints/generate/base/protocol.py`


##

`validate_structural_tag_response_format(response_format)`

[¶](https://docs.vllm.ai#vllm.entrypoints.generate.base.protocol.validate_structural_tag_response_format)

Validate structural tags before they are sent to the engine.

Engine-side validation reports malformed structural tags as generation failures. OpenAI request parsing should classify them as bad requests.