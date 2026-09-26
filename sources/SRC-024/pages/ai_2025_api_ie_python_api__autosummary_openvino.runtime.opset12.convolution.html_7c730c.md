source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset12.convolution.html
lastmod: 

# openvino.runtime.opset12.convolution[#](https://docs.openvino.ai#openvino-runtime-opset12-convolution)

-
openvino.runtime.opset12.convolution(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*filters:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*strides: list[int]*,*pads_begin: list[int]*,*pads_end: list[int]*,*dilations: list[int]*,*auto_pad: str = 'EXPLICIT'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset12.convolution) Return node performing batched convolution operation.

- Parameters:
**data**– The node providing data batch tensor.**filter**– The node providing filters tensor.**strides**– The kernel window movement strides.**pads_begin**– The number of zero padding elements to add on each axis below 0 coordinate.**pads_end**– The number of zero padding elements to add on each axis above max coordinate**dilations**– The data batch dilation strides.**auto_pad**– The type of padding. Range of values: explicit, same_upper, same_lower, valid.**name**– The optional new name for output node.

- Returns:
New node performing batched convolution operation.