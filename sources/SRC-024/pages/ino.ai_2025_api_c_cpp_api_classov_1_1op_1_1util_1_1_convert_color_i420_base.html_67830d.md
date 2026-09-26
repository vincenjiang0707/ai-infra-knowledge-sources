source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_convert_color_i420_base.html
lastmod: 

# Class ov::op::util::ConvertColorI420Base[#](https://docs.openvino.ai#class-ov-op-util-convertcolori420base)

-
class ConvertColorI420Base : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util20ConvertColorI420BaseE) Base class for color conversion operation from I420 to RGB/BGR format.

[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input):Operation expects input shape in NHWC layout.

[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)NV12 image can be represented in a two ways: a) Single plane: NV12 height dimension is 1.5x bigger than image height. ‘C’ dimension shall be 1 b) Three separate planes: Y, U and V. In this case b1) Y plane has height same as image height. ‘C’ dimension equals to 1 b2) U plane has dimensions: ‘H’ = image_h / 2; ‘W’ = image_w / 2; ‘C’ = 1. b3) V plane has dimensions: ‘H’ = image_h / 2; ‘W’ = image_w / 2; ‘C’ = 1.Supported element types: u8 or any supported floating-point type.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output):[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)node will have NHWC layout and shape HxW same as image spatial dimensions.Number of output channels ‘C’ will be 3

Conversion of each pixel from I420 (YUV) to RGB space is represented by following formulas: R = 1.164 * (Y - 16) + 1.596 * (V - 128) G = 1.164 * (Y - 16) - 0.813 * (V - 128) - 0.391 * (U - 128) B = 1.164 * (Y - 16) + 2.018 * (U - 128) Then R, G, B values are clipped to range (0, 255)


Subclassed by

[ov::op::v8::I420toBGR](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_i420to_b_g_r),[ov::op::v8::I420toRGB](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_i420to_r_g_b)Public Types

Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util20ConvertColorI420Base24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.