source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v8_1_1_matrix_nms.html
lastmod: 

# Class ov::op::v8::MatrixNms[#](https://docs.openvino.ai#class-ov-op-v8-matrixnms)

-
class MatrixNms : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v89MatrixNmsE) [MatrixNms](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_matrix_nms)operation.Public Functions

-
MatrixNms() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v89MatrixNms9MatrixNmsEv) Constructs a conversion operation.


-
MatrixNms(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &boxes, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scores, const[Attributes](https://docs.openvino.ai/structov_1_1op_1_1v8_1_1_matrix_nms_1_1_attributes.html#_CPPv4N2ov2op2v89MatrixNms10AttributesE)&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v89MatrixNms9MatrixNmsERK6OutputI4NodeERK6OutputI4NodeERK10Attributes) Constructs a

[MatrixNms](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_matrix_nms)operation.- Parameters:
**boxes**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the box coordinates**scores**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the box scores**attrs**–[Attributes](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1op_1_1v8_1_1_matrix_nms_1_1_attributes)of the operation



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v89MatrixNms24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline const
[Attributes](https://docs.openvino.ai/structov_1_1op_1_1v8_1_1_matrix_nms_1_1_attributes.html#_CPPv4N2ov2op2v89MatrixNms10AttributesE)&get_attrs() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v89MatrixNms9get_attrsEv) Returns attributes of the operation

[MatrixNms](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_matrix_nms).

-
struct Attributes
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v89MatrixNms10AttributesE) Structure that specifies attributes of the operation.


-
MatrixNms() = default