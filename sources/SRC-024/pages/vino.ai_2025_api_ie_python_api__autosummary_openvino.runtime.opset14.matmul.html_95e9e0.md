source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset14.matmul.html
lastmod: 

# openvino.runtime.opset14.matmul[#](https://docs.openvino.ai#openvino-runtime-opset14-matmul)

-
openvino.runtime.opset14.matmul(
*data_a:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*data_b:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*transpose_a: bool*,*transpose_b: bool*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset14.matmul) Return the Matrix Multiplication operation.

- Parameters:
**data_a**– left-hand side matrix**data_b**– right-hand side matrix**transpose_a**– should the first matrix be transposed before operation**transpose_b**– should the second matrix be transposed

- Returns:
MatMul operation node