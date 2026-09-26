source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.mvn.html
lastmod: 

# openvino.runtime.opset11.mvn[#](https://docs.openvino.ai#openvino-runtime-opset11-mvn)

-
openvino.runtime.opset11.mvn(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*axes:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*normalize_variance: bool*,*eps: float*,*eps_mode: str*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.mvn) Return a node which performs MeanVarianceNormalization (MVN).

- Parameters:
**data**– The node with data tensor.**axes**– The node with axes to reduce on.**normalize_variance**– Denotes whether to perform variance normalization.**eps**– The number added to the variance to avoid division by zero when normalizing the value. Scalar value.**eps_mode**– how eps is applied (inside_sqrt or outside_sqrt)**name**– Optional output node name.

- Returns:
The new node performing a MVN operation on input tensor.