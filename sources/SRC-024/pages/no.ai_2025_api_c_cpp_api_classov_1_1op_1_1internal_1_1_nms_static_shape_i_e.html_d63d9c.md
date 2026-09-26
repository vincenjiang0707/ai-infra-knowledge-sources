source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1internal_1_1_nms_static_shape_i_e.html
lastmod: 

Class ov::op::internal::NmsStaticShapeIE# template<typename BaseNmsOp>class NmsStaticShapeIE : public BaseNmsOp# Public Functions inline NmsStaticShapeIE(const Output<Node> &boxes, const Output<Node> &scores, const Attributes &attrs)# Constructs a NmsStaticShapeIE operation. Parameters: boxes – Node producing the box coordinates scores – Node producing the box scores attrs – Attributes of the operation