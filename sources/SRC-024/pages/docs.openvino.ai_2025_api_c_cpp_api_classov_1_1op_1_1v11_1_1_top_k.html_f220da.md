source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v11_1_1_top_k.html
lastmod: 

# Class ov::op::v11::TopK[#](https://docs.openvino.ai#class-ov-op-v11-topk)

-
class TopK : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[TopKBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_top_k_base.html#_CPPv4N2ov2op4util8TopKBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v114TopKE) Computes the top K elements of a given tensor along the specified axis.

Public Functions

-
TopK(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &k, const int64_t axis, const std::string &mode, const std::string &sort, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&index_element_type =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i32](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i32EN6Type_t3i32E), const bool stable = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v114TopK4TopKERK6OutputI4NodeERK6OutputI4NodeEK7int64_tRKNSt6stringERKNSt6stringERKN7element4TypeEKb) Constructs a

[TopK](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v11_1_1_top_k)operation with two outputs: values and indices.- Parameters:
**data**– The input tensor**k**– Specifies how many maximum/minimum elements should be computed**axis**– The axis along which the[TopK](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v11_1_1_top_k)operation should be executed**mode**– Specifies whether[TopK](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v11_1_1_top_k)selects the largest or the smallest elements from each slice**sort**– Specifies the order of corresponding elements of the output tensor**index_element_type**– Specifies the data type of the elements in the ‘indices’ output tensor.**stable**– Specifies whether the equivalent elements should maintain their relative order from the input tensor during sorting.



-
TopK(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &k, const int64_t axis, const[TopKMode](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op8TopKModeE)mode, const[TopKSortType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12TopKSortTypeE)sort, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&index_element_type =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i32](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i32EN6Type_t3i32E), const bool stable = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v114TopK4TopKERK6OutputI4NodeERK6OutputI4NodeEK7int64_tK8TopKModeK12TopKSortTypeRKN7element4TypeEKb) Constructs a

[TopK](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v11_1_1_top_k)operation with two outputs: values and indices.- Parameters:
**data**– The input tensor**k**– Specifies how many maximum/minimum elements should be computed**axis**– The axis along which the[TopK](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v11_1_1_top_k)operation should be executed**mode**– Specifies whether[TopK](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v11_1_1_top_k)selects the largest or the smallest elements from each slice**sort**– Specifies the order of corresponding elements of the output tensor**index_element_type**– Specifies the data type of the elements in the ‘indices’ output tensor.**stable**– Specifies whether the equivalent elements should maintain their relative order from the input tensor during sorting.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v114TopK24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op3v114TopK12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
TopK(const