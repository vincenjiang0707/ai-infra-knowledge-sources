source: https://docs.openvino.ai/2025/api/c_cpp_api/structov_1_1reference_1_1_unique_elements.html
lastmod: 

# Struct ov::reference::UniqueElements[#](https://docs.openvino.ai#struct-ov-reference-uniqueelements)

-
template<typename Index_t, typename Count_t>

struct UniqueElements[#](https://docs.openvino.ai#_CPPv4I00EN2ov9reference14UniqueElementsE) Public Members

-
std::vector<
[TensorSlice](https://docs.openvino.ai/structov_1_1reference_1_1_tensor_slice.html#_CPPv4I00EN2ov9reference11TensorSliceE)<[Index_t](https://docs.openvino.ai#_CPPv4I00EN2ov9reference14UniqueElementsE),[Count_t](https://docs.openvino.ai#_CPPv4I00EN2ov9reference14UniqueElementsE)>> all_tensor_elements[#](https://docs.openvino.ai#_CPPv4N2ov9reference14UniqueElements19all_tensor_elementsE) Contains descriptors of all elements in the input tensor. Possibly sorted by value.


-
std::vector<
[TensorSlice](https://docs.openvino.ai/structov_1_1reference_1_1_tensor_slice.html#_CPPv4I00EN2ov9reference11TensorSliceE)<[Index_t](https://docs.openvino.ai#_CPPv4I00EN2ov9reference14UniqueElementsE),[Count_t](https://docs.openvino.ai#_CPPv4I00EN2ov9reference14UniqueElementsE)>> unique_tensor_elements[#](https://docs.openvino.ai#_CPPv4N2ov9reference14UniqueElements22unique_tensor_elementsE) Subset of all tensor elements. First occurrences of the unique values.


-
int64_t axis = 0
[#](https://docs.openvino.ai#_CPPv4N2ov9reference14UniqueElements4axisE) Axis (optional). Used to gather unique elements over a given dimension.


-
std::vector<