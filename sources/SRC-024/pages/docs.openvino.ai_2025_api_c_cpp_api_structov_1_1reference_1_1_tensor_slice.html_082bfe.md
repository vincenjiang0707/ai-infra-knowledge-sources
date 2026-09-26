source: https://docs.openvino.ai/2025/api/c_cpp_api/structov_1_1reference_1_1_tensor_slice.html
lastmod: 

# Struct ov::reference::TensorSlice[#](https://docs.openvino.ai#struct-ov-reference-tensorslice)

-
template<typename Index_t, typename Count_t>

struct TensorSlice[#](https://docs.openvino.ai#_CPPv4I00EN2ov9reference11TensorSliceE) Public Members

-
[Index_t](https://docs.openvino.ai#_CPPv4I00EN2ov9reference11TensorSliceE)idx = 0[#](https://docs.openvino.ai#_CPPv4N2ov9reference11TensorSlice3idxE) The index of the current element in the original input tensor. It never changes even if the elements get sorted. This value is used as a mapping between a unique element in the first output tensor and the position of this element in the original input tensor.


-
[Index_t](https://docs.openvino.ai#_CPPv4I00EN2ov9reference11TensorSliceE)rev_idx = -1[#](https://docs.openvino.ai#_CPPv4N2ov9reference11TensorSlice7rev_idxE) The rev_idx is a mapping between every element in the original input and the location of a unique element in the first output tensor. More than one Element can have the same rev_idx.


-
[Count_t](https://docs.openvino.ai#_CPPv4I00EN2ov9reference11TensorSliceE)count = 1[#](https://docs.openvino.ai#_CPPv4N2ov9reference11TensorSlice5countE) The number of occurrences of a given element in the input tensor. This value is different than one only for duplicates found in the input tensor.


-
[DescriptorType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9reference14DescriptorTypeE)descriptor_type =[DescriptorType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9reference14DescriptorTypeE)::[SINGLE_VALUE](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9reference14DescriptorType12SINGLE_VALUEE)[#](https://docs.openvino.ai#_CPPv4N2ov9reference11TensorSlice15descriptor_typeE) Indicates if this object points to a single value in the input tensor (rather than a slice of the tensor)


-