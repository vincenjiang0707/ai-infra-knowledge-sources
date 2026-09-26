source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v9_1_1_eye.html
lastmod: 

# Class ov::op::v9::Eye[#](https://docs.openvino.ai#class-ov-op-v9-eye)

-
class Eye : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v93EyeE) -
Public Functions

-
Eye(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &num_rows, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &num_columns, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &diagonal_index, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &batch_shape, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&out_type)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v93Eye3EyeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERKN2ov7element4TypeE) Constructs a

[Eye](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v9_1_1_eye)operation.- Parameters:


-
Eye(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &num_rows, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &num_columns, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &diagonal_index, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&out_type)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v93Eye3EyeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERKN2ov7element4TypeE) Constructs a

[Eye](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v9_1_1_eye)operation without batch_shape.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v93Eye24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v93Eye12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Eye(const