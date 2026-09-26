source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_strided_slice.html
lastmod: 

# Class ov::op::v1::StridedSlice[#](https://docs.openvino.ai#class-ov-op-v1-stridedslice)

-
class StridedSlice : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112StridedSliceE) Takes a slice of an input tensor, i.e., the sub-tensor that resides within a bounding box, optionally with stride.

Public Functions

-
StridedSlice(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &begin, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &end, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &strides, const std::vector<int64_t> &begin_mask, const std::vector<int64_t> &end_mask, const std::vector<int64_t> &new_axis_mask = std::vector<int64_t>{}, const std::vector<int64_t> &shrink_axis_mask = std::vector<int64_t>{}, const std::vector<int64_t> &ellipsis_mask = std::vector<int64_t>{})[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112StridedSlice12StridedSliceERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERKNSt6vectorI7int64_tEERKNSt6vectorI7int64_tEERKNSt6vectorI7int64_tEERKNSt6vectorI7int64_tEERKNSt6vectorI7int64_tEE) Constructs a dynamic tensor strided slice operation.

- Parameters:
**data**– The tensor to be sliced.**begin**– 1D tensor with begin indexes for input blob slicing.**end**– 1D tensor with end indexes for input blob slicing.**strides**– The slicing strides; for example, strides of`{n,m}`

means to take every nth row and every mth column of the input matrix.**begin_mask**– When begin_mask[i] equal to 1 means that the corresponding dimension of the begin input is ignored.**end_mask**– When end_mask[i] is 1, the corresponding dimension of the end input is ignored.**new_axis_mask**– If new_axis_mask[i] is 1, a length 1 dimension is inserted on the i-th position.**shrink_axis_mask**– If shrink_axis_mask[i] is 1, the dimension on the i-th position is deleted.**ellipsis_mask**– It inserts missing dimensions on a position of a non-zero bit.



-
StridedSlice(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &begin, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &end, const std::vector<int64_t> &begin_mask, const std::vector<int64_t> &end_mask, const std::vector<int64_t> &new_axis_mask = std::vector<int64_t>{}, const std::vector<int64_t> &shrink_axis_mask = std::vector<int64_t>{}, const std::vector<int64_t> &ellipsis_mask = std::vector<int64_t>{})[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112StridedSlice12StridedSliceERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERKNSt6vectorI7int64_tEERKNSt6vectorI7int64_tEERKNSt6vectorI7int64_tEERKNSt6vectorI7int64_tEERKNSt6vectorI7int64_tEE) Constructs a dynamic tensor strided slice operation.

- Parameters:
**data**– The tensor to be sliced.**begin**– 1D tensor with begin indexes for input blob slicing.**end**– 1D tensor with end indexes for input blob slicing.**begin_mask**– When begin_mask[i] equal to 1 means that the corresponding dimension of the begin input is ignored.**end_mask**– When end_mask[i] is 1, the corresponding dimension of the end input is ignored.**new_axis_mask**– If new_axis_mask[i] is 1, a length 1 dimension is inserted on the i-th position.**shrink_axis_mask**– If shrink_axis_mask[i] is 1, the dimension on the i-th position is deleted.**ellipsis_mask**– It inserts missing dimensions on a position of a non-zero bit.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112StridedSlice24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v112StridedSlice12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
StridedSlice(const