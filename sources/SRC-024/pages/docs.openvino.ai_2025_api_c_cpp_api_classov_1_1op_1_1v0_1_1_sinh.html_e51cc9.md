source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_sinh.html
lastmod: 

Class ov::op::v0::Sinh# class Sinh : public ov::op::util::UnaryElementwiseArithmetic# Elementwise hyperbolic sine (sinh) operation. Public Functions Sinh(const Output<Node> &arg)# Constructs a hyperbolic sine operation. Parameters: arg – Node that produces the input tensor. virtual bool has_evaluate() const override# Allows to get information about availability of evaluate method for the current operation.