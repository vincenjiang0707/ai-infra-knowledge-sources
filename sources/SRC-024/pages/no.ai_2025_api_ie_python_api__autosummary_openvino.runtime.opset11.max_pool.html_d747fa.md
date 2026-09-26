source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.max_pool.html
lastmod: 

# openvino.runtime.opset11.max_pool[#](https://docs.openvino.ai#openvino-runtime-opset11-max-pool)

-
openvino.runtime.opset11.max_pool(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*strides: list[int]*,*dilations: list[int]*,*pads_begin: list[int]*,*pads_end: list[int]*,*kernel_shape: list[int]*,*rounding_type: str = 'floor'*,*auto_pad: str | None = None*,*index_element_type: str | None = 'i64'*,*axis: int | None = 0*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.max_pool) Perform max pooling operation and return both values and indices of the selected elements.

- Parameters:
**data**– The node providing input data.**strides**– The distance (in pixels) to slide the filter on the feature map over the axes.**dilations**– The dilation of filter elements(distance between elements).**pads_begin**– The number of pixels to add at the beginning along each axis.**pads_end**– The number of pixels to add at the end along each axis.**kernel_shape**– The pooling operation kernel shape.**rounding_type**– Determines used rounding schema when computing output shape. Acceptable values are: [‘floor’, ‘ceil’]. Defaults to ‘floor’.**auto_pad**– Determines how the padding is calculated. Acceptable values: [None, ‘same_upper’, ‘same_lower’, ‘valid’]. Defaults to None.**index_element_type**– The data type used for the indices output of this operator. Defaults to i64.**axis**– The first dimension in the data shape used to determine the maximum returned index value. The value is the product of all dimensions starting at the provided axis. Defaults to 0.**name**– The optional name for the created output node.

- Returns:
The new node performing max pooling operation.