source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset11.extract_image_patches.html
lastmod: 

# openvino.runtime.opset11.extract_image_patches[#](https://docs.openvino.ai#openvino-runtime-opset11-extract-image-patches)

-
openvino.runtime.opset11.extract_image_patches(
*image:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*sizes: list[int]*,*strides: list[int]*,*rates: list[int]*,*auto_pad: str*,*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset11.extract_image_patches) Return a node which produces the ExtractImagePatches operation.

- Parameters:
**image**– 4-D Input data to extract image patches.**sizes**– Patch size in the format of [size_rows, size_cols].**strides**– Patch movement stride in the format of [stride_rows, stride_cols]**rates**– Element seleciton rate for creating a patch.**auto_pad**– Padding type.**name**– Optional name for output node.

- Returns:
ExtractImagePatches node