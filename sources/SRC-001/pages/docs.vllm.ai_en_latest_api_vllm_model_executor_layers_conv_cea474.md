source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/conv/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.conv`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.conv)

Conv Layer Class.

Classes:

-
–[Conv2dLayer](https://docs.vllm.ai#vllm.model_executor.layers.conv.Conv2dLayer)Conv layer with Conv2d.

-
–[Conv3dLayer](https://docs.vllm.ai#vllm.model_executor.layers.conv.Conv3dLayer)Conv layer with Conv3d.

-
–[ConvLayerBase](https://docs.vllm.ai#vllm.model_executor.layers.conv.ConvLayerBase)Conv layer base class.


##

`Conv2dLayer`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.conv.Conv2dLayer)

Bases: [ConvLayerBase](https://docs.vllm.ai#vllm.model_executor.layers.conv.ConvLayerBase)

Conv layer with Conv2d.

Methods:

-
–[forward_native](https://docs.vllm.ai#vllm.model_executor.layers.conv.Conv2dLayer.forward_native)Expected input shape: (batch_size, in_channels, height, width).


## Source code in `vllm/model_executor/layers/conv.py`


###

`forward_native(x)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.conv.Conv2dLayer.forward_native)

Expected input shape: (batch_size, in_channels, height, width).

## Source code in `vllm/model_executor/layers/conv.py`


##

`Conv3dLayer`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.conv.Conv3dLayer)

Bases: [ConvLayerBase](https://docs.vllm.ai#vllm.model_executor.layers.conv.ConvLayerBase)

Conv layer with Conv3d.

Methods:

-
–[forward_native](https://docs.vllm.ai#vllm.model_executor.layers.conv.Conv3dLayer.forward_native)Expected input shape: (batch_size, in_channels, time, height, width).


## Source code in `vllm/model_executor/layers/conv.py`


###

`forward_native(x)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.conv.Conv3dLayer.forward_native)

Expected input shape: (batch_size, in_channels, time, height, width).

##

`ConvLayerBase`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.conv.ConvLayerBase)

Bases: [CustomOp](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.CustomOp)

Conv layer base class.