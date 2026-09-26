source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset14.random_uniform.html
lastmod: 

# openvino.runtime.opset14.random_uniform[#](https://docs.openvino.ai#openvino-runtime-opset14-random-uniform)

-
openvino.runtime.opset14.random_uniform(
*output_shape:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*min_val:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*max_val:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*output_type: str*,*global_seed: int = 0*,*op_seed: int = 0*,*alignment: str = 'tensorflow'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset14.random_uniform) Return a node which generates sequence of random values from uniform distribution.

- Parameters:
**output_shape**– Tensor with shape of the output tensor.**min_val**– Tensor with the lower bound on the range of random values to generate.**max_val**– Tensor with the upper bound on the range of random values to generate.**output_type**– Specifies the output tensor type, possible values: ‘i64’, ‘i32’, ‘f64’, ‘f32’, ‘f16’, ‘bf16’.**global_seed**– Specifies global seed value. Required to be a positive integer or 0.**op_seed**– Specifies operational seed value. Required to be a positive integer or 0.**alignment**– Specifies alignment of the randomly generated numbers to a given framework. Possible values: ‘tensorflow’, ‘pytorch’. Default is ‘tensorflow’.**name**– Optional output node name.

- Returns:
The new node which performs generation of random values from uniform distribution.