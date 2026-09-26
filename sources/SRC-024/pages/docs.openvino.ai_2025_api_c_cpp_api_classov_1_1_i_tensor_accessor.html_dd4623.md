source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_i_tensor_accessor.html
lastmod: 

Class ov::ITensorAccessor# class ITensorAccessor# Interface for data accessor. Subclassed by ov::TensorAccessor< TContainer > Public Functions virtual Tensor operator()(size_t port) const = 0# Get tensor at port. Parameters: port – Number of data port (operator input) to get tensor. Returns: Tensor to data at port.