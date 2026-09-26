source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset1.deformable_convolution.html
lastmod: 

# openvino.runtime.opset1.deformable_convolution[#](https://docs.openvino.ai#openvino-runtime-opset1-deformable-convolution)

-
openvino.runtime.opset1.deformable_convolution(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*deformable_values:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*filters:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*strides: list[int]*,*pads_begin: list[int]*,*pads_end: list[int]*,*dilations: list[int]*,*auto_pad: str = 'EXPLICIT'*,*group: int = 1*,*deformable_group: int = 1*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset1.deformable_convolution) Create node performing deformable convolution.

- Parameters:
**data**– The node providing data batch tensor.**filter**– The node providing filters tensor.**strides**– The distance (in pixels) to slide the filter on the feature map over the axes.**pads_begin**– The number of pixels to add to the beginning along each axis.**pads_end**– The number of pixels to add to the end along each axis.**dilations**– The distance in width and height between elements (weights) in the filter.**auto_pad**– The type of padding. Range of values: explicit, same_upper, same_lower, valid.**group**– The number of groups which both output and input should be split into.**deformable_group**– The number of groups which deformable values and output should be split into along the channel axis.**name**– The optional new name for output node.

- Returns:
New node performing deformable convolution operation.