source: https://docs.vllm.ai/en/latest/api/vllm/config/diffusion/
lastmod: 2026-09-24

#

`vllm.config.diffusion`

[¶](https://docs.vllm.ai#vllm.config.diffusion)

Configuration for discrete diffusion (dLLM) models.

Classes:

-
–[DiffusionConfig](https://docs.vllm.ai#vllm.config.diffusion.DiffusionConfig)Configuration for discrete diffusion language models (dLLMs).


##

`DiffusionConfig`

[¶](https://docs.vllm.ai#vllm.config.diffusion.DiffusionConfig)

Configuration for discrete diffusion language models (dLLMs).

dLLMs generate tokens via iterative denoising over a fixed-length canvas rather than left-to-right autoregressive decoding. They reuse the speculative-decoding data path (draft token ids, scheduled spec decode tokens) with overloaded semantics for block-based generation.

Attributes:

-
([canvas_length](https://docs.vllm.ai#vllm.config.diffusion.DiffusionConfig.canvas_length)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Length of the denoising canvas (block). Also determines the number of

-
([max_denoising_steps](https://docs.vllm.ai#vllm.config.diffusion.DiffusionConfig.max_denoising_steps)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneMaximum number of denoising iterations per canvas block.


## Source code in `vllm/config/diffusion.py`


###

`canvas_length = Field(default=None, gt=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.diffusion.DiffusionConfig.canvas_length)

Length of the denoising canvas (block). Also determines the number of speculative tokens scheduled per step.

###

`max_denoising_steps = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.diffusion.DiffusionConfig.max_denoising_steps)

Maximum number of denoising iterations per canvas block. If not set, read from the model's generation_config.json.