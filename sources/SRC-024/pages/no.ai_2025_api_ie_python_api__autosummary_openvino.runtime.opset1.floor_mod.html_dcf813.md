source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset1.floor_mod.html
lastmod: 

# openvino.runtime.opset1.floor_mod[#](https://docs.openvino.ai#openvino-runtime-opset1-floor-mod)

-
openvino.runtime.opset1.floor_mod(
*left_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*right_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*auto_broadcast: str = 'NUMPY'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset1.floor_mod) Return node performing element-wise FloorMod (division reminder) with two given tensors.

- Parameters:
**left_node**– The first input node for FloorMod operation.**right_node**– The second input node for FloorMod operation.**auto_broadcast**– Specifies rules used for auto-broadcasting of input tensors.**name**– Optional name for output node.

- Returns:
The node performing element-wise FloorMod operation.