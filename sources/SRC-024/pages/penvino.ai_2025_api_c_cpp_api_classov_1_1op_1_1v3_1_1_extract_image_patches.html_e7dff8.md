source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v3_1_1_extract_image_patches.html
lastmod: 

# Class ov::op::v3::ExtractImagePatches[#](https://docs.openvino.ai#class-ov-op-v3-extractimagepatches)

-
class ExtractImagePatches : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v319ExtractImagePatchesE) [ExtractImagePatches](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_extract_image_patches)operation.Public Functions

-
ExtractImagePatches(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &image, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&sizes, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&rates, const[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)&auto_pad)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v319ExtractImagePatches19ExtractImagePatchesERK6OutputI4NodeERK5ShapeRK7StridesRK5ShapeRK7PadType) Constructs a

[ExtractImagePatches](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_extract_image_patches)operation.- Parameters:
**data**– 4-D[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)data to extract image patches**sizes**– Patch size in the format of [size_rows, size_cols]**strides**– Patch movement stride in the format of [stride_rows, stride_cols]**rates**– Element seleciton rate for creating a patch. in the format of [rate_rows, rate_cols]**auto_pad**– Padding type. it can be any value from valid, same_lower, same_upper



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v319ExtractImagePatches24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
ExtractImagePatches(const