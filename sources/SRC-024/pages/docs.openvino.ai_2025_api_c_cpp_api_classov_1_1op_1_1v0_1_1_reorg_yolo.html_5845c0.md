source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_reorg_yolo.html
lastmod: 

# Class ov::op::v0::ReorgYolo[#](https://docs.openvino.ai#class-ov-op-v0-reorgyolo)

-
class ReorgYolo : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v09ReorgYoloE) [ReorgYolo](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_reorg_yolo)operation.Public Functions

-
ReorgYolo(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input, const size_t stride)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v09ReorgYolo9ReorgYoloERK6OutputI4NodeEK6size_t) Constructs a

[ReorgYolo](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_reorg_yolo)operation.- Parameters:
**input**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)**stride**– Stride to reorganize input by



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v09ReorgYolo24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
ReorgYolo(const