source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_shuffle_channels.html
lastmod: 

# Class ov::op::v0::ShuffleChannels[#](https://docs.openvino.ai#class-ov-op-v0-shufflechannels)

-
class ShuffleChannels : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v015ShuffleChannelsE) Permutes data in the channel dimension of the input.

Public Functions

-
ShuffleChannels(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const int64_t axis = 1, const int64_t group = 1)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v015ShuffleChannels15ShuffleChannelsERK6OutputI4NodeEK7int64_tK7int64_t) Constructs a

[ShuffleChannels](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_shuffle_channels)node.- Parameters:
**data**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the input tensor.**axis**– Channel dimension index in the data tensor. A negative value means that the index should be calculated from the back of the input data shape.**group**– Number of group the channel dimension should be split into.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v015ShuffleChannels24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v015ShuffleChannels12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
ShuffleChannels(const