source: https://docs.vllm.ai/en/latest/api/vllm/config/watermarking/
lastmod: 2026-09-24

#

`vllm.config.watermarking`

[¶](https://docs.vllm.ai#vllm.config.watermarking)

Classes:

-
–[WatermarkConfig](https://docs.vllm.ai#vllm.config.watermarking.WatermarkConfig)Configuration for text watermark generation.


##

`WatermarkConfig`

[¶](https://docs.vllm.ai#vllm.config.watermarking.WatermarkConfig)

Configuration for text watermark generation.

Attributes:

-
([algorithm](https://docs.vllm.ai#vllm.config.watermarking.WatermarkConfig.algorithm)`WatermarkingAlgorithm`

) –Algorithm used to watermark generated text.

-
([allow_target_only_watermarking](https://docs.vllm.ai#vllm.config.watermarking.WatermarkConfig.allow_target_only_watermarking)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Allow speculative decoding without watermarking draft tokens.

-
([alpha](https://docs.vllm.ai#vllm.config.watermarking.WatermarkConfig.alpha)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Probability of selecting key B for dual-key watermarking.

-
([context_width](https://docs.vllm.ai#vllm.config.watermarking.WatermarkConfig.context_width)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of prior tokens used by the watermark PRF.

-
([deduplicate_contexts](https://docs.vllm.ai#vllm.config.watermarking.WatermarkConfig.deduplicate_contexts)`WatermarkContextScope`

) –Which history is searched for a repeated context before a token is

-
([deduplicate_contexts_max_history](https://docs.vllm.ai#vllm.config.watermarking.WatermarkConfig.deduplicate_contexts_max_history)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneNumber of most recent history positions searched (default 8192), or

-
([key](https://docs.vllm.ai#vllm.config.watermarking.WatermarkConfig.key)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Secret key used to watermark generated text.

-
([prf](https://docs.vllm.ai#vllm.config.watermarking.WatermarkConfig.prf)`WatermarkPRFName`

) –Pseudorandom function used by the watermarking algorithm.


## Source code in `vllm/config/watermarking.py`


###

`algorithm = 'gumbel'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.watermarking.WatermarkConfig.algorithm)

Algorithm used to watermark generated text.

###

`allow_target_only_watermarking = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.watermarking.WatermarkConfig.allow_target_only_watermarking)

Allow speculative decoding without watermarking draft tokens.

###

`alpha = Field(default=0.1, ge=0, le=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.watermarking.WatermarkConfig.alpha)

Probability of selecting key B for dual-key watermarking.

###

`context_width = Field(default=4, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.watermarking.WatermarkConfig.context_width)

Number of prior tokens used by the watermark PRF.

###

`deduplicate_contexts = 'single_turn'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.watermarking.WatermarkConfig.deduplicate_contexts)

Which history is searched for a repeated context before a token is sampled; a repeated context is sampled without the watermark. `none`

disables the search. `single_turn`

(default) searches this request's generated tokens. `all`

also searches the prompt and samples the first `context_width`

generated tokens without watermarking.

###

`deduplicate_contexts_max_history = Field(default=8192, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.watermarking.WatermarkConfig.deduplicate_contexts_max_history)

Number of most recent history positions searched (default 8192), or `None`

for the whole scope. Each position is compared over the `context_width`

tokens before it. Ignored when `deduplicate_contexts`

is `none`

.

###

`key = Field(ge=0, repr=False, exclude=True)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.watermarking.WatermarkConfig.key)

Secret key used to watermark generated text.

###

`prf = 'philox'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.watermarking.WatermarkConfig.prf)

Pseudorandom function used by the watermarking algorithm.