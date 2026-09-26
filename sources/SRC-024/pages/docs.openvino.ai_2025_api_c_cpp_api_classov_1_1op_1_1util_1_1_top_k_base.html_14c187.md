source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_top_k_base.html
lastmod: 

# Class ov::op::util::TopKBase[#](https://docs.openvino.ai#class-ov-op-util-topkbase)

-
class TopKBase : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util8TopKBaseE) Subclassed by

[ov::op::v11::TopK](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v11_1_1_top_k),[ov::op::v1::TopK](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_top_k),[ov::op::v3::TopK](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_top_k)Public Functions

-
TopKBase(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &k, const int64_t axis, const std::string &mode, const std::string &sort, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&index_element_type =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i32](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i32EN6Type_t3i32E))[#](https://docs.openvino.ai#_CPPv4N2ov2op4util8TopKBase8TopKBaseERK6OutputI4NodeERK6OutputI4NodeEK7int64_tRKNSt6stringERKNSt6stringERKN7element4TypeE) The common base class for all TopK operator versions.

- Parameters:
**data**– The input tensor**k**– Specifies how many maximum/minimum elements should be computed**axis**– The axis along which TopK should be computed**mode**– Specifies whether the maximum or minimum elements are selected**sort**– Specifies the order of output elements and/or indices Accepted values: none, index, value**index_element_type**– Specifies the type of produced indices



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util8TopKBase24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
uint64_t get_axis() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util8TopKBase8get_axisEv) Returns axis value after normalization.

Note

If input rank required to normalization is dynamic, the exception is thrown


-
inline int64_t get_provided_axis() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util8TopKBase17get_provided_axisEv) Returns axis value before normalization.


-
size_t get_k() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util8TopKBase5get_kEv) Returns the value of K, if available.

Note

If the second input to this op is a constant, the value is retrieved and returned. If the input is not constant(dynamic) this method returns 0


-
inline virtual size_t get_default_output_index() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util8TopKBase24get_default_output_indexEv) Returns the output of the default output, or throws if there is none.


-
TopKBase(const