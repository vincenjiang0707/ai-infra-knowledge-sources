source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset14.group_normalization.html
lastmod: 

# openvino.runtime.opset14.group_normalization[#](https://docs.openvino.ai#openvino-runtime-opset14-group-normalization)

-
openvino.runtime.opset14.group_normalization(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*scale:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*bias:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*num_groups: int*,*epsilon: float*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset14.group_normalization) Return a node which produces a GroupNormalization operation.

- Parameters:
**data**– The input tensor to be normalized.**scale**– The tensor containing the scale values for each channel.**bias**– The tensor containing the bias values for each channel.**num_groups**– Specifies the number of groups that the channel dimension will be divided into.**epsilon**– A very small value added to the variance for numerical stability. Ensures that division by zero does not occur for any normalized element.

- Returns:
GroupNormalization node