source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fusion/quant_activation/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fusion.quant_activation`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fusion.quant_activation)

A QuantizedActivation is a pre-quantized activation produced by a fused kernel and consumed directly by a linear layer, letting the layer skip its own input quantization. A linear advertises the key its kernel can consume via expose_input_quant_key; the kernel validates and reads the activation via as_quantized_activation. Producers query the effective capability through get_input_quant_key, which hides the key when another consumer branch needs the original activation.

Classes:

-
–[QuantizedActivation](https://docs.vllm.ai#vllm.model_executor.layers.fusion.quant_activation.QuantizedActivation)A quantized activation paired with its scale and original metadata.


Functions:

-
–[as_quantized_activation](https://docs.vllm.ai#vllm.model_executor.layers.fusion.quant_activation.as_quantized_activation)Validate and narrow a pre-quantized activation for a consumer kernel.

-
–[expose_input_quant_key](https://docs.vllm.ai#vllm.model_executor.layers.fusion.quant_activation.expose_input_quant_key)Store the kernel's pre-quantized input key on the layer, if any.

-
–[get_input_quant_key](https://docs.vllm.ai#vllm.model_executor.layers.fusion.quant_activation.get_input_quant_key)Return the pre-quantized input key the complete layer can consume.


##

`QuantizedActivation`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fusion.quant_activation.QuantizedActivation)

A quantized activation paired with its scale and original metadata.

The quant_key describes how data and scale are to be interpreted (dtype, scale granularity, value packing). Details the key does not capture, such as blockscale layout or activation padding, must follow the consumer kernel's convention.

TODO(mgoin): Encode layout and padding requirements in the contract so producers can match consumer kernels without relying on convention.

Methods:

-
–[weak_ref](https://docs.vllm.ai#vllm.model_executor.layers.fusion.quant_activation.QuantizedActivation.weak_ref)Return a copy with non-owning tensor references for CUDA graph replay.


## Source code in `vllm/model_executor/layers/fusion/quant_activation.py`


###

`weak_ref()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fusion.quant_activation.QuantizedActivation.weak_ref)

Return a copy with non-owning tensor references for CUDA graph replay.

## Source code in `vllm/model_executor/layers/fusion/quant_activation.py`


##

`as_quantized_activation(x, expected_key)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fusion.quant_activation.as_quantized_activation)

Validate and narrow a pre-quantized activation for a consumer kernel.

Returns the QuantizedActivation when x is one whose key matches the kernel's declared expected_key, and None when x is a plain tensor (the caller quantizes in-kernel). Raises on a key mismatch so a wrongly routed activation fails loudly instead of being silently re-quantized.

## Source code in `vllm/model_executor/layers/fusion/quant_activation.py`


##

`expose_input_quant_key(layer, kernel)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fusion.quant_activation.expose_input_quant_key)

Store the kernel's pre-quantized input key on the layer, if any.

This is the bridge from a kernel's input_quant_key() to the layer capability that fusion call sites read through get_input_quant_key. The raw key is left unset when the kernel quantizes its own input.

TODO(mgoin): Producers also need the consumer's quantization scales (e.g. static input scale, global scale). Expose those here as well so producers do not reach into kernel-specific layer attributes.

## Source code in `vllm/model_executor/layers/fusion/quant_activation.py`


##

`get_input_quant_key(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fusion.quant_activation.get_input_quant_key)

Return the pre-quantized input key the complete layer can consume.