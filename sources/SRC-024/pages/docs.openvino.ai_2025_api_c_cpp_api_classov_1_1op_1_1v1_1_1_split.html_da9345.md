source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_split.html
lastmod: 

# Class ov::op::v1::Split[#](https://docs.openvino.ai#class-ov-op-v1-split)

-
class Split : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v15SplitE) Splits the input tensor into a list of equal sized tensors.

Public Functions

-
Split() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v15Split5SplitEv) Constructs a split operation.


-
Split(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axis, const size_t num_splits)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v15Split5SplitERK6OutputI4NodeERK6OutputI4NodeEK6size_t) Constructs a split operation.

- Parameters:
**data**– The tensor to be split.**axis**– The index of an axis in “data” along which to perform the split.**num_splits**– The number of pieces that the data tensor should be split into.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v15Split24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v15Split12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Split() = default