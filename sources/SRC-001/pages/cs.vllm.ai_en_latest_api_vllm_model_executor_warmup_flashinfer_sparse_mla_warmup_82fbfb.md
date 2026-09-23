source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/warmup/flashinfer_sparse_mla_warmup/
lastmod: 2026-09-23

#

`vllm.model_executor.warmup.flashinfer_sparse_mla_warmup`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.flashinfer_sparse_mla_warmup)

Warmup and autotune helpers for FlashInfer sparse MLA backends.

Functions:

-
–[autotune_hisparse_flashinfer_attention](https://docs.vllm.ai#vllm.model_executor.warmup.flashinfer_sparse_mla_warmup.autotune_hisparse_flashinfer_attention)Autotune each HiSparse FlashInfer sparse-MLA configuration.

-
–[deepseek_v4_sparse_mla_attention_warmup](https://docs.vllm.ai#vllm.model_executor.warmup.flashinfer_sparse_mla_warmup.deepseek_v4_sparse_mla_attention_warmup)Warm DSv4 sparse-MLA mixed prefill+decode attention.

-
–[flashinfer_sparse_mla_decode_autotune_warmup](https://docs.vllm.ai#vllm.model_executor.warmup.flashinfer_sparse_mla_warmup.flashinfer_sparse_mla_decode_autotune_warmup)Autotune generic FlashInfer sparse MLA decode when selected.


##

`_run_flashinfer_sparse_mla_decode_autotune(worker, num_tokens, allowed_backends)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.flashinfer_sparse_mla_warmup._run_flashinfer_sparse_mla_decode_autotune)

Autotune FlashInfer's SM120 sparse-MLA decode path.

## Source code in `vllm/model_executor/warmup/flashinfer_sparse_mla_warmup.py`


|
|

##

`autotune_hisparse_flashinfer_attention(runner)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.flashinfer_sparse_mla_warmup.autotune_hisparse_flashinfer_attention)

Autotune each HiSparse FlashInfer sparse-MLA configuration.

## Source code in `vllm/model_executor/warmup/flashinfer_sparse_mla_warmup.py`


##

`deepseek_v4_sparse_mla_attention_warmup(worker)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.flashinfer_sparse_mla_warmup.deepseek_v4_sparse_mla_attention_warmup)

Warm DSv4 sparse-MLA mixed prefill+decode attention.

## Source code in `vllm/model_executor/warmup/flashinfer_sparse_mla_warmup.py`


##

`flashinfer_sparse_mla_decode_autotune_warmup(worker)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.flashinfer_sparse_mla_warmup.flashinfer_sparse_mla_decode_autotune_warmup)

Autotune generic FlashInfer sparse MLA decode when selected.