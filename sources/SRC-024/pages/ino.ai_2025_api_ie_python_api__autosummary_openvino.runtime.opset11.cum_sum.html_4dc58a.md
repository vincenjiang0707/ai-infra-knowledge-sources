source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.cum_sum.html
lastmod: 

# openvino.runtime.opset11.cum_sum[#](https://docs.openvino.ai#openvino-runtime-opset11-cum-sum)

-
openvino.runtime.opset11.cum_sum(
*arg:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*axis:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*exclusive: bool = False*,*reverse: bool = False*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.cum_sum) Construct a cumulative summation operation.

- Parameters:
**arg**– The tensor to be summed.**axis**– zero dimension tensor specifying axis position along which sum will be performed.**exclusive**– if set to true, the top element is not included**reverse**– if set to true, will perform the sums in reverse direction

- Returns:
New node performing the operation