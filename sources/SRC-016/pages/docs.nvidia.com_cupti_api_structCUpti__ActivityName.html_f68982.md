source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityName.html

# 7.98. CUpti_ActivityName[#](https://docs.nvidia.com#cupti-activityname)

-
struct CUpti_ActivityName
[#](https://docs.nvidia.com#_CPPv418CUpti_ActivityName) The activity record providing a name.

This activity record provides a name for a device, context, thread, etc. and other resource naming done via NVTX APIs (CUPTI_ACTIVITY_KIND_NAME).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityName4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_NAME.


-
[CUpti_ActivityObjectKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv424CUpti_ActivityObjectKind)objectKind[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityName10objectKindE) The kind of activity object being named.


-
[CUpti_ActivityObjectKindId](https://docs.nvidia.com/unionCUpti__ActivityObjectKindId.html#_CPPv426CUpti_ActivityObjectKindId)objectId[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityName8objectIdE) The identifier for the activity object.

‘objectKind’ indicates which ID is valid for this record.


-
uint32_t pad
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityName3padE) Undefined.

Reserved for internal use.


-
const char *name
[#](https://docs.nvidia.com#_CPPv4N18CUpti_ActivityName4nameE) The name.


-