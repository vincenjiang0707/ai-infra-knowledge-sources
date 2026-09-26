source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.squared_difference.html
lastmod: 

# openvino.runtime.opset11.squared_difference[#](https://docs.openvino.ai#openvino-runtime-opset11-squared-difference)

-
openvino.runtime.opset11.squared_difference(
*x1:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*x2:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*auto_broadcast: str = 'NUMPY'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.squared_difference) Perform an element-wise squared difference between two tensors.

f[ y[i] = (x_1[i] - x_2[i])^2 f]

- Parameters:
**x1**– The node with first input tensor.**x2**– The node with second input tensor.**auto_broadcast**– The type of broadcasting that specifies mapping of input tensor axes to output shape axes. Range of values: numpy, explicit.**name**– Optional new name for output node.

- Returns:
The new node performing a squared difference between two tensors.