source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset10.gather_elements.html
lastmod: 

# openvino.runtime.opset10.gather_elements[#](https://docs.openvino.ai#openvino-runtime-opset10-gather-elements)

-
openvino.runtime.opset10.gather_elements(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*indices:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*axis: int | None = 0*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset10.gather_elements) Return a node which performs GatherElements.

- Parameters:
**data**– N-D tensor with data for gathering**indices**– N-D tensor with indices by which data is gathered**axis**– axis along which elements are gathered

- Returns:
The new node which performs GatherElements