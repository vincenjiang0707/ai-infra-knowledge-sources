source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_gather.html
lastmod: 

Class ov::op::v1::Gather# class Gather : public ov::op::util::GatherBase# Gather slices from axis of data according to indices. Public Functions Gather(const Output<Node> ¶ms, const Output<Node> &indices, const Output<Node> &axis)# Parameters: data – The tensor from which slices are gathered indices – Tensor with indexes to gather axis – The tensor is a dimension index to gather data from