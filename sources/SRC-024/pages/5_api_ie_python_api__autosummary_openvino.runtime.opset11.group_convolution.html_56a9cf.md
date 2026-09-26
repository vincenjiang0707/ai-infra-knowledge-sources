source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.group_convolution.html
lastmod: 

# openvino.runtime.opset11.group_convolution[#](https://docs.openvino.ai#openvino-runtime-opset11-group-convolution)

-
openvino.runtime.opset11.group_convolution(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*filters:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*strides: list[int]*,*pads_begin: list[int]*,*pads_end: list[int]*,*dilations: list[int]*,*auto_pad: str = 'EXPLICIT'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.group_convolution) Perform Group Convolution operation on data from input node.

- Parameters:
**data**– The node producing input data.**filters**– The node producing filters data.**strides**– The distance (in pixels) to slide the filter on the feature map over the axes.**pads_begin**– The number of pixels to add at the beginning along each axis.**pads_end**– The number of pixels to add at the end along each axis.**dilations**– The distance in width and height between elements (weights) in the filter.**auto_pad**–Describes how to perform padding. Possible values: EXPLICIT: Pad dimensions are explicity specified SAME_LOWER: Pad dimensions computed to match input shape Ceil(num_dims/2) at the beginning and Floor(num_dims/2) at the end

- SAME_UPPER: Pad dimensions computed to match input shape
Floor(num_dims/2) at the beginning and Ceil(num_dims/2) at the end


VALID: No padding

**name**– Optional output node name.

- Returns:
The new node performing a Group Convolution operation on tensor from input node.