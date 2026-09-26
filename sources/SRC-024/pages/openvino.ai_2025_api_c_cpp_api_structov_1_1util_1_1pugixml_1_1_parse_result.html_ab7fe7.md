source: https://docs.openvino.ai/2025/api/c_cpp_api/structov_1_1util_1_1pugixml_1_1_parse_result.html
lastmod: 

# Struct ov::util::pugixml::ParseResult[#](https://docs.openvino.ai#struct-ov-util-pugixml-parseresult)

-
struct ParseResult
[#](https://docs.openvino.ai#_CPPv4N2ov4util7pugixml11ParseResultE) A XML parse result structure with an error message and the

`pugi::xml_document`

document.Public Functions

-
inline ParseResult(std::unique_ptr<pugi::xml_document> &&xml, std::string error_msg)
[#](https://docs.openvino.ai#_CPPv4N2ov4util7pugixml11ParseResult11ParseResultERRNSt10unique_ptrIN4pugi12xml_documentEEENSt6stringE) Constructs

[ParseResult](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1util_1_1pugixml_1_1_parse_result)with`pugi::xml_document`

and an error message.- Parameters:
**xml**– The`pugi::xml_document`

**error_msg**–**[in]**The error message



-
inline ParseResult(std::unique_ptr<pugi::xml_document> &&xml, std::string error_msg)