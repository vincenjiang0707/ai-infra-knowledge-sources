source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_p_s_r_o_i_pooling.html
lastmod: 

# Class ov::op::v0::PSROIPooling[#](https://docs.openvino.ai#class-ov-op-v0-psroipooling)

-
class PSROIPooling : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012PSROIPoolingE) [PSROIPooling](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_p_s_r_o_i_pooling)operation.Public Functions

-
PSROIPooling(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &coords, const size_t output_dim, const size_t group_size, const float spatial_scale, int spatial_bins_x, int spatial_bins_y, const std::string &mode)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012PSROIPooling12PSROIPoolingERK6OutputI4NodeERK6OutputI4NodeEK6size_tK6size_tKfiiRKNSt6stringE) Constructs a

[PSROIPooling](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_p_s_r_o_i_pooling)operation.- Parameters:
**input**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)feature map {N, C, …}**coords**– Coordinates of bounding boxes**output_dim**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)channel number**group_size**– Number of groups to encode position-sensitive scores**spatial_scale**– Ratio of input feature map over input image size**spatial_bins_x**– Numbers of bins to divide the input feature maps over width**spatial_bins_y**– Numbers of bins to divide the input feature maps over height**mode**– Mode of pooling - Avg or Bilinear



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012PSROIPooling24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
void set_output_dim(size_t output_dim)
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012PSROIPooling14set_output_dimE6size_t) Set the output channel dimension size.

- Parameters:
**output_dim**– Channel dimension size.


-
void set_group_size(size_t group_size)
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012PSROIPooling14set_group_sizeE6size_t) Set the output groups number.

- Parameters:
**group_size**– Number of groups.


-
void set_spatial_scale(float scale)
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012PSROIPooling17set_spatial_scaleEf) Set the spatial scale.

- Parameters:
**scale**– Spatial scale value.


-
void set_spatial_bins_x(int x)
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012PSROIPooling18set_spatial_bins_xEi) Set the number of bins over image width.

- Parameters:
**x**– Number of bins over width (x) axis.


-
void set_spatial_bins_y(int y)
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012PSROIPooling18set_spatial_bins_yEi) Set the number of bins over image height.

- Parameters:
**y**– Number of bins over height (y) axis.


-
void set_mode(std::string mode)
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012PSROIPooling8set_modeENSt6stringE) Set the pooling mode.

- Parameters:
**mode**– Pooling mode name.


-
PSROIPooling(const