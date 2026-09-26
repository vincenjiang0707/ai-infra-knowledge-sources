source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.clamp.html
lastmod: 

# openvino.runtime.opset11.clamp[#](https://docs.openvino.ai#openvino-runtime-opset11-clamp)

-
openvino.runtime.opset11.clamp(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*min_value: int | float*,*max_value: int | float*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.clamp) Perform clamp element-wise on data from input node.

- Parameters:
**data**– Input tensor. One of: input node, array or scalar.**min_value**– The lower bound of the <min_value;max_value> range. Scalar value.**max_value**– The upper bound of the <min_value;max_value> range. Scalar value.**name**– Optional output node name.

- Returns:
The new node performing a clamp operation on its input data element-wise.


Performs a clipping operation on an input value between a pair of boundary values.

For each element in data, if the element’s value is lower than min_value, it will be replaced with min_value. If the value is higher than max_value, it will be replaced by max_value. Intermediate values of data are returned without change.

Clamp uses the following logic:

if data < min_value: data=min_value elif data > max_value: data=max_value