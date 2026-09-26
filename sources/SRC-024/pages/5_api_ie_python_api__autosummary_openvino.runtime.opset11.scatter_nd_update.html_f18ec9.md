source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.scatter_nd_update.html
lastmod: 

# openvino.runtime.opset11.scatter_nd_update[#](https://docs.openvino.ai#openvino-runtime-opset11-scatter-nd-update)

-
openvino.runtime.opset11.scatter_nd_update(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*indices:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*updates:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.scatter_nd_update) Return a node which performs ScatterNDUpdate.

- Parameters:
**data**– Node input representing the tensor to be updated.**indices**– Node input representing the indices at which updates will be applied.**updates**– Node input representing the updates to be applied.**name**– Optional name for the output node.

- Returns:
New node performing the ScatterNDUpdate.