source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1reference_1_1_span.html
lastmod: 

Class ov::reference::Span# template<typename Element>class Span# Span should mimic std::span. Public Functions inline Span subspan(std::size_t offset, std::size_t size = std::numeric_limits<std::size_t>::max()) const# return sub part of span starting from offset and not greater than size inline Span &drop_front(std::size_t number_of_elements)# drop number of elements from front inline Span &drop_back(std::size_t number_of_elements)# drop number of elements from back