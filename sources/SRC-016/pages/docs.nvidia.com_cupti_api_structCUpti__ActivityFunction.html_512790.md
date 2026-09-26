source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityFunction.html

# 7.36. CUpti_ActivityFunction[#](https://docs.nvidia.com#cupti-activityfunction)

-
struct CUpti_ActivityFunction
[#](https://docs.nvidia.com#_CPPv422CUpti_ActivityFunction) The activity record for global/device functions.

This activity records function name and corresponding module information. (CUPTI_ACTIVITY_KIND_FUNCTION).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityFunction4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_FUNCTION.


-
uint32_t id
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityFunction2idE) ID to uniquely identify the record.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityFunction9contextIdE) The ID of the context where the function is launched.


-
uint32_t moduleId
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityFunction8moduleIdE) The module ID in which this global/device function is present.


-
uint32_t functionIndex
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityFunction13functionIndexE) The function’s unique symbol index in the module.


-
uint32_t pad
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityFunction3padE) Undefined.

Reserved for internal use.


-
const char *name
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityFunction4nameE) The name of the function.

This name is shared across all activity records representing the same kernel, and so should not be modified.


-