source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset12.gather_nd.html
lastmod: 

# openvino.runtime.opset12.gather_nd[#](https://docs.openvino.ai#openvino-runtime-opset12-gather-nd)

-
openvino.runtime.opset12.gather_nd(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*indices:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*batch_dims: int | None = 0*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset12.gather_nd) Return a node which performs GatherND.

- Parameters:
**data**– N-D tensor with data for gathering**indices**– K-D tensor of tuples with indices by which data is gathered**batch_dims**– Scalar value of batch dimensions

- Returns:
The new node which performs GatherND