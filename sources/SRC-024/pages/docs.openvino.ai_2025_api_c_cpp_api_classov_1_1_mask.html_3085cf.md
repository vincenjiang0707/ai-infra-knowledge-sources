source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_mask.html
lastmod: 

Class ov::Mask# class Mask : public std::vector<std::set<uint64_t>>, public std::enable_shared_from_this<Mask># each element in vector represents dimension and each element in set is an id of dimensions which contains zeros.