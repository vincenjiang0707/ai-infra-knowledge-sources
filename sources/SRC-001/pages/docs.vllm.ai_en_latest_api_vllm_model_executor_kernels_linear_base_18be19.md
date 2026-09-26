source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/base/
lastmod: 2026-09-24

#

`vllm.model_executor.kernels.linear.base`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base)

Classes:

-
–[FP8Params](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.FP8Params)FP8 layer parameters with typed fields.

-
–[MMLinearKernel](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel)Abstract base class for quantized matrix multiplication kernels.

-
–[Params](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.Params)Base class for quantized layer parameters.


##

`FP8Params`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.FP8Params)

Bases: [Params](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.Params)

FP8 layer parameters with typed fields.

Methods:

-
–[from_layer](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.FP8Params.from_layer)Extract parameters from layer.


## Source code in `vllm/model_executor/kernels/linear/base.py`


###

`from_layer(layer)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.FP8Params.from_layer)

Extract parameters from layer.

## Source code in `vllm/model_executor/kernels/linear/base.py`


##

`MMLinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel)

Bases:

, [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)[Generic](https://docs.python.org/3/library/typing.html#typing.Generic)[_ConfigT, _ParamsT]

Abstract base class for quantized matrix multiplication kernels.

This class provides the interface for implementing custom quantized linear layer kernels in vLLM. Subclasses should implement specific quantization strategies (e.g., FP8, INT8) and their corresponding compute kernels.

## Generic Type Parameters

_ConfigT: Configuration type for the kernel (subclass of MMLinearLayerConfig). Contains kernel-specific settings like quantization keys, dtypes, etc. _ParamsT: Parameter type for the kernel (subclass of Params). Defines the quantized weights and scales needed by the kernel.

## Typical Usage

- Define a config dataclass inheriting from MMLinearLayerConfig
- Define a params dataclass inheriting from Params
- Subclass MMLinearKernel with your config and params types
- Implement all abstract methods
- Register the kernel with the quantization method

## Example

@dataclass
class MyKernelConfig(MMLinearLayerConfig):
static: bool
output_dtype: torch.dtype
@dataclass
class MyKernelParams(FP8Params):
custom_scale: torch.Tensor
CUSTOM_SCALE: ClassVar[str] = "custom_scale"
class MyKernel(MMLinearKernel[MyKernelConfig, MyKernelParams]):
@classmethod
def is_supported(cls, compute_capability=None):
if compute_capability and compute_capability < 90:
return False, "Requires compute capability >= 9.0"
return True, None
@classmethod
def can_implement(cls, config):
if not config.static:
return False, "Only static quantization supported"
return True, None
def process_weights_after_loading(self, layer):
# Preprocess weights for the kernel
params = self._get_layer_params(layer)
processed = preprocess_weights(params.weight)
replace_parameter(layer, params.WEIGHT, processed)
def _get_layer_params(self, layer, **kwargs):
return MyKernelParams.from_layer(layer)
def apply_weights(self, layer, x, bias=None, **kwargs):
params = self._get_layer_params(layer)
# Call your custom kernel
output = my_custom_kernel(x, params.weight, params.weight_scale)
if bias is not None:
output += bias
return output


## Lifecycle

- Kernel selection: is_supported() and can_implement() check compatibility
- Initialization:
**init**() creates kernel instance with config - Weight loading: process_weights_after_loading() preprocesses weights
- Inference: apply_weights() executes the quantized matmul

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel.__init__)Initialize the kernel with the given configuration.

-
–[apply_weights](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel.apply_weights)Apply the quantized weights to the input tensor.

-
–[can_implement](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel.can_implement)Check if this kernel can implement the given configuration.

-
–[get_output_padding](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel.get_output_padding)Get the number of output tokens to pad for this kernel.

-
–[input_quant_key](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel.input_quant_key)Return the input quantization key supported by this kernel. If the kernel

-
–[is_supported](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel.is_supported)Check if this kernel is supported on the current hardware.

-
–[process_weights_after_loading](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel.process_weights_after_loading)Process and transform weights after loading from checkpoint.


## Source code in `vllm/model_executor/kernels/linear/base.py`


|
|

###

`__init__(config)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel.__init__)

Initialize the kernel with the given configuration.

Parameters:

-

(`config`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel.__init__(config))`_ConfigT`

) –Kernel-specific configuration containing settings like quantization keys, output dtypes, etc.


## Source code in `vllm/model_executor/kernels/linear/base.py`


###

`_get_layer_params(layer, **kwargs)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel._get_layer_params)

Extract typed parameters from the layer module.

This internal method retrieves the quantized weights and scales from the layer as a typed parameter object. Subclasses should typically delegate to ParamsClass.from_layer().

Parameters:

-

(`layer`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel._get_layer_params(layer))

) –[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)The layer module containing the parameters

-

(`**kwargs`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel._get_layer_params(**kwargs))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`{}`

) –Additional arguments


Returns:

-
`_ParamsT`

–A typed parameter object containing weights, scales, and other

-
`_ParamsT`

–quantization parameters


## Source code in `vllm/model_executor/kernels/linear/base.py`


###

`apply_weights(layer, x, bias=None, **kwargs)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel.apply_weights)

Apply the quantized weights to the input tensor.

This is the main inference method that performs the quantized matrix multiplication. It should handle input quantization (if needed), call the underlying kernel, and apply bias.

Parameters:

-

(`layer`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel.apply_weights(layer))

) –[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)The layer module containing the quantized weights

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel.apply_weights(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor of shape [..., in_features]

-

(`bias`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel.apply_weights(bias))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional bias tensor of shape [out_features]

-

(`**kwargs`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel.apply_weights(**kwargs))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`{}`

) –Additional kernel-specific arguments


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output tensor of shape [..., out_features]


## Source code in `vllm/model_executor/kernels/linear/base.py`


###

`can_implement(config)`

`abstractmethod`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel.can_implement)

Check if this kernel can implement the given configuration.

This method checks configuration-level compatibility (e.g., quantization scheme, group sizes, static vs dynamic quantization). It's called after is_supported() to determine if this kernel can handle the specific quantization configuration.

Parameters:

-

(`config`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel.can_implement(config))`_ConfigT`

) –The kernel configuration to check


Returns:

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[bool](https://docs.python.org/3/builtins/functions.html#bool),[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None]A tuple of (can_implement, reason): - can_implement: True if this kernel supports the config - reason: If not supported, a string explaining why; otherwise None


## Source code in `vllm/model_executor/kernels/linear/base.py`


###

`get_output_padding()`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel.get_output_padding)

Get the number of output tokens to pad for this kernel.

Some kernels require input padding for optimal performance. Override this method to specify padding requirements.

Returns:

-

–[int](https://docs.python.org/3/builtins/functions.html#int)| NoneNumber of tokens to pad, or None for no padding (default)


## Source code in `vllm/model_executor/kernels/linear/base.py`


###

`input_quant_key()`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel.input_quant_key)

Return the input quantization key supported by this kernel. If the kernel does not support input quantization outside of the kernel, return None.

###

`is_supported(compute_capability=None)`

`abstractmethod`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel.is_supported)

Check if this kernel is supported on the current hardware.

This method checks hardware-level compatibility (e.g., GPU architecture, compute capability, available instructions). It's called during kernel selection to filter out kernels that cannot run on the current device.

Parameters:

-

(`compute_capability`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel.is_supported(compute_capability))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –GPU compute capability (e.g., 80 for A100, 90 for H100). If None, should check the current device.


Returns:

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[bool](https://docs.python.org/3/builtins/functions.html#bool),[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None]A tuple of (is_supported, reason): - is_supported: True if the kernel can run on this hardware - reason: If not supported, a string explaining why; otherwise None


## Source code in `vllm/model_executor/kernels/linear/base.py`


###

`process_weights_after_loading(layer)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.MMLinearKernel.process_weights_after_loading)

Process and transform weights after loading from checkpoint.

This method is called once after weights are loaded but before inference. Use it to preprocess weights into the format required by your kernel (e.g., reordering, padding, format conversion).

Modifications should be done in-place using replace_parameter() to ensure the layer's parameters are properly updated.

Parameters:

## Example

## Source code in `vllm/model_executor/kernels/linear/base.py`


##

`Params`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.base.Params)

Base class for quantized layer parameters.

This class provides a typed interface for accessing quantized weights and scales from layer modules. It serves as a parameter container that can be extracted from layers and passed to kernel implementations.

Attributes:

-
(`weight`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The quantized weight tensor

-
(`weight_scale`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)weight scaling factors

-
(`input_scale`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NoneOptional input scaling factors


## Class Variables

WEIGHT: Attribute name for weight tensor on the layer module WEIGHT_SCALE: Attribute name for weight scale tensor on the layer module INPUT_SCALE: Attribute name for input scale tensor on the layer module

## Important

The string values of WEIGHT, WEIGHT_SCALE, and INPUT_SCALE class variables MUST match the attribute names used in the corresponding quantization method's create_weights() implementation. For example, if FP8LinearMethod.create_weights() sets layer.weight and layer.weight_scale, then WEIGHT="weight" and WEIGHT_SCALE="weight_scale" must be used here.