source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset10.tile.html
lastmod: 

# openvino.runtime.opset10.tile[#](https://docs.openvino.ai#openvino-runtime-opset10-tile)

-
openvino.runtime.opset10.tile(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*repeats:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset10.tile) Return a node which dynamically repeats(replicates) the input data tensor.

- Parameters:
**data**– The input tensor to be tiled**repeats**– Per-dimension replication factors

- Returns:
Tile node