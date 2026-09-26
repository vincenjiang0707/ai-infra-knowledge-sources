source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.concat.html
lastmod: 

# openvino.runtime.opset11.concat[#](https://docs.openvino.ai#openvino-runtime-opset11-concat)

-
openvino.runtime.opset11.concat(
*nodes: list[*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray]*axis: int*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.concat) Concatenate input nodes into single new node along specified axis.

- Parameters:
**nodes**– The nodes we want concatenate into single new node.**axis**– The axis along which we want to concatenate input nodes.**name**– The optional new name for output node.

- Returns:
Return new node that is a concatenation of input nodes.