source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset1.binary_convolution.html
lastmod: 

# openvino.runtime.opset1.binary_convolution[#](https://docs.openvino.ai#openvino-runtime-opset1-binary-convolution)

-
openvino.runtime.opset1.binary_convolution(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*filters:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*strides: list[int]*,*pads_begin: list[int]*,*pads_end: list[int]*,*dilations: list[int]*,*mode: str*,*pad_value: float*,*auto_pad: str = 'EXPLICIT'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset1.binary_convolution) Create node performing convolution with binary weights, binary input and integer output.

- Parameters:
**data**– The node providing data batch tensor.**filter**– The node providing filters tensor.**strides**– The kernel window movement strides.**pads_begin**– The number of pixels to add to the beginning along each axis.**pads_end**– The number of pixels to add to the end along each axis.**dilations**– The distance in width and height between elements (weights) in the filter.**mode**– Defines how input tensor 0/1 values and weights 0/1 are interpreted.**pad_value**– Floating-point value used to fill pad area.**auto_pad**– The type of padding. Range of values: explicit, same_upper, same_lower, valid.**name**– The optional new name for output node.

- Returns:
New node performing binary convolution operation.