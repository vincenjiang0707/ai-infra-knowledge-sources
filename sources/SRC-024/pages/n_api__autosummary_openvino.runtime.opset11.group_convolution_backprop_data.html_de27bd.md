source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.group_convolution_backprop_data.html
lastmod: 

# openvino.runtime.opset11.group_convolution_backprop_data[#](https://docs.openvino.ai#openvino-runtime-opset11-group-convolution-backprop-data)

-
openvino.runtime.opset11.group_convolution_backprop_data(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*filters:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*strides: list[int]*,*output_shape:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*pads_begin: list[int] | None = None*,*pads_end: list[int] | None = None*,*dilations: list[int] | None = None*,*auto_pad: str = 'EXPLICIT'*,*output_padding: list[int] | None = None*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.group_convolution_backprop_data) Perform Group Convolution operation on data from input node.

- Parameters:
**data**– The node producing input data.**filters**– The node producing filter data.**strides**– The distance (in pixels) to slide the filter on the feature map over the axes.**output_shape**– The node that specifies spatial shape of the output.**pads_begin**– The number of pixels to add at the beginning along each axis.**pads_end**– The number of pixels to add at the end along each axis.**dilations**– The distance in width and height between elements (weights) in the filter.**auto_pad**–Describes how to perform padding. Possible values: EXPLICIT: Pad dimensions are explicity specified SAME_LOWER: Pad dimensions computed to match input shape Ceil(num_dims/2) at the beginning and Floor(num_dims/2) at the end

- SAME_UPPER: Pad dimensions computed to match input shape
Floor(num_dims/2) at the beginning and Ceil(num_dims/2) at the end


VALID: No padding

**output_padding**– The additional amount of paddings added per each spatial axis in the output tensor.**name**– Optional output node name.

- Returns:
The new node performing a Group Convolution operation on tensor from input node.