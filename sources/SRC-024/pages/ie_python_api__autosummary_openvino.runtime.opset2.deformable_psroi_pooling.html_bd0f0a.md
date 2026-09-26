source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.opset2.deformable_psroi_pooling.html
lastmod: 

# openvino.runtime.opset2.deformable_psroi_pooling[#](https://docs.openvino.ai#openvino-runtime-opset2-deformable-psroi-pooling)

-
openvino.runtime.opset2.deformable_psroi_pooling(
*feature_maps:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*coords:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray*output_dim: int*,*spatial_scale: float*,*group_size: int = 1*,*mode: str = 'bilinear_deformable'*,*spatial_bins_x: int = 1*,*spatial_bins_y: int = 1*,*trans_std: float = 1.0*,*part_size: int = 1*,*offsets:*,[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)| int | float | ndarray | None = None*name: str | None = None*)[Node](https://docs.openvino.ai/openvino.Node.html#openvino.Node)[#](https://docs.openvino.ai#openvino.runtime.opset2.deformable_psroi_pooling) Return node performing DeformablePSROIPooling operation.

DeformablePSROIPooling computes position-sensitive pooling on regions of interest specified by input.

- Parameters:
**feature_maps**– 4D tensor with feature maps.**coords**– 2D tensor describing box consisting of tuples: [batch_id, x_1, y_1, x_2, y_2].**output_dim**– A pooled output channel number.**spatial_scale**– A multiplicative spatial scale factor to translate ROI.**group_size**– The number of groups to encode position-sensitive score.**mode**– Specifies mode for pooling. Range of values: [‘bilinear_deformable’].**spatial_bins_x**– Specifies numbers of bins to divide the input feature maps over width.**spatial_bins_y**– Specifies numbers of bins to divide the input feature maps over height.**trans_std**– The value that all transformation (offset) values are multiplied with.**part_size**– The number of parts the output tensor spatial dimensions are divided into.**offsets**– Optional node. 4D input blob with transformation values (offsets).**name**– The optional new name for output node.

- Returns:
New node performing DeformablePSROIPooling operation.