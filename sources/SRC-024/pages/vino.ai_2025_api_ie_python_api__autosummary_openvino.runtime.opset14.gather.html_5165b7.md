source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset14.gather.html
lastmod: 

# openvino.runtime.opset14.gather[#](https://docs.openvino.ai#openvino-runtime-opset14-gather)

-
openvino.runtime.opset14.gather(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*indices:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*axis:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*batch_dims: int | None = 0*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset14.gather) Return a node which performs Gather with support of negative indices.

- Parameters:
**data**– N-D tensor with data for gathering**indices**– N-D tensor with indices by which data is gathered. Negative indices indicate reverse indexing from the end**axis**– axis along which elements are gathered**batch_dims**– number of batch dimensions**name**– Optional output node name.

- Returns:
The new node which performs Gather