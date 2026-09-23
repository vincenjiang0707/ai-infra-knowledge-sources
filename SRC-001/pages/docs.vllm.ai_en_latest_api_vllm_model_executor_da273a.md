source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/
lastmod: 2026-09-23

#

`vllm.model_executor`

[¶](https://docs.vllm.ai#vllm.model_executor)

Modules:

-
–[custom_op](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op) -
–[determinism](https://docs.vllm.ai/determinism/#vllm.model_executor.determinism) -
–[hw_agnostic](https://docs.vllm.ai/hw_agnostic/#vllm.model_executor.hw_agnostic) -
–[kernels](https://docs.vllm.ai/kernels/#vllm.model_executor.kernels) -
–[layers](https://docs.vllm.ai/layers/#vllm.model_executor.layers) -
–[model_loader](https://docs.vllm.ai/model_loader/#vllm.model_executor.model_loader) -
–[models](https://docs.vllm.ai/models/#vllm.model_executor.models) -
–[offloader](https://docs.vllm.ai/offloader/#vllm.model_executor.offloader)Model parameter offloading infrastructure.

-
–[parameter](https://docs.vllm.ai/parameter/#vllm.model_executor.parameter) -
–[utils](https://docs.vllm.ai/utils/#vllm.model_executor.utils)Utils for model executor.

-
–[warmup](https://docs.vllm.ai/warmup/#vllm.model_executor.warmup)

Classes:

-
–[BasevLLMParameter](https://docs.vllm.ai#vllm.model_executor.BasevLLMParameter)Base parameter for vLLM linear layers. Extends the torch.nn.parameter

-
–[PackedvLLMParameter](https://docs.vllm.ai#vllm.model_executor.PackedvLLMParameter)Parameter for model weights which are packed on disk.


##

`BasevLLMParameter`

[¶](https://docs.vllm.ai#vllm.model_executor.BasevLLMParameter)

Bases: `Parameter`


Base parameter for vLLM linear layers. Extends the torch.nn.parameter by taking in a linear weight loader. Will copy the loaded weight into the parameter when the provided weight loader is called.

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.model_executor.BasevLLMParameter.__init__)Initialize the BasevLLMParameter.


## Source code in `vllm/model_executor/parameter.py`


|
|

###

`__init__(data, weight_loader)`

[¶](https://docs.vllm.ai#vllm.model_executor.BasevLLMParameter.__init__)

Initialize the BasevLLMParameter.

Parameters:

-

(`data`

[¶](https://docs.vllm.ai#vllm.model_executor.BasevLLMParameter.__init__(data))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)torch tensor with the parameter data

-

(`weight_loader`

[¶](https://docs.vllm.ai#vllm.model_executor.BasevLLMParameter.__init__(weight_loader))

) –[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)weight loader callable


## Source code in `vllm/model_executor/parameter.py`


##

`PackedvLLMParameter`

[¶](https://docs.vllm.ai#vllm.model_executor.PackedvLLMParameter)

Bases: [ModelWeightParameter](https://docs.vllm.ai/parameter/#vllm.model_executor.parameter.ModelWeightParameter)

Parameter for model weights which are packed on disk. Example: GPTQ Marlin weights are int4 or int8, packed into int32. Extends the ModelWeightParameter to take in the packed factor, the packed dimension, and optionally, marlin tile size for marlin kernels. Adjusts the shard_size and shard_offset for fused linear layers model weight loading by accounting for packing and optionally, marlin tile size.