source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.unique.html
lastmod: 

# openvino.runtime.opset11.unique[#](https://docs.openvino.ai#openvino-runtime-opset11-unique)

-
openvino.runtime.opset11.unique(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*axis:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*sorted: bool | None = True*,*index_element_type: str | None = 'i64'*,*count_element_type: str | None = 'i64'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.unique) Operator which selects and returns unique elements or unique slices of the input tensor.

- Parameters:
**data**– Input data tensor.**axis**– (Optional) An input tensor containing the axis value. If not provided or None, data input is considered as a flattened tensor. Default value: None.**sorted**– (Optional) Controls the order of the returned unique values, sorts ascendingly when true. Default value: True.**index_element_type**– (Optional) The data type set for outputs containing indices. Default value: “i64”.**count_element_type**– (Optional) The data type set for the output with repetition count. Default value: “i64”.**name**– (Optional) A name for the output node. Default value: None.

- Returns:
Node representing Unique operation.