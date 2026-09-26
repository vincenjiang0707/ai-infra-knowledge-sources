source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.fake_quantize.html
lastmod: 

# openvino.runtime.opset11.fake_quantize[#](https://docs.openvino.ai#openvino-runtime-opset11-fake-quantize)

-
openvino.runtime.opset11.fake_quantize(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*input_low:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*input_high:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*output_low:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*output_high:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*levels: int*,*auto_broadcast: str = 'NUMPY'*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.fake_quantize) Perform an element-wise linear quantization on input data.

- Parameters:
**data**– The node with data tensor.**input_low**– The node with the minimum for input values.**input_high**– The node with the maximum for input values.**output_low**– The node with the minimum quantized value.**output_high**– The node with the maximum quantized value.**levels**– The number of quantization levels. Integer value.**auto_broadcast**– The type of broadcasting specifies rules used for auto-broadcasting of input tensors.

- Returns:
New node with quantized value.


Input floating point values are quantized into a discrete set of floating point values.

if x <= input_low: output = output_low if x > input_high: output = output_high else: output = fake_quantize(output)

Fake quantize uses the following logic:

- f[ output =
dfrac{round( dfrac{data - input_low}{(input_high - input_low)cdot (levels-1)})} {(levels-1)cdot (output_high - output_low)} + output_low f]