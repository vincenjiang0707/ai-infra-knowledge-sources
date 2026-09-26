source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__shape__c__api.html
lastmod: 

# Group Shape[#](https://docs.openvino.ai#group-shape)

-
*group*Shape The definitions & operations about shape.

Functions

-
ov_shape_create(const int64_t rank, const int64_t *dims,
[ov_shape_t](https://docs.openvino.ai/structov__shape__t.html#_CPPv410ov_shape_t)*shape)[#](https://docs.openvino.ai#_CPPv415ov_shape_createK7int64_tPK7int64_tP10ov_shape_t) Initialize a fully shape object, allocate space for its dimensions and set its content id dims is not null.

- Parameters:
**rank**– The rank value for this object, it should be more than 0(>0)**dims**– The dimensions data for this shape object, it’s size should be equal to rank.**shape**– The input/output shape object pointer.

- Returns:
ov_status_e The return status code.



-
ov_shape_free(
[ov_shape_t](https://docs.openvino.ai/structov__shape__t.html#_CPPv410ov_shape_t)*shape)[#](https://docs.openvino.ai#_CPPv413ov_shape_freeP10ov_shape_t) Free a shape object’s internal memory.

- Parameters:
**shape**– The input shape object pointer.- Returns:
ov_status_e The return status code.



-
struct ov_shape_t
[#](https://docs.openvino.ai#_CPPv410ov_shape_t) *#include <ov_shape.h>*Reprents a static shape.


-
ov_shape_create(const int64_t rank, const int64_t *dims,