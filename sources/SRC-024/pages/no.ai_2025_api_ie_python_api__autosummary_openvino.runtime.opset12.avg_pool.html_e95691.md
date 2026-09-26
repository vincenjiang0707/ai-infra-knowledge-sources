source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset12.avg_pool.html
lastmod: 

# openvino.runtime.opset12.avg_pool[#](https://docs.openvino.ai#openvino-runtime-opset12-avg-pool)

-
openvino.runtime.opset12.avg_pool(
*data_batch:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*strides: list[int]*,*pads_begin: list[int]*,*pads_end: list[int]*,*kernel_shape: list[int]*,*exclude_pad: bool*,*rounding_type: str = 'floor'*,*auto_pad: str | None = None*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset12.avg_pool) Return average pooling node.

- Parameters:
**data_batch**– The input node providing data.**strides**– The window movement strides.**pads_begin**– The input data optional padding below filled with zeros.**pads_end**– The input data optional padding below filled with zeros.**kernel_shape**– The pooling window shape.**exclude_pad**– Whether or not to include zero padding in average computations.**rounding_type**– Determines used rounding schema when computing output shape. Acceptable values are: [‘floor’, ‘ceil’]**auto_pad**– Determines how the padding is calculated. Acceptable values: [None, ‘same_upper’, ‘same_lower’, ‘valid’]**name**– Optional name for the new output node.

- Returns:
New node with AvgPool operation applied on its data.