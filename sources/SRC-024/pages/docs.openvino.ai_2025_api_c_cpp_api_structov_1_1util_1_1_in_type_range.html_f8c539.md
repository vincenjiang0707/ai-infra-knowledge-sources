source: https://docs.openvino.ai/2025/api/c_cpp_api/structov_1_1util_1_1_in_type_range.html
lastmod: 

Struct ov::util::InTypeRange# template<class T>struct InTypeRange# Check if input data is in [T::min(), T::max()] and then cast it to T. Template Parameters: T – Type of returned value and used to specified min, max of valid value range. Throws ov::AssertFailure: if input value not in type range.