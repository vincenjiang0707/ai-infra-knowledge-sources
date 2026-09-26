source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset13.bucketize.html
lastmod: 

# openvino.runtime.opset13.bucketize[#](https://docs.openvino.ai#openvino-runtime-opset13-bucketize)

-
openvino.runtime.opset13.bucketize(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)*buckets:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*output_type: str = 'i64'*,*with_right_bound: bool = True*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset13.bucketize) Return a node which produces the Bucketize operation.

- Parameters:
**data**– Input data to bucketize**buckets**– 1-D of sorted unique boundaries for buckets**output_type**– Output tensor type, “i64” or “i32”, defaults to i64**with_right_bound**– indicates whether bucket includes the right or left edge of interval. default true = includes right edge**name**– Optional name for output node.

- Returns:
Bucketize node