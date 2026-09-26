source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.experimental.evaluate_both_bounds.html
lastmod: 

# openvino.experimental.evaluate_both_bounds[#](https://docs.openvino.ai#openvino-experimental-evaluate-both-bounds)

-
openvino.experimental.evaluate_both_bounds(
*output:*) tuple[[openvino._pyopenvino.Output](https://docs.openvino.ai/openvino.Output.html#openvino.Output)[openvino._pyopenvino.Tensor](https://docs.openvino.ai/openvino.Tensor.html#openvino.Tensor),[openvino._pyopenvino.Tensor](https://docs.openvino.ai/openvino.Tensor.html#openvino.Tensor)][#](https://docs.openvino.ai#openvino.experimental.evaluate_both_bounds) Evaluates lower and upper value estimations of the output tensor. It traverses the graph upwards to deduce the estimation.

- Parameters:
**output**() – Node output pointing to the tensor for estimation.*openvino.Output*- Returns:
Tensors representing the lower and upper bound value estimations.

- Return type:
tuple[

[openvino.Tensor](https://docs.openvino.ai/openvino.Tensor.html#openvino.Tensor),[openvino.Tensor](https://docs.openvino.ai/openvino.Tensor.html#openvino.Tensor)]