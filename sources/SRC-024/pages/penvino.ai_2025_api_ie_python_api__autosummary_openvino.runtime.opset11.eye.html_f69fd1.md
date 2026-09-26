source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.eye.html
lastmod: 

# openvino.runtime.opset11.eye[#](https://docs.openvino.ai#openvino-runtime-opset11-eye)

-
openvino.runtime.opset11.eye(
*num_rows:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*num_columns:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*diagonal_index:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*output_type: str*,*batch_shape:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.eye) Return a node which performs eye operation.

- Parameters:
**num_rows**– The node providing row number tensor.**num_columns**– The node providing column number tensor.**diagonal_index**– The node providing the index of the diagonal to be populated.**output_type**– Specifies the output tensor type, supports any numeric types.**batch_shape**– The node providing the leading batch dimensions of output shape. Optionally.**name**– The optional new name for output node.

- Returns:
New node performing deformable convolution operation.