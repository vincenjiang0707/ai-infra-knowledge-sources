source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset10.broadcast.html
lastmod: 

# openvino.runtime.opset10.broadcast[#](https://docs.openvino.ai#openvino-runtime-opset10-broadcast)

-
openvino.runtime.opset10.broadcast(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*target_shape:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*axes_mapping:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*broadcast_spec: str = 'NUMPY'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset10.broadcast) Create a node which broadcasts the input node’s values along specified axes to a desired shape.

- Parameters:
**data**– The node with input tensor data.**target_shape**– The node with a new shape we want to broadcast tensor to.**axes_mapping**– The node with a axis positions (0-based) in the result that are being broadcast.**broadcast_spec**– The type of broadcasting that specifies mapping of input tensor axes to output shape axes. Range of values: NUMPY, EXPLICIT, BIDIRECTIONAL.**name**– Optional new name for output node.

- Returns:
New node with broadcast shape.