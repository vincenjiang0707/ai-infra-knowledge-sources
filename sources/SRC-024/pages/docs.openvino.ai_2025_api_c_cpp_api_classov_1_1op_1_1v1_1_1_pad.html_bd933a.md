source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_pad.html
lastmod: 

# Class ov::op::v1::Pad[#](https://docs.openvino.ai#class-ov-op-v1-pad)

-
class Pad : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[PadBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_pad_base.html#_CPPv4N2ov2op4util7PadBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v13PadE) Generic padding operation.

Public Functions

-
Pad() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v13Pad3PadEv) Constructs a Pad-1 operation.


-
Pad(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &pads_begin, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &pads_end, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg_pad_value,[PadMode](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadModeE)pad_mode)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v13Pad3PadERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE7PadMode) Constructs a Pad-1 operation.

- Parameters:
**arg**– The output producing input tensor to be padded.**pads_begin**– The output which specifies the number of padding elements added before position 0 on each axis of arg.**pads_end**– The output which specifies the number of padding elements after the last element on each axis.**arg_pad_value**– The scalar output with the value used for padding if pad_mode is CONSTANT**pad_mode**– The padding mode: CONSTANT, EDGE, REFLECT or SYMMETRIC. CONSTANT initializes new elements with arg_pad_value, EDGE uses the nearest value from arg. REFLECT and SYMMETRIC tile the background by flipping arg at the edge (SYMMETRIC) or on the last row/column/etc. (REFLECT).



-
Pad(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &pads_begin, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &pads_end,[PadMode](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadModeE)pad_mode)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v13Pad3PadERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE7PadMode) Constructs a Pad-1 operation.

- Parameters:
**arg**– The output producing input tensor to be padded.**pads_begin**– The output which specifies the number of padding elements added**pads_end**– The output which specifies the number of padding elements after the last element on each axis.**pad_mode**– The padding mode: CONSTANT, EDGE, REFLECT or SYMMETRIC.



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v13Pad12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
virtual bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &outputs, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &inputs) const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v13Pad8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorE) Evaluates the op on input_values putting results in output_values.

- Parameters:
**output_values**– Tensors for the outputs to compute. One for each result**input_values**– Tensors for the inputs. One for each inputs.

- Returns:
true if successful



-
Pad() = default