source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v8_1_1_n_v12to_r_g_b.html
lastmod: 

# Class ov::op::v8::NV12toRGB[#](https://docs.openvino.ai#class-ov-op-v8-nv12torgb)

-
class NV12toRGB : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ConvertColorNV12Base](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_convert_color_n_v12_base.html#_CPPv4N2ov2op4util20ConvertColorNV12BaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v89NV12toRGBE) Color conversion operation from NV12 to RGB format.

[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input):[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)NV12 image can be represented in two ways: a) Single plane (as it is in the file): NV12 height dimension is 1.5x bigger than image height. ‘C’ dimension shall be 1. b) Two separate planes (used this way in many physical video sources): Y and UV. In this case b1) Y plane has height same as image height. ‘C’ dimension equals to 1 b2) UV plane has dimensions: ‘H’ = image_h / 2; ‘W’ = image_w / 2; ‘C’ = 2.Supported element types: u8 or any supported floating-point type.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output):[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)node will have NHWC layout and shape HxW same as image spatial dimensions.Number of output channels ‘C’ will be 3, as per interleaved RGB format, first channel is R, last is B

Conversion of each pixel from NV12 (YUV) to RGB space is represented by following formulas: R = 1.164 * (Y - 16) + 1.596 * (V - 128) G = 1.164 * (Y - 16) - 0.813 * (V - 128) - 0.391 * (U - 128) B = 1.164 * (Y - 16) + 2.018 * (U - 128) Then R, G, B values are clipped to range (0, 255)


Public Functions

-
explicit NV12toRGB(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v89NV12toRGB9NV12toRGBERK6OutputI4NodeE) Constructs a conversion operation from input image in NV12 format As per NV12 format definition, node height dimension shall be 1.5 times bigger than image height so that image (w=640, h=480) is represented by NHWC shape {N,720,640,1} (height*1.5 x width)


-
NV12toRGB(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg_y, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg_uv)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v89NV12toRGB9NV12toRGBERK6OutputI4NodeERK6OutputI4NodeE) Constructs a conversion operation from 2-plane input image in NV12 format In general case Y channel of image can be separated from UV channel which means that operation needs two nodes for Y and UV planes respectively. Y plane has one channel, and UV has 2 channels, both expect ‘NHWC’ layout.

- Parameters:
**arg_y**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor for Y plane (NHWC layout). Shall have WxH dimensions equal to image dimensions. ‘C’ dimension equals to 1.**arg_uv**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor for UV plane (NHWC layout). ‘H’ is half of image height, ‘W’ is half of image width, ‘C’ dimension equals to 2. Channel 0 represents ‘U’, channel 1 represents ‘V’ channel