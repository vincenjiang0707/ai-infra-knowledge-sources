source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset1.pad.html
lastmod: 

# openvino.runtime.opset1.pad[#](https://docs.openvino.ai#openvino-runtime-opset1-pad)

-
openvino.runtime.opset1.pad(
*arg:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*pads_begin:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*pads_end:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*pad_mode: str*,*arg_pad_value:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset1.pad) Return a generic padding operation.

- Parameters:
**arg**– The node producing input tensor to be padded.**pads_begin**– number of padding elements to be added before position 0 on each axis of arg.**pads_end**– number of padding elements to be added after the last element.**pad_mode**– “constant”, “edge”, “reflect” or “symmetric”**arg_pad_value**– value used for padding if pad_mode is “constant”

- Returns:
Pad operation node.