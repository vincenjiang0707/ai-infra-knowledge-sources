source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset1.topk.html
lastmod: 

# openvino.runtime.opset1.topk[#](https://docs.openvino.ai#openvino-runtime-opset1-topk)

-
openvino.runtime.opset1.topk(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*k:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*axis: int*,*mode: str*,*sort: str*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset1.topk) Return a node which performs TopK.

- Parameters:
**data**– Input data.**k**–**axis**– TopK Axis.**mode**– Compute TopK largest (‘max’) or smallest (‘min’)**sort**– Order of output elements (sort by: ‘none’, ‘index’ or ‘value’)

- Returns:
The new node which performs TopK (both indices and values)