source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset14.normalize_l2.html
lastmod: 

# openvino.runtime.opset14.normalize_l2[#](https://docs.openvino.ai#openvino-runtime-opset14-normalize-l2)

-
openvino.runtime.opset14.normalize_l2(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*axes:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*eps: float*,*eps_mode: str*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset14.normalize_l2) Construct an NormalizeL2 operation.

- Parameters:
**data**– Node producing the input tensor**axes**– Node indicating axes along which L2 reduction is calculated**eps**– The epsilon added to L2 norm**eps_mode**– how eps is combined with L2 value (add or max)

- Returns:
New node which performs the L2 normalization.