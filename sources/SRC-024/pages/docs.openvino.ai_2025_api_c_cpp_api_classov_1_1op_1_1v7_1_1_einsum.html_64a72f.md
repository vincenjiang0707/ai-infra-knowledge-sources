source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v7_1_1_einsum.html
lastmod: 

# Class ov::op::v7::Einsum[#](https://docs.openvino.ai#class-ov-op-v7-einsum)

-
class Einsum : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v76EinsumE) [Einsum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v7_1_1_einsum)operation.Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v76Einsum24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


Public Static Functions

-
static void parse_equation(const std::string &equation, std::vector<std::string> &input_subscripts, std::string &output_subscript)
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v76Einsum14parse_equationERKNSt6stringERNSt6vectorINSt6stringEEERNSt6stringE) Check correctness of equation format and extract input subscripts and output subscript.

- Parameters:
**equation**– Equation to be parsed and checked**input_subscripts**– A vector of extracted input subscripts**output_subscript**– An output subscript



-
static std::vector<std::string> extract_labels(const std::string &subscript)
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v76Einsum14extract_labelsERKNSt6stringE) Extract labels (from subscript) that can be alphabetic letters or ellipsis.

- Parameters:
**subscript**– Subscript- Returns:
A vector of extracted labels from the input subscript in the order of appearence



-
virtual void validate_and_infer_types() override