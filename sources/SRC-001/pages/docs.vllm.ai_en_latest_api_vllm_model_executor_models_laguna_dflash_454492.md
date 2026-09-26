source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/laguna_dflash/
lastmod: 2026-09-24

#

`vllm.model_executor.models.laguna_dflash`

[¶](https://docs.vllm.ai#vllm.model_executor.models.laguna_dflash)

DFlash speculator for Laguna target models.

Laguna DFlash uses a uniform drafter layer flavor (`layer_types`

all full or all sliding). The draft checkpoint shares token embedding and lm_head weights with the target model through the generic spec-decode proposer.