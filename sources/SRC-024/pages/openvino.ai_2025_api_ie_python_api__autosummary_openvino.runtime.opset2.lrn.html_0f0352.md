source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset2.lrn.html
lastmod: 

# openvino.runtime.opset2.lrn[#](https://docs.openvino.ai#openvino-runtime-opset2-lrn)

-
openvino.runtime.opset2.lrn(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*axes:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*alpha: float = 1*,*beta: float = 0.5*,*bias: float = 1*,*size: int = 5*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset2.lrn) Return a node which performs element-wise Local Response Normalization (LRN) operation.

- Parameters:
**data**– Input data.**alpha**– A scale factor (usually positive).**beta**– An exponent.**bias**– An offset (usually positive) to avoid dividing by 0.**size**– Width of the 1-D normalization window.**name**– An optional name of the output node.

- Returns:
The new node which performs LRN.