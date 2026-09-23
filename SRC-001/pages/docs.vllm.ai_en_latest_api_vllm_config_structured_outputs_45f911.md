source: https://docs.vllm.ai/en/latest/api/vllm/config/structured_outputs/
lastmod: 2026-09-23

#

`vllm.config.structured_outputs`

[¶](https://docs.vllm.ai#vllm.config.structured_outputs)

Classes:

-
–[StructuredOutputsConfig](https://docs.vllm.ai#vllm.config.structured_outputs.StructuredOutputsConfig)Dataclass which contains structured outputs config for the engine.


##

`StructuredOutputsConfig`

[¶](https://docs.vllm.ai#vllm.config.structured_outputs.StructuredOutputsConfig)

Dataclass which contains structured outputs config for the engine.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.structured_outputs.StructuredOutputsConfig.compute_hash)WARNING: Whenever a new field is added to this config,


Attributes:

-
([backend](https://docs.vllm.ai#vllm.config.structured_outputs.StructuredOutputsConfig.backend)`StructuredOutputsBackend`

) –Which engine will be used for structured outputs (e.g. JSON schema,

-
([disable_additional_properties](https://docs.vllm.ai#vllm.config.structured_outputs.StructuredOutputsConfig.disable_additional_properties)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, the`guidance`

backend will not use`additionalProperties`

-
([disable_any_whitespace](https://docs.vllm.ai#vllm.config.structured_outputs.StructuredOutputsConfig.disable_any_whitespace)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, json output will always be compact without any whitespace. -
([enable_in_reasoning](https://docs.vllm.ai#vllm.config.structured_outputs.StructuredOutputsConfig.enable_in_reasoning)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to use structured input for reasoning.

-
([reasoning_parser](https://docs.vllm.ai#vllm.config.structured_outputs.StructuredOutputsConfig.reasoning_parser)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Select the reasoning parser depending on the model that you're using.

-
([reasoning_parser_plugin](https://docs.vllm.ai#vllm.config.structured_outputs.StructuredOutputsConfig.reasoning_parser_plugin)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Path to a dynamically reasoning parser plugin that can be dynamically


## Source code in `vllm/config/structured_outputs.py`


###

`backend = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.structured_outputs.StructuredOutputsConfig.backend)

Which engine will be used for structured outputs (e.g. JSON schema, regex, etc) by default. With "auto", we will make opinionated choices based on request contents and what the backend libraries currently support, so the behavior is subject to change in each release.

###

`disable_additional_properties = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.structured_outputs.StructuredOutputsConfig.disable_additional_properties)

If `True`

, the `guidance`

backend will not use `additionalProperties`

in the JSON schema. This is only supported for the `guidance`

backend and is used to better align its behaviour with `outlines`

and `xgrammar`

.

###

`disable_any_whitespace = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.structured_outputs.StructuredOutputsConfig.disable_any_whitespace)

If `True`

, json output will always be compact without any whitespace. If `False`

, the model may generate whitespace between JSON fields, which is still valid JSON. This is only supported for xgrammar and guidance backends.

###

`enable_in_reasoning = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.structured_outputs.StructuredOutputsConfig.enable_in_reasoning)

Whether to use structured input for reasoning.

###

`reasoning_parser = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.structured_outputs.StructuredOutputsConfig.reasoning_parser)

Select the reasoning parser depending on the model that you're using. This is used to parse the reasoning content into OpenAI API format.

###

`reasoning_parser_plugin = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.structured_outputs.StructuredOutputsConfig.reasoning_parser_plugin)

Path to a dynamically reasoning parser plugin that can be dynamically loaded and registered.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.structured_outputs.StructuredOutputsConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.