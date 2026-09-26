source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset10.batch_norm_inference.html
lastmod: 

# openvino.runtime.opset10.batch_norm_inference[#](https://docs.openvino.ai#openvino-runtime-opset10-batch-norm-inference)

-
openvino.runtime.opset10.batch_norm_inference(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*gamma:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*beta:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*mean:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*variance:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*epsilon: float*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset10.batch_norm_inference) Perform layer normalizes a input tensor by mean and variance with appling scale and offset.

- Parameters:
**data**– The input tensor with data for normalization.**gamma**– The scalar scaling for normalized value.**beta**– The bias added to the scaled normalized value.**mean**– The value for mean normalization.**variance**– The value for variance normalization.**epsilon**– The number to be added to the variance to avoid division by zero when normalizing a value.**name**– The optional name of the output node.

- Returns:
The new node which performs BatchNormInference.