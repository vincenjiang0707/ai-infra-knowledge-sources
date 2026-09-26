source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset12.parameter.html
lastmod: 

# openvino.runtime.opset12.parameter[#](https://docs.openvino.ai#openvino-runtime-opset12-parameter)

-
openvino.runtime.opset12.parameter(
*shape: list[int], dtype: type | ~numpy.dtype | ~openvino._pyopenvino.Type = <class 'numpy.float32'>, name: str | None = None*)[Parameter](https://docs.openvino.ai/openvino.runtime.op.Parameter.html#openvino.runtime.op.Parameter)[#](https://docs.openvino.ai#openvino.runtime.opset12.parameter) Return an openvino Parameter object.

- Parameters:
**shape**– The shape of the output tensor.**dtype**– The type of elements of the output tensor. Defaults to np.float32.**name**– The optional name for output new node.

- Returns:
The node that specifies input to the model.