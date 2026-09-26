source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset15.stft.html
lastmod: 

# openvino.runtime.opset15.stft[#](https://docs.openvino.ai#openvino-runtime-opset15-stft)

-
openvino.runtime.opset15.stft(
*data:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*window:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*frame_size:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*frame_step:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*transpose_frames: bool*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset15.stft) Return a node which generates STFT operation.

- Parameters:
**data**– The node providing input data.**window**– The node providing window data.**frame_size**– The node with scalar value representing the size of Fourier Transform.**frame_step**– The distance (number of samples) between successive window frames.**transpose_frames**– Flag to set output shape layout. If true the frames dimension is at out_shape[2], otherwise it is at out_shape[1].**name**– The optional name for the created output node.

- Returns:
The new node performing STFT operation.