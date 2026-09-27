source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/diffusion_gemma_sampler/
lastmod: 2026-09-27

#

`vllm.model_executor.models.diffusion_gemma_sampler`

[¶](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma_sampler)

One-pass row statistics for the DiffusionGemma denoise sampler.

The step needs, for every canvas position, the argmax of the temperature-scaled logits, a Gumbel-max sample from them, the entropy of their softmax, and the softmax itself in the model dtype for the self-conditioning matmul. As PyTorch ops these are several passes over a `[rows, vocab]`

fp32 tensor plus a same-sized noise tensor. The Triton kernel reads each row once with an online max and sum, draws the noise inline, and writes the probabilities once.

Functions:

-
–[sample_row_stats](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma_sampler.sample_row_stats)Argmax, Gumbel-max sample, entropy and (optionally) softmax per row.

-
–[sample_row_stats_reference](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma_sampler.sample_row_stats_reference)The PyTorch form of the same statistics, for tests and non-CUDA runs.


##

`sample_row_stats(logits, temps, canvas_len, seed, probs_dtype)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma_sampler.sample_row_stats)

Argmax, Gumbel-max sample, entropy and (optionally) softmax per row.

`logits`

is `[rows, vocab]`

and row `i`

uses temperature `temps[i // canvas_len]`

. A zero temperature is greedy: the sample is the argmax, and the entropy is the reference's, which clamps the temperature at 1e-10.

## Source code in `vllm/model_executor/models/diffusion_gemma_sampler.py`


##

`sample_row_stats_reference(logits, temps, canvas_len, probs_dtype)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.diffusion_gemma_sampler.sample_row_stats_reference)

The PyTorch form of the same statistics, for tests and non-CUDA runs.