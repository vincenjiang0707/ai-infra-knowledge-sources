source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_unroll_tensor_iterator.html
lastmod: 

# Class ov::pass::UnrollTensorIterator[#](https://docs.openvino.ai#class-ov-pass-unrolltensoriterator)

-
class UnrollTensorIterator : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[ModelPass](https://docs.openvino.ai/classov_1_1pass_1_1_model_pass.html#_CPPv4N2ov4pass9ModelPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass20UnrollTensorIteratorE) Unrolls the body of the TensorIterator layer. Multiple body copies, the number of which is determined by the number of iterations of the TensorIterator layer, are created and connected to each other and to the external network. If the number of TensorIterator iterations is greater than 1, then additional Concat and Split layers are added to the network.