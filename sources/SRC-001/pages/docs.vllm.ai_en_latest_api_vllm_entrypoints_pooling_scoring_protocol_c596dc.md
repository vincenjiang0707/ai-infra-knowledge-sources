source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/pooling/scoring/protocol/
lastmod: 2026-09-24

#

`vllm.entrypoints.pooling.scoring.protocol`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.scoring.protocol)

Classes:

##

`ScoringRequestMixin`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.scoring.protocol.ScoringRequestMixin)

Bases: `PoolingBasicRequestMixin`

, `ClassifyRequestMixin`


## Source code in `vllm/entrypoints/pooling/scoring/protocol.py`


###

`_merge_instruction_into_kwargs()`

[¶](https://docs.vllm.ai#vllm.entrypoints.pooling.scoring.protocol.ScoringRequestMixin._merge_instruction_into_kwargs)

Fold the top-level `instruction`

field into `chat_template_kwargs`

.

This allows callers to use either the convenience field or the generic dict. Explicit keys inside `chat_template_kwargs`

take precedence over the top-level `instruction`

field.