source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset12.nv12_to_bgr.html
lastmod: 

# openvino.runtime.opset12.nv12_to_bgr[#](https://docs.openvino.ai#openvino-runtime-opset12-nv12-to-bgr)

-
openvino.runtime.opset12.nv12_to_bgr(
*arg:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*arg_uv:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset12.nv12_to_bgr) Return a node which performs NV12toBGR operation.

- Parameters:
**arg**– The node providing single or Y plane data.**arg_uv**– The node providing UV plane data. Required for separate planes.**name**– The optional name for the created output node.

- Returns:
The new node performing NV12toBGR operation.