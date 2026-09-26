source: https://docs.vllm.ai/en/latest/api/vllm/config/device/
lastmod: 2026-09-24

#

`vllm.config.device`

[¶](https://docs.vllm.ai#vllm.config.device)

Classes:

-
–[DeviceConfig](https://docs.vllm.ai#vllm.config.device.DeviceConfig)Configuration for the device to use for vLLM execution.


##

`DeviceConfig`

[¶](https://docs.vllm.ai#vllm.config.device.DeviceConfig)

Configuration for the device to use for vLLM execution.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.device.DeviceConfig.compute_hash)WARNING: Whenever a new field is added to this config,


Attributes:

-
([device](https://docs.vllm.ai#vllm.config.device.DeviceConfig.device)`SkipValidation[Device |`

) –[device](https://pytorch.org/docs/stable/tensor_attributes.html#torch.device)| None]Device type for vLLM execution.

-
([device_type](https://docs.vllm.ai#vllm.config.device.DeviceConfig.device_type)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Device type from the current platform. This is set in


## Source code in `vllm/config/device.py`


###

`device = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.device.DeviceConfig.device)

Device type for vLLM execution. This parameter is deprecated and will be removed in a future release. It will now be set automatically based on the current platform.

###

`device_type = field(init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.device.DeviceConfig.device_type)

Device type from the current platform. This is set in `__post_init__`

.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.device.DeviceConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.