source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_tensor_iterator.html
lastmod: 

# Class ov::op::v0::TensorIterator[#](https://docs.openvino.ai#class-ov-op-v0-tensoriterator)

-
class TensorIterator : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[SubGraphOp](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_sub_graph_op.html#_CPPv4N2ov2op4util10SubGraphOpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v014TensorIteratorE) Iterate a body over tensors, accumulating into tensors.

Public Functions

- Parameters:
**body**– set the body of the iteration


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v014TensorIterator24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.