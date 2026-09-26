source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset1.max_pool.html
lastmod: 

# openvino.runtime.opset1.max_pool[#](https://docs.openvino.ai#openvino-runtime-opset1-max-pool)

-
openvino.runtime.opset1.max_pool(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*strides: list[int]*,*pads_begin: list[int]*,*pads_end: list[int]*,*kernel_shape: list[int]*,*rounding_type: str = 'floor'*,*auto_pad: str | None = None*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset1.max_pool) Perform max pooling operation with given parameters on provided data.

- Parameters:
**data**– The node providing input data.**strides**– The distance (in pixels) to slide the filter on the feature map over the axes.**pads_begin**– The number of pixels to add at the beginning along each axis.**pads_end**– The number of pixels to add at the end along each axis.**kernel_shape**– The pooling operation kernel shape.**rounding_type**– Determines used rounding schema when computing output shape. Acceptable values are: [‘floor’, ‘ceil’]**auto_pad**– Determines how the padding is calculated. Acceptable values: [None, ‘same_upper’, ‘same_lower’, ‘valid’]**name**– The optional name for the created output node.

- Returns:
The new node performing max pooling operation.