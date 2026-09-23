source: https://docs.vllm.ai/en/latest/api/vllm/config/aux_output/
lastmod: 2026-09-23

#

`vllm.config.aux_output`

[¶](https://docs.vllm.ai#vllm.config.aux_output)

Configuration for execution auxiliary outputs.

Classes:

-
–[AuxOutputConfig](https://docs.vllm.ai#vllm.config.aux_output.AuxOutputConfig)Configuration for auxiliary-output delivery.


##

`AuxOutputConfig`

[¶](https://docs.vllm.ai#vllm.config.aux_output.AuxOutputConfig)

Configuration for auxiliary-output delivery.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.aux_output.AuxOutputConfig.compute_hash)Hash AuxOutput settings that alter the model forward graph.


Attributes:

-
([enable_return_routed_experts](https://docs.vllm.ai#vllm.config.aux_output.AuxOutputConfig.enable_return_routed_experts)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Capture and return routed-experts auxiliary outputs.

-
([enabled](https://docs.vllm.ai#vllm.config.aux_output.AuxOutputConfig.enabled)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether any execution auxiliary output is enabled.

-
([max_bytes](https://docs.vllm.ai#vllm.config.aux_output.AuxOutputConfig.max_bytes)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneLRU capacity, or

`None`

to derive it from the KV cache capacity.

## Source code in `vllm/config/aux_output.py`


###

`enable_return_routed_experts = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.aux_output.AuxOutputConfig.enable_return_routed_experts)

Capture and return routed-experts auxiliary outputs.

###

`enabled`

`property`

[¶](https://docs.vllm.ai#vllm.config.aux_output.AuxOutputConfig.enabled)

Whether any execution auxiliary output is enabled.

###

`max_bytes = Field(default=None, gt=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.aux_output.AuxOutputConfig.max_bytes)

LRU capacity, or `None`

to derive it from the KV cache capacity.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.aux_output.AuxOutputConfig.compute_hash)

Hash AuxOutput settings that alter the model forward graph.