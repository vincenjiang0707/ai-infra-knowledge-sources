source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_r_o_i_pooling.html
lastmod: 

# Class ov::op::v0::ROIPooling[#](https://docs.openvino.ai#class-ov-op-v0-roipooling)

-
class ROIPooling : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v010ROIPoolingE) [ROIPooling](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_r_o_i_pooling)operation.Public Functions

-
ROIPooling(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &coords, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&output_size, const float spatial_scale, const std::string &method = "max")[#](https://docs.openvino.ai#_CPPv4N2ov2op2v010ROIPooling10ROIPoolingERK6OutputI4NodeERK6OutputI4NodeERK5ShapeKfRKNSt6stringE) Constructs a

[ROIPooling](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_r_o_i_pooling)operation.- Parameters:
**input**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)feature map {N, C, H, W}**coords**– Coordinates of bounding boxes**output_size**– Height/Width of ROI output features**spatial_scale**– Ratio of input feature map over input image size**method**– Method of pooling - Max or Bilinear



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v010ROIPooling24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
void set_output_roi(
[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)output_size)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v010ROIPooling14set_output_roiE5Shape) Set the output ROI feature map (pooled_h, pooled_w).

- Parameters:
**output_size**–[Shape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_shape)with pooling attributes pooled_h and pooled_w sizes.


-
const
[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&get_output_roi() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v010ROIPooling14get_output_roiEv) Get the output ROI feature map shape (H x W)

- Returns:
[Shape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_shape)with pooled_h and pooled_w attributes.


-
void set_spatial_scale(float scale)
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v010ROIPooling17set_spatial_scaleEf) Set the spatial scale value.

- Parameters:
**scale**– Scale value to set.


-
void set_method(std::string method_name)
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v010ROIPooling10set_methodENSt6stringE) Set the method of pooling.

- Parameters:
**method_name**– Pooling method name.


-
ROIPooling(const