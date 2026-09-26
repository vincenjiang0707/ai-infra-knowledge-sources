source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset14.elu.html
lastmod: 

# openvino.runtime.opset14.elu[#](https://docs.openvino.ai#openvino-runtime-opset14-elu)

-
openvino.runtime.opset14.elu(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*alpha: type | dtype*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset14.elu) Perform Exponential Linear Unit operation element-wise on data from input node.

Computes exponential linear: alpha * (exp(data) - 1) if < 0, data otherwise.

For more information refer to: [Fast and Accurate Deep Network Learning by Exponential Linear Units](

[http://arxiv.org/abs/1511.07289](http://arxiv.org/abs/1511.07289))- Parameters:
**data**– Input tensor. One of: input node, array or scalar.**alpha**– Scalar multiplier for negative values.**name**– Optional output node name.

- Returns:
The new node performing an ELU operation on its input data element-wise.