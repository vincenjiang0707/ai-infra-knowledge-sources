source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/warmup/cutedsl_warmup/
lastmod: 2026-09-23

#

`vllm.model_executor.warmup.cutedsl_warmup`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.cutedsl_warmup)

Deprecated compatibility registry for legacy CuTeDSL warmups.

Functions:

-
–[cutedsl_warmup](https://docs.vllm.ai#vllm.model_executor.warmup.cutedsl_warmup.cutedsl_warmup)Run CuTeDSL compile providers before serving.

-
–[register_cutedsl_warmup_provider](https://docs.vllm.ai#vllm.model_executor.warmup.cutedsl_warmup.register_cutedsl_warmup_provider)Register an object that can expose CuTeDSL warmup compile units.


##

`cutedsl_warmup()`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.cutedsl_warmup.cutedsl_warmup)

Run CuTeDSL compile providers before serving.

## Source code in `vllm/model_executor/warmup/cutedsl_warmup.py`


##

`register_cutedsl_warmup_provider(provider)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.cutedsl_warmup.register_cutedsl_warmup_provider)

Register an object that can expose CuTeDSL warmup compile units.