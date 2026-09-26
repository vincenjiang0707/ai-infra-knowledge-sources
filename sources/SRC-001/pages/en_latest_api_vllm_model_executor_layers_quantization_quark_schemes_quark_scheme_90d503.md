source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/quark/schemes/quark_scheme/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.quantization.quark.schemes.quark_scheme`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.quark_scheme)

Classes:

-
–[QuarkScheme](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.quark_scheme.QuarkScheme)Abstract class used to describe the weight creation and forward pass


##

`QuarkScheme`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.quark_scheme.QuarkScheme)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Abstract class used to describe the weight creation and forward pass of different quantization schemes supported by Quark.

Methods:

-
–[apply_weights](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.quark_scheme.QuarkScheme.apply_weights)Run the forward pass for the particular scheme. This is where

-
–[create_weights](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.quark_scheme.QuarkScheme.create_weights)Weight creation for the particular scheme. Inputs to this function.

-
–[get_min_capability](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.quark_scheme.QuarkScheme.get_min_capability)Get minimum device capability.

-
–[process_weights_after_loading](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.quark_scheme.QuarkScheme.process_weights_after_loading)Called after weight loading is complete for any cleanup that


## Source code in `vllm/model_executor/layers/quantization/quark/schemes/quark_scheme.py`


###

`apply_weights(layer, x, bias)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.quark_scheme.QuarkScheme.apply_weights)

Run the forward pass for the particular scheme. This is where scheme-specific dequant/quant steps/kernels should be applied.

Parameters:

-

(`layer`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.quark_scheme.QuarkScheme.apply_weights(layer))

) –[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)torch.nn.Module with the registered weights and other parameters relevant to the particular scheme.

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.quark_scheme.QuarkScheme.apply_weights(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)input to the layer

-

(`bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.quark_scheme.QuarkScheme.apply_weights(bias))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| Nonebias parameter


## Source code in `vllm/model_executor/layers/quantization/quark/schemes/quark_scheme.py`


###

`create_weights(*args, **kwargs)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.quark_scheme.QuarkScheme.create_weights)

Weight creation for the particular scheme. Inputs to this function.

###

`get_min_capability()`

`abstractmethod`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.quark_scheme.QuarkScheme.get_min_capability)

###

`process_weights_after_loading(layer)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.quark.schemes.quark_scheme.QuarkScheme.process_weights_after_loading)

Called after weight loading is complete for any cleanup that needs to occur.