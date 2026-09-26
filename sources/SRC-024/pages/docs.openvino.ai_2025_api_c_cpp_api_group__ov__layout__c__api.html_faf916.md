source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__layout__c__api.html
lastmod: 

# Group Layout[#](https://docs.openvino.ai#group-layout)

-
*group*Layout The definitions & operations about layout.

Functions

-
ov_layout_create(const char *layout_desc,
[ov_layout_t](https://docs.openvino.ai/structov__layout__t.html#_CPPv411ov_layout_t)**layout)[#](https://docs.openvino.ai#_CPPv416ov_layout_createPKcPP11ov_layout_t) Create a layout object.

- Parameters:
**layout**– The layout input pointer.**layout_desc**– The description of layout.

- Returns:
ov_status_e a status code, return OK if successful



-
ov_layout_free(
[ov_layout_t](https://docs.openvino.ai/structov__layout__t.html#_CPPv411ov_layout_t)*layout)[#](https://docs.openvino.ai#_CPPv414ov_layout_freeP11ov_layout_t) Free layout object.

- Parameters:
**layout**– will be released.


-
ov_layout_to_string(const
[ov_layout_t](https://docs.openvino.ai/structov__layout__t.html#_CPPv411ov_layout_t)*layout)[#](https://docs.openvino.ai#_CPPv419ov_layout_to_stringPK11ov_layout_t) Convert layout object to a readable string.

- Parameters:
**layout**– will be converted.- Returns:
string that describes the layout content.



-
struct ov_layout_t
[#](https://docs.openvino.ai#_CPPv411ov_layout_t) *#include <ov_layout.h>*type define

[ov_layout_t](https://docs.openvino.ai#structov__layout__t)from ov_layout

-
ov_layout_create(const char *layout_desc,