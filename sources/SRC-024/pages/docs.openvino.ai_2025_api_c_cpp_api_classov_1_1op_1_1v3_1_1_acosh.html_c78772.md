source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v3_1_1_acosh.html
lastmod: 

Class ov::op::v3::Acosh# class Acosh : public ov::op::util::UnaryElementwiseArithmetic# Elementwise inverse hyperbolic cos operation. Public Functions Acosh() = default# Constructs an Acosh operation. Acosh(const Output<Node> &arg)# Constructs an Acosh operation. Output [d1, ...] Parameters: arg – Output that produces the input tensor.[d1, ...] virtual bool has_evaluate() const override# Allows to get information about availability of evaluate method for the current operation.