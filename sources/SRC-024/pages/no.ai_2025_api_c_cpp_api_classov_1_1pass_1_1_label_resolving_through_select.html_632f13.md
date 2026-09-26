source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_label_resolving_through_select.html
lastmod: 

# Class ov::pass::LabelResolvingThroughSelect[#](https://docs.openvino.ai#class-ov-pass-labelresolvingthroughselect)

-
class LabelResolvingThroughSelect : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass27LabelResolvingThroughSelectE) Transformation requires equal labels on one input of Add and output of last Reshape in the pattern: -> Add -> Reshape -[then or else input]-> Select -> Softmax -> Reshape ->

If shape labels onn mentioned tensors are equal we proved that no broadcasting of this input was done for Add and for Select. Therefore, we can put the same labels on the output of Add and Select. This transformation helps propagate labels and will not be needed if we would use information on equality of products of input and output dimensions of Reshape operations