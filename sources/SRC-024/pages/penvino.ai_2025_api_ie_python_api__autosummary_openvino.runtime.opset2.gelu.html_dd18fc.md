source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset2.gelu.html
lastmod: 

# openvino.runtime.opset2.gelu[#](https://docs.openvino.ai#openvino-runtime-opset2-gelu)

-
openvino.runtime.opset2.gelu(
*node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset2.gelu) Perform Gaussian Error Linear Unit operation element-wise on data from input node.

Computes GELU function:

f[ f(x) = 0.5cdot xcdot(1 + erf( dfrac{x}{sqrt{2}}) f]

For more information refer to [Gaussian Error Linear Unit (GELU)](

[https://arxiv.org/pdf/1606.08415.pdf](https://arxiv.org/pdf/1606.08415.pdf)>)- Parameters:
**node**– Input tensor. One of: input node, array or scalar.**name**– Optional output node name.

- Returns:
The new node performing a GELU operation on its input data element-wise.