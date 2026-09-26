source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset1.grn.html
lastmod: 

# openvino.runtime.opset1.grn[#](https://docs.openvino.ai#openvino-runtime-opset1-grn)

-
openvino.runtime.opset1.grn(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*bias: float*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset1.grn) Perform Global Response Normalization with L2 norm (across channels only).

Computes GRN operation on channels for input tensor:

f[ output_i = dfrac{input_i}{sqrt{sum_{i}^{C} input_i}} f]

- Parameters:
**data**– The node with data tensor.**bias**– The bias added to the variance. Scalar value.**name**– Optional output node name.

- Returns:
The new node performing a GRN operation on tensor’s channels.