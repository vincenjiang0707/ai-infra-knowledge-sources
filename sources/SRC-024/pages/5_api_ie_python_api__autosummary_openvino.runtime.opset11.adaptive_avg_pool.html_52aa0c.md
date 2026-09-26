source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.adaptive_avg_pool.html
lastmod: 

# openvino.runtime.opset11.adaptive_avg_pool[#](https://docs.openvino.ai#openvino-runtime-opset11-adaptive-avg-pool)

-
openvino.runtime.opset11.adaptive_avg_pool(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*output_shape:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.adaptive_avg_pool) Return a node which performs AdaptiveAvgPool operation.

- Parameters:
**data**– The list of input nodes**output_shape**– the shape of spatial dimentions after operation**name**– Optional output node name.

- Returns:
The new node performing AdaptiveAvgPool operation on the data