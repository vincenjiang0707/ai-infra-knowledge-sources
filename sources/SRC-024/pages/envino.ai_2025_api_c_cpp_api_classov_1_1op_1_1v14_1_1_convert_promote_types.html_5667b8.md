source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v14_1_1_convert_promote_types.html
lastmod: 

# Class ov::op::v14::ConvertPromoteTypes[#](https://docs.openvino.ai#class-ov-op-v14-convertpromotetypes)

-
class ConvertPromoteTypes : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1419ConvertPromoteTypesE) Elementwise operation that promote and convert input types to one common datatype.

Public Functions

-
ConvertPromoteTypes() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1419ConvertPromoteTypes19ConvertPromoteTypesEv) Constructs operation that promote and convert input types to one common datatype.


-
ConvertPromoteTypes(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input_0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input_1, const bool promote_unsafe = false, const bool pytorch_scalar_promotion = false, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&u64_integer_promotion_target =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[f32](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3f32EN6Type_t3f32E))[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1419ConvertPromoteTypes19ConvertPromoteTypesERK6OutputI4NodeERK6OutputI4NodeEKbKbRKN7element4TypeE) Constructs operation that promote and convert input types to one common datatype.

- Parameters:
**input_0**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)with datatype to be promoted.**input_1**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)with datatype to be promoted.**promote_unsafe**– Bool attribute whether to allow promotions that might result in bit-widening, precision loss and undefined behaviors.**pytorch_scalar_promotion**– Bool attribute whether to promote scalar input to type provided by non-scalar input when number format is matching.**u64_integer_promotion_target**– Element type attribute to select promotion result for u64 and signed integers.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1419ConvertPromoteTypes24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
bool get_pytorch_scalar_promotion() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op3v1419ConvertPromoteTypes28get_pytorch_scalar_promotionEv) Get bool attribute whether to promote scalar input to type provided by non-scalar input when number format is matching.


-
void set_pytorch_scalar_promotion(bool pytorch_scalar_promotion)
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1419ConvertPromoteTypes28set_pytorch_scalar_promotionEb) Set bool attribute whether to promote scalar input to type provided by non-scalar input when number format is matching.


-
bool get_promote_unsafe() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op3v1419ConvertPromoteTypes18get_promote_unsafeEv) Get bool attribute whether to allow promotions that might result in bit-widening, precision loss and undefined behaviors.


-
void set_promote_unsafe(bool promote_unsafe)
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1419ConvertPromoteTypes18set_promote_unsafeEb) Set bool attribute whether to allow promotions that might result in bit-widening, precision loss and undefined behaviors.


-
ConvertPromoteTypes() = default