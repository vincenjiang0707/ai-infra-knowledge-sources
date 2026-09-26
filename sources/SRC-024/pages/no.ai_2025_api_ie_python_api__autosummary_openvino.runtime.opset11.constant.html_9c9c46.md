source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.constant.html
lastmod: 

# openvino.runtime.opset11.constant[#](https://docs.openvino.ai#openvino-runtime-opset11-constant)

-
openvino.runtime.opset11.constant(
*value: int | float | ndarray | number | bool | bool | list*,*dtype: type | dtype |*,[Type](https://docs.openvino.ai/openvino.Type.html#openvino.Type)= None*name: str | None = None*)[Constant](https://docs.openvino.ai/openvino.runtime.op.Constant.html#openvino.runtime.op.Constant)[#](https://docs.openvino.ai#openvino.runtime.opset11.constant) Create a Constant node from provided value.

- Parameters:
**value**– One of: array of values or scalar to initialize node with.**dtype**– The data type of provided data.**name**– Optional name for output node.

- Returns:
The Constant node initialized with provided data.