source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_relu.html
lastmod: 

Class ov::op::v0::Relu# class Relu : public ov::op::util::UnaryElementwiseArithmetic# Elementwise Relu operation. Public Functions Relu(const Output<ov::Node> &arg)# Constructs a Relu operation. Parameters: arg – Node that produces the input tensor. virtual bool has_evaluate() const override# Allows to get information about availability of evaluate method for the current operation.