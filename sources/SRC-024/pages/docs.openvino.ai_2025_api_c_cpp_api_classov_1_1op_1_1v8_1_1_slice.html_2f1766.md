source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v8_1_1_slice.html
lastmod: 

# Class ov::op::v8::Slice[#](https://docs.openvino.ai#class-ov-op-v8-slice)

-
class Slice : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v85SliceE) [Slice](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_slice)operation.Public Functions

-
Slice(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &start, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &stop, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &step)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v85Slice5SliceERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs

[Slice](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_slice)operation (default axes).- Parameters:
**data**– The tensor to be sliced.**start**– 1D tensor with start indices of the slice.**stop**– 1D tensor with end indices of the slice.**step**– 1D tensor specifies the increment to use in slicing along corresponding axes.



-
Slice(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &start, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &stop, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &step, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axes)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v85Slice5SliceERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs

[Slice](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_slice)operation.- Parameters:
**data**– The tensor to be sliced.**start**– 1D tensor with start indices of the slice.**stop**– 1D tensor with end indices of the slice.**step**– 1D tensor specifies the increment to use in slicing along corresponding axes.**axes**– 1D tensor indicating which dimensions the values in the`start`

and`stop`

apply to.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v85Slice24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v85Slice12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Slice(const