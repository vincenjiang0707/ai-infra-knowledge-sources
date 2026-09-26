source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.adaptive_max_pool.html
lastmod: 

# openvino.runtime.opset11.adaptive_max_pool[#](https://docs.openvino.ai#openvino-runtime-opset11-adaptive-max-pool)

-
openvino.runtime.opset11.adaptive_max_pool(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*output_shape:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*index_element_type: str = 'i64'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.adaptive_max_pool) Return a node which performs AdaptiveMaxPool operation.

- Parameters:
**data**– The list of input nodes**output_shape**– the shape of spatial dimentions after operation**index_element_type**– Type of indices output.**name**– Optional output node name.

- Returns:
The new node performing AdaptiveMaxPool operation on the data