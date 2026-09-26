source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset14.convert_promote_types.html
lastmod: 

# openvino.runtime.opset14.convert_promote_types[#](https://docs.openvino.ai#openvino-runtime-opset14-convert-promote-types)

-
openvino.runtime.opset14.convert_promote_types(
*left_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*right_node:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*promote_unsafe: bool = False*,*pytorch_scalar_promotion: bool = False*,*u64_integer_promotion_target: str |*,[Type](https://docs.openvino.ai/openvino.Type.html#openvino.Type)= 'f32'*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset14.convert_promote_types) Return a node performing conversion to common type based on promotion rules.

- Parameters:
**left_node**– input node with type to be promoted to common one.**right_node**– input node with type to be promoted to common one.**promote_unsafe**– Bool attribute whether to allow promotions that might result in bit-widening, precision loss and undefined behaviors.**pytorch_scalar_promotion**– Bool attribute whether to promote scalar input to type provided by non-scalar input when number format is matching.**u64_integer_promotion_target**– Element type attribute to select promotion result when inputs are u64 and signed integer.**name**– Optional name for the new output node.

- Returns:
The new node performing ConvertPromoteTypes operation.