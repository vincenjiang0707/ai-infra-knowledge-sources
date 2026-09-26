source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v3_1_1_asinh.html
lastmod: 

Class ov::op::v3::Asinh# class Asinh : public ov::op::util::UnaryElementwiseArithmetic# Elementwise inverse hyperbolic sin operation. Public Functions Asinh() = default# Constructs an Asinh operation. Asinh(const Output<Node> &arg)# Constructs an Asinh operation. Output [d1, ...] Parameters: arg – Output that produces the input tensor.[d1, ...] virtual bool has_evaluate() const override# Allows to get information about availability of evaluate method for the current operation.