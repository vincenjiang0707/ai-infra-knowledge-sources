source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset10.one_hot.html
lastmod: 

# openvino.runtime.opset10.one_hot[#](https://docs.openvino.ai#openvino-runtime-opset10-one-hot)

-
openvino.runtime.opset10.one_hot(
*indices:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*depth:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*on_value:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*off_value:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*axis: int*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset10.one_hot) Create node performing one-hot encoding on input data.

- Parameters:
**indices**– Input tensor of rank N with indices of any supported integer data type.**depth**– Scalar of any supported integer type that specifies number of classes and the size of one-hot dimension.**on_value**– Scalar of any type that is the value that the locations in output tensor represented by indices in input take.**off_value**– Scalar of any type that is the value that the locations not represented by indices in input take.**name**– The optional name for new output node.

- Returns:
New node performing one-hot operation.