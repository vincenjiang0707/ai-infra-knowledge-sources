source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__partial__shape__c__api.html
lastmod: 

# Group Partial Shape[#](https://docs.openvino.ai#group-partial-shape)

-
*group*Partial Shape The definitions & operations about partial shape.

Functions

-
ov_partial_shape_create(const int64_t rank, const ov_dimension_t *dims, ov_partial_shape_t *partial_shape_obj)
[#](https://docs.openvino.ai#_CPPv423ov_partial_shape_createK7int64_tPK14ov_dimension_tP18ov_partial_shape_t) Initialze a partial shape with static rank and dynamic dimension.

- Parameters:
**rank**– support static rank.**dims**– support dynamic and static dimension. Static rank, but dynamic dimensions on some or all axes. Examples:`{1,2,?,4}`

or`{?,?,?}`

or`{1,2,-1,4}`

Static rank, and static dimensions on all axes. Examples:`{1,2,3,4}`

or`{6}`

or`{}`


- Returns:
Status code of the operation: OK(0) for success.



-
ov_partial_shape_create_dynamic(const
[ov_rank_t](https://docs.openvino.ai/structov__rank__t.html#_CPPv49ov_rank_t)rank, const ov_dimension_t *dims, ov_partial_shape_t *partial_shape_obj)[#](https://docs.openvino.ai#_CPPv431ov_partial_shape_create_dynamicK9ov_rank_tPK14ov_dimension_tP18ov_partial_shape_t) Initialze a partial shape with dynamic rank and dynamic dimension.

- Parameters:
**rank**– support dynamic and static rank.**dims**– support dynamic and static dimension. Dynamic rank: Example:`?`

Static rank, but dynamic dimensions on some or all axes. Examples:`{1,2,?,4}`

or`{?,?,?}`

or`{1,2,-1,4}`

Static rank, and static dimensions on all axes. Examples:`{1,2,3,4}`

or`{6}`

or`{}"`


- Returns:
Status code of the operation: OK(0) for success.



-
ov_partial_shape_create_static(const int64_t rank, const int64_t *dims, ov_partial_shape_t *partial_shape_obj)
[#](https://docs.openvino.ai#_CPPv430ov_partial_shape_create_staticK7int64_tPK7int64_tP18ov_partial_shape_t) Initialize a partial shape with static rank and static dimension.

- Parameters:
**rank**– support static rank.**dims**– support static dimension. Static rank, and static dimensions on all axes. Examples:`{1,2,3,4}`

or`{6}`

or`{}`


- Returns:
Status code of the operation: OK(0) for success.



-
ov_partial_shape_free(ov_partial_shape_t *partial_shape)
[#](https://docs.openvino.ai#_CPPv421ov_partial_shape_freeP18ov_partial_shape_t) Release internal memory allocated in partial shape.

- Parameters:
**partial_shape**– The object’s internal memory will be released.- Returns:
Status code of the operation: OK(0) for success.



-
ov_partial_shape_to_shape(const ov_partial_shape_t partial_shape,
[ov_shape_t](https://docs.openvino.ai/structov__shape__t.html#_CPPv410ov_shape_t)*shape)[#](https://docs.openvino.ai#_CPPv425ov_partial_shape_to_shapeK18ov_partial_shape_tP10ov_shape_t) Convert partial shape without dynamic data to a static shape.

- Parameters:
**partial_shape**– The partial_shape pointer.**shape**– The shape pointer.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_shape_to_partial_shape(const
[ov_shape_t](https://docs.openvino.ai/structov__shape__t.html#_CPPv410ov_shape_t)shape, ov_partial_shape_t *partial_shape)[#](https://docs.openvino.ai#_CPPv425ov_shape_to_partial_shapeK10ov_shape_tP18ov_partial_shape_t) Convert shape to partial shape.

- Parameters:
**shape**– The shape pointer.**partial_shape**– The partial_shape pointer.

- Returns:
Status code of the operation: OK(0) for success.



-
ov_partial_shape_is_dynamic(const ov_partial_shape_t partial_shape)
[#](https://docs.openvino.ai#_CPPv427ov_partial_shape_is_dynamicK18ov_partial_shape_t) Check this partial_shape whether is dynamic.

- Parameters:
**partial_shape**– The partial_shape pointer.- Returns:
Status code of the operation: OK(0) for success.



-
ov_partial_shape_to_string(const ov_partial_shape_t partial_shape)
[#](https://docs.openvino.ai#_CPPv426ov_partial_shape_to_stringK18ov_partial_shape_t) Helper function, convert a partial shape to readable string.

- Parameters:
**partial_shape**– The partial_shape pointer.- Returns:
A string reprensts partial_shape’s content.



-
struct ov_partial_shape
[#](https://docs.openvino.ai#_CPPv416ov_partial_shape) *#include <ov_partial_shape.h>*It represents a shape that may be partially or totally dynamic. A PartialShape may have: Dynamic rank. (Informal notation:

`?`

) Static rank, but dynamic dimensions on some or all axes. (Informal notation examples:`{1,2,?,4}`

,`{?,?,?}`

,`{-1,-1,-1}`

) Static rank, and static dimensions on all axes. (Informal notation examples:`{1,2,3,4}`

,`{6}`

,`{}`

)An interface to make user can initialize ov_partial_shape_t


-
ov_partial_shape_create(const int64_t rank, const ov_dimension_t *dims, ov_partial_shape_t *partial_shape_obj)