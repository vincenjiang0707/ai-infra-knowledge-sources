source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_pad_base.html
lastmod: 

# Class ov::op::util::PadBase[#](https://docs.openvino.ai#class-ov-op-util-padbase)

-
class PadBase : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util7PadBaseE) Subclassed by

[ov::op::v12::Pad](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v12_1_1_pad),[ov::op::v1::Pad](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_pad)Public Functions

-
PadBase(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &pads_begin, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &pads_end, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg_pad_value,[PadMode](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadModeE)pad_mode)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util7PadBase7PadBaseERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE7PadMode) Constructs a generic padding operation.

- Parameters:
**arg**– The output producing input tensor to be padded.**pads_begin**– The output which specifies the number of padding elements added before position 0 on each axis of arg.**pads_end**– The output which specifies the number of padding elements after the last element on each axis.**arg_pad_value**– The scalar output with the value used for padding if pad_mode is CONSTANT**pad_mode**– The padding mode



-
PadBase(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &pads_begin, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &pads_end,[PadMode](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadModeE)pad_mode)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util7PadBase7PadBaseERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE7PadMode) Constructs a generic padding operation.

- Parameters:
**arg**– The output producing input tensor to be padded.**pads_begin**– The output which specifies the number of padding elements added**pads_end**– The output which specifies the number of padding elements after the last element on each axis.**pad_mode**– The padding mode



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util7PadBase24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)get_pads_begin() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util7PadBase14get_pads_beginEv) return The node which specifies the number of padding elements added at the beginning of each axis


-
[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)get_pads_end() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util7PadBase12get_pads_endEv) return The node which specifies the number of padding elements added at the end of each axis


-
PadBase(const