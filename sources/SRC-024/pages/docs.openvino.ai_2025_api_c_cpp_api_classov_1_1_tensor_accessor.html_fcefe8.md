source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_tensor_accessor.html
lastmod: 

# Class ov::TensorAccessor[#](https://docs.openvino.ai#class-ov-tensoraccessor)

-
template<class TContainer>

class TensorAccessor : public[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[ITensorAccessor](https://docs.openvino.ai/classov_1_1_i_tensor_accessor.html#_CPPv4N2ov15ITensorAccessorE)[#](https://docs.openvino.ai#_CPPv4I0EN2ov14TensorAccessorE) [Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)data accessor functor.Creates the

[ov::Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)found in tensors container. This accessor does not take ownership of tensors container. Supports following containers:std::unordered_map<size_t, ov::Tensor>


- Template Parameters:
**TContainer**– Type of tensor container.

Public Functions

-
inline constexpr TensorAccessor(const
[TContainer](https://docs.openvino.ai#_CPPv4I0EN2ov14TensorAccessorE)*tensors)[#](https://docs.openvino.ai#_CPPv4N2ov14TensorAccessor14TensorAccessorEPK10TContainer) Construct a new

[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)Accessor object for tensors container.- Parameters:
**tensors**– Pointer to container with tensors.


-
virtual
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)operator()(size_t port) const override[#](https://docs.openvino.ai#_CPPv4NK2ov14TensorAccessorclE6size_t) Get tensor for given port number.

- Parameters:
**port**– Port number to get data.- Returns:
[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)to data or empty tensor if data not found.


-
virtual
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)operator()(size_t port) const Get tensor at port.

- Parameters:
**port**– Number of data port (operator input) to get tensor.- Returns:
[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)to data at port.