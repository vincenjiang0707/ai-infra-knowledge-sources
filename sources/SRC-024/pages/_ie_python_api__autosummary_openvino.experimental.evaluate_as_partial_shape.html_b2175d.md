source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.experimental.evaluate_as_partial_shape.html
lastmod: 

# openvino.experimental.evaluate_as_partial_shape[#](https://docs.openvino.ai#openvino-experimental-evaluate-as-partial-shape)

-
openvino.experimental.evaluate_as_partial_shape(
*output:*,[openvino._pyopenvino.Output](https://docs.openvino.ai/openvino.Output.html#openvino.Output)*partial_shape:*) bool[openvino._pyopenvino.PartialShape](https://docs.openvino.ai/openvino.PartialShape.html#openvino.PartialShape)[#](https://docs.openvino.ai#openvino.experimental.evaluate_as_partial_shape) Evaluates lower and upper value estimations for the output tensor. The estimation will be represented as a partial shape object, using Dimension(min, max) for each element.

- Parameters:
**output**() – Node output pointing to the tensor for estimation.*openvino.Output***partial_shape**() – The resulting estimation will be stored in this PartialShape.*openvino.PartialShape*

- Returns:
True if estimation evaluation was successful, false otherwise.

- Return type:
bool