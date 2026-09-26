source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__dimension__c__api.html
lastmod: 

# Group Dimension[#](https://docs.openvino.ai#group-dimension)

-
*group*Dimension The definitions & operations about dimension.

Functions

-
ov_dimension_is_dynamic(const ov_dimension_t dim)
[#](https://docs.openvino.ai#_CPPv423ov_dimension_is_dynamicK14ov_dimension_t) Check this dimension whether is dynamic.

- Parameters:
**dim**– The dimension pointer that will be checked.- Returns:
Boolean, true is dynamic and false is static.



-
struct ov_dimension
[#](https://docs.openvino.ai#_CPPv412ov_dimension) *#include <ov_dimension.h>*This is a structure interface equal to

[ov::Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension).

-
ov_dimension_is_dynamic(const ov_dimension_t dim)