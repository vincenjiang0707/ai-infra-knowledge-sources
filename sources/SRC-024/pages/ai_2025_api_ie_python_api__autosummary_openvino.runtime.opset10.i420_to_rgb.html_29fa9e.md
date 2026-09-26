source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset10.i420_to_rgb.html
lastmod: 

# openvino.runtime.opset10.i420_to_rgb[#](https://docs.openvino.ai#openvino-runtime-opset10-i420-to-rgb)

-
openvino.runtime.opset10.i420_to_rgb(
*arg:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*arg_u:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*arg_v:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset10.i420_to_rgb) Return a node which performs I420toRGB operation.

- Parameters:
**arg**– The node providing single or Y plane data.**arg_u**– The node providing U plane data. Required for separate planes.**arg_v**– The node providing V plane data. Required for separate planes.**name**– The optional name for the created output node.

- Returns:
The new node performing I420toRGB operation.