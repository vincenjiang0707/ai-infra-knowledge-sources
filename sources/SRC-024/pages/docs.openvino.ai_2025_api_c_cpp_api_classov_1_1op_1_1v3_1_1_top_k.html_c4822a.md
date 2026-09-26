source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v3_1_1_top_k.html
lastmod: 

# Class ov::op::v3::TopK[#](https://docs.openvino.ai#class-ov-op-v3-topk)

-
class TopK : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[TopKBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_top_k_base.html#_CPPv4N2ov2op4util8TopKBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v34TopKE) Computes indices and values of the k maximum/minimum values for each slice along specified axis.

Public Functions

-
TopK(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &k, const int64_t axis, const std::string &mode, const std::string &sort, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&index_element_type =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i32](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i32EN6Type_t3i32E))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v34TopK4TopKERK6OutputI4NodeERK6OutputI4NodeEK7int64_tRKNSt6stringERKNSt6stringERKN7element4TypeE) Constructs a

[TopK](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_top_k)operation with two outputs: values and indices. By default the indices output is described by i32 data type.- Parameters:
**data**– The input tensor**k**– Specifies how many maximum/minimum elements should be computed (note: scalar input tensor)**axis**– The axis along which to compute top k indices**mode**– Specifies which operation (min or max) is used to select the biggest element of two.**sort**– Specifies order of output elements and/or indices Accepted values: none, index, value**index_element_type**– Specifies type of produced indices



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v34TopK12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
TopK(const