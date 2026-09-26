source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_variadic_split.html
lastmod: 

# Class ov::op::v1::VariadicSplit[#](https://docs.openvino.ai#class-ov-op-v1-variadicsplit)

-
class VariadicSplit : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v113VariadicSplitE) [VariadicSplit](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_variadic_split)operation splits an input tensor into pieces along some axis. The pieces may have variadic lengths depending on “split_lengths” attribute.Public Functions

-
VariadicSplit() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v113VariadicSplit13VariadicSplitEv) Constructs a variadic split operation.


-
VariadicSplit(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axis, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &split_lengths)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v113VariadicSplit13VariadicSplitERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a variadic split operation.

outputs. The sum of split_lengths must match data.shape[axis]

- Parameters:
**data**– The tensor to be split.**axis**– The index of an axis in “data” along which to perform the split.**split_lengths**– A list containing the sizes of each output tensor along the split “axis”. Size of “split_lengths” should be equal to the number of



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v113VariadicSplit24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline virtual size_t get_default_output_index() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v113VariadicSplit24get_default_output_indexEv) Returns the output of the default output, or throws if there is none.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v113VariadicSplit12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
VariadicSplit() = default