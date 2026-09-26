source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/warmup/mamba_triton_warmup/
lastmod: 2026-09-24

#

`vllm.model_executor.warmup.mamba_triton_warmup`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.mamba_triton_warmup)

Warm Mamba-style Triton kernels shared across GDN / Mamba / KDA models.

Functions:

-
–[mamba_triton_warmup](https://docs.vllm.ai#vllm.model_executor.warmup.mamba_triton_warmup.mamba_triton_warmup)Warm prefix-cache memcpy for every Mamba-style KV cache group.


##

`_warm_batch_memcpy_kernel(device)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.mamba_triton_warmup._warm_batch_memcpy_kernel)

Warm the Mamba prefix-cache state copy specialization.

## Source code in `vllm/model_executor/warmup/mamba_triton_warmup.py`


##

`mamba_triton_warmup(runner)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.mamba_triton_warmup.mamba_triton_warmup)

Warm prefix-cache memcpy for every Mamba-style KV cache group.